from core import timing


class PrimitiveBase(object):
    def __init__(self):
        self.time = 0

        # store the variable name of this instance
        self.id = str(id(self))
        self.states: list[State] = []
        self.internal_children: list[PrimitiveBase] = []

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

    def add_child(self, child: 'PrimitiveBase'):
        self.internal_children.append(child)
        child.parent_id = self.id


    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('internal_')}


class State(object):
    pass
