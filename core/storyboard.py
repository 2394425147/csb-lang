import json

from primitives.controller import SceneController
from primitives.line import Line
from primitives.note_controller import NoteController
from primitives.sprite import Sprite
from primitives.template import Template
from primitives.text import Text
from primitives.video import Video


class StoryboardDefinition(object):
    def __init__(self):
        self.texts: list[Text] = []
        self.sprites: list[Sprite] = []
        self.lines: list[Line] = []
        self.videos: list[Video] = []
        self.controllers: list[SceneController] = []
        self.note_controllers: list[NoteController] = []
        self.templates: list[Template] = []

    pass

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


storyboard_definition = StoryboardDefinition()


def export(path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(storyboard_definition.to_json())
    pass
