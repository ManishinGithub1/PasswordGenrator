import string
import random

def generate_pass():
    s1= string.ascii_letters
    s2= string.digits
    s3= string.punctuation
    passlen=int(input("Enter the length of the password: \n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    random.shuffle(s)
    
    password = ("".join(s[0:passlen]))
    print("Your password is generated: ", password)


generate_pass()    
