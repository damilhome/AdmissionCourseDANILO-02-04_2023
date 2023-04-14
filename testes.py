import os

# Definindo o diretório base
base_dir = '/home/user'

# Definindo um subdiretório e um nome de arquivo
sub_dir = 'imagens'
file_name = 'imagem1.jpg'

# Concatenando o diretório base, subdiretório e nome do arquivo e normalizando o caminho
caminho_completo = os.path.normpath(os.path.join(base_dir, sub_dir, file_name))

print(caminho_completo)