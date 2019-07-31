class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self.__name = name
    # instance method
    def say_hi(self):
        print("hi {0}".format(self.__name))

class AdminUser(User):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say_hello(self):
        print("hello {0} ({1})".format(self._User__name, self.age))
    
    # override
    def say_hi(self):
        print("hi {0}".format(self._User__name))

def say_hi_global():
    print("HELLO, GLOBAL")