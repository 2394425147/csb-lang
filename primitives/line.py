from core import timing
from core.storyboard import storyboard_definition
from primitives.base import PrimitiveBase


class Line(PrimitiveBase):
    def __init__(self):
        super().__init__()
    pass


def create() -> Line:
    line = Line()
    storyboard_definition.lines.append(line)
    line.time = timing.now
    return line
