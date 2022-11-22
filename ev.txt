wr = open("H:\ Ev.txt" , "w")
ev = [2984 ,2348, 2069, 2204, 2418, 2037, 2092, 2495, 2487, 2827, 2305, 2650]

##1

ev = False
if len(ev) == 12:
    ev = True
    print(f"Ez egy év adatsora")
    wr.write ("print(Ez egy év adatsora)\n")
else:
    print(f"Ez nen egy év adatsora")
    wr.write ("print(Ez nen egy év adatsora)\n")
##2

legnagyobb = ev[0]
for elem in ev:
    if elem > legnagyobb:
        legnagyobb=elem
wr.write("print(legnagyobb)\n")
print(legnagyobb)


##3

legkisebb = ev[0]
for elem in ev:
    if elem < legkisebb:
        legkisebb=elem
print(legkisebb)
wr.write("print(legkisebb)\n")

##4

ossz=0
for num in ev:
    ossz=ossz+num
print(f"Az összeg : {ossz}")
wr.write("print("f"Az összeg : {ossz})\n")
##5

hanyszor=0
for x in ev:
    ossz+= x
    if x > legnagyobb:
        legnagyobb = x
    elif x < legkisebb:
        legkisebb = x
    if x > 2400:
        hanyszor+=1

legnagyobb1=max(ev)
legkisebb1=min(ev)

print(legnagyobb1)
wr.write("print(legnagyobb1)\n")
print(legkisebb1)
wr.write("print(legkisebb1)\n")

#legnagyobb hely
hossz=len(ev)
ker=legnagyobb
i=0
while ev[i] != ker:
    i+= 1

print(f"legnagyobb helye: {i+1}")

wr.write("print("f"legnagyobb helye: {i+1}\n")

#legkisebb hely
hossz=len(ev)
ker=legkisebb
i=0
while ev[i] != ker:
    i+= 1
print(f"legnagyobb helye: {i+1}")

wr.write("print("f"legnagyobb helye: {i+1}\n")

wr.close()
