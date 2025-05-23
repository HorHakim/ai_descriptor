import streamlit as st
import tempfile
import os
from backend import describe_image

st.set_page_config(page_title="Description d'image piquante", layout="centered")

st.title("🖼️ Analyse d’image à la sauce Mistral")
st.markdown("Dépose une image et laisse Mistral te balancer une description pleine de mordant 😏")

uploaded_file = st.file_uploader("Choisis une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Affiche l'image
    st.image(uploaded_file, caption="Image sélectionnée", use_container_width =True)

    # Crée un fichier temporaire pour passer le chemin à ton backend
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    if st.button("Décris cette œuvre d’art 🎨"):
        with st.spinner("Je décortique ça avec insolence..."):
            try:
                description = describe_image(temp_path)
                st.success("Voilà le verdict !")
                st.markdown(f"🗯️ *{description}*")
            except Exception as e:
                st.error(f"Oups, une erreur s'est produite : {e}")
