def main():
    with open('4 - FATURAMENTO MENSAL\DATA.TXT') as f:
        lines = f.readlines()
    dataDic={}
    total = 0
    for item in lines:
        estado = item.split(' ')[0]
        valor = item.split(' ')[2]
  
        if estado not in dataDic:
            valor = str(valor.replace("R$","").strip(" ").rstrip("\n")).replace(",",".").replace(".","")
            dataDic[estado] = valor
    
    print(dataDic)
            
    for valor in dataDic.values():
        total += float(valor)
        
    for value,keys in zip(dataDic.values(),dataDic.keys()):
        print("Estado {} Porcentagem {:.2f}".format(keys,(float(value)/total)*100))
        


    #json_str = '{"name": "John", "age": 30, "city": "New York"}'

if __name__ == '__main__':
    main()