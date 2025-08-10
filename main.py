import streamlit as st
from PIL import Image
import tempfile
import os

from model_loader import load_model
from mode_factory import ModeFactory

def main():
    st.set_page_config(page_title="FastSAM Modular App", layout="wide")
    st.title("FastSAM Interactive Segmentation - Modular Version")

    model = load_model()

    mode_name = st.sidebar.selectbox(
        "Select Segmentation Mode",
        list(ModeFactory.modes.keys())
    )
    mode = ModeFactory.get_mode(mode_name, model)

    params = mode.get_sidebar_inputs()

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        image = Image.open(uploaded_image).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Run Segmentation"):
            with st.spinner("Running FastSAM..."):
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
                image.save(temp_file.name)

                results = mode.run_segmentation(temp_file.name, params)

                output_path = os.path.join(tempfile.gettempdir(), "segmented.png")
                results[0].save(output_path)

                st.image(Image.open(output_path), caption="Segmentation Result", use_column_width=True)

                os.unlink(temp_file.name)

if __name__ == "__main__":
    main()
