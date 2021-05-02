# encoding=utf-8

''' Uppgift 1
# 1. Skriv ut ett program som skriver ut texten "hello world" på skärmen'
print("hello world")
'''

''' Uppgift 2
# 2. Gör ett program som tar reda på användarens namn och sedan utser användaren som bäst.
name=input("Vad heter du: ")
print(name)
print(name, "är bäst")
'''

''' Uppgift 3
# 3. Gör följande beräkningar:
print("123+123-456=",123+123-456)
print("12+(3*8)=",12+(3*8))
print("7**6=", 7**6)
print("(6+8)(2+5)=",(6+8)*(2+5))
'''

''' Uppgift 4
# 4. Skriv ett program för att omvandla från meter till (brittiska) längdmått.
meter = input("Hur många meter: ")
m = int(meter)
mile = m/1609.344
yard = m/0.9144
foot = m/0.3048
inch = m/0.0254

print("mile:", mile)
print("yard:", yard)
print("foot:", foot)
print("inch:", inch)
'''

''' Uppgift 5
# 5. Vad blir resten vid följande division?
print("12345678987654321 / 13 =",12345678987654321//13,"med",12345678987654321%14,"i rest")
'''

''' Uppgift 6
# 6. Gör ett program för omkrets och area på en rektangel som har sidan 5 och 7. Exempel: l.e. är längdenheter och a.e. är areaenheter.
s1 = 5
s2 = 7
print("Rektangelns omkrets är", (s1*2) + (s2*2), "l.e.")
print("Rektangelns area är", s1*s2, "a.e.")
'''

''' Uppgift 7
# 7. Gör ett program för omkrets och area på en rektangel. Programmet ska fråga användaren efter höjd och bredd. 
#    Därefter ska programmet skriva ut omkrets och area.
höjd = input("Ange höjd: ")
h = int(höjd)

bredd = input("Ange bredd: ")
b = int(bredd)

print("Rektangelns omkrets är", (h*2)+(b*2))
print("Rektangelns area är", h*b)
'''

''' Uppgift 8
#    antal barn och därefter skriver ut den totala biljettkostnaden. 

vuxna = input("Ange antal vuxna: ")
v = int(vuxna)
vb = v * 55

barn = input("Ange antal barn: ")
b = int(barn)
bb = b * 27.50

print("den totala biljettkostnaden är:", vb + bb, "kr")
'''

''' Uppgift 9
# a) Bengt "Bengan" Jansson 
# b) Tecknet \ kallas 'backslash'

# två sätt att skriva detta på, att börja och avsluta strängar på görs på två sätt, antingen " eller '. Ska man använda något av det i texten ska man använda den andra än den man ska ha i texten.
# print("Bengt \"Bengan\" Jansson")
print('Bengt "Bengan" Jansson')
print("Tecknet \ kallas 'backslash'")
'''

''' Uppgift 10
# 10. Skriv ett program för att omvandla grader i Celsius (C) till grader i Farenheit (F) och vice versa.
celsius = input("Ange grader i celsius: ")
c = int(celsius)
ctf = 1.8*c + 32
print("Det blir", ctf, "Farenheit")

Farenheit = input("Ange grader i Farenheit: ")
f = int(Farenheit)
ftc = (((f-32)*5)/9)
print("Det blir", ftc, "Celsius")

'''

''' Uppgift 11
# 11. Vad kommer att skrivas ut när följande kod körs? Gissa först och testa sedan.
x=10
y=20
print(x<10)
print(y>=2*x)
print(y==10 and y==15)
print(y==10 and y>15)
print(y==10 or y==15)
'''

''' Uppgift 12
# 12. Skriv ett program som skriver ut frågan "regnar det (j/n)?". Svarar man 'j' ska "tag paraply!" skrivas ut,
#     I annat fall händer ingenting (programmet avslutas).

regn=input("Regnar det (j/n)?: ")
if regn=="j" or regn=="J":
    print("Tag paraply!")
'''

''' Uppgift 13
må=input("Mår du bra (j/n)?: ")
if må=="j" or må=="J":
    print("Ha en fortsatt bra dag")
else:
    print("Hoppas du mår bättre snart!")
'''
    
''' Provade uppgift 14
1 = input ("1. Skapa nytt")
2 = input("2. Öppna")
3 = input("3. Skriv ut")
4 = input ("4. Avsluta")
print(1
2
3
4)
todo = input("Vad ville du göra?: ")
print("Du valde: todo") 
'''

''' Uppgift 14
print(" 1. Skapa nytt\n 2. Öppna \n 3. Skriv ut \n 4. Avsluta")
answer=input("Vad ville du göra?: ")
a= int(answer)
if a==1:
    print("Du valde: Skapa nytt")
'''

