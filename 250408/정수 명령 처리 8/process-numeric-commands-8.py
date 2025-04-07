N = int(input())
command = []
A = []

# Read all commands
for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)


###########################################
# Doubly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List (used as a Deque)
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_node = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        # If list is non-empty
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            # List is empty
            self.head = new_node
            self.tail = new_node
        self.num_node += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        # If list is non-empty
        if self.tail is not None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            # List is empty
            self.head = new_node
            self.tail = new_node
        self.num_node += 1

    def pop_front(self):
        if self.head is None:
            # Empty list
            return None
        # If only one node
        if self.head == self.tail:
            tmp = self.head
            self.head = None
            self.tail = None
            self.num_node = 0
            return tmp.data
        else:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            self.num_node -= 1
            return tmp.data

    def pop_back(self):
        if self.tail is None:
            # Empty list
            return None
        # If only one node
        if self.head == self.tail:
            tmp = self.tail
            self.head = None
            self.tail = None
            self.num_node = 0
            return tmp.data
        else:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.num_node -= 1
            return tmp.data

    def size(self):
        return self.num_node

    def empty(self):
        return 1 if self.num_node == 0 else 0

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def back(self):
        if self.tail is None:
            return None
        return self.tail.data

###########################################
# Process commands and print results
dll = DLL()

for val, cmd in zip(A, command):
    if cmd == "push_front":
        dll.push_front(val)
    elif cmd == "push_back":
        dll.push_back(val)
    elif cmd == "pop_front":
        result = dll.pop_front()
        # Print -1 if empty, else the popped value
        print(result if result is not None else -1)
    elif cmd == "pop_back":
        result = dll.pop_back()
        print(result if result is not None else -1)
    elif cmd == "size":
        print(dll.size())
    elif cmd == "empty":
        print(dll.empty())
    elif cmd == "front":
        result = dll.front()
        print(result if result is not None else -1)
    elif cmd == "back":
        result = dll.back()
        print(result if result is not None else -1)
