import socket
import sys
import subprocess
from datetime import datetime

HOST = ""
PORT = 8888
WACHTWOORD = "HU2026"

def schrijf_log(commando):
    tijd = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bestand = open("server.log", "a")
    bestand.write(tijd + " - " + commando + "\n")
    bestand.close()


try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket gemaakt")
except:
    print("Fout bij maken van socket")
    sys.exit()


try:
    server.bind((HOST, PORT))
    print("Socket gebonden aan poort", PORT)
except:
    print("Fout bij binden aan poort")
    server.close()
    sys.exit()


try:
    server.listen(10)
    print("Server luistert op poort", PORT)
except:
    print("Fout bij luisteren")
    server.close()
    sys.exit()


client, adres = server.accept()

print("Verbonden met", adres[0])

client.sendall(b"Welkom op de server\r\n")
client.sendall(b"Voer wachtwoord in: ")

wachtwoord = client.recv(1024).decode().strip()

if wachtwoord != WACHTWOORD:
    client.sendall(b"Verkeerd wachtwoord\r\n")
    client.close()
    server.close()
    sys.exit()


client.sendall(b"Login succesvol\r\n")
client.sendall(b"Commando's: CALC, NOTEPAD, stop\r\n")

while True:

    try:
        data = client.recv(1024)

        if not data:
            break

        commando = data.decode().strip()

        if commando == "":
            continue

        print("Ontvangen:", commando)

        if commando.lower() == "stop":
            client.sendall(b"Server stopt\r\n")
            break

        elif commando.upper() == "CALC":
            subprocess.Popen("calc.exe")
            schrijf_log("CALC")
            client.sendall(b"Calculator gestart\r\n")

        elif commando.upper() == "NOTEPAD":
            subprocess.Popen("notepad.exe")
            schrijf_log("NOTEPAD")
            client.sendall(b"Notepad gestart\r\n")

        else:
            client.sendall(b"Onbekend commando\r\n")

    except:
        print("Verbinding verbroken")
        break


client.close()
server.close()

print("Server gestopt")