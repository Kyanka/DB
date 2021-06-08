from helpers.redis import redis_connection

def get_username(user_id):
    return redis_connection.hmget(f"user{user_id}", ["name"])[0]

def is_signed_in(user_id):
    return user_id != -1

def sign_up(username):
    if redis_connection.hget("users", username):
        print(username, "already exist. Please sign in :)")
        return -1

    user_id = redis_connection.incr("user_id")
    user_key = f"user{user_id}"
    user_info = {
        "id": user_id,
        "name": username,
        "in_queue": 0,
        "checking": 0,
        "blocked": 0,
        "sent": 0,
        "delivered": 0
    }

    redis_connection.hset("users", username, user_id)
    for key in user_info.keys():
        redis_connection.hset(user_key, key, user_info[key])

    redis_connection.publish("sign_up", f"User {username} signed up.")
    redis_connection.sadd("online", username)
    return user_id

def sign_in(username):
    user_id = redis_connection.hget("users", username)

    if not user_id:
        print(username, "does not exist. Please sign up :)")
        return -1

    redis_connection.publish("sign_in", f"User {username} signed in.")
    redis_connection.sadd("online", username)
    return user_id

def sign_out(user_id):
    username = get_username(user_id)
    redis_connection.publish("sign_out", f"User {username} signed out.")
    redis_connection.srem("online", username)