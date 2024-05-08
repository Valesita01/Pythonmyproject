

user = "pp@mail.com"
key = 1234


usuario = input("Usuario")

clave = int(input("Clave"))

usuario = input("Sea bienvenido al sistema, digite su usario")
clave = int(input("Ingresaste con exito"))

# Usuario if-else cree un sistema de login que valida las credenciales, si cumple permita iniciar sesion
# y si no, que imprima un mensaje de validar credenciales


if usuario == user:
    print("Ingresaste correctamente")
elif usuario and not user:
    print("Su Correo es incorrecto")

if key == clave:
    print("Ingresaste correctamente")
elif clave and not key:
    print("Su clave es incorrecta")



