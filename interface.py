import tkinter as tk
import cliente

# Função para enviar mensagens
def send_message():
    message = entry.get()
    if message:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "Você: " + message + "\n")
        chat_log.config(state=tk.DISABLED)
        client.client_socket.send(message.encode('utf-8'))
        entry.delete(0, tk.END)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Chat")
root.geometry("400x400")

chat_log = tk.Text(root, state=tk.DISABLED)
chat_log.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(root)
entry.pack(fill=tk.BOTH, expand=True)

send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

root.mainloop()
