import schedule
import time
import random
import os
import tweepy
import threading
from dotenv import load_dotenv
from bottle import route, run

load_dotenv()

client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

def post_random_number():
    try:
        digits = random.randint(1, 140)
        n = random.randint(10**(digits-1), 10**digits - 1)

        client.create_tweet(text=str(n))
        print(f"✅ posted: {n}")
    except Exception as e:
        print("❌ error:", e)

# 起動時に1回ツイート
post_random_number()

schedule.every(90).minutes.do(post_random_number)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(30)

threading.Thread(target=run_scheduler, daemon=True).start()

@route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    run(host="0.0.0.0", port=5000, debug=True)
