import socket
import threading

# Configurações do cliente
HOST ="localhost"
PORT =12345


# Criação de um socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

# Função para receber mensagens do servidor
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(e)
            break

# Função principal para enviar mensagens ao servidor
def main():
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()
    
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

if __name__ == '__main__':
    main()

# while True:
#     try message. == True:
#         print(message)
#     except Exception as e:
#         print(e)