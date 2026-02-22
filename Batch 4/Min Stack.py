class MinStack:
    """
    LeetCode #155 - Min Stack (Medium)

    Approach:
        Store each element as a (value, current_minimum) tuple. The second
        field captures the minimum of all values at or below this entry at
        the time of the push, so getMin() can return it in O(1) without any
        auxiliary stack or scan. When a new value is pushed, the new minimum
        is min(value, top_min_so_far).

    Time Complexity:  O(1) for all operations — push, pop, top, getMin.
    Space Complexity: O(n) — one tuple stored per pushed element.
    """

    def __init__(self) -> None:
        self._stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        current_min = val if not self._stack else min(val, self._stack[-1][1])
        self._stack.append((val, current_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


if __name__ == "__main__":
    # Test 1: Standard LeetCode example
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2

    # Test 2: Minimum updates correctly after popping the current min
    ms2 = MinStack()
    ms2.push(5)
    ms2.push(3)
    ms2.push(7)
    assert ms2.getMin() == 3
    ms2.pop()          # remove 7
    assert ms2.getMin() == 3
    ms2.pop()          # remove 3 — min reverts to 5
    assert ms2.getMin() == 5

    # Test 3: Single element
    ms3 = MinStack()
    ms3.push(42)
    assert ms3.top() == 42
    assert ms3.getMin() == 42

    print("All test cases passed.")
