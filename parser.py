import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os

def epub_to_text(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    
    text = ""
    for html_content in chapters:
        soup = BeautifulSoup(html_content, 'html.parser')
        text += soup.get_text() + "\n\n"
    
    return text

def main():
    epub_file = input("Ingresa la ruta del archivo EPUB: ")
    if not os.path.exists(epub_file):
        print("El archivo no existe.")
        return

    try:
        extracted_text = epub_to_text(epub_file)
        
        with open("texto.txt", "w", encoding="utf-8") as f:
            f.write(extracted_text)
        
        print("El texto ha sido extraído y guardado en 'texto.txt'")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    main()