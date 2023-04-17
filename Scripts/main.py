import os
import requests
import openai
import configparser
import json
from time import sleep

print('Welcome to AutoTweetGPT.')

print('Reading config...')
# Read the config file
config = configparser.ConfigParser()
config.read('personalConfig.ini')
print('Done.')

print('Authenticating against TwitterAPI...')
# Set up the Twitter API
bearer_token = config['Twitter']['bearer_token']
print('Done.')

print('Authenticating against OpenAI...')
# Set up the OpenAI API
openai.api_key = config['OpenAI']['API_key']
print('Done.')

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

def post_tweet(bearer_token, tweet):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json',
    }

    data = {
        'status': tweet
    }

    response = requests.post('https://api.twitter.com/2/tweets', headers=headers, data=json.dumps(data))

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
            post_tweet(bearer_token, tweet)
            sleep(interval)
        except Exception as e:
            print(f'Error: {e}')
            sleep(interval)

if __name__ == '__main__':
    main()
