def binary_search_recursive(data, target, low, high):
    if high - low <= 1:
        return low if data[low] == target else None
    mid = (low + high) // 2
    if target < data[mid]:
        return binary_search_recursive(data, target, low, mid)
    else:
        return binary_search_recursive(data, target, mid, high)

    print(binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8 ], 2,0,8))

    # Binary
    # search
    # has
    # excellent
    # performance
    # when
    # it
    # comes
    # to
    # time
    # complexity - 
    # 𝑂(log
    # 𝑛)
    # O(logn).This
    # logarithmic
    # time
    # behavior
    # makes
    # binary
    # search
    # ideal
    # for large datasets.This is because, with each comparison, binary search eliminates half of the elements, reducing the search time exponentially.
    # Regarding
    # space
    # complexity, the
    # iterative
    # version
    # of
    # binary
    # search
    # has
    # a
    # space
    # complexity
    # of 𝑂(1)
    # O(1)  as it
    # only
    # uses
    # a
    # fixed
    # amount
    # of
    # space
    # to
    # store
    # the
    # data.However, the
    # recursive
    # version
    # has
    # higher
    # space
    # complexity — 𝑂(log
    # 𝑛)
    # O(logn) — since
    # it
    # uses
    # additional
    # space in the
    # form
    # of
    # a
    # call
    # stack
    # during
    # recursive
    # tasks.