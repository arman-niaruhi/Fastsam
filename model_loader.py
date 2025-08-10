import streamlit as st
from ultralytics import FastSAM

@st.cache_resource
def load_model():
    return FastSAM("FastSAM-s.pt")
