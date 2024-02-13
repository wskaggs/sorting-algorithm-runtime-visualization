from typing import TypeVar, Callable

T = TypeVar("T")


def _merge(lst1: list[T], lst2: list[T], dest: list[T], comp: Callable[[T, T], bool]) -> None:
    """
    Merge two sorted lists into a larger sorted list

    :param lst1: the first sorted list
    :param lst2: the second sorted list
    :param dest: the list to merge into. Assumed to be large enough to hold elements of both lst1 and lst2
    :param comp: binary predicate comparator. Returns `True` if the first argument is ordered before the second
    :return: None
    """
    total = len(lst1) + len(lst2)
    itr1 = itr2 = 0

    while itr1 + itr2 < total:
        if itr2 == len(lst2) or itr1 < len(lst1) and comp(lst1[itr1], lst2[itr2]):
            dest[itr1 + itr2] = lst1[itr1]
            itr1 += 1
        else:
            dest[itr1 + itr2] = lst2[itr2]
            itr2 += 1


def merge_sort(lst: list[T], comp: Callable[[T, T], bool] = lambda lhs, rhs: lhs < rhs) -> None:
    """
    Sort a list using the merge sort algorithm

    :param lst: the list to sort
    :param comp: binary predicate comparator. Returns `True` if the first argument is ordered before the second
    :return: None
    """
    # An empty or single-element list is already sorted
    if len(lst) <= 1:
        return

    # Otherwise, recursively split and merge sorted sub-arrays
    middle = len(lst) // 2
    half1 = lst[:middle]
    half2 = lst[middle:]

    merge_sort(half1, comp)
    merge_sort(half2, comp)
    _merge(half1, half2, lst, comp)
