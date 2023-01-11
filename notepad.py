import tkinter as tk
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        data = text.get(1.0, "end-1c")
        file.write(data)
        file.close()

def open_file():
    file = filedialog.askopenfile(mode="r", defaultextension=".txt")
    if file:
        data = file.read()
        text.delete(1.0, tk.END)
        text.insert(tk.END, data)

def main():
    root = tk.Tk()
    root.title("Notepad")
    root.geometry("300x250")

    text = tk.Text(root)
    text.pack()

    menubar = tk.Menu(root)
    file = tk.Menu(menubar, tearoff=0)
    file.add_command(label="Open", command=open_file)
    file.add_command(label="Save", command=save_file)
    menubar.add_cascade(label="File", menu=file)
    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    main()
