#encoding=utf-8


#hanterar dock bara lowercase, man skulle kunna använda en if-sats för att få den att gå igenom uppercase också.

def encrypt(text,key):
    encrypt = "" #tom sträng som sedan kommer fyllas av tecken genom "return". Detta är det värde som kommer visa sig när man kallar på funktionen.
    upper = "ABCDEFGHIJKLMNOPQRSTUVWYZÅÄÖ" #uppercase, string som tecknet sen ska tittas mot. 
    lower = "abcdefghijklmnopqrstuvwyzåäö" #lowercase, string som tecknet sen ska tittas mot
    textindex = 0 #blir som "för varje tecken" i texten
    keyindex = 0 #blir som "för varje tecken" i keyn
    
    while textindex < len(text): #medan textindexet är mindre än längden av texten.
        keychar=key[keyindex] #bokstaven på key[keyindex], första varvet = key[0] = första tecknet i keystringen.
        keypos=lower.index(keychar) #indexet på keychar (dvs bokstaven) i stringen lower.
        textchar=text[textindex] #bokstaven på text[textindex], första varvet = text[0] = första tecknet i textstringen.
        textpos=lower.index(textchar) #indexet på textchar(dvs bokstaven) i stringen lower.
        newposition=(keypos+textpos)%len(lower) #ny position tas ut
        encrypt+=lower[newposition] #nya bokstaven tas ut
        textindex+=1 #1 läggs till på textindex för varje varv så att nästa bokstaven i stringsen kan jämföras.
        keyindex+=1  #1 läggs till på keyindex för varje varv så att nästa bokstav i stringsen kan jämföras   
    return encrypt #returnera den nya bokstaven till den tomma stringen. 
    
def decrypt(text,key):
    decrypt = "" #tom sträng som sedan kommer fyllas av tecken genom "return". Detta är det värde som kommer visa sig när man kallar på funktionen.
    upper = "ABCDEFGHIJKLMNOPQRSTUVWYZÅÄÖ" #uppercase, string som tecknet sen ska tittas mot. 
    lower = "abcdefghijklmnopqrstuvwyzåäö" #lowercase, string som tecknet sen ska tittas mot
    textindex = 0 #blir som "för varje tecken" i texten
    keyindex = 0 #blir som "för varje tecken" i keyn
    
    while textindex < len(text):
        keychar=key[keyindex] #bokstaven på key[keyindex], första varvet = key[0] = första tecknet i keystringen.
        keypos=lower.index(keychar) #indexet på keychar (dvs bokstaven) i stringen lower.
        textchar=text[textindex] #bokstaven på text[textindex], första varvet = text[0] = första tecknet i textstringen.
        textpos=lower.index(textchar) #indexet på textchar(dvs bokstaven) i stringen lower.
        newposition=(textpos-keypos)%len(lower) #nya positionen 
        decrypt+=lower[newposition] #den nya bokstaven 
        textindex+=1 #1 läggs till på textindex för varje varv så att nästa bokstaven i stringsen kan jämföras.
        keyindex+=1  #1 läggs till på keyindex för varje varv så att nästa bokstav i stringsen kan jämföras   
    return  decrypt #returnera den nya bokstaven, i detta fall den bokstav som ska ha blivit okrypterad. 


def runtestcode (text, key):
    print('-'*50)
    print("Klartext :",text,"Key :",key)
    krypterat = encrypt(text, key)
    print("Krypterat:",krypterat)
    okrypterat =  decrypt(krypterat,key)
    print("Avkodat:", okrypterat)

runtestcode("oki","hej")



#hanterar alla typer av tecken

def encrypt(text,key):
    encrypt="" #tom sträng
    textindex = 0 #blir som "för varje tecken" i texten
    keyindex = 0 #blir som "för varje tecken" i keyn 
    while textindex < len(text): #medan textindexet är mindre än längden (i siffror, alltså hur många texten som finns i texten) av texten. 
        keychar=key[keyindex] #bokstaven på key[keyindex], första varvet = key[0] = första tecknet i keystringen.
        keyi=ord(keychar) #bokstaven som index i ascii-tabellen. 
        textchar=text[textindex] #bokstaven på text[textindex], första varvet = text[0] = första tecknet i textstringen.
        texti=ord(textchar) #bokstaven som index i ascii-tabellen. 
        newposition=(keyi+texti+1) #nya positionen, indexen plussas på + 1.
        newletter=chr(newposition) #nya bokstaven utifrån ascii-tabellen 
        textindex+=1 #1 läggs till på textindex för varje varv så att nästa bokstaven i stringsen kan jämföras.
        keyindex+=1  #1 läggs till på keyindex för varje varv så att nästa bokstav i stringsen kan jämföras       
        encrypt+=newletter #för varje varv ska det nya eller bokstaven läggas till i encrypt.
    return encrypt #nya bokstaven skickas till den tomma strängen, (som sen inte kommer vara tom)

def decrypt(text,key):
    decrypt="" #tom sträng
    textindex = 0 #blir som "för varje tecken" i texten
    keyindex = 0 #blir som "för varje tecken" i keyn
    while textindex < len(text): 
        keychar=key[keyindex] #bokstaven på key[keyindex], första varvet = key[0] = första tecknet i keystringen.
        keyi=ord(keychar) #bokstaven som index i ascii-tabellen. 
        textchar=text[textindex] #bokstaven på text[textindex], första varvet = text[0] = första tecknet i textstringen.
        texti=ord(textchar) #bokstaven som index i ascii-tabellen. 
        newposition=(texti-keyi-1) #nya positionen, text- 1.
        newletter=chr(newposition)
        textindex+=1 #1 läggs till på textindex för varje varv så att nästa bokstaven i stringsen kan jämföras.
        keyindex+=1  #1 läggs till på keyindex för varje varv så att nästa bokstav i stringsen kan jämföras       
        decrypt+=newletter #för varje varv ska det nya eller bokstaven läggas till i encrypt.
    return decrypt #nya bokstaven skickas till den tomma strängen, (som sen inte kommer vara tom)


def runtestcode (text, key):
    print('-'*50)
    print("Klartext :",text,"Key :",key)
    krypterat = encrypt(text, key)
    print("Krypterat:",krypterat)
    okrypterat =  decrypt(krypterat,key)
    print("Avkodat:", okrypterat)

runtestcode("z{","z]")
