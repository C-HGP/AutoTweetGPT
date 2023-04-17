import os
import requests
import openai
import configparser
import json
from requests_oauthlib import OAuth1Session
from time import sleep
print("Welcome to AutoTweetGPT.")

print("Reading config...")
# Read the config file
config = configparser.ConfigParser()
config.read('personalConfig.ini')
print("Done.")

print("Authenticating against Twitter API...")
# Set up the Twitter API
api_key = config['Twitter']['API_key']
api_key_secret = config['Twitter']['API_key_secret']
access_token = config['Twitter']['access_token']
access_token_secret = config['Twitter']['access_token_secret']
twitter = OAuth1Session(api_key, client_secret=api_key_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)
print("Done.")

print("Authenticating against OpenAI API...")
# Set up the OpenAI API
openai.api_key = config['OpenAI']['API_key']
print("Done.")

def generate_tweet(prompt, engine, temperature, max_tokens):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def post_tweet(tweet):
    url = 'https://api.twitter.com/2/tweets'
    headers = {'Content-Type': 'application/json'}
    data = {'text': tweet}
    response = twitter.post(url, headers=headers, data=json.dumps(data))

    if response.status_code != 201:
        raise Exception(f'Error posting tweet: {response.text}')
    else:
        print(f'Tweeted: {tweet}')

def main():
    interval = int(config['Settings']['interval'])
    temperature = float(config['Settings']['temperature'])
    max_tokens = int(config['Settings']['max_tokens'])
    engine = config['Settings']['engine']
    prompt = config['Settings']['prompt']

    while True:
        try:
            tweet = generate_tweet(prompt, engine, temperature, max_tokens)
            if len(tweet) <= 280:
                post_tweet(tweet)
            else:
                print(f"Generated tweet is too long: {tweet}")
            sleep(interval)
        except Exception as e:
            print(f'Error: {e}')
            sleep(interval)


if __name__ == '__main__':
    main()
