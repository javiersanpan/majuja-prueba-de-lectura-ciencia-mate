'''
Creado por:
Mariann Esther Jimenez Bautista (A01639923)
Juan Pablo Perez Duran (A01639947)
Francisco Javier Sanchez Panduro (A01639832)
Clase:
TC1028 GPO 92
Profesor:
Kenneth Bauer
'''

import time

modo = input("Selecciona tu modo: 1. Lecturas, 2. Ciencias, 3, Matemáticas: ")

def preguntas_de_ciencias():

    def leer_preguntas(question_file):
        f=open(question_file, "r")
        q=f.readline()
        answer=f.readline()
        opciona=f.readline()
        opcionb=f.readline()
        opcionc=f.readline()
        f.close()
        return [q,answer,opciona, opcionb, opcionc ]


    #Lista de preguntas

    preguntass=[1, 2, 3, 4, 5, 6]
    preguntas=[]

    for j in range(len(preguntass)):
        j += 1
        j = str(j)
        pre = leer_preguntas("quest"+j+".txt")
        preguntas.append(pre)


    #
    def ask (question):
        print(question[0])
        print(" ")
        print(question[2]+ "\n" + question[3] + "\n" + question[4])
        print(" ")
        answer = input("Escribe la letra de la respuesta correcta: ")
        answer = answer + "\n"
        

        if answer==question[1]:
            print("Bien hecho, tu respuesta es correcta.\n")
        else:
            print("Lo siento, tu respuesta es incorrecta.")
            print("La respuesta correcta es:")
            print(question[1])
            
    for i in preguntas:
            question = i
            ask(question)

def preguntas_de_matematicas():
    print("Coming soon...")

def preguntas_de_lecturas():

    def clear():
        for _ in range(1000):
            print("")

    def importar_historia(archivo_historia, archivo_preguntas):
        file = open(archivo_historia, "r")
        historia = file.readlines()
        file.close()
        
        file2 = open(archivo_preguntas)
        preguntas = []
        for j in file2:
            preguntas.append(j)
        
        lectura = [historia, preguntas]
        return lectura

    def importar_lecturas(a):
        ln = str(a+1)
        lec = importar_historia("story"+ln+".txt","story_questions"+ln+".txt")
        return lec

    cantidad_de_lecturas = 5

    cantidad_de_preguntas = 3

    puntaje = 0

    todas = []

    print("Se te mostrarán",cantidad_de_lecturas,"breves hisotrias, con límite de tiempo, y se te harán \
        3 preguntas por lectura, elige la letra que corresponda a la respuesta correcta\n\n")

    for k in range(cantidad_de_lecturas):
        todas.append(importar_lecturas(k))

    for lectura_actual in range(cantidad_de_lecturas):
        print(*todas[lectura_actual][0],sep ="\n")
        
        time.sleep(45)
        clear()
        
        for pregunta_actual in range(cantidad_de_preguntas):
            pregunta_actual = pregunta_actual * 5
            print(todas[lectura_actual][1][pregunta_actual])
            
            print(todas[lectura_actual][1][pregunta_actual+2])
            print(todas[lectura_actual][1][pregunta_actual+3])
            print(todas[lectura_actual][1][pregunta_actual+4],"\n")
            
            respuesta = input("Respuesta: ")
            respuesta = respuesta + "\n"
            
            if respuesta == todas[lectura_actual][1][pregunta_actual+1]:
                puntaje += 1
                print("\n""¡Respuesta correcta! ganaste 1 punto, tu puntaje actual es:",puntaje,"\n")
                time.sleep(3)
                clear()
            else:
                respuesta_correcta = todas[lectura_actual][1][pregunta_actual+1]
                respuesta_correcta = respuesta_correcta[:-1] + "."
                print("\nRespuesta incorrecta, la respuesta correcta era:", respuesta_correcta, "Tu punta\
                    je actual es:", puntaje,"\n")
                time.sleep(3)
                clear()
    
    print("Has terminado, tu puntaje final fue de", puntaje, "puntos de 15")

if modo == "1":
    preguntas_de_lecturas()
elif modo == "2":
    preguntas_de_ciencias()
elif modo == "3":
    preguntas_de_matematicas()
else:
    print("Error: Por favor ingrese un valor de los siguientes: 1, 2, 3")