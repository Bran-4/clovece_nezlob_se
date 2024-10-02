#Moj skript simuluje hru "clovece nezlob se" dvoch hracov na lubovolne velkej hracej ploche
#vypisovanie hracej plochy som nastavil raz po kazdom tahu oboch hracov z dovodu velkeho mnozstva vypisov(hlavne pri vacsich rozmeroch)

from random import*

n=int(input("zadaj aku velkost bude mat hracia plocha(iba neparne cisla, minimum 5)"))
while n<5 or n%2==0:
    n=int(input("zle čislo, zadaj aku velkost bude mat hracia plocha(iba neparne cisla, minimum 5)"))
    

def hraci_zoznam(n):
    """vytvori a vrati zoznam hracej plochy, parameter: n-velkost hracej plochy"""
    dlzka=4*(n-5)+16 #toto je dlzka zoznamu na ktorom bude prebiehat hra
    zoznam=dlzka*["*"]
    return zoznam
  
def domov(n):
    """vytvori a vrati zoznam na zaznamenavanie pozicie panacikov v dome, parameter: n-velkost hracej plochy"""
    dlzka=(n-3)/2
    zoznam=int(dlzka)*["D"]#na zaciatok vytvori zoznam zo samych d-čok
    return zoznam

def pozicie_panacikov(n):
    """vytvori a vrati zoznam na zaznamenavanie vzdialenosti panacikov od domu,parameter: n-velkost hracej plochy"""
    dlzka=(n-3)/2
    zoznam=int(dlzka)*["Nezacal"]#na zaciatok vytvori zoznam zo samych slov "nezacal"
    return zoznam

def nakresli_hru(n,zozn,domov1,domov2,domov3,domov4):
    """
    nakresli hraciu plochu,
    parametre: n-velkost hracej plochy, zozn-hraci_zoznam, domov<1-4>-obsadenie domceka hraca  
    poznamka: domov2 a domov4 by sme vyuzili pri hre 4 hracov
    """
    prazdno="  "*(int((n-3)/2))+" "
    def kresli_riadok(prazdno,y,a,b,c): #kresli riadky typu "0   * D *    ", parametre:a,b-hodnota namiesto lavej a pravej hviedicky*,b=hodnota namiesto-D
        print(y,end=prazdno)
        print(a,b,c)
    def kontroluj_y(y):#pripocitava 1 k y a nuluje ked y>9, y sluzi na cislovanie riadkov
        y+=1
        if y>9:
            return 0
        return y
    x=y=a=b=0 #x=ocislovanie stlpcov,y=ocislovanie riadkov, a,b=urcenie indexu v hracom zozname
    print(" ",end=" ")
    for i in range(n):#nakresli prvy riadok hry: ocislovanie stlpcov
        print(x,end=" ") 
        x+=1
        if x>9:
            x=0
    print()  
    kresli_riadok(prazdno,y,zozn[-2],zozn[-1],zozn[0]) #riadok "0   ***    " 
    y=kontroluj_y(y)
    for i in range(int((n-5)/2)): #riadky typu "1   * d *     "
        kresli_riadok(prazdno,y,zozn[-3-a],domov1[i],zozn[1+b])
        y=kontroluj_y(y)
        a+=1
        b+=1
    
    print(y,end=" ")
    a=a+int((n-1)/2)-1 #aby sa prvky v zozname vykreslili v spravnom poradi je potrebne ich v tejto casti pisat odzadu
    for i in range(int((n-1)/2)): #kresli riadok "5 * * * D * * *"
        print(zozn[-3-a],end=" ")
        a-=1
    print(domov1[-1],end=" ")
    for i in range(int((n-1)/2)):
        print(zozn[1+b],end=" ")
        b+=1
    a=a+int((n-1)/2)+1
    print()
    y=kontroluj_y(y)
    
    print(y,end=" ") #kresli riadok "* d d X d d *
    print(zozn[-3-a],end=" ")
    for i in domov4:
        print(i,end=" ")
    print("X",end=" ")
    for i in range(len(domov2)):
        print(domov2[-i-1],end=" ")#prvky domova2 pise odzadu
    print(zozn[1+b])
    y=kontroluj_y(y)
    
    a+=1
    print(y,end=" ")
    b=b+int((n-1)/2)#aby prvky v zozname sa vykreslili v spravnom poradi je potrebne ich v tejto casti pisat odzadu
    for i in range(int((n-1)/2)): #riadok "5 * * * D * * *
        print(zozn[-3-a],end=" ")
        a+=1
    print(domov3[-1],end=" ")
    for i in range(int((n-1)/2)):
        print(zozn[1+b],end=" ")
        b-=1
    b=b+int((n-1)/2)
    print()
    
    b+=1
    for i in range(int((n-5)/2)): #riadky typu "1   * d *     "
        y=kontroluj_y(y)
        kresli_riadok(prazdno,y,zozn[-3-a],domov3[-i-2],zozn[1+b])
        a+=1
        b+=1
    y=kontroluj_y(y)
    kresli_riadok(prazdno,y,zozn[-3-a],zozn[-4-a],zozn[-5-a]) #riadok "0   ***    " 

