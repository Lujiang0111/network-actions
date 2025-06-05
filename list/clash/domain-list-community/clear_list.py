import os
import pathlib

curr_dir = pathlib.Path(__file__).resolve().parent
for file_name in os.listdir(curr_dir):
    if file_name.endswith(".list"):
        file_path = os.path.join(curr_dir, file_name)
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("")
        except Exception as e:
            print(f"claer {file_path} error: {e}")
