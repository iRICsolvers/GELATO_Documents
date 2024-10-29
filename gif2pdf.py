from PIL import Image
import os

# 変換するルートディレクトリを指定
root_directory = 'source'

for dirpath, _, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith(".gif"):
            gif_path = os.path.join(dirpath, filename)
            png_path = os.path.join(dirpath, filename.replace(".gif", ".png"))
            with Image.open(gif_path) as img:
                # 最後のコマに移動
                img.seek(img.n_frames - 1)
                img.save(png_path, "PNG")
            print(f"Converted {filename} to PNG (last frame).")