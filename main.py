import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def traducir_texto(texto):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un traductor experto. Traduce el siguiente texto completo del español al inglés, manteniendo el contexto y la estructura del texto original. Asegurate de traducir los nombres de los personajes de su version en espanol a la version en ingles. Por ejemplo: Tito Macio es Titus Maccius, y la ciudad de Qart Hadasht tienes que llamarla por el mismo nombre, Qart Hadasht. No llamarla Carthage.:"},
            {"role": "user", "content": texto}
        ]
    )
    return response.choices[0].message.content

def agregar_al_archivo(texto_traducido):
    with open("libro.txt", "a", encoding="utf-8") as archivo:
        archivo.write(texto_traducido)
        archivo.write("\n\n")  # Separador entre parrafos

def main():
    while True:
        print("Ingresa el texto completo en español (o 'salir' para terminar):")
        print("Presiona Enter dos veces cuando hayas terminado de ingresar el texto.")
        
        lineas = []
        while True:
            linea = input()
            if linea == "":
                break
            lineas.append(linea)
        
        texto_original = "\n".join(lineas)
        
        if texto_original.lower() == 'salir':
            break

        if texto_original:
            texto_traducido = traducir_texto(texto_original)
            agregar_al_archivo(texto_traducido)
            print("Texto traducido y agregado al archivo 'libro.txt'")
        else:
            print("No se ingresó ningún texto. Intenta de nuevo.")

if __name__ == "__main__":
    main()