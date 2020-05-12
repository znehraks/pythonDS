'''
학번:60152572
이름:유정민
'''


class minheap:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)
        self.__up_heap(len(self.array)-1)

    def pop(self):
        result = self.array[0]
        value = self.array.pop()
        if len(self.array) > 0:
            self.array[0] = value
            self.__down_heap(0)
        return result

    def is_empty(self):
        return not self.array

    def __parent_idx(self, idx):
        return int((idx+1)/2 - 1)

    def __left_idx(self, idx):
        return 2*idx + 1

    def __right_idx(self, idx):
        return 2*idx + 2

    def __up_heap(self, current):
        parent = self.__parent_idx(current)
        while current > 0 and self.array[current] < self.array[parent]:
            self.array[parent], self.array[current] = self.array[current], self.array[parent]
            current = parent
            parent = self.__parent_idx(current)

    def __down_heap(self, current):
        left, right = self.__left_idx(current), self.__right_idx(current)
        while left < len(self.array):
            if right >= len(self.array) or self.array[right] > self.array[left]:
                child = left
            elif self.array[left] > self.array[right]:
                child = right

            if self.array[current] > self.array[child]:
                self.array[current], self.array[child] = self.array[child], self.array[current]
                current = child
                left, child = self.__left_idx(
                    current), self.__right_idx(current)
            else:
                return

    def print(self):
        print(self.array)


heap = minheap()

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

# print(heap.pop())
# heap.print()
# print(heap.pop())
# heap.print()

while not heap.is_empty():
    print(heap.pop())
