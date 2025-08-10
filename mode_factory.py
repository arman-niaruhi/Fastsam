from modes.text_prompt import TextPromptMode
from modes.point_prompt import PointPromptMode
from modes.bbox_prompt import BoundingBoxPromptMode
from modes.everything import EverythingMode

class ModeFactory:
    modes = {
        "Text Prompt": TextPromptMode,
        "Point Prompt": PointPromptMode,
        "Bounding Box Prompt": BoundingBoxPromptMode,
        "Everything": EverythingMode,
    }

    @classmethod
    def get_mode(cls, mode_name, model):
        mode_class = cls.modes.get(mode_name)
        if not mode_class:
            raise ValueError(f"Mode '{mode_name}' not found")
        return mode_class(model)
