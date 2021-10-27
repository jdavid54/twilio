from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
from credentials_template import *

# ssid = ""
# authtoken = ""
# phonetocall = ""
# trialphone = ""

text = "C'est Jean Je t'envoie un SMS en python depuis Twilio pour test !"
#phonetocall = karim  # le numéro doit d'abord être vérifié dans twilio (Verified phone numbers)
client = Client(ssid,authtoken)
client.messages.create(to =[phonetocall], from_ =trialphone, body = text)