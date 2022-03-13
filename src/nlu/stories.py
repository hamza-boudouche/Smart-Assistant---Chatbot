from ast import List, Str
from enum import Enum
from xmlrpc.client import Boolean

# intent enum


class Intent(Enum):
    CREATE_TASK = "create task"
    GET_TASKS = "get tasks"

# state class


class State:
    def __init__(self, name: Str) -> None:
        self._name = name

    def run(self, info={}):
        pass

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, State):
            return False
        return self._name == __o._name

    def __hash__(self) -> int:
        return hash((self._name,))

    @property
    def name(self):
        return self._name

# link class


class Link:
    def __init__(self, origin: State, destination: State, intent: Intent) -> None:
        self.origin = origin
        self.destination = destination
        self.intent = intent

# stories class


class Stories:
    def __init__(self, states, links, start: State, end: State):
        self.states = states
        self.links = links  # dict with states as keys (states are immutable)
        self.current = start
        self.end = end

    def move(self, nlu_model, input) -> bool:
        parsed = nlu_model.parse(input)
        intent = Intent(parsed.get("intent"))
        info = parsed.get("slots")
        links = self.links.get(self.current)
        found = False
        for link in links:
            if link.intent == intent:
                self.current = link.destination
                found = True
        if not found:
            return False
        self.current.run(info)
        return self.current != self.end
