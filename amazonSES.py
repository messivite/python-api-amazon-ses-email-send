__author__ = 'Mustafa Aksoy'
from amazonMain import *
AWS_KEY = "AKIAIIHDRM67ZNIY7UUA"
AWS_SECRET_KEY = "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"

to_addresses = ["kendinizle@gmail.com","ayseedremitoglu35@gmail.com"]
templatePath = "templates/test.html"
subject = "This is a test subject string!"
param = {"{deneme}":"MUSTAFA"}
sender = "senderemailadress@blabla.com"

obj = AmazonSES(AWS_KEY,AWS_SECRET_KEY)
obj.setMimeType("html")
print obj.sendEmail(sender,subject,param,to_addresses,templatePath);

