import streamlit as st
from rembg import remove
from PIL import Image
import io

# Titre de l'application
st.title("Suppression d'arrière-plan d'une image")

# Description de l'application
st.markdown("""
    Téléchargez une image pour supprimer son arrière-plan. Cette application utilise la bibliothèque `rembg` pour effectuer cette tâche.
""")

# Fonction pour supprimer l'arrière-plan d'une image
def remove_background(input_image):
    # Vérifier si l'image est correctement lue
    try:
        image = Image.open(io.BytesIO(input_image))
        image.verify()  # Vérifie si l'image est valide
        output_image = remove(input_image)  # Supprimer l'arrière-plan
        return output_image
    except Exception as e:
        st.error(f"Erreur lors de la lecture de l'image: {e}")
        return None

# Téléchargement de l'image par l'utilisateur
uploaded_file = st.file_uploader("Choisir une image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Affichage de l'image téléchargée
    input_image = uploaded_file.read()

    # Suppression de l'arrière-plan
    output_bytes = remove_background(input_image)
    
    if output_bytes is not None:
        # Convertir les bytes de l'image résultante en image PIL
        output_image = Image.open(io.BytesIO(output_bytes))
        st.image(output_image, caption="Image sans arrière-plan", use_column_width=True)

        # Option pour télécharger l'image sans arrière-plan
        st.download_button(
            label="Télécharger l'image sans arrière-plan",
            data=output_bytes,
            file_name="image_sans_arriere_plan.png",
            mime="image/png"
        )
