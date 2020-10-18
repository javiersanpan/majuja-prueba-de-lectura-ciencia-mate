import time

def clear():
    for cl in range(1000):
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

print("Se te mostrarán",cantidad_de_lecturas,"breves hisotrias, con límite de tiempo, y se te harán 3 preguntas por lectura, elige la letra que corresponda a la respuesta correcta\n\n")

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
            print("\nRespuesta incorrecta, la respuesta correcta era:", respuesta_correcta, "Tu puntaje actual es:", puntaje,"\n")
            time.sleep(3)
            clear()
   
print("Has terminado, tu puntaje final fue de", puntaje, "puntos de 15")