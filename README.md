# TOTP Authenticator 🔐

Utilidad en Python para generar y validar contraseñas de un solo uso basadas en tiempo (**TOTP**),
compatible con Google Authenticator y cualquier aplicación que cumpla el estándar RFC 6238.

## ¿Cómo funciona TOTP?

TOTP genera un código de 6 dígitos a partir de una clave secreta compartida y el tiempo actual,
renovándose cada 30 segundos mediante HMAC-SHA1. Esto lo hace resistente a ataques de repetición
y adecuado para implementar autenticación de dos factores (2FA).

## Requisitos

```bash
pip install pyotp qrcode[pil]
```

## Pasos seguidos

### 1. Generar la clave secreta y el código QR

`generar_qr.py` genera una clave secreta aleatoria en Base32, construye la URI `otpauth://`
que entienden las apps de autenticación y la convierte en un código QR listo para escanear.

![generar_qr.py](imagen_generar_qr_codigo)

Al ejecutarlo se crea el fichero `qr_totp.png` y se imprime la clave secreta por consola:

![Ejecución generar_qr.py](imagen_consola_generar)

### 2. Escanear el QR con Google Authenticator

Con Google Authenticator instalado en el móvil, se pulsa **`+`** → "Escanear código QR"
y se apunta la cámara al `qr_totp.png` generado en el paso anterior.
La app empieza a mostrar códigos de 6 dígitos renovados cada 30 segundos.

![Código QR generado](qr_totp.png)

### 3. Validar el código TOTP

`validar_totp.py` pide al usuario que introduzca el código que muestra Google Authenticator
y lo compara con el código esperado calculado a partir de la clave secreta y el tiempo actual.
Indica si el código es válido o inválido.

![validar_totp.py](imagen_validar_totp_codigo)

![Ejecución validar_totp.py](imagen_consola_validar)

## Archivos del repositorio

| Archivo | Descripción |
|---|---|
| `generar_qr.py` | Genera la clave secreta y el código QR |
| `validar_totp.py` | Valida un código TOTP introducido por el usuario |

## Uso

```bash
# Generar el QR (ejecutar solo una vez)
python generar_qr.py

# Validar un código
python validar_totp.py
```
