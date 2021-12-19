from typing import Dict
import yaml
import tweepy
import json


def load_yaml_config_for_tweepy(yaml_config_file: str) -> Dict[str, str]:
    """
    Loads the yaml config file for tweepy.
    """
    with open(yaml_config_file, "r") as yaml_file:
        config_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return config_dict


class TweetStream(tweepy.Stream):
    """
    A tweepy.Stream subclass that can be used to stream tweets from a Twitter
    account.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tweet_count = 0

    def on_data(self, data):
        """
        Overrides the on_status method of tweepy.Stream.
        """
        print(json.loads(data)["text"])

    def on_error(self, status_code):
        """
        Overrides the on_error method of tweepy.Stream.
        """
        print(f"Error: {status_code}")

    def on_connection_error(self):
        self.disconnect()
