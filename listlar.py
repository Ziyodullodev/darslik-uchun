


# list, tuple, set, dict

# append(), insert(), remove(), pop(), sort(), reverse(), extend(), clear(), index(), count()
# count(), index()
# add(), remove(), discard(), pop(), clear(), update(), difference(), intersection(), union(), 
# clear(), get(), items(), keys(), values(), pop(), update()



# int, str, float, bool


# list
# meva = "olma"
# raqamalar = [1, 4, 5, 9, 0, 2, 4]
# mevalar = ["olma", "behi"]
# mevalar.append("anor") # - list oxiriga malumot qo'shadi
# mevalar.insert(0, "banan") # - listni belgilangan joyiga element qo'shadi
# # mevalar.remove("olma") # - belgilangan elmentni ro'yxatdan o'chiradi
# # mevalar.pop() # - o'chirish uchun ishlatiladi va o'chirishda index qabul qiladi agar index berilmasa oxirdan malumot o'chiradi.
# # mevalar.sort() # - tartiblab berish uchun foydalaniladi. (alfabit, raqamalar)
# # sort + reverse=True - bu teskari tartibda malumotlarni saralaydi.
# # print(mevalar)
# mevalar.reverse() # - listni qanday holatda bo'lsa shundayicha teskari tartiblab beradi
# # mevalar.extend(["qulpinay", "olcha"])
# mevalar.extend(raqamalar) # - list boyicha barcha elementlarni oxiriga qo'shadi
# # mevalar.clear() # - listni bo'm bo'sh xolatga keltiradi
# mevalar.append("olma")
# print(mevalar)
# print(mevalar.index("olma")) # - bu elementni listda nechinchi o'rinda turganini aniqlab beradi
# print(mevalar.count("olma")) # - elementni listda necha marta foydalanilganini aytib beradi


# raqamalar.sort(reverse=True)
# print(raqamalar)


# mevalar = ("olma", "banan", "olma", "anor", "shaftoli", "uzum")

# # index(), count()

# # print(mevalar.count("olma"))
# # print(mevalar.index("olma"))


# # packeing, unpacking

# # unpacking
# # meva1, meva2, meva3, *boshqalar = mevalar
# # print(meva2)
# # print(boshqalar)


# ism1 = "Ali"
# ism2 = "vali"
# ism3 = "TOshmat"
# # packing
# ismlar = ism1, ism2, ism3
# print(ismlar)



# mevalar = ("olma", "banan", "olma", "anor", "shaftoli", "uzum")

# # 1-usul listga o'zgartirib qo'shamiz va yana tuplega qaytaramiz
# # mevalar = list(mevalar)
# # mevalar.append("olcha")
# # mevalar = tuple(mevalar)

# # 2-usul oxiriga + bilan qo'shish
# mevalar = mevalar + ("olcha",)
# print(mevalar)




# add(), remove(), discard(), pop(), clear(), update(), difference(), intersection(), union()

# [], (), {}

# mevalar = {"olma", "behi", "olma"}
# mevalar2 = {"uzum", "anor", "shaftoli", "olma"}
# mevalar3 = {"gaynoli", "olma", "behi"}

# mevalar.add("uzum")
# mevalar.discard("banan")
# mevalar.remove("banan")
# mevalar.pop()
# mevalar.clear()
# mevalar.update(["anor"])

# print(mevalar)

# print(mevalar.union(mevalar2, mevalar3)) |
# print(mevalar.intersection(mevalar2, mevalar3)) &
# print(mevalar.difference(mevalar2, mevalar3)) - 

# print(mevalar | mevalar2)
# print(mevalar & mevalar2)
# print(mevalar - mevalar3)






# list - []
# tuple - ()
# set - {}
# dict - {}

# set_blank = set()
# set_blank = {}
# print(type(set_blank))

# clear(), get(), items(), keys(), values(), pop(), update()


# kalit -> qiymat

# car -> mashina


# tarjimalar = {"car":"mashina"}
# mevalar = {
#     "olma": "qizil",
#     "banan": "sariq",
#     "anor": "kok",
#     "poliz_ekanlari": {
#         "tarvuz": "qizil"
#     }
# }
# print(mevalar['poliz_ekanlari']['tarvuz'])

# olma = mevalar.get("olma")
# banan = mevalar.get("banan")
# anor = mevalar.get("anor", "anor mavjud emas")
# olma = mevalar['olma1']
# mevalar.pop("olma")
# mevalar.update({"anor":"qizil"})

# mevalar['anor'] = "qizil" # - ham o'zgartirish ham yangi qo'shish uchun

# print(mevalar)
# print(olma)
# print(anor)
# print(tarjimalar)


# print(mevalar.keys())
# print(mevalar.values())
# print(mevalar.items())
# for kalit, qiymat in mevalar.items():
#     print(kalit, qiymat)