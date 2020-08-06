import socket

print ("Inicia el Servidor!!")
mi_socket = socket.socket()
mi_socket.bind( ('localhost',8000) )
mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    #print ("Nueva conexion establecida!!")
    peticion = conexion.recv(1024).decode()
    #print addr
    print (peticion)
    print("Escuchando")

    conexion.send(decode("Saludo desde el Servidor Python!!"))
    conexion.close()


