__author__ = 'Mustafa Aksoy'
from amazonMain import *
AWS_KEY = ""
AWS_SECRET_KEY = ""

to_addresses = ["email1@blabla.com","email2@blaba.com"]
templatePath = "templates/test.html"
subject = "This is a test subject string!"
param = {"{deneme}":"MUSTAFA"}
sender = "senderemailadress@blabla.com"

obj = AmazonSES(AWS_KEY,AWS_SECRET_KEY)
obj.setMimeType("html")
print obj.sendEmail(sender,subject,param,to_addresses,templatePath);

