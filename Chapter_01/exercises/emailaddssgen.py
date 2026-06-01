#take 3 letters of first name,last two digits of birth yr,entire last name for username gen
#take the username generated and append @university.edu to generate email address
firstname=input("Enter your First Name: ")
lastname=input("Enter your Last Name: ")
birthyr=int(input("Enter your Birth Year: "))
username=firstname[0:3].lower()+str(birthyr)[-2:]+lastname.lower()
email=username+"@university.edu"
print("Your Username is: ",username)
print("Your Email Address is: ",email)