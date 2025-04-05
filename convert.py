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

    # Carrega o arquivo HEIC
    heif_file = pyheif.read(image_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode
    )

    # Define nome do novo arquivo
    output_path = os.path.splitext(image_path)[0] + f".{output_format}"

    # Salva no novo formato
    image.save(output_path, format=output_format.upper())
    print(f"Imagem convertida: {output_path}")

def convert_heic_2(image_path):
    pillow_heif.register_heif_opener()

    image = Image.open(image_path)
    image_path = os.path.splitext(image_path)[0] + ".jpeg"
    print(image_path)
    image.save(image_path, format="JPEG")

if __name__ == "__main__":
    file_path = input("Digite o caminho do arquivo HEIC: ")
    output_format = input("Digite o formato de saída (jpeg/png): ")
    # convert_heic_to(file_path, output_format)
    convert_heic_2(file_path)
