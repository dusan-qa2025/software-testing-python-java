import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8005))
server.listen()
print("Server is listening...")

konekcije, adresa = server.accept()

print("Konekcija prihvacena: ", adresa)
time.sleep(2)

podaci = konekcije.recv(1024) #Citanje dobijenih podataka
dekodovani_podaci = podaci.decode("utf-8")
print("Stigli podaci od klijenta:" dekodovani_podaci)

konekcije.close()
server.close()

