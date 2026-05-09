import pyotp
import qrcode

# Generamos una clave secreta aleatoria en Base32
secreto = pyotp.random_base32()
print(f"Clave secreta: {secreto}")

# Se construye la URI otpauth:// 
totp = pyotp.TOTP(secreto)
uri = totp.provisioning_uri(
    name="raulsineiro2@gmail.com",
    issuer_name="ServicioModulo8"
)
print(f"URI: {uri}")

# Generamos la imagen QR y la guarda
img = qrcode.make(uri)
img.save("qr_totp.png")
print("QR guardado en qr_totp.png — ¡escanéalo con Google Authenticator!")