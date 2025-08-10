from abc import ABC, abstractmethod
import streamlit as st

class SegmentationMode(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def get_sidebar_inputs(self):
        """Display UI inputs and return parameters."""
        pass

    @abstractmethod
    def run_segmentation(self, image_path, params):
        """Run FastSAM and return results."""
        pass
