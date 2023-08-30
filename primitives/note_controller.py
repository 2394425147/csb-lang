from core import timing
from core.storyboard import storyboard_definition
from primitives.base import PrimitiveBase


class NoteController(PrimitiveBase):
    def __init__(self):
        super().__init__()

    pass


def create() -> NoteController:
    note_controller = NoteController()
    storyboard_definition.note_controllers.append(note_controller)
    note_controller.time = timing.now
    return note_controller
