from core import timing


class PrimitiveBase(object):
    def __init__(self):
        self.time = 0
        self.states: list[State] = []

    pass

    def state(self, properties: dict, time: float | None = None):
        new_state = State(time if time is not None else timing.now)

        # pass all the properties to the new state
        for key, value in properties.items():
            new_state.__dict__[key] = value

        self.states.append(new_state)


class State(object):
    def __init__(self, time: float):
        self.time: float = time

    pass