''' Uppgift 15
print("Du ska ange två tal, en täljare och en nämnare")
T=input("Täljaren: ")
t = int(T)
N=input("Nämnaren: ")
n = int(N)
if n==0:
    print("Kvoten går inte att räkna ut eftersom nämnaren är 0")
else:
    print(t / n)
'''

''' Uppgift 16
stal =input("Skriv in ett tal: ")
st =int(stal)
mtal =input("Skriv in ett till tal: ")
mt = int(mtal)
if st== mt:
    print("Talen är lika stora")
if st>mt:
    print("Talet", st, "är större än", mt)
if st<mt:
    print("Talet", st, "är mindre än", mt)
'''

''' Uppgift 17
vikt=input("Skriv in en vikt: ")
v=int(vikt)
if v>5:
    print("Vikten större än 5")
if v<5:
    print("Vikten mindre än 5")
if v==5:
    print("Vikten är lika med 5")

'''

''' Uppgift 18 ej klar
year=int(input("Vilket år är du född? "))
birthday=input("Har du fyllt år i år (j/n)? ")
if birthday=="j" or birthday=="J":
    age=2020-year

else:
    age=2020-year-1
'''

''' Uppgift 23
n=1
text = ' '
while n<=20:
    print("hej")
    n+=1
print()
'''

''' Uppgift 24
n=1
text = ' '
while n<=31:
    print(n)
    n+=1
print()
'''

''' Uppgift 25
svar=input("Mår du bra (j/n)? ")
while svar!='j':
    svar=input("Mår du bra (j/n)? ")
'''

''' Uppgift 26
c=0
n=10000
text = ' '
while n<=20000:
    print(n, c)
    n*=1.03
    c+=1
print()
# svar = 23 år
'''

''' Uppgift 27
svar=input("Ange lösenord: ")
while svar!='j':
    print("Felaktigt lösenord. Försök igen!")
    svar=input("Ange lösenord: ")
print("Lösenord ok!")
'''

''' Uppgift 28
import random
x = random.randint(0,1000)
n = 1
print("Jag har ett tal mellan 1 och 1000.")
svar=int(input("Vilket tal gissar du på?: "))
while svar!=x:
        if svar>x:
                print("Mitt tal är mindre!")
                svar=int(input("Vilket tal gissar du på?: "))
                n+=1
        if svar<x:
                print("Mitt tal är större!")
                svar=int(input("Vilket tal gissar du på?: "))
                n+=1
print("Rätt gissat på", n, "försök!!")
'''

''' Uppgift 31
x=0
while x<101:
    print(x)
    x+=1
'''

''' Uppgift 31
for i in range(1,101):
    print(i)
'''

''' Uppgift 32
for i in range(100,0,-1):
    print(i)
'''

''' Uppgift 33
for i in range (1,100,2):
    print(i)
'''

''' Uppgift 34
answer=input("Välj tabell: ")
x=int(answer)
for i in range(1,11):
    print(i*x)
'''

''' Uppgift 35
for y in range(1,9):
    for x in range(1,y):
        print('*', end=' ')
    print()
'''

''' Uppgift 36
months = ["januari", "februari", "mars", "april", "maj", "juni", "juli", "augusti", "september", "oktober", "november", "december"]

answer=input("Välj månadsnummer: ")
x=int(answer)

print(months[x])
'''

''' Uppgift 37
x = [17, 4, 6, 1, 43, 32]
y = [1, 4, 6, 21, 43, 32]
z = [17, 4, 6, 11, 43, 32, 1]

numbers = [2,64,1,46,32]
memory = 999
memoryindex = 0
loop = 0
for t in numbers:
    if memory > t:
        memory = t
        memoryindex = loop
    loop+=1

print("Detta är dina tal: ", numbers)
print("Det lägsta talet i listan är: ",memory)
print("Det lägsta talet är på position: ",memoryindex)
'''


''' Uppgift 38
numbers = [2,64,1,46,32]

temp = numbers[2]
numbers[2] = numbers[0]
numbers[0] = temp
print("numbers[2]= ",numbers[2])
print("numbers[0] = ",numbers[0])
'''
    
''' Uppgift 39
tal = int(input("Hur många tal?: "))
x = int(input("Ange ett tal: "))
y = int(input("Ange ett tal: "))
z = int(input("Ange ett tal: "))

lista = [x,y,z]
print("Detta är dina tal:", lista)
boom = x+y+z
print("Summan är:", boom)
abow = boom//tal
print("Medelvärdet är:", abow)
'''

