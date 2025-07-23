Ings = 500
Double_Swords = 125
Sniper = 85
Nu = 75
Kratha = 50

while True:
    print("1.ต่อสู้กับ Ings")
    print("2.คามุย")
    choice = int(input("พิมพ์ 1 / 2 เพื่อเลือก: "))
    if choice == 1:
        round = int(input("จะตีกี่รอบ"))
        for i in range(round):
            print("จงเลือกอาวุธของเจ้าสะ")
            print("1. Double_Sword (AT= 125)")
            print("2. Sniper (AT= 85)")
            print("3. Nu (AT= 75)")
            print("4. Kratha (AT= 50)")
            weapon = int(input("พิมพ์ AT ของอาวุธที่เลือก :"))
            if weapon == 1:
                Ings = Ings-weapon
                print("เลือดของ Ing เหลือ", Ings)
            
        if 
        elif Ings == 0 :
            print("ดีใจด้วย Ing ได้ตาย")
        elif Ings < 0 :
            Ings = 20
            print("เลือดของ Ings เพิ่มมาเป็น 20 หน่วย")
        else :
            print("เสียใจด้วยคุณแพ้แล้ว TT" / "ไว้มาเล่นใหม่นะ")
    elif choice == 2:
       print("คุณได้เลือกที่จะไม่สู้กับ Ings" / "ขอให้คุณโชคดีกับทางที่เลือก เพราะคุณทำให้ประเทศไม่ได้ไปต่อ")