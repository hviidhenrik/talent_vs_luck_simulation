import numpy as np

from src.core import Environment, Agent, Event
from src.helpers import print_agent_stats
import matplotlib.pyplot as plt

env = Environment(size=(30, 30))

# configure the environment for the agents and events to be the one we just created
Agent.set_environment(env)
Event.set_environment(env)

# put agents and events on the environment
Agent.put_agents_randomly(100)
Event.put_events_randomly(50, event_type="lucky")
Event.put_events_randomly(50, event_type="unlucky")

# [event.random_move() for event in Event.event_list]

# # start the simulation by letting the lucky and unlucky events move around the environment
for years in range(1, 81):
    env.iterations_elapsed += 1
    [event.random_move() for event in Event.event_list]

capital = [agent.capital for agent in Agent.agent_list]

# plt.hist(capital, bins=30)
# plt.show()

idx_high = np.argmax(capital)
idx_low = np.argmin(capital)

print(f"============\nRichest agent stats: ")
print_agent_stats(Agent.agent_list[idx_high])

print(f"============\nPoorest agent stats: ")
print_agent_stats(Agent.agent_list[idx_low])
