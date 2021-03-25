# encoding=utf-8

#min kommentering är inte i detta fall så snygg, men jag ville vara tydlig med min kommentering
#på denna uppgift eftersom att det är den första och för att jag vill visa att jag kan och förstår, därför har jag också
#blandat semnatik och syntax i min kommentering.

def encrypt(text,key):
    encrypt = '' #tom sträng som sedan kommer fyllas av tecken genom "return". Detta är det värde som kommer visa sig när man kallar på funktionen.
    
    
    upper = "ABCDEFGHIJKLMNOPQRSTUVWYZÅÄÖ" #uppercase, string som tecknet sen ska tittas mot. 
    lower = "abcdefghijklmnopqrstuvwyzåäö" #lowercase, string som tecknet sen ska tittas mot.
    
    for i in text:
        if i in upper: #om tecknet är en versal ska den följa denna väg.
            position=upper.index(i) #att ta ut tecknets nuvarande position/index i den string som den jämför mot (upper)
            newposition=(position+key)%len(upper) #ta ut tecknets nya position/index. Adderat key:n.
            encrypt+=upper[newposition] #det nya tecknet tas ut (ifrån upper-stringen)
        elif i in lower: #om tecknet är en gemen ska den följa denna väg.
            position=lower.index(i) #ta ut nuvarande position/index i stringen som den jämför mot (lower)
            newposition=(position+key)%len(lower) #ta ut tecknets nya position/index. Adderat key:n
            encrypt+=lower[newposition] #nya tecknet tas ut (ifrån lower-stringen)
        else: #om tecknet inte tillhör någon av stringsen som den jämför mot ska den följa denna väg.
            encrypt+=i #tecknet ska då inte krypteras, dvs att ett mellanslag förblir ett mellanslag.
    return encrypt #skicka värdet till encrypt = ''.


def decrypt(text,key):
    decrypt = '' #tom sträng som sedan kommer fyllas av tecken genom "return". Detta är det värde som kommer visa sig när man kallar på funktionen.
    
    
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWYZÅÄÖ' #uppercase, string som tecknet sen ska tittas mot. 
    lower = 'abcdefghijklmnopqrstuvwyzåäö' #lowercase, string som tecknet sen ska tittas mot. 
    
    for i in text: #för varje tecken i text...
        if i in upper: #om tecknet är en versal ska den följa denna väg.
            position=upper.index(i) #tecknets nuvarande position/index. 
            newposition=(position-key)%len(upper) #tecknets nya position/index, subtraherat key:n.
            decrypt+=upper[newposition] #det nya tecknet.
        elif i in lower: #om tecknet är en gemen ska den följa denna väg.
            position=lower.index(i) #tecknets nuvarande position/index.
            newposition=(position-key)%len(lower) #tecknets nya position/index, subtraherat key:n.
            decrypt+=lower[newposition] #det nya tecknet
        else: #om tecknet inte tillhör någon av stringsen som den jämför mot ska den följa denna väg.
            decrypt+=i #ex. om tecknet är ", så ska det ej krypteras. 
    return decrypt #skicka tecknet till decrypt ''.

def runtestcode (text, key):
    print('-'*50)
    print("Klartext :",text,"Key :",key)
    krypterat = encrypt(text, key)
    print("Krypterat:",krypterat)
    okrypterat =  decrypt(krypterat,key)
    print("Avkodat:", okrypterat)
    
runtestcode("Hej jag heter Sonja",2)




#Funktion nedan hanterar alla möjliga olika tecken och är mycket smartare än den ovan som jag först skrev,
#men tänker att jag tar med båda funktionerna.

def encrypt(text,key):
    encrypt="" #tom sträng som sedan fylls med tecknen via "return" som sedan är det värde som kommer att "visa" sig när man kallar på funktionen.
    for char in text: #för varje tecken i text...
        encrypt+=chr(ord(char)+key) #tar ut det nya tecknet: chr() omvandlar tal till bokstav, ord() omvandlar bokstav till tal, detta enligt ascii-tabellen.
        #alltså innebär (ord(char)+key) att tecknet omvandlas till det tal/position som tecknet har i ascii-tabellen, sedan adderas key:n, i och med det så får vi ut ett nytt tal i ascii-tabellen som sedan omvandlas via chr() tillbaks till tecken.
    return encrypt #skicka det nya

def decrypt(text,key):
    decrypt="" #tom sträng som sedan fylls med tecknen via "return" som sedan är det värde som kommer att "visa" sig när man kallar på funktionen.
    for char in text: #för varje tecken i text...
        decrypt+=chr(ord(char)-key) #tar ut det nya tecknet: chr() omvandlar tal till bokstav, ord() omvandlar bokstav till tal, detta enligt ascii-tabellen.
        #alltså innebär (ord(char)-key) att tecknet omvandlas till det tal/position som tecknet har i ascii-tabellen, sedan subtraheras key:n, i och med det så får vi ut ett nytt tal i ascii-tabellen som sedan omvandlas via chr() tillbaks till tecken.
    return decrypt #skicka tecknet till decrypt="" stringen. 


def runtestcode (text, key):
    print('-'*50)
    print("Klartext :",text,"Key :",key)
    krypterat = encrypt(text, key)
    print("Krypterat:",krypterat)
    okrypterat =  decrypt(krypterat,key)
    print("Avkodat:", okrypterat)
    
runtestcode("hej, j!ag heter SONJA'",2)