import streamlit as st
from .base import SegmentationMode

class EverythingMode(SegmentationMode):
    def get_sidebar_inputs(self):
        st.sidebar.write("No additional input needed for this mode.")
        return {}

    def run_segmentation(self, image_path, params):
        return self.model(image_path, retina_masks=True)
