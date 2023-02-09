import subprocess
import re

def fnGetIpsFromArpScan(strText: str) -> list:
    # Utilizamos una expresión regular para extraer las direcciones IP del texto
    strIpPattern = r"^\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*$"
    lstIps = re.findall(strIpPattern, strText, re.MULTILINE)
    return lstIps

try:
    # Ejecutamos el comando 'arp-scan -l' y obtenemos el resultado
    objResult = subprocess.run(["arp-scan", "-l"], stdout=subprocess.PIPE, check=True)
except subprocess.CalledProcessError as e:
    # Si hubo un error al ejecutar el comando, mostramos un mensaje y salimos
    strErrorMessage = f"Error al ejecutar el comando: {e}"
    print(strErrorMessage)
    exit(1)

# El resultado del comando se encuentra en la propiedad 'stdout' del objeto 'CompletedProcess'
strText = objResult.stdout.decode("utf-8")

# Obtenemos las direcciones IP del texto
lstIps = fnGetIpsFromArpScan(strText)

# Abrimos un archivo de texto en modo de escritura
with open("resultado.txt", "w") as f:
    # Escribimos cada dirección IP en una línea del archivo
    for strIp in lstIps:
        f.write(strIp + "\n")

