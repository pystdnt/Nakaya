import sys
"""
#練習2
import sys

print(int(sys.argv[1])+int(sys.argv[2]))
"""

"""
#練習3
import sys 
print(len(sys.argv)-1)
"""

"""
#練習4
print("練習4-------------------")
a = 10
b = 20

def comparison(a,b):
    if a > b:
        print(a)
    elif a == b:
        print("aとbは等しいです")
    else:
        print(b)

comparison(a,b)

#練習5
print("練習5-------------------")
def comparison_str(a,b):
    if len(a) > len(b):
        print(a)
    elif len(a) == len(b):
        print("aとbは等しいです")
    else:
        print(b)

a = "aaa"
b = "bbbbb"

comparison_str(a,b)

"""

"""
#練習6
if sys.argv[1] == sys.argv[2]:
    print("等しい")
else:
    if len(sys.argv[1]) > len(sys.argv[2]):
        print(sys.argv[1])
    else:
        print(sys.argv[2])
"""

"""
#練習7
if int(sys.argv[1]) > int(sys.argv[2]):
    print(sys.argv[1]+","+sys.argv[2])
elif int(sys.argv[1]) < int(sys.argv[2]):
    print(sys.argv[2]+","+sys.argv[1])
else:
    print("Equal")
"""

"""
#練習8
#インポート
import numpy as np
#並び替え関数の作成
def sort_array(a):
    #配列の0番目の削除
    del a[0]
    #空配列の作成
    return_array = []
    #int化
    x = list(map(int,a))
    n = len(x)
    #並び替え
    for i in range(n):
        n_max = max(x)
        return_array.append(n_max)
        x.remove(n_max)

    #配列の表示
    print(return_array)

#実行
sort_array(sys.argv)   
"""

"""
#練習9
#1~10までの整数
print("(",end="")
for i in range(1,11):
    if i == 10:
        print(i,end="")
    else:
        print(i,",",end="")
print(")",end="")

print("\n")

#10~1までの整数
print("(",end="")
for i in range(10,0,-1):
    if i == 1:
        print(i,end="")
    else:
        print(i,",",end="")
print(")",end="")

print("\n")

#奇数だけ
print("(",end="")
for i in range(1,11,2):
    if i == 9:
        print(i,end="")
    else:
        print(i,",",end="")
print(")",end="")

print("\n")

#偶数だけ
print("(",end="")
for i in range(2,11,2):
    if i == 10:
        print(i,end="")
    else:
        print(i,",",end="")
print(")",end="")
"""

"""
#練習10
x = 0.1
y = 0.2

def float_add(x,y):
    num_x = float(x)
    num_y = float(y)
    print(num_x + num_y)

def float_subtraction(x,y):
    num_x = float(x)
    num_y = float(y)
    print(num_x - num_y)

def float_multi(x,y):
    num_x = float(x)
    num_y = float(y)
    print(num_x * num_y)

def float_division(x,y):
    num_x = float(x)
    num_y = float(y)
    print(num_x / num_y)

print("--------------------")
float_add(x,y)
print("--------------------")
float_subtraction(x,y)
print("--------------------")
float_multi(x,y)
print("--------------------")
float_division(x,y)
"""

"""
#練習11
x = "abcdefg"
def display_str(x):
    print("最初の文字は：",x[0])
    print("最後の文字は：",x[-1])

display_str(x)
"""

"""
#練習12
x = "abcdefg"

def reverse_str(x):
    str_x=''
    for i in x:
        str_x = i + str_x
    print(str_x)

reverse_str(x)
"""

"""
#授業
nums = [1,1,1]
while len(nums) <= 5:
    nums.append(1)
    print(nums)
"""

"""
#練習13
#1~100までの数をカンマ区切りで
for i in range(1,101):
    if i == 100:
        print(i)
    else:
        print(i,",",end="")

#100~1までの数をカンマ区切りで
for i in range(100,0,-1):
    if i == 1:
        print(i)
    else:
        print(i,",",end="")

#1~100までの合計値
num = 0
for i in range(101):
    num += i
print("合計値：",num)

#1~100までの偶数をカンマ区切りで
for i in range(1,101):
    if i % 2 == 0:
        if i == 100:
            print(i)
        else:
            print(i,",",end="")
    else:
        continue

#1~100までの3の倍数をカンマ区切りで
for i in range(1,101):
    if i % 3 == 0:
        if i == 99:
            print(i)
        else:
            print(i,",",end="")
    else:
        continue

#1~100までの3の倍数と3を含む数をカンマ区切りで
for i in range(1,101):
    if "3" in str(i):
        print(i,",",end="")
    elif i % 3 == 0:
        if i == 99:
            print(i)
        else:
            print(i,",",end="")
    else:
        continue

"""

