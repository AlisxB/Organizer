import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def organize_files_by_extension(folder_path):
    try:
        # Lista todos os arquivos na pasta
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        for file in files:
            # Obtém a extensão do arquivo
            file_extension = file.split('.')[-1]

            # Cria uma nova pasta com o nome da extensão se ela não existir
            new_folder = os.path.join(folder_path, file_extension)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            # Move o arquivo para a nova pasta
            shutil.move(os.path.join(folder_path, file), os.path.join(new_folder, file))

        messagebox.showinfo("Sucesso", f"Os arquivos em '{folder_path}' foram organizados por suas extensões.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


def select_folder():
    folder_path = filedialog.askdirectory(title="Selecione uma pasta")
    if folder_path:
        organize_files_by_extension(folder_path)


# Criação da interface gráfica
def create_gui():
    # Janela principal
    window = tk.Tk()
    window.title("Organizador de Arquivos")
    window.geometry("400x200")
    window.resizable(False, False)

    # Título
    title_label = tk.Label(window, text="Organizador de Arquivos por Extensão", font=("Arial", 14), pady=20)
    title_label.pack()

    # Botão para selecionar a pasta
    select_button = tk.Button(window, text="Selecionar Pasta", font=("Arial", 12), command=select_folder, width=20)
    select_button.pack(pady=10)

    # Rodapé
    footer_label = tk.Label(window, text="Desenvolvido por Alison Santos", font=("Arial", 10), pady=20)
    footer_label.pack(side=tk.BOTTOM)

    # Inicia o loop da interface
    window.mainloop()


# Executa o programa
if __name__ == "__main__":
    create_gui() # Create