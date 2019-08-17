# はじめてのPythonプログラム

sample.py
```Python
# コメントは先頭に#をつける

"""
複数行にコメントするときはダブル/シングルクォーテーション3つ
"""

# Python3系ではprintは括弧とダブル/シングルクォーテーションをつける
print("Hello World")
```

# 変数を使ってみよう

```Python
# 変数代入
msg = "Hello World"

# Pythonは値の再代入を禁止することはできないが、大文字の変数は暗黙的に再代入を行わない慣習となっている

ADMIN_EMAIL = "hoge@gmail.com"

print(msg)
```

# さまざまなデータを扱ってみよう

```python

# \n は改行 \t はタブ
s = "he\nllo wor\tld"
html = """<html><body>
<body>
<html>"""

# 整数
i = 10

# 浮動小数点
f = 23.4

# 論理値
flag = False # or True

print(s)
print(html)
print(i)
print(f)
print(flag)
```

# さまざまなデータを扱ってみよう

```python
i = 10

# べき乗
print(i**2) # 100

# 切り捨て
print(i//3) # 3

# 他の言語でおなじみの += も使用できる
y = 10 
y += 10
print(y) # 20

# 論理値には and or notを使用
print(True and False) # False
print(True or False) # True
print(not True) # False

# 文字列も*で繰り返しが可能
print("hello" * 3) # hellohellohello
```

# 文字列に値を埋め込んでみよう

```python
name = "hoge"
score = 50.3

"""
文字列型は%s, 浮動小数点は%f
%10sは右揃えで10桁、%-10.2fは左揃えで10桁で小数点第二位まで
"""
print("name: %10s, score: %-10.2f" % (name, score))

"""
{0} -> .format()関数の第一引数に対応
{1} -> .format()関数の第二引数に対応
>10sは右揃えで10桁、<10.2fは左揃えで10桁で小数点第二位まで
"""
print("name: {0:>10s}, score: {1:<10.2f}".format(name, score)
```

# ifで条件分岐をしてみよう

```python
score = int(input("score ? "))

if score > 80:
    print("Great!")
elif score > 60:
    print("Good!")
else:
    print("so so ...")

"""
条件演算子
if ... else ... で値を返す場合以下の記法が使用できる
"""
print("Great!" if score > 80 else "so so ...")
```

# whileでループ処理をしてみよう
while文は他の言語での実装と相違ないが、else句はwhileの条件がはじめてFalseになった場合に呼ばれる
```python
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("end")
```

実行結果
```
0
1
2
3
4
5
6
7
8
9
end
```

breakで抜けた場合はelse句の処理は行われない
```python
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
else:
    print("end")
```

実行結果
```
0
1
2
3
4
```

# for で繰り返し処理をしてみよう
前項の while の処理とほぼ同じ
範囲指定は`range`を使用する。
```python
for i in range(0,10): # この場合範囲は [0,10) また、0始まりの場合は単にrange(0)で良い
    print(i)
else:  # while と同じ
    print("end")
```

実行結果
```shell
0
1
2
3
4
5
6
7
8
9
end
```

# 関数を作ってみよう

`def`を使って関数を自作する
```python
def say_hi(name, age = 20): # 引数には初期値を与えることができる
    print("hi {0} ({1})".format(name, age))

say_hi("tom", 23)
say_hi("bob", 21)
say_hi("steeve")
say_hi(age = 10, name = "rick") # 引数名を指定した呼び方もできる
```

実行結果
```
hi tom (23)
hi bob (21)
hi steeve (20)
hi rick (10)
```

# 関数の返り値を使ってみよう
それから関数の中身が何もなかった場合、もしくは後で書くので何か書いておきたい場合は pass というキーワードが使える

```python
def say_hi():
    pass

msg = say_hi()
print(msg)
```

実行結果
```shell
None
```

ちなみに関数に何も書かないで実行しようとするとエラーが発生する
```python
def say_hi():

msg = say_hi()
print(msg)
```

実行結果
```shell
    msg = say_hi()
      ^
IndentationError: expected an indented block
```

# 変数のスコープを理解しよう

以下のコードでは関数でグローバル変数を変更することはできない
```python
msg = "hello"

def say_hi():
    msg = "hello global"
    print(msg)

say_hi()
print(msg)
```

実行結果
```shell
hello global
hello
```

関数からグローバル変数を変更したい場合は`global`修飾子を使う
```python
msg = "hello"

def say_hi():
    global msg # global 変数の 'msg'を使用するという宣言
    msg = "hello global"
    print(msg)

say_hi()
print(msg)
```

実行結果
```shell
hello global
hello global
```

# クラスを作ってみよう

