import streamlit as st
from .base import SegmentationMode

class EverythingMode(SegmentationMode):
    def get_sidebar_inputs(self):
        conf = st.sidebar.slider("Confidence threshold", 0.0, 1.0, 0.3, 0.01)
        st.sidebar.write("No additional input needed for this mode.")
        return {"conf": conf}

    def run_segmentation(self, image_path, params):
        return self.model(image_path, conf=params["conf"], retina_masks=False)
