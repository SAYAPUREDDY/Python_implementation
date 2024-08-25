import random
import string

choice=str(input(f"weak or strong"))
characters=["!","2","#","$","%","^","&","*","~"]
# weak=8
# strong=16
def choosing(choice):
    if choice=="weak":
        return "weak password"
    elif choice=="strong":
        return "strong password"
    else:
        raise Exception ("pick one from weak and strong")
    
def upper_case():
    type_password=choosing(choice)
    length=2
    password=str()
    if type_password=="strong password":
        password=''.join(random.choices(string.ascii_uppercase,k=length))
        return password
    else:
        return password
    
#print(upper_case())

def other_letters():
    password=upper_case()
    #print(strong_password)
    if password!="":
        password+=''.join(random.choices(string.ascii_lowercase,k=7))
        return password
    else:
        password+=''.join(random.choices(string.ascii_lowercase,k=9))
        return password
    
#print(other_letters())

def special_characters():
    characters=["!","@","#","$","%","^","&","*","~"]
    password=other_letters()
    if any(ele.isupper() for ele in password):
        password+=''.join(random.sample(characters,3))
        return password
    else:
        password+=''.join(random.sample(characters,1))
        return password
    
#print(special_characters())

def password_generator():
    password=special_characters()
    if int(len(password))==12:
        password+=''.join(str(random.randint(0,9)) for i in range(3))
        return password
    else:
        password+=''.join(str(random.randint(0,9)) for i in range(2))
        return password
    
print(password_generator())
    



# def password_generator():
#     while True:
