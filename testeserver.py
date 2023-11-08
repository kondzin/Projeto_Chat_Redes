import socket
import threading

HOST = 'localhost' #127.0.0.1
PORT = 9999
#inicializar o socket com seus parâmetros básicos (IPv4 e TCP)
#AF_INET É IPV4
#SOCK_STREAM É TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#PRECISAMOS VINCULAR O SOCKET SERVIDOR: ENDEREÇO IP : PORTA -> BIND
#LOCALHOST:9999 COMO SERVIDOR
sock.bind((HOST,PORT))

#AGORA O SERVIDOR COMEÇA A ESCUTAR CONEXÕES
sock.listen() #abre a porta
print(f"O Servidor {HOST}:{PORT} está aguardando conexões")

lista_clientes=[]

def recebeDados(sock_cliente):
    while True:
        try:
            mensagem = sock_cliente.recv(1024).decode()
            for conexao in lista_clientes:
                if conexao != sock_cliente:
                    conexao.sendall(mensagem.encode())
        except Exception as e:
            print(e)
            break
        msgNome = nome + " >> " + mensagem
        print(msgNome)




while True:
    #ACEITAMOS A CONEXÃO de vários clientes
    #conn é o socket do cliente
    #ender é a porta do cliente
    try:
        conn, ender = sock.accept()
    except:
        print('Ocorreu um erro durante o ACCEPT() na conexão com um novo usuário')
        continue
    #recebimento do nome do cliente que teve a conexão aceita
    
   
    
    
    lista_clientes.append(conn)
        
    try:
        nome = conn.recv(50).decode() #50 é o tamanho do buffer
    except:
        print("Ocorreu um erro durante o recebimento do nome. A conexão será encerrada")
        break
    print(f"Conectado com {nome}, IP: {ender[0]}, PORTA: {ender[1]}")
    threading.Thread(target= recebeDados, args=[conn]).start() 
    # while True:
    #     try:
    #         mensagem = conn.recv(1024).decode()
    #     except:
    #         print("Ocorreu algum erro na recepção dos dados, encerrando conexão.")
    #         break
    #     msgNome = nome + " >> " + mensagem
    #     print(msgNome)
        #Envio o dado para o cliente (eco)
        #conn.sendall(msgNome)
   #threadRecebeDados.start()    

#função que deve rodar na thread
