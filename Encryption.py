# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:35:15 2019

@author: aljaser

Encryption using Dictionary
"""

alphabitDictionary={"A":"E", "B":"F", "C":"G", "D":"H", "E":"I",
           "F":"J", "G":"K", "H":"L", "I":"M", "J":"N",
           "K":"O", "L":"P", "M":"Q", "N":"R", "O":"S",
           "P":"T", "Q":"U", "R":"V", "S":"W", "T":"X",
           "U":"Y", "V":"Z", "W":"A", "X":"B", "Y":"C",
           "Z":"D", "1":"4", "2":"5", "3":"6",
           "4":"7", "5":"8","6":"9","7":"0","8":"1",
           "9":"2","0":"3", " ":" "}

telegram=input("Send your telegram: ").upper()
encryptedTelegram=""

for letters in telegram:
    if letters in alphabitDictionary:
        encryptedTelegram+=alphabitDictionary[letters]
    else:
        encryptedTelegram+=letters

print(encryptedTelegram.lower())



