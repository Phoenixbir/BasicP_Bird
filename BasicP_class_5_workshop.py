import random

lottery_number = random.randint(00, 99)
max_RD = 7
round = 0

print("🦊🦊🦊🦊")
print("เงินอยู่ในอากาศ...เดี๋ยวเจ้าพ่อจิ้งจอกขว้างให้เอง😁😁😁")
#-------------------------------------------


#--------------------------------------------
while round < max_RD:

    rd_num = int(input('ทายตัวเลขของท่าน(เจ้าพ่อจิ้งจอกบอก): '))
    round += 1

    if rd_num == lottery_number:
        print('เจ้าทายถูกแล้วว🦊 ')
        print('บิดแล้วรวย ซวยแล้วมึง🦊')
        break
    elif rd_num < lottery_number:
        print('เจ้าพ่อศาลเจ้าจิ้งจอกบอก "ยังน้อยไปนะลูก "🦊')
    elif rd_num > lottery_number:
        print('เจ้าพ่อศาลเจ้าจิ้งจอกบอก "ยังมากไปนะลูก"🦊')
    else:
        print('เจ้าพ่อศาลเจ้าจิ้กจอกบอก"ยังมากไปนะลูก "🦊')
        print('แป้งหมดป๋องแล้ว🦊')
        break
print(lottery_number,"🦊")


x = rd_num
the_winner_number = [x]
# rd_num.append(the_winner_number)
print('คุณถูกรางวัล 2 ตัวท้าย😁',the_winner_number, 'มูลค่า 2 แบงค์เทา😁')



#-----------------------------------------------
