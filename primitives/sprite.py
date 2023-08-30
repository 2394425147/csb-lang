from core import timing
from core.storyboard import storyboard_definition
from primitives.base import PrimitiveBase


class Sprite(PrimitiveBase):
    def __init__(self, path: str):
        super().__init__()
        self.path = path
    pass


def create(path: str) -> Sprite:
    sprite = Sprite(path)
    storyboard_definition.sprites.append(sprite)
    sprite.time = timing.current_time
    return sprite
