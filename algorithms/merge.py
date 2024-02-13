from typing import TypeVar, Callable

T = TypeVar("T")


def _merge(lst1: list[T], lst2: list[T], dest: list[T], comp: Callable[[T, T], bool]):
    """
    Merge two sorted lists into a larger sorted list

    :param lst1: the first sorted list
    :param lst2: the second sorted list
    :param dest: the list to merge into. Assumed to be large enough to hold elements of both lst1 and lst2
    :param comp: binary predicate comparator. Returns `True` if the first argument is ordered before the second
    """
    return NotImplemented


def merge_sort(lst: list[T], comp: Callable[[T, T], bool] = lambda lhs, rhs: lhs < rhs):
    """
    Sort a list using the merge sort algorithm

    :param lst: the list to sort
    :param comp: binary predicate comparator. Returns `True` if the first argument is ordered before the second
    """
    return NotImplemented
