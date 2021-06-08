from helpers.redis import redis_connection

from threading import Thread
import datetime
import logging

logging.basicConfig(filename="activity_logs.txt", level=logging.INFO)

class Listener(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        pubsub = redis_connection.pubsub()
        pubsub.subscribe(["spam", "sign_out", "sign_in", "sign_up"])
        for item in pubsub.listen():
            if item["type"] == "message":
                log = f"({datetime.datetime.now()}) {item['data']}"
                logging.info(log)