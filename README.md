# REDES DE COMPUTADORES

## Grupo 
- Enzo Lopes Campanholo - 10190463
- Felipe Bonatto Zwaizdis Scaquetti - 10438149

## Laboratório 3

### Introdução

Este laboratório se trata da implementação do conceito de sockets, a implementação dos códigos apresentados e as respotas às perguntas reforçãm o conhecimento de redes de maneira mais prática.

### Vídeos

 - Exercícios 1 e 2: https://www.youtube.com/watch?v=ejHOanxZpoo
 - Exercício 3: https://youtu.be/AYCaQvvuH8w

### Exercicio 1

#### Perguntas

(a) Execute o cliente TCP antes de executar o servidor TCP. O que
acontece? Por quê?

- Ocorre um erro quando o cliente é iniciado antes do servidor já que o TCP requer que uma conexão tenha sido préviamente estabelecida com o servidor.

b) Faça o mesmo procedimento para o cliente e servidor UDP.
O resultado foi similar ao socket TCP? Compare os resultados
e justifique.

- Utilizando a versão de UDP não há erro, porém o servidor não recebe a mensagem. Isso se deve ao fato do UDP não ter controle de conexão e sessão, então o cliente envia a mensagem sem se conectar ao servidor e nem verifica se o servidor respondeu.

c) O que acontece se o número da porta que o cliente tentar
se conectar for diferente da porta disponibilizada pelo
servidor?

- Se a porta de conexão do cliente for diferente da qual o servidor escuta, ocorre um erro de conexão, já que para que soquetes se comuniquem corretamente, é necessário o mapeamento correto de portas.


### Exercicio 2

#### Contexto

Aqui é implementado um simples aplicativo de mensagens entre cliente e servidor, utilizando TCP para garantir que as mensagens sejam transmitidas sem erro.


#### Execução Cliente

```bash
python ex12/msg_client.py
```

#### Execução Servidor

```bash
python ex12/msg_server.py
```

### Exercicio 3

#### Contexto

Aqui é implementado um simples aplicativo de controle remoto baseado em terminal, similar a ssh ou telnet, utilizando TCP para garantir que as mensagens sejam transmitidas sem erro.


#### Execução Cliente

```bash
python ex3/client.py
```

#### Execução Servidor

```bash
python ex3/server.py
```

