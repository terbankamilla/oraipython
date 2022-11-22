wr = open("H:\ Aug.txt" , "w")
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]
#1
if len(aug) == 12:
    ev = True
    print(f"Ez egy év adatsora")
    wr.write("print("f"Ez egy év adatsora\n")
else:
    print(f"Ez nem egy év adatsora")
    wr.write("print("f"Ez egy nem év adatsora\n")
#2
legn=max(aug)
print(f" {legn} a legnagyobb hőmérséklet.")
wr.write("("f" {legn} a legnagyobb hőmérséklet.\n")
#3
legk=min(aug)
print(f" {legk} a legkisebb hőmérséklet.")
wr.write("("f" {legn} a legkisebb hőmérséklet.\n")
#4
count=0
for x in aug:
    if x > 31:
        count +=1
print(f"{count} darab 31 fok fölötti érték van.")    
wr.write("print("f"{count} darab 31 fok fölötti érték van. \n")
#5
print(f"Az augusztus 20. hőmérséklet : {aug[21]}")
wr.write("print("f"Az augusztus 20. hőmérséklet : {aug[21]}" "\n")
#6
egesz=sum(aug)
atlag= egesz/len(aug)
print(f" Az átlag hőmérséklet {atlag:.2f} ")
wr.write("print("f" Az átlag hőmérséklet {atlag:.2f} " "\n")

#7
hoing= legn-legk
print(f"{hoing} fok volt a hőingadozás")
wr.write("print("f"{hoing} fok volt a hőingadozás""\n")

# 1 Lehet e augusztus havi hóméséklet
# 2 A legnagyobb hóméséklet
# 3 A legkisebb hóméséklet
# 4 Hány alkalommal volt a hőmeséklet 31 fok felett?
# 5 mekkora volt a hómérséklet augusztus 20.-án?
# 6 mekkora volt az átlag hőmérséklet?
# 7 mekkora volt a hőingadoszás?
# Fájl írás
wr.close()
