from datetime import datetime

def noFestivos(): #Definición de la función
    nombre=input('Dime tu nombre: ') #Se pide un nombre
    fecha=input('Dime una fecha(DD-MM-YYYY): ') #Se pide una fecha con formato
    fechaFormateada=datetime.strptime(fecha,"%d-%m-%Y") #Transformador de string a formato fecha
    dia=fechaFormateada.day #Se guarda el día del mes en la variable dia
    diaSemana=datetime.weekday(fechaFormateada)  #Se guarda el día de la semana en la variable diaSemana como valor numerico (lunes==0)
    if dia in(5,9,22) and (diaSemana < 5):  #Los días 5, 19 y 22 de cada mes que no sean fin de semana se escribe por pantalla que toca natación
        print(f'Hay natación en el día {dia}')
    elif dia in(19,28) and (diaSemana < 5): #Los días 19 y 28 que no sean fin de semana toca inglés
        print(f'Hay inglés en el día {dia}')
    elif (dia==14) and (diaSemana < 5): #El día 14 que no sea fin de semana tocan ambos
        print(f'Hay natación e inglés en el día {dia}')
    elif diaSemana == 5: #Los sábados hay baloncesto
        print(f'{nombre} toca baloncesto')
noFestivos() #Se llama a la función