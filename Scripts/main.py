import openai
import tweepy
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

# Twitter API keys and access tokens
auth = tweepy.OAuthHandler(config['Twitter']['consumer_key'], config['Twitter']['consumer_secret'])
auth.set_access_token(config['Twitter']['access_token'], config['Twitter']['access_token_secret'])
api = tweepy.API(auth)

# OpenAI API key and GPT-3 parameters
openai.api_key = config['OpenAI']['api_key']
interval = int(config['AutoTweetGen']['interval'])
temperature = float(config['AutoTweetGen']['temperature'])
max_tokens = int(config['AutoTweetGen']['max_tokens'])
engine = config['AutoTweetGen']['engine']
prompt = config['AutoTweetGen']['prompt']

def generate_tweet():
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    tweet = response.choices[0].text.strip()
    return tweet

while True:
    tweet = generate_tweet()
    api.update_status(tweet)
    print('Tweeted:', tweet)
    time.sleep(interval)
