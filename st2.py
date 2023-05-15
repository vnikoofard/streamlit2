import streamlit as st
from PIL import Image, ImageDraw, ImageFont


def text_on_image(image, text, color, font_size):
    img = Image.open(image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw.text((30, 30), text, fill=color, font=font)
    # st.image(img, width=300)
    img.save("image.png")
    return img


image = st.file_uploader("Escolhe uma imagem", type=["png", "jpeg", "jpg"])

text = st.text_input("Escreve um texto")

color = st.selectbox("Escolhe uma cor", ["red", "green", "blue"])
# st.write(color)
font_size = st.slider("Escolhe o tamanho da fonte", 10, 100, 20)
# font_size2 = st.number_input(
#     "Escolhe o tamanho da fonte", min_value=10, max_value=100, value=20
# )
if image:
    # st.image(image, width=300)
    result = st.button(
        "Gerar marca dàgua",
        type="primary",
        help="Clique para gerar a marca d'água",
        on_click=text_on_image,
        args=(image, text, color, font_size),
    )
    st.write(result)
    if result:
        st.image("image.png", width=300)
        with open("image.png", "rb") as file:
            st.download_button("Baixar imagem", file.read(), mime="image/png")
