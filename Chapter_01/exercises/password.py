password = input("Create a password: ").strip()
if len(password)>= 6 and password.isalnum():
    print("Password meets security standards!")
else:
    print("Weak,Must be 6+ characters and letters/numbers only.")
