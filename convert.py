import os
import pyheif
from PIL import Image
import pillow_heif

def convert_heic_to(image_path, output_format="jpeg"):
    """
    Converte uma imagem .heic para .jpeg ou .png.
    
    Parâmetros:
    - image_path (str): caminho do arquivo .heic
    - output_format (str): 'jpeg' ou 'png'
    """
    if output_format.lower() not in ['jpeg', 'png']:
        raise ValueError("Formato de saída deve ser 'jpeg' ou 'png'.")

    pillow_heif.register_heif_opener()

    image = Image.open(image_path)
    image_path = f"{os.path.splitext(image_path)[0]}.{output_format}"
    image.save(image_path, format=output_format.upper())
    print(f"Imagem convertida: {image_path}")   

if __name__ == "__main__":
    file_path = input("Digite o caminho do arquivo HEIC: ")
    output_format = input("Digite o formato de saída (jpeg/png): ")
    convert_heic_to(file_path, output_format)
