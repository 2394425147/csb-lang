from core import timing
from core.storyboard import storyboard_definition
from primitives.base import PrimitiveBase


class SceneController(PrimitiveBase):
    def __init__(self):
        super().__init__()

    pass


def create() -> SceneController:
    scene_controller = SceneController()
    storyboard_definition.controllers.append(scene_controller)
    scene_controller.time = timing.current_time
    return scene_controller
