
# PDF Converter MVC

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1.22%2B-orange)

Conversor de arquivos PDF para imagens PNG, com interface gráfica em **Tkinter**, utilizando o padrão arquitetural **MVC (Model-View-Controller)**.

Este projeto permite selecionar uma pasta de entrada com arquivos `.pdf` e uma pasta de saída para salvar as imagens `.png` geradas, convertendo todas as páginas de cada PDF.

---

## 🎯 Funcionalidades

✅ Interface gráfica intuitiva  
✅ Seleção de pasta de entrada e saída  
✅ Conversão de todas as páginas de PDFs para PNG  
✅ Barra de progresso e status de conversão  
✅ Arquitetura separada em Model, View e Controller  
✅ Compatível com Windows, Linux e macOS  

---

## 🖼️ Layout

![screenshot](https://via.placeholder.com/600x300.png?text=PDF+Converter+MVC)

---

## 📂 Estrutura do Projeto

```
pdf_converter/
├── controller/
│   └── converter_controller.py
├── model/
│   └── pdf_converter_model.py
├── view/
│   └── app_view.py
├── main.py
└── README.md
```

- **model/**: lógica de conversão de PDF para imagem.
- **controller/**: lógica de controle da aplicação.
- **view/**: interface gráfica com Tkinter.
- **main.py**: ponto de entrada da aplicação.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) – manipulação e renderização de PDFs.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – criação da interface gráfica.

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/vasconceloseverton/pdf-converter.git
cd pdf-converter
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install pymupdf
```

---

## ▶️ Como Usar

```bash
python main.py
```

1. Clique em "Selecionar Pasta" para escolher a pasta de entrada com os arquivos `.pdf`.
2. Clique em "Selecionar Pasta" para definir a pasta onde as imagens `.png` serão salvas.
3. Pressione "Converter PDFs".
4. Acompanhe a barra de progresso.

---

## 📦 Gerar Executável (.exe)

Se quiser gerar um executável para Windows:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```

O arquivo `.exe` estará na pasta `dist/`.

---

## ✅ Contribuindo

Contribuições são bem-vindas!  
Para contribuir, por favor:

1. Fork o repositório.
2. Crie uma branch (`git checkout -b feature/sua-feature`).
3. Commit suas mudanças (`git commit -m 'Add sua feature'`).
4. Push para a branch (`git push origin feature/sua-feature`).
5. Abra um Pull Request.

---

## 📝 Licença

Este projeto está licenciado sob a **Licença MIT** – veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

Desenvolvido por **[Everton Vasconcelos](https://github.com/vasconceloseverton)**.  

---

## ⭐ Agradecimento

Se este projeto te ajudou, deixe uma ⭐ no repositório!  
Isso motiva a manter o projeto sempre atualizado. 🚀
