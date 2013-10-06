__author__ = 'Messivite'
from boto.ses import SESConnection
import json
class AmazonSES(object):
    EMPTY_EMAIL = "Email adress parameter is empty"
    TEMPLATE_NOT_FOUND = "Email template not found!"
    @classmethod
    def __init__(self,AWS_KEY,AWS_SECRET_KEY):
        self.connection = SESConnection(aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
        self.mimeType = "text"

    def replaceContent(self,content,param):
        for k,v in param.iteritems():
            content = content.replace(k,v)
        return content

    def sendEmail(self,email=None,subject=None,param=None,to_addresses=None,templatePath=None):
        print email
        print templatePath + " sss"
        if not self.connection:
            raise Exception, 'No connection found'

        if templatePath is None:
            raise Exception, "Please set to email template!"

        if email is None:
            result = {"status":"error","msg":self.EMPTY_EMAIL}
            result = self.jsonOutput(result)
            print result
            return result

        file = self.isReadFile(templatePath)
        if file is not False:
            if param is not None:
                message = self.replaceContent(file,param)
            else:
                message = file
        else:
            result = {"status":"error","msg":self.TEMPLATE_NOT_FOUND}
            result = self.jsonOutput(result)
            print result
            return result

        to_addresses = to_addresses

        print self.connection.send_email(email, subject, message,to_addresses ,None,None, self.mimeType, None, None)

    # template file is readable?
    # return string , bool
    def isReadFile(self,file):
        file = open(file).read()
        if file is not None:
            return file
        else:
            return False
    #email setting mimeType
    # default text
    def setMimeType(self,type):
        types = ["text","html"]
        if type in types:
            self.mimeType = type
        else:
            self.mimeType = "text";

    # print jsonOutput function
    def jsonOutput(self,dict):
        output = json.dumps(dict)
        return output