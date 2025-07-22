s = int(input("ระยะทาง :"))

# if s >= 5 and s <= 50 :
#     print("ค่าจัดส่ง 10 บาท")
# elif s >= 51 and s <= 100 :
#     print("ค่าจัดส่ง 15 บาท")
# elif s >= 101 and s <= 300 :
#     print("ค่าจัดส่ง 25 บาท")
# elif s >= 301 and s <= 500 :
#     print("ค่าจัดส่ง 35 บาท")
# elif s >= 501 :
#     print("ค่าจัดส่ง 45 บาท")
# else:
#     print("ไม่มีบริการจัดส่ง")

if s > 500 :
    print("ค่าจัดส่ง 45 บาท")
elif s > 300 :
    print("ค่าจัดส่ง 35 บาท")
elif s > 100 :
    print("ค่าจัดส่ง 25 บาท")
elif s > 50 :
    print("ค่าจัดส่ง 15 บาท")
elif s > 5 :
    print("ค่าจัดส่ง 10 บาท")
else :
    print("ไม่มีบริการจัดส่ง")