クラスを作るには以下のように記述する
```python
class User:
    pass # 何も設定されていないクラス

tom = User() # Java と違って new は必要ない
tom.name = "tom" # フィールドに値をセット。クラスの設定とは関係なく自由にセットすることができる
tom.score = 20

bob = User()
bob.name = "bob"
bob.level = 5

print(tom.name)
print(bob.level)
```

実行結果
```
tom
5
```

# コンストラクタを使ってみよう
ここがJavaと少し違うところ。コンストラクタは`__init__`で定義する

```python
class User:
    def __init__(self, name): # self は Javaでいうthisみたいなもの
        self.name = name # このクラスのフィールドにはnameが存在するということを表す

tom = User("tom")
bob = User("bob")

print(tom.name)
print(bob.name)
```

実行結果
```
tom
bob
```

# クラス変数を使ってみよう
先ほどのクラスごとに定義できる`name`のような変数はインスタンス変数と呼ぶ
一方でクラス単位で定義している変数のことをクラス変数と呼ぶ
クラス変数は各インスタンスで共通の値を持つ

```python
class User:
    count = 0 # クラス変数
    def __init__(self, name):
        User.count += 1
        self.name = name

print(User.count)
tom = User("tom")
bob = User("bob")
print(User.count)

print(tom.count) # インスタンス変数で count が定義されていなければクラス変数の値が参照される
```

実行結果
```shell
0
2
2
```

# メソッドを使ってみよう
メソッドにはインスタンス変数を用いたインスタンスメソッドとクラス変数を用いたクラスメソッドの2種類が存在する

```python
class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name

    # instance method
    def say_hi(self):
        print("hi {0}".format(self.name))
    
    # class method
    @classmethod # デコレータと呼ばれる
    def show_info(cls): # 特殊な変数である cls を使用する. これでクラス変数にアクセスできる
        print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

tom.say_hi()
bob.say_hi()
User.show_info()
```

実行結果
```shell
hi tom
hi bob
2 instances
```

# アクセス制限をしてみよう

python3 では private のような修飾子は存在しないが、フィールド名の前にに `_` をつけることであたかも private で扱うような慣習が存在する

```python
class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self._name = name
    # instance method
    def say_hi(self):
        print("hi {0}".format(self.name))
    
    # class method
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

bob = User("bob")
print(bob._name)
```

しかし慣習なので実際にはアクセスできてしまう
```shell
bob
```

アクセスを制限するにはフィールド名の前に `__` をつけることで実現できるのだが、例外が存在する

```python
class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self.__name = name
    # instance method
    def say_hi(self):
        print("hi {0}".format(self.name))
    
    # class method
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

bob = User("bob")
# print(bob.__name) エラーが発生する
print(bob._User__name) # bob
```
instance._<Class名>__<field名> でたとえフィールド名に`__`がついていてもアクセスできてしまう

実行結果
```
bob
```

# クラスを継承してみよう

クラスの継承は以下のように実装する。またメソッドのオーバーライドも可能
```python
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
        # 親クラスのprivate?フィールドを参照するには_<親クラス>__<field>と記述する
        print("hello {0} ({1})".format(self._User__name, self.age))
    
    # override
    def say_hi(self):
        print("hi {0}".format(self.__name))

bob = AdminUser("bob", 23)
bob.say_hello()
```

実行結果
```shell
hello bob (23)
```

# クラスの多重継承について

python3 ではクラスの多重継承が可能。え
```python
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

c = C()
c.say_a()
c.say_b()
c.say_hi() # 同じメソッドが存在した場合は継承の際に先に指定されたクラスのメソッドが呼ばれる
```

実行結果
```
A!
B!
hi! from A!
```

# モジュールによるファイル分割

```shell
$ tree
├── sample.py
└── user.py
```

user.py
```python
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
```

sample.py
```python
# ファイル全体を import したい時
# import user

# ファイル内の特定のモジュールを import したい時
from user import User, AdminUser, say_hi_global #クラスだけでなくメソッドも import できる

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
```

```shell
$ python3 sample.py
hello bob (24)
HELLO, GLOBAL
```

# パッケージを利用したモジュール管理

ファイルが複数になってくるとそれを逐一 import するのは手間がかかるので、パッケージを使って使用するモジュールを import しやすくする。今回は`mypackage`配下のモジュールを import してみる  
ファイル構成は以下の通り
```shell
$ tree
.
├── README.md
├── __pycache__
│   └── user.cpython-37.pyc
├── mypackage
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── user.cpython-37.pyc
│   └── user.py
└── sample.py
```
__init__.py に関してはパッケージを作る上で必要なファイルとなるが、内容自体は何も書かなくてよい(なくても動いたけど...)

```python
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
```
user.py の内容は前項と同じであるため省略

