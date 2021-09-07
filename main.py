import timeit


def main():
    num = 2**10

    t = timeit.Timer
    kwargs = dict(
        function = t(lambda: divide(num)),
        method = t(lambda: Method(num).divide()),
        class_method = t(lambda: ClassMethod().divide(num)),
        static_method = t(lambda: StaticMethod().divide(num)),
        property_method = t(lambda: PropertyMethod(num).divide),
    )

    for k, v in kwargs.items():
        print(f"{k} took: {v.timeit(10**7):.3f}")


def divide(num: int) -> float:
    """Divide a number by 2

    Args:
        num (int): Number

    Returns:
        float: Half of it
    """
    return num / 2


class Method:
    def __init__(self, num: int) -> None:
        self.num = num

    def divide(self) -> float:
        """Divide a number by 2

        Args:
            num (int): Number

        Returns:
            float: Half of it
        """
        return self.num / 2

class ClassMethod:

    @classmethod
    def divide(cls, num: int) -> float:
        """Divide a number by 2

        Args:
            num (int): Number

        Returns:
            float: Half of it
        """
        return num / 2

class StaticMethod:
    @staticmethod
    def divide(num: int) -> float:
        """Divide a number by 2

        Args:
            num (int): Number

        Returns:
            float: Half of it
        """
        return num / 2

class PropertyMethod:
    def __init__(self, num: int) -> None:
        self.num = num

    @property
    def divide(self) -> float:
        """Divide a number by 2

        Args:
            num (int): Number

        Returns:
            float: Half of it
        """
        return self.num / 2

if __name__ == "__main__":
    main()
