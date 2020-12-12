import re
print("Escoja la opción que desea ejecutar")
print ("1.Variables validas\n"
"2.Enteros y decimales\n"
"3.Operadores aritméticos\n"
"4.Operaciones relacionales\n"
"5.Palabras reservadas\n")

opcion = int(input("Ingresa una opcion"))

if opcion==1:
     filename="recurso.txt"
     textfile = open(filename,"r")
     regex = "[aA-zZ]+[0-9]?[=][\w]+"
     reg = re.compile(regex)
     print("Variables validas declaradas: ")
     for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
                print(elemento) 
           
elif opcion==2:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"\d+[.]?\d+"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
            print(elemento)
        
       
elif opcion==3:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"[\+?\-?\*?\/?]"
    reg = re.compile(regex)
    ele=""
    
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
                ele+=elemento + " "
    print("Los operadores ariteméticos encontrados son: "+ele )    
    
            
        

elif opcion==4:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex= r"[<?>?<=?=>?=?]"
    reg = re.compile(regex)
    ele=""
    print("Operadores relacinales encontrados son:")
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
                ele+=elemento+" "
    print(ele)    
    
    
elif opcion==5:
    filename="recurso.txt"
    textfile=open(filename,"r")
    regex=  r'\b[System]+\b|\b[using]+\b|\b[namespace]+\b|\b[classs]+\b|\b[Program]+\b|\b[static]+\b|\b[void]+\b|\b[Main]+\b|\b[Strig]+\b|\b[args]+\b|\b[bool]+\b|\b[double]+\b|\b[if]+\b|\b[else]+\b|\b[Console]+\b|\b[Read]+\b|\b[Lain]\b'
    reg = re.compile(regex)
    ele=""
    for line in textfile:
        lista=reg.findall(line)
        for elemento in lista:
                ele+=elemento + " "
    print("Las palabras reservadas encontradass son las siguientess: "+ele )  