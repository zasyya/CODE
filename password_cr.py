
import random


print("ŞİFRE OLUŞTURUCU")

password_chaerechters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
created_password = ""

uzunluk = int(input ("şifreniz kaç harf uzunluğunda olsun"))

for i in range (uzunluk):
    created_password += random.choice  (password_chaerechters) 

print ("ŞİFRENİZ:")


print (created_password)