"""
#練習14
print("①----------")
for i in range(5):
    for j in range(1,6):
        if j == 5:
            print(j)
        else:
            print(j,end="")

print("②----------")

for i in range(1,6):
    for j in range(5):
        if j == 4:
            print(i)
        else:
            print(i,end="")

print("③----------")

for i in range(5):
    for j in range(5,0,-1):
        if j == 1:
            print(j)
        else:
            print(j,end="")

print("④----------")

for i in range(5,0,-1):
    for j in range(5):
        if j == 4:
            print(i)
        else:
            print(i,end="")

print("⑤----------")

for i in range(6):
    for j in range(i):
        if j == i-1:
            print(i)
        else:
            print(i,end="")

print("⑥----------")

for i in range(5,0,-1):
    for j in range(i):
        if j == i-1:
            print(i)
        else:
            print(i,end="")

print("⑦----------")

for i in range(5):
    for j in range(1,i+2):
        if j == i+1:
            print(j)
        else:
            print(j,end="")
        
print("⑧----------")
for i in range(5):
    for j in range(5,i,-1):
        if j == i+1:
            print(j)
        else:
            print(j,end="")
"""

"""
result = []
for i in range(1,6):
    result.append(i**2)
print(result)

new_result = [i**2 for i in range(1,6)]
print(new_result)
"""

"""
zoo = {'cat','dog','whale','whale'}
print(zoo)

nums = {i%2 for i in range(5)}
print(nums)
"""

"""
nums1 = {1,2,3}
nums2 = {3,4,5}
print(nums1|nums2)
print(nums1&nums2)
print(nums1-nums2)
print(nums1^nums2)
"""

#練習15
#[[1,2,3],[10,20,30],[100,200,300]]
"""
array1 = []
for i in range(1,4):
    array2 = []
    for j in range(1,4):
        array2.append(j * 10 ** (i-1))
    array1.append(array2)
print(array1)
"""

#練習16
"""
#2つの集合の和、交差、差、対象差を求める
a = {'A','B','C','D','E'}
b = {'A','C','E','G','I'}

print('和：',a|b)
print('交差：',a&b)
print('差：',a-b)
print('対象差：',a^b)
"""

#練習17
"""
dict1 = {'a':1,'b':2,'c':3}
print(dict1['b'])
"""

#練習18
#要素を5つ持つ集合を作成
#input()を使用
#集合に含まれていれば「集合に含まれています」、含まれていなければ「集合に含まれていませんと表示」
"""
set_input = {1,2,3,4,5}
user_input = input("数字を入力してください：")
if int(user_input) in set_input:
    print("集合に含まれています")
else:
    print("集合に含まれていません")
"""

"""
#練習19
#キーと値の組み合わせを5つ持つ辞書を作成
#キーが存在していれば、対応する値を表示
#キーが存在していなければ、「指定したキーはありません」と表示
key_input = {"red":"赤","yellow":"黄","green":"緑","blue":"青","black":"黒"}
user_input = input("キーを入力してください：")
if user_input in key_input.keys():
    print(key_input[user_input])
else:
    print("指定したキーはありません")
"""

"""
#練習20
#input()を用いて、str型の値を入力させ、その文字の文字数を表示する処理
input_str = input("文字を入力してください：")
print(len(input_str))
"""

"""
#練習21
#input()を用いて、2つのint型の値を入力させ、1つ目と2つ目の数の合計を表示する処理
input_int1 = int(input("1つ目の数字を入力してください："))
input_int2 = int(input("2つ目の数字を入力してください："))
print(input_int1 + input_int2)
"""

