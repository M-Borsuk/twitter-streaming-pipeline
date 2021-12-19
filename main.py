import argparse
import twitter_scraper_utils as utils

# Parse arguments
parser = argparse.ArgumentParser(description="Twitter Scraper")
parser.add_argument("--config", type=str, help="Path to the config file.")
parser.add_argument("--keywords", type=str, help="Keywords to search for.")

if __name__ == "__main__":
    args = parser.parse_args()
    config_dict = utils.load_yaml_config_for_tweepy(args.config)
    stream = utils.TweetStream(config_dict["consumer_key"],config_dict["consumer_secret"],config_dict["access_token"],config_dict["access_token_secret"])
    stream.filter(track=[args.keywords])
