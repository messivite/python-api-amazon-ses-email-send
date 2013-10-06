__author__ = 'Messivite'


class Spam(object):
    @classmethod
    def parrot(cls,message):
        print cls.__name__, "says:", message
class Eggs(Spam):
    @classmethod
    def parrot(cls,message):
        super(Eggs,cls).parrot(message)
        pass


object = Eggs()
print object.parrot("I LOVE PYTHON")