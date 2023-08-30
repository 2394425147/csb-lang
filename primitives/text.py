from core import timing
from core.storyboard import storyboard_definition
from primitives.base import PrimitiveBase


class Text(PrimitiveBase):
    def __init__(self, text: str):
        super().__init__()
        self.text = text
    pass


def create(text: str) -> Text:
    text = Text(text)
    storyboard_definition.texts.append(text)
    text.time = timing.current_time
    return text
