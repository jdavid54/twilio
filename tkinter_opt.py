from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
from credentials import *     # first create credentials.py from credentials_template.py

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x500')
        self.resizable(False, False)
        self.n=random.randint(10000,99999)
        print('OTP=',self.n)
        self.client=Client(ssid,authtoken)
        self.client.messages.create(to =[phonetocall], from_ =trialphone, body = self.n)
        
        self.Labels()
        self.Entry()
        self.Buttons()
        
    def Labels(self):
        self.c = Canvas(self,bg="white", width=400, height=280)
        self.c.place(x=100, y=60)
        
        self.Login_Title=Label(self, text="OTP Verification", font="bold, 20",bg="white")
        self.Login_Title.place(x=210,y=90)
    
    def Entry(self): #, hightlightthickness=0,
        self.User_Name=Text(self, borderwidth=2, wrap="word", width=29, height=2)
        self.User_Name.place(x=190, y=160)

    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="submit.png")
        self.submitButton=Button(self, image=self.submitButtonImage, command=self.checkOTP, border=0)
        self.submitButton.place(x=250, y=240)
        
        self.resendOTPImage=PhotoImage(file="resendotp.png")
        self.resendOTP=Button(self, image=self.resendOTPImage, command=self.resendOTP, border=0)
        self.resendOTP.place(x=250, y=400)
    
    def checkOTP(self):
        print('>>checking')
        try:
            self.userInput=int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo", "Login success")
                self.n = "logged"
            elif self.n == "logged":
                messagebox.showinfo("showinfo", "You are already logged in")
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except:
            messagebox.showinfo("showinfo", "INVALID OTP")
        
    
    def resendOTP(self):
        print('<<resend')
        self.n=random.randint(1000,9999)
        self.client=Client(ssid,authtoken)
        self.client.messages.create(to =[phonetocall], from_ =trialphone, body = self.n)
        print('OTP=',self.n)
        
if __name__ == "__main__":
    window=otp_verifier()    
    window.mainloop()