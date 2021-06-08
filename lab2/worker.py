from helpers.redis import redis_connection
from helpers.message import message_is_spam
from helpers.user import get_username

from threading import Thread
from random import randint
import time

DELAY = randint(0, 2)

class Worker(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        message = redis_connection.brpop("queue")
        if message:
            message_id = message[1]
            message_key = f"message{message_id}"
            redis_connection.hset(message_key, "status", "checking")

            message = redis_connection.hmget(message_key, ["sender_id", "recipient_id"])

            sender_id = message[0]
            redis_connection.hincrby(f"user{sender_id}", "in_queue", -1)
            redis_connection.hincrby(f"user{sender_id}", "checking", 1)

            time.sleep(DELAY)

            is_spam = message_is_spam()
            redis_connection.hincrby(f"user{sender_id}", "checking", -1)

            if is_spam:
                sender_name = get_username(sender_id)
                message_text = redis_connection.hmget(message_key, ["text"])[0]
                redis_connection.publish("spam", f"User {sender_name} sent spam: {message_text}.")

                redis_connection.zincrby(f"spam", 1, f"user{sender_id}")
                redis_connection.hset(message_key, "status", "blocked")
                redis_connection.hincrby(f"user{sender_id}", "blocked", 1)
            else:
                recipient_id = message[1]
                redis_connection.hset(message_key, "status", "sent")
                redis_connection.hincrby(f"user{sender_id}", "sent", 1)
                redis_connection.sadd(f"sent_to:{recipient_id}", message_id)

def main():
    workers_count = 5
    for i in range(workers_count):
        worker = Worker()
        worker.daemon = True
        worker.start()

    while True:
        pass

if __name__ == '__main__':
    main()