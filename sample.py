class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name
    # instance method
    def say_hi(self):
        print("hi {0}".format(self.name))
    
    # class method
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

tom.say_hi()
bob.say_hi()
User.show_info()