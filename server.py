# import socket 
# import threading 

# # configuração do servidor

# HOST = "localhost"
# PORT = 3030

# # criando um socket pro servidor

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #familia,tipo e protocolo 
# server_socket.bind((HOST,PORT)) #liga o socket a um endereço
# server_socket.listen() # coloca ele em modo escuta para aceitar entradas 

# #lista para guardar as conexões

# client_connections = [] #permite armazenar os usuários


# # função para tratar as mensagens recebidas

# def mensagem_cliente(client_socket):
#     while True:
#         try:
#             mensagem = client_socket.recv(1024).deode('utf-8')
#             if not mensagem:
#                 client_connections.remove(client_socket)
#                 client_socket.close()
#                 break

# #reenvia a mensagem para todos os clientes
#             for connection in client_connections:
#                 if connection != client_socket:
#                     connection.send(mensagem.encode('utf-8'))
#         except exception as e:
#             print(e)
#             break   

# #função principal para aceitar conexôes de clientes

# def main():
#     print(f'Entrando no servidor {HOST}, {PORT} ...')
#     while True:
#         client_socket, address = server_socket.accept()
#         print(f'A conexão foi aceita com sucesso  {address[0]}:{address[1]} !!!!')
#         client_connections.append(client_socket)
#         client_handler = threading.Thread(target=mensagem_cliente, args = (client_socket))
#         client_handler.start()

# if __name__ == '__main__':
#     main()

import socket
import threading
import time

# Configurações do servidor
HOST = 'localhost'
PORT = 12345

# Criação de um socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Lista para armazenar as conexões dos clientes
client_connections = []

# Função para lidar com as mensagens recebidas de um cliente
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
            # if not message:
            #     client_connections.remove(client_socket)
            #     client_socket.close()
            #     break

            # Reenvia a mensagem para todos os outros clientes
            for connection in client_connections:
                if connection != client_socket:
                    connection.send(message.encode('utf-8'))
        except Exception as e:
            print(e)
            break

# Função principal para aceitar conexões de clientes
def main():
    print("Servidor escutando em {}:{}...".format(HOST, PORT))
    while True:
        client_socket, address = server_socket.accept()
        print(f"Conexão aceita de {address[0]}:{address[1]}")
        client_connections.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()





