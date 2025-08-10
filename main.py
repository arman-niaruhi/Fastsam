import streamlit as st
from PIL import Image
import tempfile
import os
from streamlit_drawable_canvas import st_canvas

from model_loader import load_model
from mode_factory import ModeFactory

def extract_points_and_labels(drawn_objects):
    # drawn_objects is a list of dicts from canvas.json_data['objects']
    points = []
    labels = []

    for obj in drawn_objects:
        if obj["type"] == "circle":
            # Assuming circles represent points
            # Extract center x,y
            x = obj["left"] + obj["radius"]
            y = obj["top"] + obj["radius"]
            points.append([int(x), int(y)])
            labels.append(1)  # label 1 = foreground for points
    return points, labels

def extract_bboxes(drawn_objects):
    bboxes = []
    for obj in drawn_objects:
        if obj["type"] == "rect":
            x1 = int(obj["left"])
            y1 = int(obj["top"])
            x2 = int(obj["left"] + obj["width"])
            y2 = int(obj["top"] + obj["height"])
            bboxes.append([x1, y1, x2, y2])
    return bboxes

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

        canvas_result = None
        if mode_name in ["Point Prompt", "Bounding Box Prompt"]:
            stroke_width = 5 if mode_name == "Point Prompt" else 2
            drawing_mode = "freedraw" if mode_name == "Point Prompt" else "rect"

            canvas_result = st_canvas(
                fill_color="",
                stroke_width=stroke_width,
                stroke_color="#FF0000",
                background_image=image,
                update_streamlit=True,
                height=image.height,
                width=image.width,
                drawing_mode=drawing_mode,
                key="canvas",
            )

            if canvas_result.json_data is not None:
                objects = canvas_result.json_data["objects"]

                if mode_name == "Point Prompt":
                    points, labels = extract_points_and_labels(objects)
                    params["points"] = points
                    params["labels"] = labels

                elif mode_name == "Bounding Box Prompt":
                    bboxes = extract_bboxes(objects)
                    params["bboxes"] = bboxes

        if st.button("Run Segmentation"):
            with st.spinner("Running FastSAM..."):
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
                image.save(temp_file.name)

                results = mode.run_segmentation(temp_file.name, params)

                if results:
                    output_path = os.path.join(tempfile.gettempdir(), "segmented.png")
                    results[0].save(output_path)

                    st.image(Image.open(output_path), caption="Segmentation Result", use_column_width=True)

                os.unlink(temp_file.name)

if __name__ == "__main__":
    main()
#streamlit run main.py
