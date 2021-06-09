def transform(lista):
    lista = [str(i) for i in lista]
    L='.'.join(lista)
    return L

while True:
    print("\n<<<INFORME O ENDEREÇO IP E DESCUBRA SUA REDE>>>")
    classeA=128
    classeB=192
    classeC=224
    classeD=240
    rede=[]
    rede1=[]
    broadcast=[]
    broadcast1=[]
    ip = input("IP: ")

    lista = ip.split(".")
    try:
        q, sub = lista[3].split('/')
        lista[3]=q
        lista.append(sub)
    except:
        print("\n")
    lista = list(map(int, lista))
    host=2**(32-lista[4])
    mascara = ''.ljust(lista[4],'1').ljust(32,'0')
    masc=[]
    for i in range(0, len(mascara), 8):
        masc.append(int(mascara[i:i+8],2))

    if lista[0] < classeA:
        classe='A'
        subrede = 2**(lista[4]-8)
        pot_sub = lista[4]-8
    elif lista[0] < classeB:
        classe='B'
        subrede = 2**(lista[4]-16)
        pot_sub = lista[4]-16
    elif lista[0] < classeC:
        classe='C'
        subrede = 2**(lista[4]-24)
        pot_sub = lista[4]-24
    elif lista[0] < classeD:
        classe='D'
        subrede = 2**(lista[4]-32)
        pot_sub = lista[4]-32
    for i in range(len(masc)):
        lista[i]
        rede.append(masc[i] & lista[i])

    print(f"Mascara: {transform(masc)}")
    print("Classe:",classe)
    print(f"Host: 2^{32-lista[4]}= {int(host)}")
    print(f"Subrede: 2^{pot_sub}= {int(subrede)}")

    var=False
    num_sub=0
    while True:
        try:
            if var:
                num_sub = int(input("\nNumero Subrede:"))
        except:
            break
        var=True
        intervalo = host*num_sub
        for i in range(len(masc)):
            a = int(intervalo/256)
            b = intervalo%256
            rede1.insert(0,(rede[3-i]+b))
            intervalo = a

        intervalo = host*num_sub    
        for i in range(len(rede1)):
            val = rede1[3-i]+host-1
            if masc[3-i]==255:
                broadcast1.insert(0,rede1[3-i])
            else:
                if val > 255:
                    a = val%256
                    broadcast1.insert(0,a)
                    host = int(host/256)
                else:
                    broadcast1.insert(0,val)
                    host=0

        print(f"{num_sub}) Rede: {transform(rede1)} Broadcast: {transform(broadcast1)}")
        rede1=[]
        broadcast1=[]
        host=2**(32-lista[4])
        