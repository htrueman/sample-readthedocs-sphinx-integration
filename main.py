def sample_func1(p1: str, p2: int, *args, **kwargs):
    """
    Sample description.

    :param p1:
    :param p2:
    :param args:
    :param kwargs:
    :return:
    """

    return p1, p2


def sample_func2():
    """Return sample"""

    return "sample"


class SampleClass:
    a = 'a'
    b = 'b'

    def sample_method1(self):
        return self.a

    def sample_method2(self) -> str:
        """
        Print self.b.
        :return: str
        """

        print(self.b)
        return sample_func2()
