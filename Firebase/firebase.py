# PUT DATA

from firebase import firebase
import time
firebase = firebase.FirebaseApplication('https://***.firebaseio.com/')
SECRET_KEY = ''

import random

while(1):
	x = (random.randint(0,9))
	sending_data = firebase.put("fire","fire",x)
	time.sleep(2)
	print(x)
	print("Data sent to firebase successfully")

# GET DATA

from firebase import firebase

firebase = firebase.FirebaseApplication('https://***.firebaseio.com/')
SECRET_KEY = ''

x = firebase.get('/fire/fire', None)

print(x)