class Point():
    # define parameter type: https://docs.python.org/3/library/typing.html [15.06.23]
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({int(self.x)}, {int(self.y)})"
