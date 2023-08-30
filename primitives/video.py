from core import timing
from core.storyboard import storyboard_definition
from primitives.base import PrimitiveBase


class Video(PrimitiveBase):
    def __init__(self):
        super().__init__()

    pass


def create() -> Video:
    video = Video()
    storyboard_definition.videos.append(video)
    video.time = timing.current_time
    return video
