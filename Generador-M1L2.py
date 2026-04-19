import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Ingresa la longitud de la contraseña: "))
clave = ""
for i in range(longitud):
    clave += random.choice(caracteres)

print("La contraseña es: ", clave)

