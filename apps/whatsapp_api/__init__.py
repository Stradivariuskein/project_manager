from .modules.whatsapp_api import WhatsappApi
import os
def initial_task():
    wp_api = WhatsappApi()
    host = os.getenv("NGROK_HOST")
    message = f"url: {host}"
    wp_api.send_mesege(message)


initial_task()