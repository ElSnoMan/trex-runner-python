# trex-runner-python
We started this on stream, but please help me and Tiny Tim T-Rex make this better!

Also, subscribe to my channel for more awesome coding stuff!
https://twitch.tv/carloskidman

## Challenge
The challenge was to convert Java + Selenium code to Python + Pylenium so the Python viewers could play with the code and work on it.

Full credit for this goes to Sudharsan Selvaraj!

Here is the LinkedIn Post that started the challenge:
https://www.linkedin.com/posts/sudharsan-selvaraj_selenium-automation-seleniumtesting-activity-6668798318711336960-u18V

Here is the Github Repo with the Java code that I used as a reference:
https://github.com/sudharsan-selvaraj/chrome-dino-game-bot

## Setup

1. Clone the project
2. Install the Packages
    * Install `pipenv`
    
    ```bash
    pip install pipenv
   
    ---or---
   
    brew install pipenv
    ```

    * Install required packages

    ```bash
    pipenv install
    ```

3. Configure IDE to use `pytest`
4. That's it! Just run `test_trex_runner.py`

## Tiny Tim needs your help!

T-Rex is getting killed by clusters of `CACTUS_LARGE` obstacles... Can you solve this?

### TIPS

Inside of the `models` directory, there are example JSON files for the `obstacle` and `tRex` objects.

These are represented as pydantic models in `game.py`. That should give you enough data to see how you can calculate the best time to jump.

Good luck!
