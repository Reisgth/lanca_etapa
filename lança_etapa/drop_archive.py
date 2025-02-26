import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES

def get_file_path():
    root = TkinterDnD.Tk()
    root.title("Arraste e solte seu arquivo .docx")
    root.geometry("400x200")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 200) // 2
    root.geometry(f"400x200+{x}+{y}")

    file_path_var = tk.StringVar()

    def file_path(event):
        file_path_var.set(event.data.strip("{}"))
        root.destroy()

    instrucao = tk.Label(root, text="Arraste seu arquivo .docx aqui", pady=20)
    instrucao.pack()

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', file_path)

    root.mainloop()

    return file_path_var.get()
