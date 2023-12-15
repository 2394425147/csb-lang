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
        self.templates: dict[str, PrimitiveBase] = {}

    pass

    def to_dict(self):
        return {
            "texts": [text.to_dict() for text in self.texts],
            "sprites": [sprite.to_dict() for sprite in self.sprites],
            "lines": [line.to_dict() for line in self.lines],
            "videos": [video.to_dict() for video in self.videos],
            "controllers": [controller.to_dict() for controller in self.controllers],
            "note_controllers": [note_controller.to_dict() for note_controller in self.note_controllers],
            "templates": {k: v.to_dict() for k, v in self.templates.items()},
        }

    def to_json(self):
        return json.dumps(self.to_dict(), default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


storyboard_definition = StoryboardDefinition()


def export(path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(storyboard_definition.to_json())
    pass
