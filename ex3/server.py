# Enzo Lopes Campanholo - 10190463
# Felipe Bonatto Zwaizdis Scaquetti - 10438149

import socket
import subprocess

TCP_PORTA = 10190
SERVER_HOST = "0.0.0.0"
SERVER_PASSWORD = "123"


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((SERVER_HOST, TCP_PORTA))
        server.listen()

        print(f"Servidor ouvindo em {SERVER_HOST}:{TCP_PORTA}")

        try:
            while True:
                connection, address = server.accept()
                print(f"Conexao de {address[0]}:{address[1]}")

                with connection:
                    handle_client(connection)

                print(f"Conexao encerrada para {address[0]}:{address[1]}")
        except KeyboardInterrupt:
            print("\nServidor encerrado.")


def handle_client(connection):
    reader = connection.makefile("r", encoding="utf-8", newline="\n")
    writer = connection.makefile("w", encoding="utf-8", newline="\n")

    try:
        password = reader.readline()
        if not password:
            return

        if password.strip() == SERVER_PASSWORD:
            writer.write("AUTENTICADO\n")
            writer.flush()
            repl(reader, writer)
        else:
            writer.write("SENHA_INVALIDA\n")
            writer.flush()
    finally:
        writer.close()
        reader.close()


def repl(reader, writer):
    while True:
        command = reader.readline()
        if not command:
            continue

        if command.strip() == "terminar":
            break

        try:
            result = subprocess.run(command.strip().split(" "),
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,
                                    timeout=5, text=True)
            combined_output = result.stdout
            if combined_output and not combined_output.endswith("\n"):
                combined_output += "\n"
            writer.write(combined_output)
            writer.write("<<FIM>>\n")
            writer.flush()

        except subprocess.SubprocessError:
            writer.write("Deu problema.\n")
            writer.write("<<FIM>>\n")
            writer.flush()
            continue


if __name__ == "__main__":
    main()
