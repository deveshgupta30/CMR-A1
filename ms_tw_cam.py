from gpiozero import MotionSensor
import time
import tweepy
import os
pir=MotionSensor(4)
time.sleep(3)
if pir.motion_detected:
	print("Motion detected!")
	consumer_key= 'IrQcPnoAwMMoxeXaXMzzvR72E'
	consumer_secret= 'cDZxcCxJIviqf4DvSKdDHwIOeeNjlAG5TSIBTvWFXqdqvB38xc'
	access_token= '967252345133457409-7V7tTvuBQZd1KBThsLwb4X7dSgyZXu7'
	access_token_secret= '0z2cYXWWDa211EDeu0BLyvJLQ1BFlheUZrLWj00jacmSJ'
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api=tweepy.API(auth)
	img="/home/cs2017a115/Desktop/imgforTwitter.jpg"
  cmd="fswebcam -r 1280x720 -S 3 --jpeg 100 "+img
  os.system(cmd)
  print("pic taken")
  api.update_with_media(img, status="Can this world be more complex?")
  print("Uploaded")
else
	print("Eh! No Motion detected!")
