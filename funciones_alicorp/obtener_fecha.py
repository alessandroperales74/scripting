from datetime import datetime

def indicar_fecha():

    fecha_actual = datetime.now()

    anio_valido = False 
    mes_valido = False 

    while not anio_valido:
        try:
            anio = int(input('Ingrese año de descarga: '))
            if anio in range(2020,fecha_actual.year + 1):
                print(f'Año seleccionado: {anio}\n')
                anio_valido = True
            else:
                print('Año no válido. Selecciona un año válido\n')
        except:
            print('Digite un número válido para el año\n')

    while not mes_valido:
        try:
            mes = int(input('Ingrese mes de descarga: '))
            if mes in range(1,13):
                print(f'Mes seleccionado: {mes}\n')
                mes_valido = True
            else:
                print('Mes no válido. Selecciona un año válido\n')
        except:
            print('Digite un número válido para el mes\n')

    if mes in (1,3,5,7,8,10,12):
        dia = 31
    elif mes in (4,6,9,11):
        dia = 30
    else:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dia = 29
        else:
            dia = 28


    periodo = f'{anio}{str(mes).zfill(2)}'
    fecha_inicial = f'01.{str(mes).zfill(2)}.{anio}'
    fecha_final = f'{str(dia).zfill(2)}.{str(mes).zfill(2)}.{anio}'

    print(f'Periodo: {periodo}')
    print(f'Fecha Inicial: {fecha_inicial}')
    print(f'Fecha Final: {fecha_final}\n')

    return periodo,fecha_inicial,fecha_final
