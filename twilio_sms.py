from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
# import from external file 
from credentials_template import *

# or enter here your credentials
# ssid = ""
# authtoken = ""
# phonetocall = ""
# trialphone = ""

text = "This is me ! Hello World"
#phonetocall = karim  # must be a verified phone numbers in your twilio account
client = Client(ssid,authtoken)
client.messages.create(to =[phonetocall], from_ =trialphone, body = text)
