from core import chart, timing, storyboard
from primitives import text

import math
import random

with open("chart.json", "r", encoding="utf-8") as f:
    # Required to process
    chart.parse(f)

timing.set_tempo(197)

title = "vivid/stasis is my favourite gay game"

for i in range(len(title)):
    timing.seek(start=0)
    txt = text.create(title[i])
    txt.opacity = 0
    startTime = timing.current_time
    for j in range(60 * 2):
        txt.state(properties={"x": -300 + i * 15, "y": math.sin(i / 2 + timing.current_time - startTime) * 30, "opacity": 1})
        timing.current_time += 1 / 2
    timing.beat(count=2)
    txt.state(properties={"x": -300 + i * 15, "y": math.sin(i / 2) * 30, "opacity": 0})



storyboard.export("D:/Tools/CytoidPlayer/player/storyboard.json")
