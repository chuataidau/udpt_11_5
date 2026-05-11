import hashlib

M = 4
MAX_NODES = 2 ** M


def hash_key(key):
    return int(hashlib.sha1(str(key).encode()).hexdigest(), 16) % MAX_NODES


class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.finger_table = []

    def __str__(self):
        return f"Node({self.id})"


class Chord:
    def __init__(self):
        self.nodes = []

    def add_node(self, node_id):
        node = Node(node_id)
        self.nodes.append(node)
        self.nodes.sort(key=lambda x: x.id)

    def find_successor(self, key):
        for node in self.nodes:
            if key <= node.id:
                return node
        return self.nodes[0]

    def build_finger_tables(self):
        for node in self.nodes:
            node.finger_table = []

            for i in range(M):
                start = (node.id + 2 ** i) % MAX_NODES
                successor = self.find_successor(start)

                node.finger_table.append(
                    (start, successor.id)
                )

    def display(self):
        print("=== CHORD RING ===")

        for node in self.nodes:
            print(f"\nNode {node.id}")

            for index, entry in enumerate(node.finger_table):
                print(
                    f"Finger {index}: start={entry[0]} -> node {entry[1]}"
                )

chord = Chord()

nodes = [1, 4, 8, 12]

for n in nodes:
    chord.add_node(n)

chord.build_finger_tables()

chord.display()

print("\n=== LOOKUP TEST ===")

keys = [2, 5, 10, 14]

for key in keys:
    successor = chord.find_successor(key)

    print(
        f"Key {key} stored at Node {successor.id}"
    )