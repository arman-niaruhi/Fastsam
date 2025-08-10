import streamlit as st
from streamlit_drawable_canvas import st_canvas
from .base import SegmentationMode

class PointPromptMode(SegmentationMode):
    def get_sidebar_inputs(self):
        st.sidebar.write("Draw points on the image canvas (click to add points).")

        # We'll get points from main.py by passing the image and canvas data later
        # So just return empty here; main will call a function to handle drawing

        return {}

    def run_segmentation(self, image_path, params):
        points = params.get("points", [])
        labels = params.get("labels", [])

        if not points:
            st.warning("No points provided for segmentation.")
            return None

        return self.model(image_path, points=points, labels=labels, retina_masks=False)
