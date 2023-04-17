# [WIP] AutoTweetGPT
AutoTweetGen is a Python script that automates the process of generating and posting tweets using GPT, allowing for easy and efficient content creation on Twitter. With AutoTweetGen, you can generate and post tweets automatically, freeing up time and energy for other tasks.

## Getting started

To use AutoTweetGen, you'll need to have a Twitter developer account and an OpenAI API key. You'll also need to install the necessary Python packages. Here's how to get started:

- Clone this repository to your local machine.
- Install the required packages by running pip install -r requirements.txt.
- Create a new Twitter app and obtain your API keys and access tokens. You can find instructions on how to do this in Twitter's documentation.
- Obtain your OpenAI API key. You can sign up for an account and obtain an API key on the OpenAI website.
- Replace the placeholders in config.ini with your Twitter and OpenAI API keys and tokens.
- Customize the prompt in tweet.py to generate the type of content you want to tweet.
- Run python tweet.py to start generating and posting tweets automatically.

## Configuration

You can customize the behavior of AutoTweetGen using the config.ini file. Here's what the different settings do:

- interval: The interval between tweets, in seconds.
- temperature: The "temperature" parameter for the GPT-3 model, which controls the level of randomness in the generated text. Higher values result in more creative and -- unpredictable output, while lower values result in more predictable and conservative output.
- max_tokens: The maximum number of tokens to generate for each tweet.
- engine: The name of the GPT-3 engine to use. By default, AutoTweetGen uses the davinci engine, which is the most powerful and expensive one.
- prompt: The prompt to use for generating tweets. You can customize this to generate different types of content.

## Contributing

If you'd like to contribute to AutoTweetGen, feel free to fork this repository and submit a pull request. You can also open an issue if you have any suggestions or feedback.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
