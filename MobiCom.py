
import streamlit as st
import gdown
from PIL import Image
import os
os.system('pip install gdown')

# Função para baixar imagens do Google Drive
def download_image_from_drive(drive_url, output_path):
    try:
        gdown.download(drive_url, output_path, quiet=False)
        return True
    except Exception as e:
        st.error(f"Erro ao baixar a imagem: {e}")
        return False

# Página Streamlit
st.title("Google Drive Image Viewer")

# Links das imagens no Google Drive
# Exemplo: URLs públicas do Google Drive
image_links = {
    "Imagem 1": "https://drive.google.com/file/d/1tw5Ys2ZlaH_M8tXLdpVdWT5Z2M1kAGQ9/view?usp=drive_link"
}

# Loop para baixar e exibir imagens
for image_name, image_url in image_links.items():
    st.write(f"### {image_name}")
    
    image_file = f"{image_name}.jpg"
    if download_image_from_drive(image_url, image_file):
        image = Image.open(image_file)
        st.image(image, caption=image_name)
    
    # Remover o arquivo após exibição (opcional)
    if os.path.exists(image_file):
        os.remove(image_file)