'''print("Ange de tal du vill summera. Avsluta med att svara med q:")
i = "q"
x = int(input("Ange ett tal: "))
while x!=i:
    print("Ange ett tal")
            
'''

''' Uppgift 41
text=input("Skriv ut en text: ")

c=text
c=c.capitalize()
print(c)

l = text
l=l.lower()
print(l)

u = text
u=u.upper()
print(u)

cen=text
cen=cen.center(30)
print(cen)

rju=text
rju=rju.rjust(30)
print(rju)

mell=text
mell=mell.strip()
print(mell)
'''

''' Uppgift 42
text=input("Skriv en sträng:")
print(len(text))
'''


''' Uppgift 43
text=input("Skriv en sträng:")
# print(len(text))

i = len(text) -1
while i >= 0:
    print(text[i], end="")
    i -= 1
'''

''' Uppgift 44
fname=input("Ditt förnamn: ")
lname=input("Ditt efternamn: ")

f=fname
f=f.capitalize()
l=lname
l=l.capitalize()

print("Ditt namn är",f, l)


h = fname[::-1]
j = lname[::-1]

print(fname,"blir",h,"och",lname,"blir",j,"baklänges")
'''

''' Uppgift 45
månvarm=input("Ange varmrätt för måndag: ")
månveg=input("Ange vegetariskt alternativ för måndag: ")
tisvarm=input("Ange varmrätt för tisdag: ")
tisveg=input("Ange vegetariskt alternativ för tisdag: ")
onsvarm=input("Ange varmrätt för onsdag: ")
onsveg=input("Ange vegetariskt alternativ för onsdag: ")
torvarm=input("Ange varmrätt för torsdag: ")
torveg=input("Ange vegetariskt alternativ för torsdag: ")
frevarm=input("Ange varmrätt för fredag: ")
freveg=input("Ange vegetariskt alternativ för fredag: ")

days = ["måndag","tisdag","onsdag","torsdag","fredag"]
varmrätt = [månvarm,tisvarm,onsvarm,torvarm,frevarm]
veg = [månveg,tisveg,onsveg,torveg,freveg]

print("Dag".ljust(15) + "Varmrätt".ljust(15) + "Vegetariskt".ljust(15))
for i in range(0,5):
    row = days[i].ljust(15) + varmrätt[i].ljust(15) + veg[i].ljust(15)
    print(row)
'''
    
''' Uppgift 46 EJ KLAR
text=input("Ange den text du vill översätta: ")

consonants = "bcdfghjklmnpqrstvwxz"
print(text.replace())
'''

''' Uppgift 54
def addition(x,y):
 """Returnerar summan av x och y"""
 z = x+y
 return z
 
x = 12
y = 3
res = addition(x,y)
print("summan var:", res)
'''

''' Uppgift 55
def lika(a,b):
    if a == b:
        return 'sann'
    else:
        return 'falsk'

a= 10
b= 11
res= lika(a,b)
print("funktionen är", res)
'''

''' Uppgift 56
def olika(a,b):
    if a != b:
        return 'sann'
    else:
        return 'falsk'

a= 10
b= 11
res= olika(a,b)
print("funktionen är", res)
'''

'''def intinput():
    tal = input("Ange ett heltal: ")
    if tal == int:
        return tal
    
tal = intinput()
print("du angav heltalet", tal)

'''

'''
def intinput():
    while True:
        tal = input("Ange ett heltal: ")
        if (tal.isdigit()) and 0<=tal=>9:
            return tal
        else:
            tal = input("Ange ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332!: ")
intinput()

'''

'''
def intinput():
    while True:
        tal = input("Ange ett heltal mellan 0 och 9: ")
        if (tal.isdigit()):
            tal = int(tal)
            if tal<=9:
                return tal
        else:
            tal = input("Ange ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332!: ")
intinput()
'''

'''def emptyspaces():
    emptyspace = []
    for i in range(len(board)):
        if board[i] =='':
            print(str(i) + ' is empty') 
            emptyspace.append((int)(str(i)))
    print(emptyspace)
emptyspaces()
'''

'''emptyspaces = [0, 1, 2 , 3]
player = "X"
board = ["","","","",""]

def computermove():
    if cornermoves() == False:
        break
    if 
        cornermoves()
        middlemove()
        sidemoves()
        if False:
            break
    
def cornermoves():
    if 0 in emptyspaces:
        board[0] = player
        return False

def middlemove():
    return None

def sidemoves():
    return None
    
computermove()
'''
import os, sys

def playagain():
    restart = input("Vill du spela igen? J för ja, N för nej: ")
    if restart == "J" or restart == "j":
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif restart == "n" or restart == "N":
        return None
playagain()
    