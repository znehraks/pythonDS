class MaxHeap:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)
        self.__up_heap(len(self.array) - 1)

    def pop(self):
        result = self.array[0]
        value = self.array.pop()
        if len(self.array) > 0:  # 마지막 수 value에
            self.array[0] = value  # value를 루트에
            self.__down_heap(0)
        return result

    def is_empty(self):
        return len(self.array) == 0

    def __parent_idx(self, idx):
        # 1,2 --> 0
        # 3,4 --> 1
        # 5,6 --> 2
        # 7,8 --> 3
        return int((idx+1)/2 - 1)

    def __left_idx(self, idx):
        # 0 --> 1
        # 1 --> 3
        # 2 --> 5
        return 2*idx + 1

    def __right_idx(self, idx):
        # 0 --> 2
        # 1 --> 4
        # 2 --> 6
        return 2*idx + 2

    def __up_heap(self, current):
        parent = self.__parent_idx(current)
        while current > 0 and self.array[current] > self.array[parent]:
            self.array[current], self.array[parent] = self.array[parent], self.array[current]
            current = parent
            parent = self.__parent_idx(current)

    def __down_heap(self, current):
        left, right = self.__left_idx(current), self.__right_idx(current)
        while left < len(self.array):
            if right >= len(self.array) or self.array[left] > self.array[right]:
                child = left
            else:
                child = right

            if self.array[current] < self.array[child]:
                self.array[current], self.array[child] = self.array[child], self.array[current]
                current = child
                left, right = self.__left_idx(
                    current), self.__right_idx(current)
            else:
                return

    def print(self):
        print(self.array)


heap = MaxHeap()

heap.push(5)
heap.print()
heap.push(10)
heap.print()
heap.push(3)
heap.print()
heap.push(8)
heap.print()
heap.push(13)
heap.print()
heap.push(27)
heap.print()
heap.push(4)
heap.print()

# print(heap.pop())  # 27
# heap.print()
# print(heap.pop())  # 13
# heap.print()

while not heap.is_empty():
    print(heap.pop())
