from core import chart, timing, storyboard
from primitives import text

import math
import random

with open("chart.json", "r", encoding="utf-8") as f:
    # Required to process chart info (e.g. time seeking to note start/end)
    chart.parse(f)

# Sets the tempo to use for timing.beat
timing.set_tempo(197)

# Example: Sine wave text

title = "Hello, procedural storyboard!"

for i in range(len(title)):
    # Sets the time to the start of the first note
    timing.seek(start=0)

    # Creates a text element with the [i]th character in the title
    txt = text.create(title[i])

    # Sets the initial opacity of the text
    txt.opacity = 0

    # Animates the text
    startTime = timing.now

    # Animations are interpolated
    for j in range(120):
        txt.state(properties={"x": -300 + i * 15, "y": math.sin(i / 2 + timing.now - startTime) * 30, "opacity": 1})
        timing.now += 1 / 2

    # Fade out the text over the next 2 seconds
    timing.beat(count=2)
    txt.state(properties={"x": -300 + i * 15, "y": math.sin(i / 2) * 30, "opacity": 0})

# Finally, export the storyboard
storyboard.export("./storyboard.json")
