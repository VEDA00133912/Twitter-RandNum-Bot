import schedule
import time
import random
import os
import tweepy
from dotenv import load_dotenv

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

post_random_number()

schedule.every(90).minutes.do(post_random_number)

while True:
    schedule.run_pending()
    time.sleep(30)
