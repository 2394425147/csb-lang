from core.storyboard import storyboard_definition
from primitives.base import PrimitiveBase, State


class Template(PrimitiveBase):
    def __init__(self):
        super().__init__()

    def state(self, properties: dict, time: float | None = None, add_time: float | None = None):
        new_state = State()

        if time is not None:
            new_state.time = time
        elif add_time is not None:
            new_state.add_time = add_time
        else:
            new_state.relative_time = 0

        # pass all the properties to the new state
        for key, value in properties.items():
            new_state.__dict__[key] = value

        self.states.append(new_state)


def create(name: str) -> Template:
    template = Template()
    template.id = name
    storyboard_definition.templates[name] = template
    return template
