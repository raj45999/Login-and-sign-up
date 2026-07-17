#importing json for file amanagement
import json

#making a class for storing details
class details:
    def __init__(self,name,email,password,customer_id):
        self.name=name
        self.customer_id=int(customer_id)
        self.email=email
        self.password=password



print()
print("---------------------------------")
print("Hello, Welcome to XYZ company")
print("---------------------------------")
print()

file_name="login_details.json"

#try except block to detect number of users already register and genrating new id
try:
    with open(file_name,"r") as file:
        data= json.load(file)
        customer_id=len(data)+1
except:
    customer_id=1
    data=[]


print()
print("---------------------------------")

#login and signup options
Login_or_signup = int(input("Enter 1 for login or 2 for signup: "))

if Login_or_signup==1 or 2:
    #if user choose for login
    found=False
    if Login_or_signup == 1:
        login_email=input("Enter email: ")#asking for email
        for i in data:#checking every for email matching by user's giver email
                if login_email==i["email"]:
                    found=True
                    #asking for password
                    n=3
                    while True:#while loop for 3 attempts
                        if n==0:#if all attempts are over
                            print("Too many failed attempts. Try again later.")
                            break

                        login_password=input("Enter password: ")

                        #asking for password
                        if i['password']==login_password:
                            #if password matches
                            print("Login Successfully")
                            break

                        #if passowrd doesnt match
                        else:
                            n=n-1
                            if n!=0:
                                print(f"Incorrect Password!! {n} Attempts left..")
        if found==False:
            #if email doesnt matches to any user
            print("Email not found!! try again")
    print()
    print("---------------------------------")



    if Login_or_signup==2:
        #if new user appears and choose for signup
        name=input("Enter name: ")
        email=input("Enter email: ")
        password=input("Enter password: ")
        customer=details(name,email,password,customer_id)
        data.append(customer.__dict__)

        with open(file_name,"w") as fh:
            json.dump(data, fh, indent = 4)
        print()
        print("---------------------------------")
else:
    print("Invalid choice")