email = input("Enter your email : ") #g@g.in/com
k ,j, d = 0, 0, 0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-3]==".") ^ (email[-4]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                        break
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                       d=1
                if k==1 or j==1 or d==1:
                        print("Invalid Email 5")
                else:
                    print("Right Email")        
            else:
                print("Invalid Email 4")
        else:
            print("Invalide Email 3")
    else:
        print("Invalid Email 2")
else:
    print("Invalid Email 1")