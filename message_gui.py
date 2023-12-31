import tkinter as tk
import cipher as ci
from server_main import Server
from client_main import Client
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class MyWindow:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Data Comunication")
        self.master.geometry("1280x720")

        self.cipher = ""

        self.server_ip = ''

        self.should_cipher = tk.IntVar()

        self.choose_screen()


    def choose_screen(self):

        self.entry_label = tk.Label(self.master, text="Server IP:")
        self.entry_label.pack()
        self.message = tk.StringVar()
        self.entry_text = tk.Entry(self.master, textvariable=self.message)
        self.entry_text.pack()

        choices = ['client', 'server']
        self.client_server_string = tk.StringVar(self.master)
        self.client_server_string.set('None')
        w = tk.OptionMenu(self.master, self.client_server_string, *choices)
        w.pack()
        submit_button = tk.Button(self.master, text="Submit", command=self.client_server_choice)
        submit_button.pack()

    def client_server_choice(self):
        if self.client_server_string.get() == 'client':
            self.clientobj = Client(self.message.get())
            self.client_screen()
        elif self.client_server_string.get() == 'server':
            self.serverobj = Server()
            self.server_screen()

    def server_screen(self):


        # Receber mensagem aqui e remover aquele sleep ali em baixo, mais especificamente, o sleep que está------┐
        #                                                                                                        |
        received_message = self.serverobj.receive_message()#                                                     |
#                                                                                                                |
#                                                                                                                |
        self.set_cipher_box = tk.Checkbutton(self.master, text="Cypher", variable=self.should_cipher)#           |
        self.set_cipher_box.pack()#                                                                              |
#                                                                                                                |
        # time.sleep(5) #  Removi!    Aqui  <--------------------------------------------------------------------┘

        graph = ci.plot_graph(received_message, 'Received Signal')
        canvas = FigureCanvasTkAgg(graph, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack()

        applied_algorithm_message = tk.Label(self.master, text="Which is: " + str(received_message))
        applied_algorithm_message.pack()

        removed_algorithm = ci.decode_2b1q(received_message)
        removed_algorithm_message = tk.Label(self.master, text="After removing the algorithm: " + str(removed_algorithm))
        removed_algorithm_message.pack()

        message = ci.to_text(removed_algorithm)
        crypted_message = tk.Label(self.master, text="The crypted text is: " + str(message) + " Since should cript was set to " + str(self.should_cipher.get()))
        crypted_message.pack()

        if self.should_cipher.get() == 1:
            message = ci.decrypt(message)

        on_screen_message = tk.Label(self.master, text="The original message was: " + message)
        on_screen_message.pack()

        self.wait_for_new_message_button = tk.Button(self.master, text="Wait for new message", command=self.new_message_setup)
        self.wait_for_new_message_button.pack()



    def new_message_setup(self):
        self.clean_screen()
        self.server_screen()

    def client_screen(self):

        for widget in self.master.winfo_children():
            widget.destroy()

        self.entry_label = tk.Label(self.master, text="Enter Text:")
        self.entry_label.pack()

        # Se precisar pegar ip manualmente é só adicionar um desses na primeira linha de choose_screen(), a variável é acessada depois com self.message.get()
        self.message = tk.StringVar()
        self.entry_text = tk.Entry(self.master, textvariable=self.message)
        self.entry_text.pack()


        self.set_cipher_box = tk.Checkbutton(self.master, text="Cypher", variable=self.should_cipher)
        self.set_cipher_box.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.client_data_screen)
        self.submit_button.pack()

    def clean_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def client_data_screen(self):

        # Enviar mensagem aqui
        # ----> Tive que enviar mais pra baixo, ela precisa estar codificada como sinal digital.

        for widget in self.master.winfo_children():
            widget.destroy()

        message = self.message.get()
        on_screen_message = tk.Label(self.master, text="The message is: " + message)
        on_screen_message.pack()

        if self.should_cipher.get() == 1:
            message = ci.encrypt(message)

        on_screen_message = tk.Label(self.master, text="The cyptography message is: " + message + " since checkbox was " + str(self.should_cipher.get()))
        on_screen_message.pack()

        binary = ci.to_binary(message)
        # binary = [0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
        binary_message = tk.Label(self.master, text="The binary is: " + str(binary))
        binary_message.pack()

        applied_algorithm = ci.encode_2b1q(binary)
        applied_algorithm_message = tk.Label(self.master, text="After applying the algorithm: " + str(applied_algorithm))
        applied_algorithm_message.pack()

        graph = ci.plot_graph(applied_algorithm, 'Sent Signal')
        canvas = FigureCanvasTkAgg(graph, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack()

        self.done_button = tk.Button(self.master, text="Back", command=self.client_screen)
        self.done_button.pack()

        # Estou enviando aqui!
        self.clientobj.send_message(applied_algorithm)


def main():
    root = tk.Tk()
    app = MyWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
