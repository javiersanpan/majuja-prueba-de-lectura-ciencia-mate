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

import random, time, sys, os
from threading import Timer

#This is to adapt our clear function to our OS
while True:
  try:
    usersys = int(input("¿Qué plataforma usas? | 1.- Windows | 2.- Linux o MacOS | 3.- Python IDLE | : "))
  
  except ValueError:
    print("Por favor introduce un valor correcto")
    continue
  
  if usersys > 3 or usersys < 1:
    print("Por favor introduce un valor correcto")
    continue

  else:
    break

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

def preguntas_de_matematicas():
  fb = []
  contador_c = 0
  check = 0


  #Function for giving feedback to our player when he looses
  def feedback():

      global fb
      
      fb.append(str(rn_easy) + " | " + "Tu respuesta fue " + str(pregunta) + " | " + "La respuesta correcta era " + str(respuesta) )

  #Function for printing a 'Game Over' ASCII art
  def game_over_art():

    print("""
    __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
    / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
  | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
    \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
    |___/                                           
    
    """)



  #Our ASCII 'HP' indicator 
  def heart_art():
    if hp == 3 and check == 0:

      print("""           
                ******       ******             ******       ******             ******       ******
              **********   **********         **********   **********         **********   **********
            ************* *************     ************* *************     ************* *************
          *****************************   *****************************   *****************************
          *****************************   *****************************   ***************************** 
          *****************************   *****************************   *****************************
            ***************************     ***************************     ***************************
              ***********************         ***********************         ***********************
                *******************             *******************             *******************
                  ***************                 ***************                 ***************
                    ***********                     ***********                     ***********  
                      *******                         *******                         *******
                        ***                             ***                             ***
                        *                               *                               * 
      """
      )

    elif hp == 2 and check == 0:

            print("""           
                ******       ******             ******       ******             * * *        * * *
              **********   **********         **********   **********         *        *   *        *
            ************* *************     ************* *************     *           * *           *
          *****************************   *****************************   *                           *
          *****************************   *****************************   *                           * 
          *****************************   *****************************   *                           *
            ***************************     ***************************     *                         *
              ***********************         ***********************         *                     *
                *******************             *******************             *                 *
                  ***************                 ***************                 *             *
                    ***********                     ***********                     *         *  
                      *******                         *******                         *     *
                        ***                             ***                             * *
                        *                               *                               * 
      """
      )

    elif hp == 1 and check == 0:

            print("""           
                ******       ******             * * *        * * *               * * *        * * *
              **********   **********         *        *   *        *          *        *   *        *
            ************* *************     *           * *           *      *           * *           *
          *****************************   *                           *    *                           *
          *****************************   *                           *    *                           * 
          *****************************   *                           *    *                           *
            ***************************     *                         *      *                         *
              ***********************         *                     *          *                     *
                *******************             *                 *              *                 *
                  ***************                 *             *                  *             *
                    ***********                     *         *                      *         *  
                      *******                         *     *                          *     *
                        ***                             * *                              * *
                        *                               *                                * 
      """
      )
    
    elif hp == 0 and check == 0:

            print("""           
                * * *        * * *               * * *        * * *               * * *        * * *
              *        *   *        *          *        *   *        *          *        *   *        *
            *           * *           *      *           * *           *      *           * *           *
          *                           *    *                           *    *                           *
          *                           *    *                           *    *                           * 
          *                           *    *                           *    *                           *
            *                         *      *                         *      *                         *
              *                     *          *                     *          *                     *
                *                 *              *                 *              *                 *
                  *             *                  *             *                  *             *
                    *         *                      *         *                      *         *  
                      *     *                          *     *                          *     *
                        * *                              * *                              * *
                        *                                *                                * 
      """
      )

  #Function to clear our screen 
  def clearrr():

      global clear 

      if usersys == 1:

          clear = os.system('cls') #Windows 
          
      elif usersys == 2:

          clear = os.system('clear') #Linux

      elif usersys == 3:

          clear = print ("\n" * 100) #Python IDLE (Python IDLE doesn't have a clear command, so we have to print a lot of \n lol)

      clear

      return clear

  clearrr()
  #########
  clear

  #Gamemode menu
  while True:

    try:

      mode = int(input("Ingresa el modo que desees | 1.- Suma | 2.- Resta | 3.- Multiplicación | : "))

      if mode == 1:

          signo = "+"

      elif mode == 2:

          signo  = "-"

      elif mode == 3:

          signo = "*"

    except ValueError:

      clearrr()
      clear
      print("Por favor introduce un valor válido")
      continue
    
    if mode > 3 or mode < 1:

      clearrr()
      clear
      print("Por favor introduce un valor correcto")
      continue
    
    else:
      
      clearrr()
      clear
      break

  clearrr()
  clear

  #Difficult menu
  while True:
    try:
      diff = int(input("Ingresa la dificultad que desees | 1.- Fácil | 2.- Difícil | : "))

      if diff == 1:

        n1 = 1
        n2 = 9
        n3 = 1
        n4 = 9

      elif diff == 2 and mode == 3:

        n1 = 1
        n2 = 9
        n3 = 10
        n4 = 19

      elif diff == 2:

        n1 = 1
        n2 = 19
        n3 = 1
        n4 = 19

      #This was supposed to be a custom gamemode but couldn't make it work :(
      """
      elif diff == 3:

        n = []

        for i in range(2):

          n.append(int(input("Ingresa el valor número " + str(i + 1) + " del rango de números aleatorios: ")))

        print(n)
        if n[0] < n[1]:

          n1 = n[1]
          n2 = n[0]
        else:
          n1 = n[0]
          n2 = n[1]
      """
    except ValueError:
      
      clearrr()
      clear
      print("Por favor introduce un valor correcto")
      continue

    if diff > 2 or diff < 1:
      
      clearrr()
      clear
      print("Por favor introduce un valor correcto")
      continue
    
    else:
      
      clear
      break

  #Some random variables


  hp = 3            #HP for our user (if you get 0 hp you lose)
  rn_easy = ""      #This is a displayable string that prints the operation the user has to solve
  respuesta = 0     #This is the correct answer of the operation that is shown to the user, we use it for validate user's input


  #Function for all the math stuff, it generates our operation
  def operation_generator():


      global rn_easy, respuesta, r1, r2
      r1 = random.randint(n1,n2)
      r2 = random.randint(n3,n4)

      #This is for the substraction gamemode, if the first number is smaller than the second one, we will have a negative value, so we avoid that with this
      if mode == 2 and r2 > r1:
          
          rn_easy = (str(r2) + " " + signo + " " + str(r1))

          respuesta = eval(rn_easy)
          
          return rn_easy, respuesta

          

      else:

          rn_easy = (str(r1) + " " + signo + " " + str(r2))

          respuesta = eval(rn_easy)
          
          return rn_easy, respuesta

  heart_art()
  operation_generator()

  run = True

  #This is used when we win the game
  def end_game():

    global run, check

    run = False
    check = 1 #Some chunky solution I did for a bug lol
    heart_art()
    game_over_art()
    print("Has ganado!")
    
    time.sleep(3.0)
    clear

    print("Respestas incorrectas \n \n")

    if len(fb) > 0:

      for i in range(len(fb)):      #This displays all the incorrect answers we gave and it's feedback

        print(fb[i])

    else:

      print("No tuviste respuestas incorrectas :)")

    time.sleep(3.0)
    clear
    
    print("Contestaste " + str(contador_c) + " operaciones correctamente en 30 segundos.")  #Some feedback
    print("Eso te da un total de " + str(contador_c / 30) + " respuestas correctas por segundo!") #This tell you how fast you are on solving operations
    print("Presiona cualquier botón para terminar el juego.") #Leaving the game

    return run, check

  #########################
  t = Timer(30.0, end_game)         #This is a timer that call our end game function when we reach 30 seconds by playing without loosing, it's kinda buggy but could make it work
  t.start()
  #########################


  #Our game loop

  while run:

      clear

      #Our game over check
      if hp == 0:         #If we answer incorrectly three times, we lose
          os.system('cls')
          heart_art()
          game_over_art()
          print("\n \n Has perdido!")

          for i in range(len(fb)):      #Feedback

              print(fb[i])

          t.cancel()
          run = False #This kills our while loop

      elif check == 0:      #This is some chunky solution I did for a bug I couldn't fix, it didn't solve it at all but it still kinda does the job

          #Printing our operation
          clear
          pregunta = input("Cuánto es " + rn_easy + ": ")

          #This validates if the user didn't type at all and just hit enter
          if not pregunta:

              os.system('cls')
              print("Mal")
              feedback()
              hp = hp - 1         #Hp remover :p
              heart_art()
              operation_generator()

          #Validation of user input
          else:

            pregunta = int(pregunta)

            if pregunta == respuesta:     #Correct answer

                #time.sleep(1)
                os.system('cls')
                print("Bien")
                heart_art()
                contador_c = contador_c + 1
                operation_generator()

            else:   #Incorrect answer
                
                #time.sleep(1)
                os.system('cls')
                print("Mal")
                feedback()
                hp = hp - 1         #Hp remover :p
                heart_art()
                operation_generator()

if modo == "1":
    preguntas_de_lecturas()
elif modo == "2":
    preguntas_de_ciencias()
elif modo == "3":
    preguntas_de_matematicas()
else:
    print("Error: Por favor ingrese un valor de los siguientes: 1, 2, 3")