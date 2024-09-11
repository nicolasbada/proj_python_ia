class Conversao:
    def velocidade():
        kmh = [75.4,30.6,120,32.8,20.8]
        mph = [round(x/1.61,2) for x in kmh]
        return mph

def temperatura():
    celsius = [45,30,12,.5,32.6,50]
    fahrenheit = [round((x*1.8)+32,2) for x in celsius]
    return fahrenheit

def altura ():
    pés = [32,46,51,67,78,81,89,91,95,100]
    metros = [round((x*1)*0.3048,2 ) for x in pés]
    return metros

def idade():
    anos =[12,29,45,2,5,18]
    meses = [round(*12,2) for x in anos]
    x = 0
    while(x<=5):
        print(anos[x], "anos em meses são",meses[x])
        x += 1