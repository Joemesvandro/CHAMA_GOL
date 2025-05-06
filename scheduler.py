
import time
from datetime import datetime
import subprocess

while True:
    agora = datetime.now()
    if 11 <= agora.hour < 23:
        print(f"🟢 Executando script às {agora.strftime('%H:%M:%S')}")
        subprocess.run(["python3", "main.py"])
    else:
        print(f"🔴 Fora do horário permitido ({agora.strftime('%H:%M:%S')}). Aguardando 5 minutos.")
        time.sleep(300)
