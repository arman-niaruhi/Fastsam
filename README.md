# FastSAM Streamlit Application

An interactive **Streamlit** application for image segmentation using [FastSAM](https://github.com/ultralytics/ultralytics).  
This app allows you to choose between different segmentation modes:
- **Text Prompt** – segment objects by describing them in words.
- **Point Prompt** – segment objects by specifying a point coordinate.
- **Bounding Box Prompt** – segment objects by specifying a rectangular region.
- **Everything** – segment all objects in the image.

## Features
- Upload an image in JPG or PNG format.
- Select segmentation mode from the sidebar.
- Provide prompt text, point coordinates, or bounding box coordinates.
- Run FastSAM and view segmented output directly in the browser.
- All logic is contained in a single Python file (`main.py`).

## Requirements
- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Ultralytics](https://github.com/ultralytics/ultralytics)
- [Pillow](https://python-pillow.org/)

## Installation

1. **Clone or download this repository** and open a terminal in the project folder.

2. **Create a virtual environment**:
    ```bash
    python3 -m venv fastsam-env
    source fastsam-env/bin/activate  # Windows: fastsam-env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install streamlit ultralytics pillow
    ```

4. **(Optional)** Download the FastSAM model in advance, or it will be automatically downloaded on the first run.

## Usage
Run the app with:
```bash
streamlit run main.py
