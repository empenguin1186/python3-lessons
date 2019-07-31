# mypackage/user.py を import する
# import mypackage.user

# モジュールに別名をつける
# import mypackage.user as mymodule

# 特定のモジュールのみ import 
from mypackage.user import AdminUser, say_hi_global

class A:
    def say_a(self):
        print("A!")
    def say_hi(self):
        print("hi! from A!")

class B:
    def say_b(self):
        print("B!")
    def say_hi(self):
        print("hi! from B!")

class C(A, B):
    pass

bob = AdminUser("bob", 24)
bob.say_hello()
say_hi_global()
