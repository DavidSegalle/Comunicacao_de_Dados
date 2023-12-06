import tkinter as tk

def clear_screen():
    # Destroy or forget all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()  # Or widget.pack_forget() for packing widgets
    main()

def create_new_screen():
    # Create new widgets or layout
    label = tk.Label(root, text="New Screen")
    label.pack()

    button = tk.Button(root, text="Back to Main Screen", command=clear_screen)
    button.pack()

def main():
    root.title("Screen Management")
    
    create_new_screen_button = tk.Button(root, text="Create New Screen", command=create_new_screen)
    create_new_screen_button.pack()

    root.mainloop()
    
root = tk.Tk()
main()