"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # count = 0

    # def __init__(self, start):
    #     self.start = start
    #     SerialGenerator.count += 1
        
    # def generate(self):
    #     return self.start + SerialGenerator.count
    
    # def reset(self):
    #     SerialGenerator.count = 0

    def __init__(self, start=0):
        """Initiate class, with zero as the default start value
        Create new attribute to track the next value"""
        self.start = start
        self.new_num = start
    def __repr__(self):
        return f"<Serial Generator: start={self.start}, next={self.new_num + 1}>"

    def generate(self):
        """Generates a new SerialGenerator instatnce and increments the new number"""
        self.new_num += 1
        return self.new_num
    
    def reset(self):
        """Resets generate method to have the original start value"""
        self.new_num = self.start - 1
        
       



         


