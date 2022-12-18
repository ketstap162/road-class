class Road:
    def __init__(self, length: int):
        if not isinstance(length, int):
            raise TypeError("Road length must be an integer")

        if length <= 0:
            raise ValueError("The road cannot have a length below 0")

        self.length = length

    @staticmethod
    def __can_compare(instance):
        if not isinstance(instance, Road):
            raise TypeError("The road can only be compared with the road")

    def __len__(self):
        return self.length

    def __add__(self, other):
        if not isinstance(other, Road):
            raise TypeError("A road can only be stacked with another road")

        self.length += other.length

        return self

    def __eq__(self, other):
        self.__can_compare(other)
        return self.length == other.length

    def __lt__(self, other):
        self.__can_compare(other)
        return self.length < other.length

    def __le__(self, other):
        self.__can_compare(other)
        return self.length <= other.length

    def __gt__(self, other):
        self.__can_compare(other)
        return self.length > other.length

    def __ge__(self, other):
        self.__can_compare(other)
        return self.length >= other.length

    def __ne__(self, other):
        self.__can_compare(other)
        return self.length != other.length
