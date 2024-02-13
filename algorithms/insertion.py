from typing import TypeVar, Callable

T = TypeVar("T")


def insertion_sort(lst: list[T], comp: Callable[[T, T], bool] = lambda lhs, rhs: lhs < rhs):
    """
    Sort a list in-place using the insertion sort algorithm

    :param lst: the list to sort
    :param comp: binary predicate comparator. Returns `True` if the first argument is ordered before the second
    """
    return NotImplemented
