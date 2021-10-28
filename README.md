# twilio

### A) Credentials file :

 * 1) From credentials_template.py, create credentials.py with your ssid, authtoken, trialphone from twilio account.

* 2) Manage all your verified phone numbers in your twilio account.

Then add me = yourphonenumber or somebodyelse = someonephonenumber

Et voilà !

### B) SMS
Send SMS with twilio_sms.py

you can import or change phonetocall as you want

### C) OPT with tkinter GUI 

Check OPT with tkinter_opt.py

The trialnumber wil send an  one-time password (OPT) to your phonetocal. The OTP is a number with 4 digits.

The phonetocall receiver then has to open verification GUI with tkinter_opt.py and check in the number to log in.

### D) Login calling opt validation 

Login and OPT validation with tkinter_opt_login.py

A first window let you enter your login name which will set varaible phonetocal.

A validation OPT window will be opened to check authentication by sending OPT to the login name phone.
