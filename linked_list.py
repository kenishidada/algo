from typing import Any

class Node():
    def __init__(self, data: Any, next_node=None):
        self.data = data
        self.next_node = None