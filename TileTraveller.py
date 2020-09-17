# Byrjum í reit 1,1 og eigum að enda í reit 3,1 
# Áttir sem maður kemst í:
# 1,1 : Norður
# 1,2 : Norður, austur, suður
# 1,3 : Austur, suður
# 2,1 : Norður
# 2,2 : Vestur, suður
# 2,3 : Vestur, austur
# 3,1 : Victory
# 3,2 : Norður, suður
# 3,3 : Vestur, suður

# while lykkja utan um allt þangað til x=3 og y=1
# eitt function fyrir núverandi staðsetingu til að segja hvað má gera næst
# eitt function sem breytir staðsetingu
# Nota tvær breytur x,y
# Norður = y hækkar, Suður = y lækkar
# Vestur = x lækkar, Austur = x hækkar

#Function fyrir áttir: 
def direction(x,y,d):
    if x == 1 and y == 1: 
        allowed_direction_str = 'You can travel: (N)orth.'
        d = 'N'
    elif x == 1 and y == 2:
        allowed_direction_str = 'You can travel: (N)orth or (E)ast or (S)outh.'
        d = 'NES'
    elif x == 1 and y == 3:
        allowed_direction_str = 'You can travel: (E)ast or (S)outh.'
        d = 'ES'
    elif x == 2 and y == 1:
        allowed_direction_str = 'You can travel: (N)orth.'
        d = 'N'
    elif x == 2 and y == 2:
        allowed_direction_str = 'You can travel: (S)outh or (W)est.'
        d = 'SW'
    elif x == 2 and y == 3:
        allowed_direction_str = 'You can travel: (E)ast or (W)est.'
        d = 'EW'
    elif x == 3 and y == 2:
        allowed_direction_str = 'You can travel: (N)orth or (S)outh.'
        d = 'NS'
    elif x == 3 and y == 3:
        allowed_direction_str = 'You can travel: (S)outh or (W)est.'
        d = 'SW'
    
    return (allowed_direction_str, d)

#Function fyrir breytingu á staðsetningu:
def movement(x,y,direction_str):
    direction_str = direction_str.upper()
    if direction_str == 'N' and d.find('N') != -1: #stafurinn er ekki í orðinu d.find('N') = -1
        y += 1
    elif direction_str == 'S' and d.find('S') != -1:
        y -= 1
    elif direction_str == 'E' and d.find('E') != -1:
        x += 1
    elif direction_str == 'W' and d.find('W') != -1:
        x -= 1
    else:
        print('Not a valid direction!')
    return x,y


x = 1
y = 1
d = 'N'
while d != 'Victory': # á meðan ekki victory
    allowed_direction_str, d = direction(x,y,d) #fallakall
    print(allowed_direction_str)

    direction_str = input('Direction: ')
    x,y = movement(x,y,direction_str) #fallakall
    
    if x == 3 and y == 1: # ef komið er í reit 3,1!
        d = 'Victory'
        print('Victory!')