total = 0
i = 1
n = int(input('จำนวนตัวเลขที่ต้องการหาผลรวม:'))
while i <= n :
    x = float(input("ตัวเลขที่:"))
    total += x
    i += 1
print("ผลรวม=",total)