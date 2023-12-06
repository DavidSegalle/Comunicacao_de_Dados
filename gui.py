import tkinter as tk
import cipher as ci

class MyWindow:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Data Comunication")
        self.master.geometry("1280x720")

        self.cipher = ""

        self.client_screen()

    def submit(self):
        pass

    def client_screen(self):
        self.entry_label = tk.Label(self.master, text="Enter Text:")
        self.entry_label.pack()

        self.message = tk.StringVar()
        self.entry_text = tk.Entry(self.master, textvariable=self.message)
        self.entry_text.pack()

        self.should_cipher = tk.IntVar()
        self.set_cipher_box = tk.Checkbutton(self.master, text="Cypher", variable=self.should_cipher)
        self.set_cipher_box.pack()
        
        self.submit_button = tk.Button(self.master, text="Submit", command=self.data_screen)
        self.submit_button.pack()

    def data_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        message = self.message.get()
        if self.should_cipher.get() == 1:
            message = ci.encrypt(message)
        a = tk.Label(self.master, text="The message is: " + message)
        a.pack()
        

def main():
    root = tk.Tk()
    app = MyWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()