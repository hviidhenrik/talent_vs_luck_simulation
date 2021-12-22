import numpy as np

from src.core import Environment, Agent, Field, Event
from src.helpers import *

env = Environment(size=(5,5))

# configure the environment for the agents and events to be the one we just created
Agent.set_environment(env)
Event.set_environment(env)

# put some agents on the board
agent1 = Agent((0,0))
agent2 = Agent((1,1))
agent3 = Agent((2,2))

# ... and some events
event1 = Event((0,1), "lucky")

for i in range(300):
    event1.random_move()


print([x.capital for x in [agent1, agent2, agent3]])
agent3.lucky_events_encountered
agent3.lucky_events_exploited
