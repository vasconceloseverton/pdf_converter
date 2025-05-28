
import os
import fitz

def pdf_to_image(input_folder, output_folder, progress_callback, error_callback):
    if not os.path.exists(input_folder):
        error_callback(f"A pasta de entrada '{input_folder}' não existe.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

    if not files:
        error_callback("Nenhum arquivo PDF encontrado na pasta de entrada.")
        return

    total_files = len(files)
    current = 0

    for file in files:
        input_path = os.path.join(input_folder, file)
        pdf_document = fitz.open(input_path)
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            image = page.get_pixmap()
            output_filename = f"{os.path.splitext(file)[0]}_page{page_number + 1}.png"
            output_path = os.path.join(output_folder, output_filename)
            image.save(output_path, "png")
        pdf_document.close()

        current += 1
        progress_callback(current, total_files)
