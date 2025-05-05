#**************1-misol********************
# savat =[]
# while True:
#     mahsulot = input("Savatga mahsulot qushing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qushasizmi?(ha/yuq)")
#     if javob != 'ha':
#         break


#**************2-misol********************
maxsulotlar = {}
while True:
    maxsulot = input("Mahsulot nomini kiriting: ")
    narx = input(f"{maxsulot.title()}ning narxini kiriting: ")
    maxsulotlar[maxsulot] = narx
    javob = input("Yana mahsulot qushasizmi? (ha/yuq) ")
    if javob != 'ha':
        break