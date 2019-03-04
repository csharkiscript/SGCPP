import random
def echo(text):
    print(text)

def say(text):
    print(text)

def text(text):
    print(text)

def e(text):
    print(text)

def s(text):
    print(text)

def t(text):
    print(text)

def p(text):
    print(text)

def ds(I):
    n = type(I)

    if n == str:
        print('Type:', type(I))
        print('Is space:', I.isspace())
        print('Is alpha:', I.isalpha())
        print('Is upper:', I.isupper())
        print('Is lower:', I.islower())
        print('Is title:', I.istitle())

    if n == int:
        print('Type:', type(I))
   
    if n == float:
        print('Type:', type(I))
        Ifo = int(n)
        print(Ifo)
            
def f(text1, text2, text3, text4, text5):
    print(text1)
    if text2 != 'O':
        print(text2)
    if text3 != 'O':
        print(text3)
    if text4 != 'O':
        print(text4)
    if text5 != 'O':
        print(text5)

x = 0
y = 0
life = 1000 
x1 = 0
y1 = 0
damagep = 20
coin = 0

def area(tamx, tamy, keyxm, keyxn, keyym, keyyn, listo):

    chi = 0
    che = 3
    global x
    global life
    global y
    global coin

    respostapoint = ''
    while respostapoint != 'e':
        typ = 0
        x3 = 1
        y3 = 2
        print("""     
            {}
        {}      {}
            {}""".format(keyxn, keyyn, keyym, keyxm))
        respostapoint = input('')
        if respostapoint == keyxn:
            x -= 1
        if respostapoint == keyxm:
            x += 1
        if respostapoint == keyyn:
            y -= 1
        if respostapoint == keyym:
            y += 1
        if x >= tamx:
            x = tamx
        if y >= tamy:
            y = tamy
        if x <= 0:
            x = 0
        if y <= 0:
            y = 0
        for item in listo:
            
            
            if chi == che:
                typ1 = listo.__getitem__(typ)
                x2 = listo.__getitem__(x3)
                y2 = listo.__getitem__(y3)
                cd = (x2, y2)
                ch = (x, y)
                if typ1 == 'chestcoin':
                   
                    if ch == cd:
                        
                            
                        c = input('Open chest?')
                        if c == 'YES':
                            vC = random.randint(10,1000)
                            coin += vC
                            print("+", vC,"COINS")

                if typ1 == 'chestlife':
                    if ch == cd:
                        
                        y = y2 - 1
                        c = input('Open chest?')
                        if c == 'YES':
                            vL = random.randint(10,1000)
                            life += vL
                            print("+", vL,"LIFE")

                che += 3 
            chi += 1

                                

        print('x=', x,'y=', y)

def bossarea(bossname, damage, lifeb, tamx, tamy, keyxn, keyyn, keyym, keyxm, listf):
    """Bossarea (Area and Artificial Inteligence)
    please def:
        life(Player life)
        x:(North, South player position)
        y:(Right, Left player position)
        y1:(Right, Left player position)
        x1:(North, South boss position)
        damagep:(Player)
    variables

    
    bossname:Bossname, ex:Misy the SUPER ANIME FAN attacked
    damage:Damage of boss
    lifeb:Life of boss
    tamx:North, South area limits
    tamy:Lest, West area limits
    keyxn:South key
    keyyn:Lest key
    keyxm:North key
    keyym:West keu
    listf: Word list
    """
    global life
    global x
    global y
    global x1
    global y1
    global damagep
    damagec = 1

    superc = 0
    

    respostapoint = ''
    while respostapoint != 0:
        f = random.choice(listf)
        cp = (x, y)
        cb = (x1, y1)
        
        print("""     
            {}
        {}      {}
            {}  f""".format(keyxn, keyyn, keyym, keyxm))
        respostapoint = input('')
        if respostapoint == keyxn:
            x -= 1
        if respostapoint == keyxm:
            x += 1
        if respostapoint == keyyn:
            y -= 1
        if respostapoint == keyym:
            y += 1
        if respostapoint == 'f':
            if y == y1:
                if x == x1:
                    print('You attacked')
                    lifeb = lifeb - damagep
                    y1 += 1
                    damagec = 0
        if x >= tamx:
            x = tamx
        if y >= tamy:
            y = tamy
        if x <= 0:
            x = 0
        if y <= 0:
            y = 0

        

        if damagec == 0:
            while superc >= 5:
                czx = 0 + x
                czy = 0 + y
                ctx = tamx - x
                cty = tamy - y
                for c in range(0, 6):
                    if x1 == tamx:
                        y1 -= 1
                    elif y1 == tamy:
                        x1 -= 1
                    elif x1 == 0:
                        y1 += 1
                    elif y1 == 0:
                        x1 += 1
                    elif xc <= yc:
                        y1 += 1
                    elif yc <= xc:
                        x1 += 1
                    else:
                        if x <= y:
                            if czy <= cty:
                                y += 1
                            if czy >= cty:
                                y -= 1
                        if y <= x:
                            if czx <= ctx:
                                x += 1
                            if czx >= ctx:
                                x -= 1
                superc = 0
            damagec = 1

            
            
                    
                


        if damagec == 1:

            xc = x - x1
            yc = y - y1
            if xc <= yc:
                if x <= x1:
                    x1 -= 1
                if x >= x1:
                    x1 += 1

            if xc >= yc:
                if y <= y1:
                    y1 -= 1
                if y >= y1:
                    y1 += 1
            
            
            if cb == cp:
                print(f)
                life = life - damage
                print(bossname, 'attacked')
                superc += 1

            
        
        if x1 >= tamx:
            x1 = tamx
        if y1 >= tamy:
            y1 = tamy
        if x1 <= 0:
            x1 = 0
        if y1 <= 0:
            y1 = 0
        
        print('YOU=', x, y, life)
     
        print('BOSSc', x1, y1, lifeb, superc)

        if life <= 0:
            print('You died')
            break

        if lifeb <= 0:
            print(bossname, 'died')
            break 

def menus():
    menu = input("""
    [1]Start
    [2]Exit
    
    
    """)
    if menu == '1'
        print('')
    elif menu == '2'
        exit()
    


