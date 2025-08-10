import streamlit as st
from streamlit_drawable_canvas import st_canvas
from .base import SegmentationMode

class BoundingBoxPromptMode(SegmentationMode):
    def get_sidebar_inputs(self):
        st.sidebar.write("Draw bounding boxes on the image canvas (drag to create boxes).")

        # Will get boxes from main.py via canvas interaction, so return empty here

        return {}

    def run_segmentation(self, image_path, params):
        bboxes = params.get("bboxes", [])

        if not bboxes:
            st.warning("No bounding boxes provided for segmentation.")
            return None

        return self.model(image_path, bboxes=bboxes, retina_masks=False)
