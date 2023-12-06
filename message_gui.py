import tkinter as tk
import cipher as ci
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MyWindow:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Data Comunication")
        self.master.geometry("1280x720")

        self.cipher = ""

        self.choose_screen()

    def choose_screen(self):

        choices = ['client', 'server']
        self.client_server_string = tk.StringVar(self.master)
        self.client_server_string.set('None')
        w = tk.OptionMenu(self.master, self.client_server_string, *choices)
        w.pack()
        submit_button = tk.Button(self.master, text="Submit", command=self.client_server_choice)
        submit_button.pack()
    
    def client_server_choice(self):
        if self.client_server_string.get() == 'client':
            self.client_screen()
        elif self.client_server_string.get() == 'server':
            self.server_screen()
        
    def server_screen():
        pass

    def client_screen(self):

        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.entry_label = tk.Label(self.master, text="Enter Text:")
        self.entry_label.pack()

        # Se precisar pegar ip manualmente é só adicionar um desses na primeira linha de choose_screen(), a variável é acessada depois com self.message.get()
        self.message = tk.StringVar()
        self.entry_text = tk.Entry(self.master, textvariable=self.message)
        self.entry_text.pack()

        self.should_cipher = tk.IntVar()
        self.set_cipher_box = tk.Checkbutton(self.master, text="Cypher", variable=self.should_cipher)
        self.set_cipher_box.pack()
        
        self.submit_button = tk.Button(self.master, text="Submit", command=self.client_data_screen)
        self.submit_button.pack()
    
    def clean_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def client_data_screen(self):

        # Enviar mensagem aqui

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
        binary_message = tk.Label(self.master, text="The binary is: " + str(binary))
        binary_message.pack()

        applied_algorithm = ci.codLin_2b1q(binary)
        applied_algorithm_message = tk.Label(self.master, text="After applying the algorithm: " + str(applied_algorithm))
        applied_algorithm_message.pack()

        graph = ci.plot_graph(applied_algorithm)
        canvas = FigureCanvasTkAgg(graph, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack()

        self.done_button = tk.Button(self.master, text="Back", command=self.client_screen)
        self.done_button.pack()
        
        

def main():
    root = tk.Tk()
    app = MyWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()