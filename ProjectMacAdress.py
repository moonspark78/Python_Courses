import random
# D8-43-AE-CE-16-43

def mac_gen():
    macaddr = ""
    counter = 0
    charset= "1234567890abcdef"
    for i in range(1, 12 +1):
        macaddr = macaddr + random.choice(charset)