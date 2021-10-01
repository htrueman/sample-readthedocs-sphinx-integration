def sample_func3(p1: str, p2: int, *args, **kwargs):
    """
    Sample description.

    :param p1:
    :param p2:
    :param args:
    :param kwargs:
    :return:
    """

    return p1, p2


def sample_func4():
    """Return sample"""

    return "sample"


class SampleClassNew:
    a = 'a'
    b = 'b'

    def sample_method1(self):
        return self.b

    def sample_method2(self) -> tuple:
        """
        Print self.a.
        :return: tuple
        """

        print(self.a)
        return sample_func3('1', 2)
