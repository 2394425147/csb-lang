import json
from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_int(x: Any) -> int:
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    if x is None:
        return 0
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


@dataclass
class EventList:
    type: int
    args: str

    @staticmethod
    def from_dict(obj: Any) -> 'EventList':
        assert isinstance(obj, dict)
        type = from_int(obj.get("type"))
        args = from_str(obj.get("args"))
        return EventList(type, args)

    def to_dict(self) -> dict:
        result: dict = {"type": from_int(self.type), "args": from_str(self.args)}
        return result


@dataclass
class EventOrderList:
    tick: int
    event_list: List[EventList]

    @staticmethod
    def from_dict(obj: Any) -> 'EventOrderList':
        assert isinstance(obj, dict)
        tick = from_int(obj.get("tick"))
        event_list = from_list(EventList.from_dict, obj.get("event_list"))
        return EventOrderList(tick, event_list)

    def to_dict(self) -> dict:
        result: dict = {"tick": from_int(self.tick),
                        "event_list": from_list(lambda x: to_class(EventList, x), self.event_list)}
        return result


@dataclass
class NoteList:
    page_index: int
    type: int
    id: int
    tick: int
    x: float
    has_sibling: bool
    hold_tick: int
    next_id: int
    is_forward: bool
    approach_rate: int

    @staticmethod
    def from_dict(obj: Any) -> 'NoteList':
        assert isinstance(obj, dict)
        page_index = from_int(obj.get("page_index"))
        type = from_int(obj.get("type"))
        id = from_int(obj.get("id"))
        tick = from_int(obj.get("tick"))
        x = from_float(obj.get("x"))
        has_sibling = from_bool(obj.get("has_sibling"))
        hold_tick = from_int(obj.get("hold_tick"))
        next_id = from_int(obj.get("next_id"))
        is_forward = from_bool(obj.get("is_forward"))
        approach_rate = from_int(obj.get("approach_rate"))
        return NoteList(page_index, type, id, tick, x, has_sibling, hold_tick, next_id, is_forward, approach_rate)

    def to_dict(self) -> dict:
        result: dict = {"page_index": from_int(self.page_index), "type": from_int(self.type), "id": from_int(self.id),
                        "tick": from_int(self.tick), "x": to_float(self.x), "has_sibling": from_bool(self.has_sibling),
                        "hold_tick": from_int(self.hold_tick), "next_id": from_int(self.next_id),
                        "is_forward": from_bool(self.is_forward), "approach_rate": from_int(self.approach_rate)}
        return result


@dataclass
class PageList:
    start_tick: int
    end_tick: int
    scan_line_direction: int

    @staticmethod
    def from_dict(obj: Any) -> 'PageList':
        assert isinstance(obj, dict)
        start_tick = from_int(obj.get("start_tick"))
        end_tick = from_int(obj.get("end_tick"))
        scan_line_direction = from_int(obj.get("scan_line_direction"))
        return PageList(start_tick, end_tick, scan_line_direction)

    def to_dict(self) -> dict:
        result: dict = {"start_tick": from_int(self.start_tick), "end_tick": from_int(self.end_tick),
                        "scan_line_direction": from_int(self.scan_line_direction)}
        return result


@dataclass
class TempoList:
    tick: int
    value: int

    @staticmethod
    def from_dict(obj: Any) -> 'TempoList':
        assert isinstance(obj, dict)
        tick = from_int(obj.get("tick"))
        value = from_int(obj.get("value"))
        return TempoList(tick, value)

    def to_dict(self) -> dict:
        result: dict = {"tick": from_int(self.tick), "value": from_int(self.value)}
        return result


