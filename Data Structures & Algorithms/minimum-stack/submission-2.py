class MinStack:

    def __init__(self):
        self.mainStack = []
        self.trackMin = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if not self.trackMin or val <= self.trackMin[-1] :
            self.trackMin.append(val)

    def pop(self) -> None:
        if self.trackMin and self.mainStack:
            if self.trackMin[-1] == self.mainStack[-1]:
                self.trackMin.pop()
        if self.mainStack:
            self.mainStack.pop()

    def top(self) -> int:
        if not self.mainStack:
            return None
        return self.mainStack[-1]

    def getMin(self) -> int:
        if not self.trackMin:
            return None
        return self.trackMin[-1]
        
