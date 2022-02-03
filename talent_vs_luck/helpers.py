import numpy as np


def add_tuples(tuple1, tuple2):
    return tuple(np.add(tuple1, tuple2))


def draw_normal_sample_in_unit_interval(loc: float = 0.6, scale: float = 0.1):
    return np.round(float(max(min(np.random.normal(loc, scale, size=1), 1), 0)), 3)


def print_agent_stats(agent):
    print(agent)
    print(f"Lucky events encountered: ", agent.lucky_events_encountered)
    print(f"Lucky events exploited: ", agent.lucky_events_exploited)
    print(f"Unlucky events encountered: ", agent.unlucky_events_encountered)
