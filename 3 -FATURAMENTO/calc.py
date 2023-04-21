def calc(data):
    vert = data
    valueSel = {
        "MaxSales":{"day":0,"value":0},
        "MinSales":{"day":0,"value":0}
        }

    SumValue = 0
    ValueAvgSales = 0
    AvgDay = 0
    
    for data in data.json_data:
        if(int(data["valor"])==0):
            pass
        else:
            AvgDay +=1
            
        SumValue += data["valor"]
        
        if(data["valor"] >= valueSel["MaxSales"]["value"]):
                valueSel["MaxSales"]["day"] = data["dia"]
                valueSel["MaxSales"]["value"] = data["valor"]
        elif(data["valor"] <= valueSel["MinSales"]["value"]):
                valueSel["MinSales"]["day"] = data["dia"]
                valueSel["MinSales"]["value"] = data["valor"]
        
        

    av = 0
    for value in vert.json_data:
        if((value["valor"]) > ValueAvgSales):
            av = av+1
    
    print("MAIOR VENDA {0}".format(valueSel["MaxSales"]))
    print("MENOR VENDA {0}".format(valueSel["MinSales"]))
    print("MEDIA DAS VENDAS {0}".format(SumValue/AvgDay))
    print("MAIORES QUE A MEDIA: {0}".format(av))
