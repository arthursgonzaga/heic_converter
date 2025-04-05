import os
from PIL import Image
import pillow_heif


def convert_heic_to(image_path, output_format="jpeg"):
    """
    Converte uma imagem .heic para .jpeg ou .png.

    Parâmetros:
    - image_path (str): Caminho do arquivo .heic.
    - output_format (str): Formato de saída ('jpeg' ou 'png').

    Retorna:
    - str: Caminho do arquivo convertido.
    """
    # Verifica se o formato de saída é válido
    if output_format.lower() not in ['jpeg', 'png']:
        raise ValueError("Formato de saída deve ser 'jpeg' ou 'png'.")

    # Registra o suporte ao formato HEIC
    pillow_heif.register_heif_opener()

    # Abre a imagem HEIC
    image = Image.open(image_path)

    # Define o caminho do arquivo de saída
    output_path = f"{os.path.splitext(image_path)[0]}.{output_format}"

    # Salva a imagem no formato desejado
    image.save(output_path, format=output_format.upper())
    print(f"Imagem convertida: {output_path}")

    return output_path


def convert_all_in_folder(folder_path, output_format="jpeg"):
    """
    Converte todas as imagens .heic em uma pasta para o formato especificado.

    Parâmetros:
    - folder_path (str): Caminho da pasta contendo as imagens .heic.
    - output_format (str): Formato de saída ('jpeg' ou 'png').
    """
    # Verifica se a pasta existe
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"A pasta '{folder_path}' não foi encontrada.")

    # Lista todos os arquivos na pasta
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".heic"):
            file_path = os.path.join(folder_path, file_name)
            try:
                print(f"Convertendo: {file_path}")
                convert_heic_to(file_path, output_format)
            except Exception as e:
                print(f"Erro ao converter '{file_path}': {e}")


def main():
    """
    Função principal para executar a conversão de imagens HEIC.
    """
    try:
        folder_path = input("Digite o caminho da pasta com imagens HEIC: ")
        output_path = input("Digite o formato de saída (jpeg ou png): ")

        # Converte todas as imagens na pasta
        convert_all_in_folder(folder_path, output_format)
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
