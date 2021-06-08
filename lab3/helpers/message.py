from helpers.redis import redis_connection
from helpers.user import get_username

import random

def message_is_spam():
    return random.random() > 0.5

def create_message(user_id, message, recipient, tags: list):
    message_id = redis_connection.incr("message_id")
    recipient_id = redis_connection.hget("users", recipient)

    if not recipient_id:
        print(f"{recipient} does not exist :(")
        return

    message_key = f"message{message_id}"
    message_info = {
        "id": message_id,
        "text": message,
        "status": "created",
        "sender_id": user_id,
        "recipient_id": recipient_id,
        "tags": ",".join(tags)
    }

    for key in message_info.keys():
        redis_connection.hset(message_key, key, message_info[key])

    redis_connection.lpush("queue", message_id)
    redis_connection.hset(message_key, "status", "in_queue")

    redis_connection.hincrby(f"user{user_id}", "in_queue", 1)
    redis_connection.zincrby("sent", 1, f"user{user_id}")

    return message_id

def get_inbox_messages(user_id):
    messages = redis_connection.smembers(f"sent_to{user_id}")

    if len(messages) == 0:
        print("Oh. You have empty inbox. Let's type someone? :)")
        return

    for message_id in messages:
        message = redis_connection.hmget(f"message{message_id}", ["text", "status", "sender_id"])

        if message[1] != "delivered":
            redis_connection.hset(f"message{message_id}", "status", "delivered")
            redis_connection.hincrby(f"user{message[2]}", "sent", -1)
            redis_connection.hincrby(f"user{message[2]}", "delivered", 1)

        print(f"{message[0]} -> FROM: {get_username(message[2])}")