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