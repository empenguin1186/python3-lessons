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
while文は他の言語での実装とそういないが、else句はwhileの条件がはじめてFalseになった場合に呼ばれる
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