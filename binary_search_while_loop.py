# TODO: Given a sorted list of grades in a class, implement Binary Search on this list
grades = [35, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# TODO: Implement the Loop-based Binary Search function without recursion
def binary_search_iterative(data, target):
    # We will search in the interval [low, high), where the right border is excluded
    low = 0
    high = len(data)

    while high - low > 1: # search until the length  of the interval > 1
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid # Continue our search in [low, mid)
        else:
            low = mid # Continue our search in [mid, high)
    return low if data[low] == target else None

# TODO: Set a query for a student's grade for your search
search_query = 70
# TODO: Invoke the Binary Search function. If you find the grade, print the position in the grade list; if not, print a not found message.
position = binary_search_iterative(grades,search_query)
if position is not None:
    print(f"Position found for {search_query} is {position}")
else:
    print(f"Searched value {search_query} not found")