import os
import requests
import json

PROXY_IP = os.getenv('PROXY_IP')
print(f"proxy ip: {PROXY_IP}")
try:
    response = requests.get(f"http://{PROXY_IP}/host.json")

    if response.status_code == 200:

        data = json.loads(response.content)
        host = data["tunnels"][0]["public_url"]
        os.environ['NGROK_HOST'] = host
        print(host)
        print(response.content)
    else:
            print(f"errro server response status code [{response.status_code}]")
except ConnectionError as e:
    print(f"Error server not response [{type(e).__name__}]")

os.system("./runserver.sh")