import streamlit as st
from .base import SegmentationMode

class PointPromptMode(SegmentationMode):
    def get_sidebar_inputs(self):
        x = st.sidebar.number_input("Point X coordinate", min_value=0, value=200)
        y = st.sidebar.number_input("Point Y coordinate", min_value=0, value=200)
        label = st.sidebar.number_input("Label (1=Foreground)", min_value=0, max_value=1, value=1)
        return {"points": [[x, y]], "labels": [label]}

    def run_segmentation(self, image_path, params):
        return self.model(image_path, points=params["points"], labels=params["labels"], retina_masks=True)
