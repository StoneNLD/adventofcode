#!/usr/bin/python3

import hashlib

inputkey = "bgvyzdsv"

for number in range(100000000000000):
    hash = hashlib.md5((inputkey+str(number)).encode()).hexdigest()
    if hash[0:5] == 5*"0":
        print("found 5 starting zero's with number: ", number)
        print(hash)
        if hash[0:6] == 6*"0":
            print("found 6 starting zero's with number: ", number)
            print(hash)
            break
