class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        
    # add value to end of array
    
    def addBack(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = Node(value)
        return self
    
    # traverse through array
    
    def displayValues(self): 
        if self.head == None:
            print("No values")
        else:
            runner = self.head
            while runner != None:
                print(runner.value)
                runner = runner.next
        return self
    
    # find highest value of array
    
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

x = SLL() # declare linked list class
x.head = Node(4) # declare head of Node class

#examples

x.addBack(3).addBack(5)
x.displayValues()
x.maxValue()
