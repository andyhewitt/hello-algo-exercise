"""deque"""


class ListNode:
    """Doubly linked list node class"""

    def __init__(self, val: int):
        self.val: int = val                # 节点值
        self.next: ListNode | None = None  # 指向后继节点的引用
        self.prev: ListNode | None = None  # 指向前驱节点的引用


class LinkedListDeque:
    """基于双向链表实现的双向队列"""

    def __init__(self):
        """构造方法"""
        self._front: ListNode | None = None  # 头节点 front
        self._rear: ListNode | None = None  # 尾节点 rear
        self._size: int = 0  # 双向队列的长度

    def size(self) -> int:
        """获取双向队列的长度"""
        return self._size

    def is_empty(self) -> bool:
        """判断双向队列是否为空"""
        return self._size == 0

    def push(self, num: int, is_front: bool):
        """入队操作"""
        node = ListNode(num)

        if self.is_empty():
            self._front = node
            self._rear = node
            self._size += 1
        elif is_front:
            # update in the front
            self._front.prev = node
            node.next = self._front
            self._front = node  # update front node.
        else:
            # update the current end next, the end.next now should be the node
            # end should be the node itself
            self._rear.next = node
            node.prev = self._rear
            self._rear = node
        self._size += 1

    def push_first(self, num: int):
        """队首入队"""
        self.push(num, True)

    def push_last(self, num: int):
        """队尾入队"""
        self.push(num, False)

    def pop(self, is_front: bool) -> int:
        """出队操作"""
        if self.is_empty():
            raise IndexError("Empty deque")
        if self._size == 1:
            value = self._front.val
            self._front = self._rear = None
        elif is_front:
            # node at the front, next.prev is None,
            value = self._front.val
            self._front = self._front.next
            self._front.prev = None
        else:
            value = self._rear.val
            self._rear = self._rear.prev
            self._rear.next = None
        self._size -= 1
        return value

    def pop_first(self) -> int:
        """队首出队"""
        return self.pop(True)

    def pop_last(self) -> int:
        """队尾出队"""
        return self.pop(False)

    def peek_first(self) -> int:
        """访问队首元素"""
        return self._front.val

    def peek_last(self) -> int:
        """访问队尾元素"""
        return self._rear.val


# 初始化双向队列
deq = LinkedListDeque()

# 元素入队
deq.push_last(2)      # 添加至队尾
deq.push_last(5)
deq.push_last(4)
deq.push_first(3)  # 添加至队首
deq.push_first(1)

# 13254

print(deq)

# 访问元素
front: int = deq.peek_first()  # 队首元素
rear: int = deq.peek_last()  # 队尾元素

print(front, rear)
# 元素出队
pop_front: int = deq.pop_first()  # 队首元素出队
pop_rear: int = deq.pop_last()       # 队尾元素出队

print(pop_front, pop_rear)
# 获取双向队列的长度
size: int = deq.size()
print(size)
# 判断双向队列是否为空
is_empty: bool = deq.is_empty()
print(is_empty)
