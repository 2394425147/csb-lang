from core import timing


class PrimitiveBase(object):
    def __init__(self):
        self.time = 0
        self.states: list[State] = []

    pass

    def state(self, properties: dict, time: float | None = None, add_time: float | None = None):
        new_state = State()

        if time is not None:
            new_state.time = time
        elif add_time is not None:
            new_state.add_time = add_time
        else:
            new_state.time = timing.now

        # pass all the properties to the new state
        for key, value in properties.items():
            new_state.__dict__[key] = value

        self.states.append(new_state)


class State(object):
    pass
