import smtplib
from random import randint 
import os 

loginID = randint(999,9999)


def startMail():
    '''
    Sender Email needs to be a Gmail address because we are using Google's SMTP
    Create a dummy gmail account for sender_email because this will be the account we use for sending our security code. 
    '''
    
    
    sender_email = "yourEmail@gmail.com" 
    rec_email = "receiverEmail@ttu.edu"
    
    login  = "password for sender_email"
    message = ("Wassup my guy your login code is {}".format(loginID))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, login)

    server.sendmail(sender_email, rec_email, message)

 
def checkCode():
    print("Wassup bro whats your code? You only have 3 tries.")
    os.system("shutdown -s -t 30 -c \" \" ")
    x = 0
    while (x < 3):
        codeID = int(input("Code: "))
        if (codeID == loginID):
            os.system("shutdown -a")
            break
        else:
            x += 1




if __name__ == "__main__":
    startMail()
    checkCode()





