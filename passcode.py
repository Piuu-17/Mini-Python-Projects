import random
import string
newString= string.ascii_letters+string.digits+string.punctuation
pass_len=6

pass_code=""
for i in range(pass_len):
    pass_code+= random.choice(newString)

print("Your random password is", pass_code)