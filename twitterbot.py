import tweepy
import time
import tweetreplies
import random

#Input the consumer, access and secret keys generated for your Twitter Developer account.
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file_name = 'latest_id.txt'

def get_latest_id(file_name):
    f_read = open(file_name, 'r')
    latest_id = int(f_read.read().strip())
    f_read.close()
    return latest_id

def store_latest_id(latest_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(latest_id))
    f_write.close()
    return

def tweetReply():
    print('Retweeting in progress...')
    latest_id = get_latest_id(file_name)
    mentions = api.mentions_timeline(latest_id, 
    tweet_mode='extended')

    for mention in reversed(mentions):
        i = random.randint(0,9)
        print(str(mention.id) + ' - ' + mention.full_text)
        latest_id = mention.id
        store_latest_id(latest_id, file_name)
    
        if '#hellogurv' in mention.full_text.lower():
            print("found #hellogurv")
            print("Responding...")
            api.update_status('@' + mention.user.screen_name + 
            tweetreplies.replies[i], mention.id)

while True:
    tweetReply()
    time.sleep(15)

