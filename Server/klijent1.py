import socket

klijent = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
klijent.connect(("127.0.0.1", 8005))

klijent.send(b"Hello!")

klijent.close()

