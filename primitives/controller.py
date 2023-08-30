from core import timing
from primitives.base import PrimitiveBase
from core.storyboard import storyboard_definition


class SceneController(PrimitiveBase):
    def __init__(self):
        super().__init__()

    pass


def create() -> SceneController:
    scene_controller = SceneController()
    storyboard_definition.controllers.append(scene_controller)
    scene_controller.time = timing.current_time
    return scene_controller
