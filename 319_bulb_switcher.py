# 319. Bulb Switcher
# There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

import math

def bulb_switch(n):
    return int(math.sqrt(n))

if __name__ == "__main__":
    print(bulb_switch(3))
