import pyotp

# Aquí ponemos la clave secreta que nos imprimió el script anterior
secreto = "PVPA7XQRN454GL65VPR4MHAEV72Q2W6W"

totp = pyotp.TOTP(secreto)

# Pide al usuario que introduzca el código
codigo = input("Introduce el código de 6 dígitos de Google Authenticator: ")

# Valida el código
if totp.verify(codigo):
    print("✅ Código VÁLIDO")
else:
    print("❌ Código INVÁLIDO")