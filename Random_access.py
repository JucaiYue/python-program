# __user :Edward Yue
# date: 2017/12/11
import random
def randomNum():
    m = int(input("How many Numbers："))
    n = int(input("The maximum:"))
    if 1 <= m <= n:
        for i in range(m):
            print(random.randint(1,n))

    else:
        print("Please confirm whether the maximum value exceeds the required number")

randomNum()