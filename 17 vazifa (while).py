# ****************1 misol *****************
# yaxwi kurgan kitoblar
# savol = "Yaxshi kurgan kitoblaringizni nomini kiriting "
# savol += "(dasturni to'xtatish uchun 'stop' deb yozing): "
# iwora = True
# while iwora:
#     qiymat = input(savol)
#     if qiymat == "stop":
#         iwora = False
#     else:
#         print(qiymat)

# ****************2 misol muzey*****************
savol = "Yowingiz nechida: "
iwora = True
while iwora:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        iwora = False
        break
    yow = int(qiymat)
    
    if yow<7:
        narx = 2000
    elif 7<=yow<18:
        narx = 3000
    elif 18<=yow<65:
        narx = 10000
    else: narx = 0
    
    if narx==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narx} so'm")

