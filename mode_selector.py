import os
import random
import pandas as pd
import time
wos.makedirs("data", exist_ok=True)
def select_mode(state):
    return {
        "AGGRESSIVE_FLOOD": "DISASTER_MODE",
        "FISH_STRESS": "FISHERIES_MODE",
        "POLLUTED": "AGRICULTURE_MODE",
        "NORMAL": "NORMAL_MODE"
    }.get(state, "NORMAL_MODE")
