import os
import time
import tweepy
consumer_key= 'IrQcPnoAwMMoxeXaXMzzvR72E'
consumer_secret= 'cDZxcCxJIviqf4DvSKdDHwIOeeNjlAG5TSIBTvWFXqdqvB38xc'
access_token= '967252345133457409-7V7tTvuBQZd1KBThsLwb4X7dSgyZXu7'
access_token_secret= '0z2cYXWWDa211EDeu0BLyvJLQ1BFlheUZrLWj00jacmSJ'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/cs2017a115/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -r 1280x720 -S 3 --jpeg 100 "+img
    os.system(cmd)
    print("pic taken")
    api.update_with_media(img, status="lol")
    print("wait")
    time.sleep(3)
    a+=1
    b+=1
    print("done")
