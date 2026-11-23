import subprocess

# Создаём zip-архив с каталогом photos и всеми файлами внутри него.
# Утилита zip вызывается из командной строки через subprocess.
subprocess.run(['zip', '-r', 'photos.zip', 'photos'], check=True)
