import streamlit as st
from ultralytics import FastSAM
from PIL import Image
import tempfile
import os

# Load model once and cache it so Streamlit doesn't reload every time
@st.cache_resource
def load_model():
    return FastSAM("FastSAM-s.pt")  # Change to FastSAM-x.pt for bigger model

model = load_model()

st.set_page_config(page_title="FastSAM App", layout="wide")
st.title("FastSAM Interactive Segmentation")

# Sidebar mode selection
app_mode = st.sidebar.selectbox(
    "Select Segmentation Mode",
    ["Text Prompt", "Point Prompt", "Bounding Box Prompt", "Everything"]
)

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Only show inputs for the selected mode
if app_mode == "Text Prompt":
    text_prompt = st.sidebar.text_input("Enter text prompt", "a dog")

elif app_mode == "Point Prompt":
    point_x = st.sidebar.number_input("Point X coordinate", min_value=0, value=200)
    point_y = st.sidebar.number_input("Point Y coordinate", min_value=0, value=200)
    point_label = st.sidebar.number_input("Label (1=Foreground)", min_value=0, max_value=1, value=1)

elif app_mode == "Bounding Box Prompt":
    bbox_x1 = st.sidebar.number_input("X1", min_value=0, value=50)
    bbox_y1 = st.sidebar.number_input("Y1", min_value=0, value=50)
    bbox_x2 = st.sidebar.number_input("X2", min_value=0, value=200)
    bbox_y2 = st.sidebar.number_input("Y2", min_value=0, value=200)

if uploaded_image:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Run Segmentation"):
        with st.spinner("Running FastSAM..."):
            # Save image temporarily
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
            image.save(temp_file.name)

            # Run segmentation based on mode
            if app_mode == "Text Prompt":
                results = model(temp_file.name, texts=text_prompt, retina_masks=True)

            elif app_mode == "Point Prompt":
                results = model(
                    temp_file.name,
                    points=[[point_x, point_y]],
                    labels=[point_label],
                    retina_masks=True
                )

            elif app_mode == "Bounding Box Prompt":
                results = model(
                    temp_file.name,
                    bboxes=[[bbox_x1, bbox_y1, bbox_x2, bbox_y2]],
                    retina_masks=True
                )

            else:  # Everything
                results = model(temp_file.name, retina_masks=True)

            # Save and display results
            output_path = os.path.join(tempfile.gettempdir(), "segmented.png")
            results[0].save(output_path)
            st.image(Image.open(output_path), caption="Segmentation Result", use_column_width=True)

            # Cleanup temp file
            os.unlink(temp_file.name)