@dataclass
class ChartDefinition:
    format_version: int
    time_base: int
    start_offset_time: int
    music_offset: float
    page_list: List[PageList]
    tempo_list: List[TempoList]
    event_order_list: List[EventOrderList]
    note_list: List[NoteList]

    @staticmethod
    def from_dict(obj: Any) -> 'ChartDefinition':
        assert isinstance(obj, dict)
        format_version = from_int(obj.get("format_version"))
        time_base = from_int(obj.get("time_base"))
        start_offset_time = from_int(obj.get("start_offset_time"))
        music_offset = from_float(obj.get("music_offset"))
        page_list = from_list(PageList.from_dict, obj.get("page_list"))
        tempo_list = from_list(TempoList.from_dict, obj.get("tempo_list"))
        event_order_list = from_list(EventOrderList.from_dict, obj.get("event_order_list"))
        note_list = from_list(NoteList.from_dict, obj.get("note_list"))
        return ChartDefinition(format_version, time_base, start_offset_time, music_offset, page_list, tempo_list,
                               event_order_list, note_list)

    def to_dict(self) -> dict:
        result: dict = {"format_version": from_int(self.format_version), "time_base": from_int(self.time_base),
                        "start_offset_time": from_int(self.start_offset_time),
                        "music_offset": to_float(self.music_offset),
                        "page_list": from_list(lambda x: to_class(PageList, x), self.page_list),
                        "tempo_list": from_list(lambda x: to_class(TempoList, x), self.tempo_list),
                        "event_order_list": from_list(lambda x: to_class(EventOrderList, x), self.event_order_list),
                        "note_list": from_list(lambda x: to_class(NoteList, x), self.note_list)}
        return result


def chart_definition_from_dict(s: Any) -> ChartDefinition:
    return ChartDefinition.from_dict(s)


def chart_definition_to_dict(x: ChartDefinition) -> Any:
    return to_class(ChartDefinition, x)


chart_definition: ChartDefinition | None = None


# https://github.com/Cytoid/Cytoid/blob/main/Assets/Scripts/Game/Chart/Chart.cs#L237
def tick_to_time(tick: int) -> float:
    """
    Convert a tick value to a corresponding time value.

    :param tick: The tick value to convert.
    :returns: The corresponding time value.
    """
    global chart_definition
    if chart_definition is None:
        return 0

    result: float = 0

    current_tick: int = 0
    current_time_zone = -1

    for i in range(len(chart_definition.tempo_list)):
        if chart_definition.tempo_list[i].tick >= tick:
            break

        result += (chart_definition.tempo_list[i].tick - current_tick) * 2e-6 * chart_definition.tempo_list[i - 1].value / chart_definition.time_base

        current_tick = chart_definition.tempo_list[i].tick
        current_time_zone += 1

    result += (tick - current_tick) * 2e-6 * chart_definition.tempo_list[current_time_zone].value / chart_definition.time_base / 2
    return result


def time_to_tick(time: float) -> int:
    """
    Calculate the tick value corresponding to a given time.

    :param time: The time value in seconds.
    :returns: The tick value corresponding to the given time.
    """
    global chart_definition
    current_time = 0.0
    current_tick = 0.0
    i = 1
    for i in range(1, len(chart_definition.tempo_list)):
        delta = (chart_definition.tempo_list[i].tick - chart_definition.tempo_list[i - 1].tick) / chart_definition.time_base * chart_definition.tempo_list[i - 1].value * 1e-6
        if current_time + delta < time:
            current_time += delta
            current_tick = chart_definition.tempo_list[i].tick
        else:
            break

    return (current_tick + (time - current_time) * 2 / chart_definition.tempo_list[i - 1].value * 1e6 * chart_definition.time_base).__round__()


def tick_to_tempo(tick: int) -> float:
    """
    Convert a tick value to a tempo.

    :param tick: The tick value to be converted.
    :returns: The corresponding tempo value.
    """
    global chart_definition
    return 1 / (tick / chart_definition.time_base * 2e-6)


def note_pos(note_id: int) -> (float, float):
    """
    Retrieves the normalized position of a note.

    :param note_id: The ID of the note.
    :returns: X and Y coordinates of the note, ranging from 0 to 1.
    """
    global chart_definition
    note = chart_definition.note_list[note_id]
    page = chart_definition.page_list[note.page_index]
    raw_y = (note.tick - page.start_tick) / (page.end_tick - page.start_tick)
    actual_y = raw_y if page.scan_line_direction > 0 else 1 - raw_y
    return note.x, actual_y


def parse(file):
    """
    Parses a Cytoid chart file.

    :param file:
    :return:
    """
    from core.timing import set_tempo
    global chart_definition
    chart_definition = chart_definition_from_dict(json.load(file))
    set_tempo(tick_to_tempo(chart_definition.tempo_list[0].value))
    pass
