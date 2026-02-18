#requests → Sirve para descargar el contenido de una web.
#BeautifulSoup → Sirve para leer y analizar el HTML.
#time → Sirve para hacer pausas (útil si quieres que revise cada cierto tiempo).
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time
import os
from dotenv import load_dotenv

# CONFIGURACIÓN
# Ponemos la URL del producto elegido.
URL = "https://www.game.es/hardware/pack-consola/playstation-5/playstation-5-1tb-pack-voucher-ea-sports-fc26/251519"

# Precio que tomo de referencia por si baja.
TARGET_PRICE = 500

# Carga las variables desde el archivo .env
load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

CHEK_INTERVAL = 86400 # Cada 24 horas

# El User-Agent hace que parezca que entras desde un navegador real y no un script o bot.
# La web lee esa línea y dice: "Ah, vale, es un usuario normal con Windows 10 usando Chrome. Pasa, aquí tienes el precio de la PS5".
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Variable para no enviar múltiples correos. Solo uno
alert_sent = False

# Función para enviar email
def send_email(current_price):
    subject = "¡El precio ha bajado!"
    body = f"El precio actual es {current_price}€.\n\nEnlace del producto:\n{URL}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    # Con with >> Abre la conexión y cuando termines, ciérrala automáticamente
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)


def check_price():

    # Usar alert_sent como global para que no de error
    global alert_sent

    # Descargamos la página
    page = requests.get(URL, headers=headers)

    # Convertimos el html para que podamos buscar lo que queremos
    soup = BeautifulSoup(page.content, "html.parser")

    # Vamos a buscar el precio. Inspeccionamos la web y buscamos id o class
    # Este sería el contenedor grande
    price_container = soup.find("div", class_="buy--price")

    if price_container:

        # Ahora buscamos lo que hay dentro del contenedor
        int_part = price_container.find("span", class_="int")
        decimal_part = price_container.find("span", class_="decimal")

        if int_part and decimal_part:

            # Limpiamos el texto
            int_part_text = int_part.get_text().strip()
            decimal_part_text = decimal_part.get_text().strip()

            # Unimos con punto
            price_complete = int_part_text + "." + decimal_part_text

            #Limpiamos cualquier carácter extraño que pueda haber quedado
            import re
            price_complete_clean = re.sub(r"[^0-9.]", "", price_complete)
            
            try:
                # Pasamos el precio de String a float
                current_price = float(price_complete_clean)
                print(f"Precio actual de la PS5: {current_price}€")
            except ValueError:
                print("Error: no se pudo convertir el precio a número")

            # Solo envía email si baja Y no se ha enviado antes
            if current_price < TARGET_PRICE and not alert_sent:
                print("🔥 ¡BAJÓ DE PRECIO!")
                send_email(current_price)
                alert_sent = True

            else:   
                print("Aún no ha bajado o ya se envié el mail.") 

        else:
            print("No se pudo obtener el precio.")
    
    else:
        print("No se encontró el contenedor del precio.")

# Bucle principal
while True:
    # Revisa precio
    check_price()
    print("Esperando 24 horas...\n")

    # Repite cada 24 horas 
    time.sleep(CHEK_INTERVAL)
    

