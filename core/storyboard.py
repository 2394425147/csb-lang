import json

from primitives.base import PrimitiveBase


class StoryboardDefinition(object):
    def __init__(self):
        self.texts: list[PrimitiveBase] = []
        self.sprites: list[PrimitiveBase] = []
        self.lines: list[PrimitiveBase] = []
        self.videos: list[PrimitiveBase] = []
        self.controllers: list[PrimitiveBase] = []
        self.note_controllers: list[PrimitiveBase] = []
        self.templates: dict[PrimitiveBase] = {}

    pass

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


storyboard_definition = StoryboardDefinition()


def export(path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(storyboard_definition.to_json())
    pass
