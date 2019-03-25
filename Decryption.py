# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:44:17 2019

@author: aljas
Decryption using Dictionary
"""

alphabitDictionaryDecrypt={"E":"A", "F":"B", "G":"C", "H":"D", "I":"E",
           "J":"F", "K":"G", "L":"H", "M":"I", "N":"J",
           "O":"K", "P":"L", "Q":"M", "R":"N", "S":"O",
           "T":"P", "U":"Q", "V":"R", "W":"S", "X":"T",
           "Y":"U", "Z":"V", "A":"W", "B":"X", "C":"Y",
           "D":"Z", "4":"1", "5":"2", "6":"3",
           "7":"4", "8":"5", "9":"6", "0":"7", "1":"8",
           "2":"9", "3":"0", " ":" "}

telegramDecrypt=input("Translate your telegram: ").upper()
decryptedTelegram=""

for letters in telegramDecrypt:
    if letters in alphabitDictionaryDecrypt:
        decryptedTelegram+=alphabitDictionaryDecrypt[letters]
    else:
        decryptedTelegram+=letters

print(decryptedTelegram.lower())