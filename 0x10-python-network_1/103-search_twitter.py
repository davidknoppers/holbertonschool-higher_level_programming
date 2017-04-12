#!/usr/bin/python3
"""
Takes in 3 strings and sends a search request to the Twitter API
"""
import base64
import requests
import sys


if __name__ == "__main__":
    consumer_key = sys.argv[1]
    consumer_secret = sys.argv[2]
    hashtag = sys.argv[3]
    hashtag = hashtag.replace("#", "23")
    url = "https://api.twitter.com/1.1/search/tweets.json?q=%" + hashtag
    credentials = base64.b64encode(
        ("{}:{}".format(sys.argv[1], sys.argv[2])).encode('ascii'))
    headers = {
        'Authorization': 'Basic {}'.format(credentials.decode('ascii')),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    data = {'grant_type': 'client_credentials'}
    token_response = requests.post("https://api.twitter.com/oauth2/token",
                                   headers=headers, data=data)
    token = dict(token_response.json())["access_token"]
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    r = requests.get(url, headers=headers)
    tweets = dict(r.json())
    i = 1
    for tweet in tweets['statuses']:
        print("[{}] {} by {}".format(tweet['id_str'], tweet['text'],
                                     tweet['user']['name']))
        i += 1
        if i == 5:
            break
