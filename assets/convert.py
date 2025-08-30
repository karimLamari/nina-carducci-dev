import os
from PIL import Image

def resize_webp_images(root_folder, max_width=1920, quality=85):
    count = 0
    root_folder = os.path.abspath(root_folder)
    for dirpath, dirnames, filenames in os.walk(root_folder):
        print(f"📂 Scan dossier : {dirpath}")
        for filename in filenames:
            if filename.lower().endswith(".webp"):
                full_path = os.path.join(dirpath, filename)
                try:
                    with Image.open(full_path) as img:
                        width, height = img.size
                        if width > max_width:
                            new_height = int((max_width / width) * height)
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                            img.save(full_path, "WEBP", quality=quality, method=6)
                            print(f"📏 Redimensionné : {filename} ({width}x{height} → {max_width}x{new_height})")
                        else:
                            print(f"ℹ️ {filename} gardée ({width}x{height})")
                        count += 1
                except Exception as e:
                    print(f"❌ Erreur {full_path}: {e}")
    print(f"\n✨ Total traité : {count} image(s)")

if __name__ == "__main__":
    dossier = "./images"  # dossier racine à traiter
    resize_webp_images(dossier, max_width=1920, quality=85)
