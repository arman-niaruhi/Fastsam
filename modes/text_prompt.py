import streamlit as st
from .base import SegmentationMode

class TextPromptMode(SegmentationMode):
    def get_sidebar_inputs(self):
        prompt = st.sidebar.text_input("Enter text prompt", "a dog")
        return {"texts": prompt}

    def run_segmentation(self, image_path, params):
        return self.model(image_path, texts=params["texts"], retina_masks=True)
