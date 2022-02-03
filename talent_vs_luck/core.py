import random
from typing import Dict, List, Tuple, Union

from talent_vs_luck.helpers import *


class Environment:
    def __init__(self, size: Tuple[int, int]):
        self.size = size
        self.empty_fields = []
        self.fields = self._make_fields()
        self.iterations_elapsed = 0

    def _make_fields(self):
        field_list = []
        for i in range(self.size[0]):
            col_list = []
            for j in range(self.size[1]):
                self.empty_fields.append((i, j))
                col_list.append(Field((i, j)))
            field_list.append(col_list)
        return np.array(field_list)


class Agent:
    environment = None
    n_agents = 0
    agent_list = []

    @classmethod
    def set_environment(cls, environment: Environment):
        cls.environment = environment

    @classmethod
    def put_agents_randomly(cls, n_agents: int = 1, **kwargs):
        empty_fields = Agent.environment.empty_fields
        assert len(empty_fields) >= n_agents, "Number of agents to put must be lower than or equal to empty fields"
        coords_list = random.sample(empty_fields, k=n_agents)
        for coords in coords_list:
            Agent(coords, **kwargs)

    def __init__(self, coords: Tuple[int, int], talent: float = None, capital: int = 10):
        self.coords = coords
        self.talent = draw_normal_sample_in_unit_interval() if talent is None else talent
        self.capital = capital
        self.lucky_events_encountered = {"count": 0, "when": []}
        self.lucky_events_exploited = {"count": 0, "when": []}
        self.unlucky_events_encountered = {"count": 0, "when": []}
        self.id = Agent.n_agents
        Agent.environment.empty_fields.remove(self.coords)
        Agent.n_agents += 1
        Agent.environment.fields[coords].occupants.append(self)
        Agent.agent_list.append(self)

    def __repr__(self):
        return f"Agent{self.id} at {self.coords}"

    def __str__(self):
        return f"Agent{self.id} at {self.coords}, capital: {self.capital}, talent: {self.talent}"


class Event:
    environment = None
    event_list = []

    @classmethod
    def set_environment(cls, environment: Environment):
        cls.environment = environment

    @classmethod
    def put_events_randomly(cls, n_events: int = 1, event_type: str = "lucky"):
        empty_fields = Agent.environment.empty_fields
        assert len(empty_fields) >= n_events, "Number of events to put must be lower than or equal to empty fields"
        coords_list = random.sample(empty_fields, k=n_events)
        for coords in coords_list:
            Event(coords, event_type)

    def __init__(self, coords: Tuple[int, int], event_type: str = "lucky"):
        self.coords = coords
        self.type = event_type
        Event.environment.fields[coords].occupants.append(self)
        Event.environment.empty_fields.remove(self.coords)
        Event.event_list.append(self)

    def __str__(self):
        return f"{self.type.title()} event at: {self.coords}"

    def __repr__(self):
        return f"{self.type.title()} event at: {self.coords}"

    @staticmethod
    def _can_move_to_field(coords: Tuple[int, int]):
        inside_bounds = 0 <= coords[0] < Event.environment.size[0] and 0 <= coords[1] < Event.environment.size[1]
        if not inside_bounds:
            return False
        field = Event.environment.fields[coords]
        no_other_event_in_field = 1 - any(isinstance(x, Event) for x in field.occupants)
        can_move = inside_bounds and no_other_event_in_field
        return can_move

    def random_move(self):
        add_to_coords = (np.random.randint(-1, 2), np.random.randint(-1, 2))
        try_coords = add_tuples(self.coords, add_to_coords)
        if self._can_move_to_field(try_coords):
            Event.environment.fields[self.coords].occupants.remove(self)  # clear the old field
            new_field_occupant_list = Event.environment.fields[try_coords].occupants
            new_field_occupant_list.append(self)
            self.coords = try_coords
            if isinstance(new_field_occupant_list[0], Agent):
                agent = new_field_occupant_list[0]
                self.apply_event_to_agent(agent)

    def apply_event_to_agent(self, agent: Agent):
        if self.type == "lucky":
            agent_exploits_opportunity = float(np.random.random(1)) < agent.talent
            agent.capital = 2 * agent.capital if agent_exploits_opportunity else agent.capital
            # agent.lucky_events_encountered["count"] += 1
            # agent.lucky_events_encountered["when"].append(Event.environment.iterations_elapsed)
            self._add_event_to_agent_event_dicts(agent.lucky_events_encountered)
            if agent_exploits_opportunity:
                self._add_event_to_agent_event_dicts(agent.lucky_events_exploited)
                # agent.lucky_events_exploited["count"] += 1
                # agent.lucky_events_exploited["when"].append(Event.environment.iterations_elapsed)
        else:
            agent.capital = agent.capital / 2
            self._add_event_to_agent_event_dicts(agent.unlucky_events_encountered)
            # agent.unlucky_events_encountered["count"] += 1
            # agent.unlucky_events_encountered["when"].append(Event.environment.iterations_elapsed)

    @staticmethod
    def _add_event_to_agent_event_dicts(agent_dict: Dict):
        agent_dict["count"] += 1
        agent_dict["when"].append(Event.environment.iterations_elapsed)


class Field:
    def __init__(self, coords: Tuple[int, int] = None, occupants: List[Union[Agent, Event, None]] = None):
        self.occupants = occupants if isinstance(occupants, list) else []
        self.coords = coords

    def __repr__(self):
        return f"Field coords: {self.coords}, occupied by: {self.occupants}"
