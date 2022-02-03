import argparse

import matplotlib.pyplot as plt
import numpy as np

from talent_vs_luck.core import Agent, Environment, Event
from talent_vs_luck.helpers import print_agent_stats

plt.style.use("seaborn")


def get_args():
    parser = argparse.ArgumentParser(description="Run agent based simulation of talent vs luck")
    parser.add_argument("--board-size", default=30, type=int)
    parser.add_argument("--num-agents", default=100, type=int)
    parser.add_argument("--num-lucky-events", default=50, type=int)
    parser.add_argument("--num-unlucky-events", default=50, type=int)
    parser.add_argument("--num-years", default=40, type=int)
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    env = Environment(size=(args.board_size, args.board_size))

    # configure the environment for the agents and events to be the one we just created
    Agent.set_environment(env)
    Event.set_environment(env)

    # put agents and events on the environment
    Agent.put_agents_randomly(args.num_agents)
    Event.put_events_randomly(args.num_lucky_events, event_type="lucky")
    Event.put_events_randomly(args.num_unlucky_events, event_type="unlucky")

    # [event.random_move() for event in Event.event_list]

    # start the simulation by letting the lucky and unlucky events move around the environment
    for half_years in range(1, 2*args.num_years):
        env.iterations_elapsed += 1
        [event.random_move() for event in Event.event_list]

    capital = [agent.capital for agent in Agent.agent_list]

    plt.hist(capital, bins=30)
    plt.title(f"Final wealth distribution \n({args.num_years} years elapsed)")
    plt.xlabel("Wealth / success")
    plt.ylabel("Frequency")
    plt.show()

    idx_high = np.argmax(capital)
    idx_low = np.argmin(capital)

    print(f"\n============\nRichest agent stats: ")
    print_agent_stats(Agent.agent_list[idx_high])

    print(f"\n============\nPoorest agent stats: ")
    print_agent_stats(Agent.agent_list[idx_low])


if __name__ == "__main__":
    main()