"""
#練習22
#input()を用いて、1つのint型の値を入力させ、0より大きければ「正の数です」、0より小さければ「負の数です」、0の場合は「0です」と表示する処理
def answer(x):
    if x > 0:
        print("正の数です")
    elif x < 0:
        print("負の数です")
    else:
        print("0です")

int_input = int(input("数値を入力してください："))
answer(int_input)
"""

"""
#練習23
int_input1 = int(input("1つ目の数値を入力してください："))
int_input2 = int(input("2つ目の数値を入力してください："))

if int_input1 < int_input2:
    n = 1
elif int_input1 > int_input2:
    n = -1
else:
    n = 1

for i in range(int_input1,int_input2+n,n):
    if i == int_input2:
        print(i)
    else:
        print(i,",",end="")
"""

"""
#練習24
for i in range(1,6):
    for j in range(i):
        print("●",end="")
    print("")
"""
"""
#練習25
for i in range(1,6):
    for j in range(5):
        if j+1 == i:
            print("×",end="")
        else:
            print("●",end="")
    print("")
"""
"""
#練習26
def return_str(n):
    return len(n)

print(return_str("aaaaa"))
"""

"""
#練習27
#1
def wa(a,b):
    return a + b

#2
def sa(a,b):
    if a - b < 0:
        return -(a - b)
    elif a - b > 0:
        return a - b  
    else:
        return 0

#3
def bigger(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "値は等しい"
    
#4
def biggest(*a):
    n = max(a)
    return n

print(biggest(100,54,68,944,45))
"""
"""
#5
def square(a):
    for i in range(a):
        for j in range(a):
            print("〇",end="")
        print("")

#6
def rectangle(width:int,height:int)->str:
    for i in range(height):
        for j in range(width):
            print("〇",end="")
        print("")

rectangle(5,4)
"""
"""
#car.py
class Car:
    gasoline = 40.0
    def rufule(self):
        self.gasoline += 10.0
        print(self.gasoline)

obj = Car()
obj.rufule()
"""

from turtle import Turtle,Screen

#正三角形
#kame =Turtle()
#screen = Screen()
#kame.forward(200)
#kame.left(120)
#kame.forward(200)
#kame.left(120)
#kame.forward(200)
#screen.exitonclick()

#正方形
#screen1=Screen()
#kame1 = Turtle()
#kame1.forward(200)
#kame1.left(90)
#kame1.forward(200)
#kame1.left(90)
#kame1.forward(200)
#kame1.left(90)
#kame1.forward(200)
#screen1.exitonclick()

#円
#screen = Screen()
#kame = Turtle()
#kame.circle(1000)
#screen.exitonclick()

#星
#kame = Turtle()
#screen = Screen()
#kame.forward(200)
#kame.right(144)
#kame.forward(200)
#kame.right(144)
#kame.forward(200)
#kame.right(144)
#kame.forward(200)
#kame.right(144)
#kame.forward(200)
#kame.right(253)
#kame.circle(106)
#screen.exitonclick()

#練習29

"""
class Animal:


    #__init__
    def __init__(self,name,meow):
        self.name = name
        self.meow = meow

    #purrメソッド
    def purr(self):
        print("{0}は{1}鳴く".format(self.name,self.meow))

lion = Animal('ライオン','ガオー')
lion.purr()

goat = Animal('ヤギ','メェ')
goat.purr()
"""

"""
#練習31
class Rensyu31():
    #dispNumber()
    def dispnumber(self):
        for i in range(1,11):
            print(i,",",end="")
        print("")

    #dispNumber2()
    def dispNumber2(self,x:int):
        if x > 0:
            for i in range(1,x+1):
                print(i,",",end="")
            print("")
        else:
            x = -x
            for i in range(0,x+1):
                if i == 0:
                    print(i,",",end="")
                else:
                    print(-i,",",end="")
            print("")
        
    #getBiggerNumber()
    def getBiggerNumber(self,x:int,y:int)->int:
        if x > y:
            return x
        elif x < y:
            return y
        else:
            print("2つの値は等しいです")

    #getBiggestNumber()
    def getBiggestNumber(self,*x:tuple):
        return max(x)

rensyu = Rensyu31()
print(rensyu.getBiggerNumber(25,64))

rensyu.dispNumber2(-5)


print(rensyu.getBiggestNumber(230,363,75,1523))

"""


