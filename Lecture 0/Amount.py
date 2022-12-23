# 指定print哪個字的方法(list才有辦法更換字元)
s1 = ("int")
s2 = ["i", "n", "t"]

print(s1[0])
print(s2[0])

s2[0] = 1
print(s2[0])

# 檢查長度
x = "merry christmas"
print(len(x))

#計算機例子
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(amt):
    return float(amt[1:])
        
def percent_to_float(amt):
    return float(amt[:2])/100

