import random
print("Please and a year: " )
year =  int(input())
def is_leap(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0) :
        leap = True
    else:
        leap = False
    return leap

print(is_leap(year))