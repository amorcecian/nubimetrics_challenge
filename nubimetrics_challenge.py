import csv

#Creo el diccionario de marcas e inicializo todo en 0
marcas_dinero_ventas={
    "IPHONE":{"dinero":0,"ventas":0,"sinonimos":["IPHONE"]},
    "BLU":{"dinero":0,"ventas":0,"sinonimos":["BLU"]},
    "SAMSUNG":{"dinero":0,"ventas":0,"sinonimos":["SAMSUNG","GALAXY","J7","J5","SAMSUMG","J4"]},
    "XIAOMI":{"dinero":0,"ventas":0,"sinonimos":["XIAOMI","REDMI","XIO"]},
    "MOTOROLA":{"dinero":0,"ventas":0,"sinonimos":["MOTOROLA","MOTO"]},
    "RAZER":{"dinero":0,"ventas":0,"sinonimos":["RAZER"]},
    "SONY":{"dinero":0,"ventas":0,"sinonimos":["SONY","XPERIA","Z4"]},
    "ALCATEL":{"dinero":0,"ventas":0,"sinonimos":["ALCATEL","ALKATEL"]},
    "HUAWEI":{"dinero":0,"ventas":0,"sinonimos":["HUAWEI","HONOR","HUAWIE"]},
    "NOKIA":{"dinero":0,"ventas":0,"sinonimos":["NOKIA"]},
    "LG":{"dinero":0,"ventas":0,"sinonimos":["LG"]},
    "TCL":{"dinero":0,"ventas":0,"sinonimos":["TCL"]},
    "BGH":{"dinero":0,"ventas":0,"sinonimos":["BGH"]},
    "CATERPILLAR":{"dinero":0,"ventas":0,"sinonimos":["CATERPILLAR","CAT"]},
    "BLACKBERRY":{"dinero":0,"ventas":0,"sinonimos":["BLACKBERRY","Z10","BLACBERRY"]},
    "HYUNDAI":{"dinero":0,"ventas":0,"sinonimos":["HYUNDAI"]},
    "KODAK":{"dinero":0,"ventas":0,"sinonimos":["KODAK"]},
    "ASUS":{"dinero":0,"ventas":0,"sinonimos":["ASUS"]},
    "ZTE":{"dinero":0,"ventas":0,"sinonimos":["ZTE"]},
    "PHILIPS":{"dinero":0,"ventas":0,"sinonimos":["PHILIPS"]},
    "NOBLEX":{"dinero":0,"ventas":0,"sinonimos":["NOBLEX"]},
    "PHILCO":{"dinero":0,"ventas":0,"sinonimos":["PHILCO"]},
    "MICROSOFT":{"dinero":0,"ventas":0,"sinonimos":["MICROSOFT"]},
    "HTC":{"dinero":0,"ventas":0,"sinonimos":["HTC"]},
    "MAXWEST":{"dinero":0,"ventas":0,"sinonimos":["MAXWEST"]},
    "SENSEI":{"dinero":0,"ventas":0,"sinonimos":["SENSEI","SANSEI"]},
    "KANJI":{"dinero":0,"ventas":0,"sinonimos":["KANJI"]},
    "QUANTUM":{"dinero":0,"ventas":0,"sinonimos":["QUANTUM"]},
    "PANACOM":{"dinero":0,"ventas":0,"sinonimos":["PANACOM"]},
    "SKY":{"dinero":0,"ventas":0,"sinonimos":["SKY"]},
    "OTRO":{"dinero":0,"ventas":0,"sinonimos":["OTRO"]}
}

cant_ventas=0

marcas = marcas_dinero_ventas.keys()

# Recorro el csv, lleno el diccionario y muestro el resultado
with open('cellphoneslisting.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            cant_ventas+=1
            otros=0
            for marca in marcas_dinero_ventas.keys():
                for sin in marcas_dinero_ventas[marca]["sinonimos"]:
                    if sin in row[1].upper():
                        marcas_dinero_ventas[marca]["dinero"]=marcas_dinero_ventas[marca]["dinero"]+float(row[2])
                        marcas_dinero_ventas[marca]["ventas"]=marcas_dinero_ventas[marca]["ventas"]+int(float(row[3]))
                        otros=1
                        break
            if otros==0:
                marcas_dinero_ventas["OTRO"]["dinero"]=marcas_dinero_ventas["OTRO"]["dinero"]+float(row[2])
                marcas_dinero_ventas["OTRO"]["ventas"]=marcas_dinero_ventas["OTRO"]["ventas"]+int(float(row[3]))
            line_count += 1
    for marcas in marcas_dinero_ventas.keys():
        print(f'\tMarca: {marcas} -- Ingreso por ventas:  ${marcas_dinero_ventas[marcas]["dinero"]:.2f} -- Cantidad vendida: {marcas_dinero_ventas[marcas]["ventas"]}')
        
    print(f'\tCant total de ventas: {cant_ventas}')