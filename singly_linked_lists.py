class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    def addBack(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = Node(value)
        return self
    def displayValues(self):
        if self.head == None:
            print("No values")
        else:
            runner = self.head
            while runner != None:
                print(runner.value)
                runner = runner.next
        return self
    def maxValue(self):
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

x.addBack(3).addBack(5)

x.displayValues()

x.maxValue()