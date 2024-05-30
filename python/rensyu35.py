while True:
    num1 = input("1つ目の数値：")
    num2 = input("2つ目の数値：")

    try:
        num1 = int(num1)
        num2 = int(num2)
        print(num1 / num2)
        break
    except ZeroDivisionError:
        print("0では割れません")
    except ValueError:
        print('整数を入力してください')
