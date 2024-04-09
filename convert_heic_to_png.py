import os
import pyheif
from PIL import Image

def convert_heic_to_png(source_folder, output_folder):
    print(f"Source folder: {os.path.abspath(source_folder)}")
    print(f"Output folder: {os.path.abspath(output_folder)}")
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".heic"):  # Ignora mayúsculas/minúsculas
            try:
                input_path = os.path.join(source_folder, filename)
                output_path = os.path.join(output_folder, filename.replace(".HEIC", ".png").replace(".heic", ".png"))
                
                print(f"Convirtiendo: {input_path} -> {output_path}")
                
                heif_file = pyheif.read(input_path)
                image = Image.frombytes(
                    heif_file.mode, 
                    heif_file.size, 
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )
                image.save(output_path, "PNG")
                print(f"Convertido: {output_path}")
            except Exception as e:
                print(f"Error al convertir {filename}: {e}")

if __name__ == "__main__":
    source_dir = "./source"
    output_dir = "./output"
    convert_heic_to_png(source_dir, output_dir)
