import os

from requests_oathlib import PAuth1Session

#Get the authentication infor fomr the enviromental vaulables
TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

#Get the OAuth1session object with the authentication

twitter = OAuth1Session(TWITTER_API_KEY,
                        client_secret=TWITTER_API_SECRET_KEY,
                        resource_owner_key=TWITTER_ACCESS_TOKEN
                        resource_owner_secret=TWITTER_ACCESS_TOKEN_SECRET)

# gete the user7s timeline
response = twitter.get('https://api.twitter.com/1.1/statuses/user_timeline.json')

# since the format of the time line is JSON, parse it with response.json() and get a list
# status is the dic that shows a tweet(in the twitter API, it's called status)

for status in response.json():
    print('@' + status['user']['screen_name'], status['text']) #shows the username and tweets
