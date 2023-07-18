import random, string
passwrd = ''
for x in range(random.randrange(12,15)):
    passwrd += random.choice(string.ascii_letters + string.digits + string.punctuation)
print (passwrd)