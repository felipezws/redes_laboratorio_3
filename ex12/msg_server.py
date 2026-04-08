# Enzo Lopes Campanholo - 10190463
# Felipe Bonatto Zwaizdis Scaquetti - 10438149

import socket
import datetime

TCP_IP = "127.0.0.1"
TCP_PORTA = 10438
TAMANHO_BUFFER = 1024

_LINE_UP = "\033[1A"
_LINE_CLEAR = "\x1b[2K"

PREFIXO = "[SERVIDOR]: " 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((TCP_IP, TCP_PORTA))

servidor.listen(1)

print(f"Servidor dispoivel na porta {TCP_PORTA} e escutando.....")

conn, addr = servidor.accept()

print("Endereço conectado:", addr)

print("Digite QUIT para sair")

while True:
    MENSAGEM = conn.recv(TAMANHO_BUFFER).decode()

    if MENSAGEM:
        if MENSAGEM == "QUIT":
            print("Cliente fechou a conexão")
            print("Saindo...")
            break

        print(f"[CLIENTE] {datetime.datetime.now()}: {MENSAGEM}")

    in_data = input(PREFIXO)
    print(f"{_LINE_UP}{_LINE_CLEAR}[SERVIDOR] {datetime.datetime.now()}: {in_data}")

    if in_data == "QUIT":
        print(f"{PREFIXO} saindo...")
        conn.send("QUIT".encode())
        break

    conn.send(in_data.encode())

conn.close()
servidor.close()
