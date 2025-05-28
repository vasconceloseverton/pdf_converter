
import threading
import subprocess
import sys
import os
from model.pdf_converter_model import pdf_to_image

class ConverterController:
    def __init__(self, view):
        self.view = view

    def iniciar_conversao(self, input_folder, output_folder):
        if not input_folder or not output_folder:
            self.view.show_warning("Por favor, selecione as pastas de entrada e saída.")
            return

        self.view.reset_progress()
        self.view.set_status("Iniciando...")

        def run():
            pdf_to_image(
                input_folder, 
                output_folder, 
                self.view.update_progress, 
                self.view.show_error
            )
            self.view.set_status("Conversão concluída!")
            self.abrir_pasta(output_folder)

        threading.Thread(target=run).start()

    def abrir_pasta(self, pasta):
        try:
            if sys.platform == 'win32':
                os.startfile(pasta)
            elif sys.platform == 'darwin':
                subprocess.Popen(['open', pasta])
            else:
                subprocess.Popen(['xdg-open', pasta])
        except Exception as e:
            self.view.show_error(f"Não foi possível abrir a pasta: {e}")
