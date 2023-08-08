from core import timing
from core.storyboard import storyboard_definition
from primitives.base import PrimitiveBase


class TextPrimitive(PrimitiveBase):
    def __init__(self, text: str):
        super().__init__()
        self.text = text
    pass


def create(text: str) -> TextPrimitive:
    text = TextPrimitive(text)
    storyboard_definition.texts.append(text)
    text.time = timing.current_time
    return text
