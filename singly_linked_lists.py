class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    # add node to front of array

    def add_to_front(self, key):
        new_node = Node(key) # initialize new node from Node class
        current_head = self.head # create new variable to store current head (temp)
        new_node.next = current_head # direct the new nodes 'next' pointer to existing head (stored in new variable)
        self.head = new_node # reassign new node as head
        return self

    # add value to end of array

    def add_to_back(self, key):
        if self.head == None: # check if head is None
            self.head = Node(key)
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = Node(key)
        return self

    # traverse through array

    def display_values(self):
        if self.head == None:
            print("No values")
        else:
            runner = self.head
            while runner != None:
                print(runner.value)
                runner = runner.next
        return self

    # find sum of all node values

    def max_value(self):
        sum = 0
        if self.head == None:
            print("No values")
        else:
            runner = self.head
            while runner != None:
                sum = sum + runner.value
                runner = runner.next
            print(sum)
            return self

x = SLL()
x.head = Node(4)

x.add_to_front(3).add_to_back(5)

x.display_values()

x.max_value()