# Enzo Lopes Campanholo - 10190463
# Felipe Bonatto Zwaizdis Scaquetti - 10438149

import ipaddress
import socket

TCP_PORTA = 10190


def main():
    ipv4_address = prompt_ipv4_address()
    client = establish_tcp_connection(ipv4_address)
    if client is None:
        print("Nao foi possivel estabelecer uma conexao TCP com o servidor.")
        return

    reader = client.makefile("r", encoding="utf-8", newline="\n")
    writer = client.makefile("w", encoding="utf-8", newline="\n")

    try:
        password = input("Senha: ").strip()
        writer.write(password + "\n")
        writer.flush()

        auth_response = reader.readline()
        if not auth_response:
            print("Servidor encerrou a conexao.")
            return

        print(auth_response.strip())
        if auth_response.strip() != "AUTENTICADO":
            return

        while True:
            try:
                command = input("> ").strip()
            except EOFError:
                command = "terminar"

            if not command:
                continue

            writer.write(command + "\n")
            writer.flush()

            if command == "terminar":
                break

            while True:
                response = reader.readline()
                if not response:
                    print("Servidor encerrou a conexao.")
                    return
                if response.strip() == "<<FIM>>":
                    break
                print(response, end="")
    finally:
        writer.close()
        reader.close()
        client.close()


def prompt_ipv4_address():
    while True:
        ipv4_address = input("Endereco IPv4 do servidor: ").strip()

        try:
            ipaddress.IPv4Address(ipv4_address)
        except ipaddress.AddressValueError:
            print("Endereco IPv4 invalido.")
            continue

        return ipv4_address


def establish_tcp_connection(ipv4_address):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ipv4_address, TCP_PORTA))
    except OSError as error:
        print(f"Erro ao conectar: {error}")
        client.close()
        return None

    print("Conexao estabelecida.")
    return client


if __name__ == "__main__":
    main()
