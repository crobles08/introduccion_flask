from email import message
import hashlib

message = hashlib.sha256() #Algoritmo de encriptación
message.update(b"ITP_2022*")

print(message.hexdigest())