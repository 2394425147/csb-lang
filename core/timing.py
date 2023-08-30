from core import chart
from core.chart import tick_to_time, time_to_tick, tick_to_tempo


def set_tempo(value: float):
    global current_tempo
    current_tempo = value
    pass


def beat(subdivision: int = 1, count: int = 1, progress: bool = True) -> float:
    """
    Gets the time in seconds of a beat with the current tempo
    :param subdivision: How many subdivisions per beat
    :param count: How many beats to include
    :param progress: Whether to increment the current time
    :return: Time in seconds
    """
    global current_tempo
    global now

    beat_duration = 60 / current_tempo / subdivision * count

    if progress:
        now += beat_duration

    return beat_duration


def seek(tick: int | None = None,
         time: float | None = None,
         start: int | None = None,
         end: int | None = None,
         progress: bool = True,
         override_tempo: bool = True) -> float:
    """
    Gets the time given the song position
    :param tick: Value of time defined in chart
    :param time: Value of literal time
    :param start: Gets the time from the start of the given note ID
    :param end: Gets the time from the end of the given note ID (Used for hold notes)
    :param progress: Whether to increment the current time
    :param override_tempo: Set the tempo to the value defined in the chart
    :return: Time in seconds
    """
    global now
    global current_tempo

    accumulated_time = 0
    accumulated_tick = 0

    if tick is not None:
        accumulated_tick += tick
        accumulated_time += tick_to_time(tick)

    if time is not None:
        accumulated_tick += time_to_tick(time)
        accumulated_time += time

    if start is not None:
        start_tick = chart.chart_definition.note_list[start].tick
        accumulated_tick += start_tick
        accumulated_time += tick_to_time(start_tick)
    elif end is not None:
        end_tick = (chart.chart_definition.note_list[end].tick +
                    chart.chart_definition.note_list[end].hold_tick)
        accumulated_tick += end_tick
        accumulated_time += tick_to_time(end_tick)

    if override_tempo:
        for i in range(len(chart.chart_definition.tempo_list)):
            if chart.chart_definition.tempo_list[i].tick >= accumulated_tick:
                current_tempo = tick_to_tempo(chart.chart_definition.tempo_list[i].value)
                break

    if progress:
        now = accumulated_time

    return accumulated_time


current_tempo: float = 0
now: float = 0
