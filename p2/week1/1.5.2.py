class Buffer:
    def __init__(self):
        self.sequence = []
    
    def add(self, *a):
        self.sequence += a
        while len(self.sequence) >= 5:
            print(sum(self.sequence[:5]))
            del self.sequence[:5]
    
    def get_current_part(self):
        return self.sequence