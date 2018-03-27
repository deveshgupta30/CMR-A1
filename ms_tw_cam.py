from gpiozero import MotionSensor
import time
import tweepy
import os
pir=MotionSensor(4)
time.sleep(3)
if pir.motion_detected:
	print("Motion detected!")
	consumer_key= ''
	consumer_secret= ''
	access_token= ''
	access_token_secret= ''
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api=tweepy.API(auth)
	img="/home/cs2017a115/Desktop/imgforTwitter.jpg"
  cmd="fswebcam -r 1280x720 -S 3 --jpeg 100 "+img
  os.system(cmd)
  print("pic taken")
  api.update_with_media(img, status="Can this world be more complex?")
  print("Uploaded")
else:
print("Eh! No Motion detected!")
