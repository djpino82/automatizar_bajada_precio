# 🎮 PS5 Price Tracker - Automatización de Ofertas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![BeautifulSoup](https://img.shields.io/badge/Scraping-BeautifulSoup4-green?style=for-the-badge)
![SMTP](https://img.shields.io/badge/Email-SMTP_SSL-orange?style=for-the-badge)

Este script de Python monitoriza el precio de la **PlayStation 5** en tiempo real.  
Cuando el precio cae por debajo de un umbral establecido (ej. 500€), envía automáticamente una notificación por correo electrónico.

---

## 🛠️ Tecnologías y Librerías

Para este proyecto he utilizado herramientas clave del ecosistema Python:

| Librería | Función en este proyecto |
| :--- | :--- |
| **`requests`** | Realiza la petición HTTP y descarga el contenido de la web usando un `User-Agent` para evitar bloqueos. |
| **`BeautifulSoup`** | Analiza el HTML de la web para localizar el contenedor `buy--price` y extraer la parte entera y decimal. |
| **`smtplib`** | Establece una conexión segura `SSL` con el servidor de Gmail para enviar las alertas. |
| **`python-dotenv`** | Gestiona las credenciales (Email y Contraseñas) de forma segura desde un archivo externo. |
| **`time`** | Controla los intervalos de chequeo (configurado actualmente cada 24 horas). |

---

## 🧠 Lógica de Funcionamiento

El script no solo "mira" la web, sino que procesa los datos de forma inteligente:

1. **Identidad:** Usa un `User-Agent` real para que la web reconozca el script como un navegador Chrome legítimo.  
2. **Limpieza:** Combina las etiquetas HTML de enteros y decimales, elimina símbolos extraños con `re` (Expresiones Regulares) y convierte el texto en un número `float` operable.  
3. **Control de Alertas:** Incluye una variable `alert_sent` para evitar el spam. Solo recibirás **un correo** cuando se produzca la bajada de precio.

---

## 🚀 Instalación y Uso

### 1️⃣ Clonar y preparar
```bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate

### 2️⃣ Instalar dependencias
📦 Ejecuta el siguiente comando para instalar todas las librerías necesarias:

pip install -r requirements.txt

### 3️⃣ Configurar credenciales (.env)
🔑 Crea un archivo .env en la raíz del proyecto y añade tus datos:

EMAIL_SENDER=tu_correo@gmail.com
EMAIL_PASSWORD=tu_contraseña_de_aplicacion
EMAIL_RECEIVER=correo_donde_recibes_aviso

### 4️⃣Ejecutar el script
🚀 Lanza el tracker para comenzar a monitorizar precios:

python ps5_price_tracker.py

### 📌 Consejos

🔒 Usa contraseñas de aplicación en Gmail si tienes verificación en dos pasos.
⏰ Programa el script con **Tareas Programadas** (Windows) o **cron** (Linux/Mac) para ejecución automática.
🎯 Ajusta el umbral de precio según tu presupuesto para recibir alertas precisas.



