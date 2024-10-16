import os

folder_path = r'caminho da pasta' 
files = os.listdir(folder_path)

for index, file in enumerate(sorted(files)):
    ext = os.path.splitext(file)[1]
    new_name = f"{index + 1}{ext}"
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
