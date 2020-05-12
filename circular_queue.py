"""
아래에 학번과 이름을 꼭 적으세요.

학번:60152572
이름:유정민
"""
class CircularQueue:  
    def __init__(self, max_size):
        self.max_size = max_size + 1
        self.queue = [None] * self.max_size
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if self.is_full():
            return None
        self.queue[self.front] = data
        self.front += 1
        self.front %= self.max_size
        return True

        # 원형 큐에 data를 추가
        # 이미 큐가 full인 경우 data추가하지 않고 None을 반환
        # 성공적으로 enqueue한 경우 True반환
        # 아래에 코드를 완성하시오.
        

    def dequeue(self):
        if self.is_empty():
            return None
        d = self.queue[self.rear]
        self.queue[self.rear] = None
        self.rear += 1
        self.rear %= self.max_size
        return d

        # 큐가 비어 있는 경우 None을 반환
        # 그렇지 않은 경우 data를 반환
        # 아래에 코드를 완성하시오.
        

    def is_full(self):
        if self.rear - self.front == 1 or self.front - self.rear == self.max_size - 1:
            return True
        return False
        # 큐가 꽉 찼으면 True, 아니면 False
        # 아래에 코드를 완성하시오.

    def is_empty(self):
        return self.front == self.rear
        # 큐가 비었으면 True, 아니면 False
        # 아래에 코드를 완성하시오.

    def size(self):
        if self.front < self.rear:
            return self.front+self.max_size - self.rear
        return self.front - self.rear
        # 현재 큐에 몇 개의 item이 있는지 개수를 반환
        # 아래에 코드를 완성하시오.


if __name__ == "__main__":
    q = CircularQueue(3)
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Enque 10", q.enqueue(10))
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())
    print("Enque 20", q.enqueue(20))
    print("Enque 30", q.enqueue(30))
    print("Enque 40", q.enqueue(40))
    print("Deque", q.dequeue())
    print("Enque 50", q.enqueue(50))
    print("Deque", q.dequeue())
    print("Deque", q.dequeue())
    print("Enque 60", q.enqueue(60))
    print("Enque 70", q.enqueue(70))

    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print(len(q.queue)) # should be 4. list 자체의 크기는 변하지 않아야 함!!!

# 아래는 위 코드 테스트를 위해서 만들어놓은 샘플입니다. 수정하지 마세요.
# 다음과 같은 결과가 나와야 합니다.
"""
Empty? True , Full? False , Size= 0
Enque 10 True
Empty? False , Full? False , Size= 1
Enque 20 True
Enque 30 True
Enque 40 None
Deque 10
Enque 50 True
Deque 20
Deque 30
Enque 60 True
Enque 70 True
Empty? False , Full? True , Size= 3
Deque 50
Empty? False , Full? False , Size= 2
Deque 60
Empty? False , Full? False , Size= 1
Deque 70
Empty? True , Full? False , Size= 0
Deque None
Empty? True , Full? False , Size= 0
4
"""