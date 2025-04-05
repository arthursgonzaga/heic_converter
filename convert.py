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


def main():
    """
    Função principal para executar a conversão de imagens HEIC.
    """
    try:
        file_path = input("Digite o caminho do arquivo HEIC: ").strip()
        output_format = input("Digite o formato de saída (jpeg/png): ").strip().lower()

        # Executa a conversão
        convert_heic_to(file_path, output_format)
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
