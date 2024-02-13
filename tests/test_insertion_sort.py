from algorithms import insertion_sort


def test_trivially_sortable() -> None:
    """
    Test insertion sort on lists that are already sorted

    :return: None
    """
    # Empty lists are already sorted
    lst = []
    expected = []
    insertion_sort(lst)
    assert lst == expected

    # Single element lists are also already sorted
    lst = [1]
    expected = [1]
    insertion_sort(lst)
    assert lst == expected


def test_custom_comparators() -> None:
    """
    Test insertion sort using custom comparators

    :return: None
    """
    # By default, the list is sorted in ascending order
    lst = [3, 5, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    insertion_sort(lst)
    assert lst == expected

    # Sort in descending order
    lst = [1, 9, 0, 5, 7, 3, 2, 8, 4, 6]
    expected = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    insertion_sort(lst, lambda lhs, rhs: lhs > rhs)
    assert lst == expected

    # Sort integers lexicographically
    lst = [1, 7, 12, 69, 100, 150, 420]
    expected = [1, 100, 12, 150, 420, 69, 7]
    insertion_sort(lst, lambda lhs, rhs: str(lhs) < str(rhs))
    assert lst == expected
