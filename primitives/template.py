from core import timing
from core.storyboard import storyboard_definitio
from primitives.base import PrimitiveBase


class Template(PrimitiveBase):
    def __init__(self):
        super().__init__()

    pass


def create() -> Template:
    template = Template()
    storyboard_definition.templates.append(template)
    template.time = timing.current_time
    return template