def krok_hraca(tim):
    """
    rozhodne s ktorym hracom je potrebne sa pohnut na zaklade pozicie a vylosovaneho kroku
    parametre: tim-A/B podla toho ktory hrac je na rade
    return:vylosovany krok
    """
    if tim=="A": #na zaklade zvoleneho timu sa menia vlastnosti 
        zacinajuca_pozicia=-len(z)
        zacinajuca_pozicia_super=int(-len(z)/2)
        domov=domova
        domov_super=domovb
        pozicie_panacikov=pozicie_panacikov_a
        pozicie_panacikov_super=pozicie_panacikov_b
    else:#tym B
        zacinajuca_pozicia=int(-len(z)/2)
        zacinajuca_pozicia_super=-len(z)
        domov=domovb
        domov_super=domova
        pozicie_panacikov=pozicie_panacikov_b
        pozicie_panacikov_super=pozicie_panacikov_a
    
    krok=randrange(1,7)#tocenie kockou
    print("Hrac "+tim+" vytocil cislo "+str(krok))
    if krok==6 and z[zacinajuca_pozicia]=="*": #pripad ked hrac hodi 6 a ma hracov ktori este nehraju (hrac sa postavi na zaciatocnu poziciu iba ked tam nie je iny hrac)
        for i in range(len(domov)):
            if pozicie_panacikov[i]=="Nezacal":
                pozicie_panacikov[i]=0
                z[zacinajuca_pozicia]=tim
                return krok
    if z[zacinajuca_pozicia]==tim: #ked je hrac na zaciatocnej pozicii tak ma prednost kroku, aby sa pri pripadnej hodenej 6 mohol spawnut novy hrac
        for i in range(len(domov)):
            if pozicie_panacikov[i]==0:
                z[zacinajuca_pozicia+pozicie_panacikov[i]]="*"
                pozicie_panacikov[i]+=krok              
                if z[zacinajuca_pozicia+pozicie_panacikov[i]]!="*" and z[zacinajuca_pozicia+pozicie_panacikov[i]]!=tim:#ak je na pozicii hrac ineho timu
                    if pozicie_panacikov[i]>=len(z)/2:#zistovanie pozicie supera vzhladom na jeho domovsku poziciu                    
                        cislo=(-len(z)/2)+pozicie_panacikov[i]
                    else:
                        cislo=(len(z)/2)+pozicie_panacikov[i]
                    poradie=pozicie_panacikov_super.index(cislo)
                    pozicie_panacikov_super[poradie]="Nezacal"#vynulovanie progresu súpera        
                z[zacinajuca_pozicia+pozicie_panacikov[i]]=tim#na novej pozicii bude hrac
                return krok
    else:#ked hrac nie je na zaciatocnej pozicii a nevyhodil 6 alebo vyhodil 6 no ma vsetkych hracov na hracom poli alebo v dome
        for i in range(len(domov)):
            if pozicie_panacikov[i]!="Nezacal":# ked je hrac na hracej ploche alebo v dome
                if (pozicie_panacikov[i]+krok)<len(z):#ked je jeho nova pozicia este na hracej ploche
                    if pozicie_panacikov.count(pozicie_panacikov[i])==1:#tento if riesi bug- ked bola figurka na rovnakom mieste ako jeho dalsia figurka-> pri dalsom pohybe jedna z figuriek zmizla
                        z[zacinajuca_pozicia+pozicie_panacikov[i]]="*"
                    pozicie_panacikov[i]+=krok              
                    if z[zacinajuca_pozicia+pozicie_panacikov[i]]!="*" and z[zacinajuca_pozicia+pozicie_panacikov[i]]!=tim:#ked je na vylosovanej novej pozicii súper tak ho vyhodi- rovnaky postup ako od riadku 139
                        if pozicie_panacikov[i]>=len(z)/2:                    
                            cislo=(-len(z)/2)+pozicie_panacikov[i]
                        else:
                            cislo=(len(z)/2)+pozicie_panacikov[i]
                        poradie=pozicie_panacikov_super.index(cislo)
                        pozicie_panacikov_super[poradie]="Nezacal"        
                    z[zacinajuca_pozicia+pozicie_panacikov[i]]=tim
                    return krok
                else: # ked nova pozicia je v dome
                    if pozicie_panacikov[i]+krok-len(z)<len(domov):
                        if domov[pozicie_panacikov[i]+krok-len(z)]=="D":
                            if pozicie_panacikov[i]<len(z):#ked je stara pozicia na hracej ploche
                                z[zacinajuca_pozicia+pozicie_panacikov[i]]="*"
                            else:#ked je stara pozicia v dome
                                domov[pozicie_panacikov[i]-len(z)]="D"
                            domov[pozicie_panacikov[i]+krok-len(z)]=tim
                            pozicie_panacikov[i]+=krok
                            return krok              

def hraj_hru(n):
    """cyklus ktory hraje hru kym nevyhra niektory hrac
    parameter:n-velkost hracej plochy
    """
    while True:
        a=krok_hraca("A")
        while a==6:#ak vytoci 6 hraje znova
            a=krok_hraca("A")
        a=krok_hraca("B")
        while a==6:
            a=krok_hraca("B")
        nakresli_hru(n,z,domova,domov(n),domovb,domov(n))
        if "D" not in domova:
            return("Vyhral hrac A")
        if "D" not in domovb:
            return ("Vyhral hrac B")

#vygenerovanie vsetkych zoznamov potrebnych na hru
domova=domov(n)
domovb=domov(n)
pozicie_panacikov_a=pozicie_panacikov(n)
pozicie_panacikov_b=pozicie_panacikov(n)
z=hraci_zoznam(n)
nakresli_hru(n,z,domova,domov(n),domovb,domov(n))#kreslenie prvotnej prazdnej plochy
        
print(hraj_hru(n))#zapnutie hry