```shell
$ python3 sample.py
hello bob (24)
HELLO, GLOBAL
```

# 例外処理の実装方法

例外処理はJavaと似ている
```python
# (1)
class MyException(Exception):
    pass

def div(a, b):
    try: # (2)
        if (b < 0):
            raise MyException("not minus") # (3)
        print(a/b)
    except ZeroDivisionError: # (4)
        print("not by zero!")
    except MyException as e: # (5)
        print(e)
    else:
        print("no exception!") # (6)
    finally:
        print("-- end --") # (7)

div(10, 3)
div(10, 0)
div(10, -1)
```

| No | 内容 |
|:----:|-----|
|(1)|例外を自作する場合は Exception を継承する|
|(2)|tryで例外処理を始める|
|(3)|例外を発生させる場合は `raise` を使う。またコンストラクタの引数はエラーメッセージ|
|(4)|例外を捉えるには`except`を使う|
|(5)|捉えた例外は変数として宣言できる|
|(6)|例外が発生せずに処理が完了したのちに呼ばれる|
|(7)|例外の発生の有無に関わらずに実行される|

実行結果
```shell
3.3333333333333335
no exception!
-- end --
division by zero
-- end --
not minus
-- end --
```

# リスト型

```py
hoge = [40, 50]

# 要素数
print(len(hoge)) # 2

# 要素追加
hoge.append(1000)
print(len(hoge)) # 3

# for 文との併用
for el in hoge:
    print(el)

# enumerate によるインデックスの取得
for i, el in enumerate(hoge):
    print("{0}: {1}".format(i, el))
```

# タプル

```py
hoge = (10, "foo", 33.4)
print(hoge[1])

# 値の再代入は不可能
hoge[1] = 50

# tuple -> list
fuga = list((10, 20, 30))

# list -> tuple
piyo = tuple(["one", "two", "three"])
```

# リストのスライス

```py
hoge = ["one", "two", "three", "four", "five"]

print(hoge[2:]) # ["three", "four", "five"]
print(hoge[:2]) # ["one", "two"]
print(hoge[1:4]) # ["two", "three", "four"]
print(hoge[-2:]) # ["four", "five"]

fuga = "happy"
print(fuga[1:]) # appy
```

# 集合型

```py
hoge = {1, 2, 3, 1}
print(hoge)
print(2 in hoge)

# 値追加&削除
hoge.add(4)
hoge.remove(1)
print(len(hoge))
print(hoge)

fuga = {4, 5, 6}

# 和集合
print(hoge | fuga)

# 積集合
print(hoge & fuga)

# 差集合
print(hoge - fuga)
```

# 辞書型

```py
# 定義
hoge = {"foo": 200, "bar": 400}
print(hoge["foo"])

# 値の更新は可能
hoge["foo"] = 300

# 追加&削除も可能
hoge["baz"] = 500
del(hoge["bar"])

print(hoge)

# ループ処理では items() 関数で key, value の値を取得することが可能
for key, value in hoge.items():
    print("{0}: {1}".format(key, value))
```

# イテレータ

```py
hoge = [40, 50, 70, 90, 60]

it = iter(hoge)

print(next(it)) # 40
print(next(it)) # 50
print("foo")
print(next(it)) # 70

# iterator を返すジェネレータオブジェクトを作成することが可能
def get_index():
    i = 0
    while True:
        yield i * 2
        i += 1

for el in get_index():
    if el == 10:
        break
    else:
        print(el)
```

# map, lambda

```py
def double(n):
    return n * 2;

# map(適用させたい関数, 適用対象のイテレータ) で各要素に処理を施し、ジェネレータを返す
print(list(map(double, [1,2,3])))

# lambda で Java の無名関数っぽい書き方ができる
print(list(map(lambda n: n * 2, [1,2,3])))

# ジェネレータを返すので for 文などで応用することが可能
for i in map(double, [2,3,4]):
    print(i)
```

# filter

```py
# filter(関数, イテレータ) で条件にマッチした要素を取り出すことが可能

def even(n):
    return n % 2 == 0

print(list(filter(even, range(10))))

# lambda を使用した書き方
print(list(filter(lambda n: n % 2 == 0, range(10))))
```

# 内包表記

集合に関しては様々な記法が存在する
```py
# i: [0,10)
print([i for i in range(10)]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i * 3 for i in range(10)]) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
print([i * 3 for i in range(10) if i % 2 == 0]) # [0, 6, 12, 18, 24]
print(list(i * 3 for i in range(10) if i % 2 == 0)) # [0, 6, 12, 18, 24]
print({i * 3 for i in range(10) if i % 2 == 0}) # {0, 6, 12, 18, 24}
```