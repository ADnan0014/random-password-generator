import random
import string

pass_len = int(input("Enter password length: "))
charValues = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choices(charValues, k=pass_len))
print("Your random password is:", password)
