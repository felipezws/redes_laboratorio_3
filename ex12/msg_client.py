# Enzo Lopes Campanholo - 10190463
# Felipe Bonatto Zwaizdis Scaquetti - 10438149

import socket
import datetime

TCP_IP = "127.0.0.1"
TCP_PORTA = 10438
TAMANHO_BUFFER = 1024

_LINE_UP = "\033[1A"
_LINE_CLEAR = "\x1b[2K"

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((TCP_IP, TCP_PORTA))

MENSAGEM = ""
PREFIXO = "[CLIENTE]: "

print("Digite QUIT para sair")

while True:
    MENSAGEM = input(PREFIXO)

    if MENSAGEM:
        if MENSAGEM == "QUIT":
            print(f"{PREFIXO} saindo...")
            cliente.send("QUIT".encode())
            break

        print(f"{_LINE_UP}{_LINE_CLEAR}[CLIENTE] {datetime.datetime.now()}: {MENSAGEM}")

    cliente.send(MENSAGEM.encode())

    data, addr = cliente.recvfrom(TAMANHO_BUFFER)

    if data:
        if data.decode() == "QUIT":
            print("Servidor fechou a conexão")
            print("Saindo...")
            break

    print(f"[SERVIDOR] {datetime.datetime.now()} {data.decode()}")

cliente.close()
