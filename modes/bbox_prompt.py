import streamlit as st
from .base import SegmentationMode

class BoundingBoxPromptMode(SegmentationMode):
    def get_sidebar_inputs(self):
        x1 = st.sidebar.number_input("X1", min_value=0, value=50)
        y1 = st.sidebar.number_input("Y1", min_value=0, value=50)
        x2 = st.sidebar.number_input("X2", min_value=0, value=200)
        y2 = st.sidebar.number_input("Y2", min_value=0, value=200)
        return {"bboxes": [[x1, y1, x2, y2]]}

    def run_segmentation(self, image_path, params):
        return self.model(image_path, bboxes=params["bboxes"], retina_masks=True)
