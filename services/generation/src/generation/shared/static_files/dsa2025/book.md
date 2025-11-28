# Cấu trúc dữ liệu và giải thuật

## Stack & Queue

### 1. Stack (Ngăn xếp)

#### 1.1. Khái niệm cơ bản

Stack là một cấu trúc dữ liệu tuyến tính hoạt động theo nguyên tắc **LIFO (Last In First Out)** - "vào sau ra trước". Điều này có nghĩa là phần tử được thêm vào cuối cùng sẽ là phần tử được lấy ra đầu tiên.

**Ví dụ thực tế:**
- Chồng sách: Cuốn sách đặt lên trên cùng sẽ là cuốn được lấy ra đầu tiên
- Lịch sử trình duyệt: Nút "Back" đưa bạn về trang trước đó theo thứ tự ngược lại
- Undo/Redo trong text editor

#### 1.2. Các thao tác cơ bản

**a) Push (Đẩy):** Thêm một phần tử vào đỉnh stack
- Độ phức tạp: O(1)
- Thao tác: Tăng con trở top lên 1 và thêm phần tử

**b) Pop (Lấy ra):** Xóa và trả về phần tử ở đỉnh stack
- Độ phức tạp: O(1)
- Thao tác: Lấy phần tử tại top và giảm top xuống 1

**c) Peek/Top:** Xem phần tử ở đỉnh stack mà không xóa
- Độ phức tạp: O(1)

**d) isEmpty:** Kiểm tra stack có rỗng không
- Độ phức tạp: O(1)

**e) Size:** Trả về số lượng phần tử trong stack
- Độ phức tạp: O(1)

#### 1.3. Cài đặt Stack

**Cách 1: Sử dụng mảng (Array)**

```python
class Stack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.stack = []
        self.top = -1
    
    def push(self, item):
        if self.top >= self.capacity - 1:
            raise Exception("Stack Overflow")
        self.stack.append(item)
        self.top += 1
        return True
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        item = self.stack[self.top]
        self.stack.pop()
        self.top -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]
    
    def is_empty(self):
        return self.top == -1
    
    def size(self):
        return self.top + 1
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements:", end=" ")
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()
```

**Cách 2: Sử dụng Linked List**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
        self.size_count = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size_count += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        item = self.head.data
        self.head = self.head.next
        self.size_count -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self.size_count
```

#### 1.4. Ứng dụng của Stack

**a) Kiểm tra dấu ngoặc hợp lệ:**

```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Test
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("([)]"))    # False
```

**b) Chuyển đổi biểu thức Infix sang Postfix:**

```python
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():  # Toán hạng
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Loại bỏ '('
        else:  # Toán tử
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# Test
print(infix_to_postfix("A+B*C"))  # ABC*+
```

**c) Tính giá trị biểu thức Postfix:**

```python
def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)
    
    return stack.pop()

# Test
print(evaluate_postfix("23*5+"))  # 11
```

**d) Thuật toán quay lui (Backtracking):**
Stack được sử dụng trong các thuật toán quay lui như giải mê cung, N-Queens, sudoku solver.

**e) Đánh giá biểu thức số học và biên dịch:**
Compiler sử dụng stack để parse và đánh giá các biểu thức.

---

### 2. Queue (Hàng đợi)

#### 2.1. Khái niệm cơ bản

Queue là một cấu trúc dữ liệu tuyến tính hoạt động theo nguyên tắc **FIFO (First In First Out)** - "vào trước ra trước". Phần tử được thêm vào đầu tiên sẽ là phần tử được lấy ra đầu tiên.

**Ví dụ thực tế:**
- Hàng người xếp hàng mua vé: Người đến trước được phục vụ trước
- Hàng đợi in ấn: Tài liệu gửi in trước sẽ được in trước
- Hàng đợi xử lý trong hệ thống: CPU scheduling, disk scheduling

#### 2.2. Các thao tác cơ bản

**a) Enqueue (Thêm vào):** Thêm phần tử vào cuối queue
- Độ phức tạp: O(1)

**b) Dequeue (Lấy ra):** Xóa và trả về phần tử ở đầu queue
- Độ phức tạp: O(1)

**c) Front/Peek:** Xem phần tử ở đầu queue mà không xóa
- Độ phức tạp: O(1)

**d) Rear:** Xem phần tử ở cuối queue
- Độ phức tạp: O(1)

**e) isEmpty:** Kiểm tra queue có rỗng không
- Độ phức tạp: O(1)

**f) Size:** Trả về số lượng phần tử trong queue
- Độ phức tạp: O(1)

#### 2.3. Cài đặt Queue

**Cách 1: Sử dụng mảng (Circular Queue)**

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size_count = 0
    
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        
        if self.front == -1:  # Queue rỗng
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.queue[self.front]
        
        if self.front == self.rear:  # Chỉ còn 1 phần tử
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.size_count -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def size(self):
        return self.size_count
```

**Cách 2: Sử dụng Linked List**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_count = 0
    
    def enqueue(self, item):
        new_node = Node(item)
        
        if self.rear is None:  # Queue rỗng
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.front.data
        self.front = self.front.next
        
        if self.front is None:  # Queue trở nên rỗng
            self.rear = None
        
        self.size_count -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self.size_count
```

#### 2.4. Các loại Queue đặc biệt

**a) Deque (Double-ended Queue):**
Cho phép thêm và xóa phần tử ở cả hai đầu.

```python
from collections import deque

dq = deque()
dq.append(1)      # Thêm vào phải
dq.appendleft(2)  # Thêm vào trái
dq.pop()          # Xóa từ phải
dq.popleft()      # Xóa từ trái
```

**b) Priority Queue (Hàng đợi ưu tiên):**
Mỗi phần tử có một độ ưu tiên, phần tử có độ ưu tiên cao nhất được xử lý trước.

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))
    
    def pop(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        return heapq.heappop(self.heap)[1]
    
    def is_empty(self):
        return len(self.heap) == 0
```

#### 2.5. Ứng dụng của Queue

**a) BFS (Breadth-First Search) trong đồ thị:**

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Test
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
```

**b) Quản lý tài nguyên chia sẻ:**
- CPU scheduling
- Disk scheduling
- Printer queue

**c) Xử lý bất đồng bộ:**
- Message queue trong các hệ thống phân tán
- Event handling trong GUI

**d) Cache implementation:**
- LRU (Least Recently Used) cache sử dụng kết hợp queue và hash map

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

#### 2.6. So sánh Stack và Queue

| Đặc điểm | Stack | Queue |
|----------|-------|-------|
| Nguyên tắc | LIFO | FIFO |
| Thao tác chính | Push, Pop | Enqueue, Dequeue |
| Truy cập | Chỉ ở đỉnh (top) | Ở đầu (front) và cuối (rear) |
| Ứng dụng | Backtracking, Expression evaluation | BFS, Scheduling |
| Cài đặt | Array, Linked List | Array (Circular), Linked List |

---

## Basic Sorting Algorithms

### 1. Giới thiệu về Sắp xếp

#### 1.1. Khái niệm

Sắp xếp (Sorting) là quá trình sắp đặt các phần tử trong một tập hợp theo một thứ tự nhất định (tăng dần hoặc giảm dần). Đây là một trong những thao tác cơ bản và quan trọng nhất trong khoa học máy tính.

**Tại sao sắp xếp quan trọng?**
- Giúp tìm kiếm nhanh hơn (Binary Search)
- Tối ưu hóa các thuật toán khác
- Cải thiện hiệu suất của database
- Trực quan hóa và phân tích dữ liệu

#### 1.2. Phân loại thuật toán sắp xếp

**a) Theo phương pháp:**
- **Comparison-based:** So sánh các phần tử (Bubble, Selection, Insertion, Merge, Quick)
- **Non-comparison-based:** Không so sánh trực tiếp (Counting, Radix, Bucket)

**b) Theo tính ổn định (Stability):**
- **Stable:** Giữ nguyên thứ tự tương đối của các phần tử bằng nhau
- **Unstable:** Không đảm bảo thứ tự tương đối

**c) Theo bộ nhớ:**
- **In-place:** Sử dụng O(1) bộ nhớ phụ
- **Out-of-place:** Cần thêm bộ nhớ phụ

#### 1.3. Các tiêu chí đánh giá

- **Time Complexity:** Độ phức tạp thời gian (Best, Average, Worst case)
- **Space Complexity:** Độ phức tạp không gian
- **Stability:** Tính ổn định
- **Adaptive:** Hiệu quả với dữ liệu đã gần sắp xếp
- **Online:** Có thể xử lý dữ liệu đến theo thời gian thực

---

### 2. Bubble Sort (Sắp xếp nổi bọt)

#### 2.1. Ý tưởng

Bubble Sort so sánh từng cặp phần tử liền kề và hoán đổi chúng nếu chúng sai thứ tự. Quá trình này lặp lại cho đến khi mảng được sắp xếp. Phần tử lớn nhất sẽ "nổi" lên vị trí cuối cùng sau mỗi lượt.

**Hình ảnh trực quan:**
- Lượt 1: Phần tử lớn nhất "nổi" lên cuối
- Lượt 2: Phần tử lớn thứ hai nổi lên vị trí kế cuối
- Tiếp tục cho đến khi mảng được sắp xếp

#### 2.2. Thuật toán

```python
def bubble_sort(arr):
    n = len(arr)
    
    # Duyệt qua tất cả các phần tử
    for i in range(n):
        # Cờ để tối ưu hóa
        swapped = False
        
        # Phần tử cuối cùng i phần tử đã được sắp xếp
        for j in range(0, n - i - 1):
            # So sánh phần tử liền kề
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Nếu không có hoán đổi nào, mảng đã sắp xếp
        if not swapped:
            break
    
    return arr

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
print("Mảng ban đầu:", arr)
print("Mảng sau khi sắp xếp:", bubble_sort(arr.copy()))
```

#### 2.3. Phân tích

**Độ phức tạp thời gian:**
- **Best case:** O(n) - Mảng đã được sắp xếp
- **Average case:** O(n²)
- **Worst case:** O(n²) - Mảng sắp xếp ngược

**Độ phức tạp không gian:** O(1) - In-place

**Đặc điểm:**
- ✅ Stable
- ✅ In-place
- ✅ Adaptive (với tối ưu hóa)
- ❌ Hiệu quả thấp với dữ liệu lớn

#### 2.4. Biến thể: Cocktail Shaker Sort

```python
def cocktail_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True
    
    while swapped:
        swapped = False
        
        # Đi từ trái sang phải
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        # Đi từ phải sang trái
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start += 1
    
    return arr
```

---

### 3. Selection Sort (Sắp xếp chọn)

#### 3.1. Ý tưởng

Selection Sort chia mảng thành hai phần: phần đã sắp xếp và phần chưa sắp xếp. Trong mỗi bước, thuật toán tìm phần tử nhỏ nhất trong phần chưa sắp xếp và đưa nó vào cuối phần đã sắp xếp.

**Các bước:**
1. Tìm phần tử nhỏ nhất trong mảng chưa sắp xếp
2. Hoán đổi nó với phần tử đầu tiên của mảng chưa sắp xếp
3. Di chuyển ranh giới giữa phần đã sắp xếp và chưa sắp xếp
4. Lặp lại cho đến khi mảng được sắp xếp

#### 3.2. Thuật toán

```python
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Tìm phần tử nhỏ nhất trong phần chưa sắp xếp
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Test
arr = [64, 25, 12, 22, 11]
print("Mảng ban đầu:", arr)
print("Mảng sau khi sắp xếp:", selection_sort(arr.copy()))
```

#### 3.3. Minh họa từng bước

```
Mảng: [64, 25, 12, 22, 11]

Bước 1: Tìm min = 11, hoán đổi với vị trí 0
        [11, 25, 12, 22, 64]

Bước 2: Tìm min = 12, hoán đổi với vị trí 1
        [11, 12, 25, 22, 64]

Bước 3: Tìm min = 22, hoán đổi với vị trí 2
        [11, 12, 22, 25, 64]

Bước 4: Tìm min = 25, không cần hoán đổi
        [11, 12, 22, 25, 64]
```

#### 3.4. Phân tích

**Độ phức tạp thời gian:**
- **Best case:** O(n²)
- **Average case:** O(n²)
- **Worst case:** O(n²)
- Số lần so sánh luôn cố định: n(n-1)/2

**Độ phức tạp không gian:** O(1)

**Đặc điểm:**
- ❌ Unstable (có thể làm stable với cài đặt khác)
- ✅ In-place
- ❌ Không adaptive
- ✅ Số lần hoán đổi ít nhất: O(n)

**Ưu điểm:**
- Đơn giản, dễ hiểu
- Số lần hoán đổi ít (tốt khi chi phí hoán đổi cao)
- Hoạt động tốt với mảng nhỏ

**Nhược điểm:**
- Không hiệu quả với dữ liệu lớn
- Không tận dụng được dữ liệu đã sắp xếp

---

### 4. Insertion Sort (Sắp xếp chèn)

#### 4.1. Ý tưởng

Insertion Sort xây dựng mảng đã sắp xếp từng phần tử một. Nó giống như cách chúng ta sắp xếp bài trong tay: lấy một lá bài và chèn nó vào đúng vị trí trong phần đã sắp xếp.

**Nguyên lý:**
1. Bắt đầu từ phần tử thứ hai
2. So sánh với các phần tử bên trái
3. Dịch các phần tử lớn hơn sang phải
4. Chèn phần tử vào vị trí đúng

#### 4.2. Thuật toán

```python
def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Di chuyển các phần tử lớn hơn key sang phải
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Chèn key vào vị trí đúng
        arr[j + 1] = key
    
    return arr

# Test
arr = [12, 11, 13, 5, 6]
print("Mảng ban đầu:", arr)
print("Mảng sau khi sắp xếp:", insertion_sort(arr.copy()))
```

#### 4.3. Minh họa từng bước

```
Mảng: [12, 11, 13, 5, 6]

Bước 1: key = 11
        [11, 12, 13, 5, 6]

Bước 2: key = 13, không thay đổi
        [11, 12, 13, 5, 6]

Bước 3: key = 5
        [5, 11, 12, 13, 6]

Bước 4: key = 6
        [5, 6, 11, 12, 13]
```

#### 4.4. Phân tích

**Độ phức tạp thời gian:**
- **Best case:** O(n) - Mảng đã sắp xếp
- **Average case:** O(n²)
- **Worst case:** O(n²) - Mảng sắp xếp ngược

**Độ phức tạp không gian:** O(1)

**Đặc điểm:**
- ✅ Stable
- ✅ In-place
- ✅ Adaptive
- ✅ Online

**Ưu điểm:**
- Đơn giản, dễ cài đặt
- Hiệu quả với mảng nhỏ hoặc gần như đã sắp xếp
- Stable và adaptive
- Online - có thể sắp xếp dữ liệu đến dần dần
- Ít hoán đổi hơn Bubble Sort

**Nhược điểm:**
- Không hiệu quả với dữ liệu lớn và ngẫu nhiên

#### 4.5. Tối ưu hóa: Binary Insertion Sort

```python
def binary_search(arr, item, start, end):
    """Tìm vị trí chèn bằng Binary Search"""
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < item:
            start = mid + 1
        elif arr[mid] > item:
            end = mid - 1
        else:
            return mid + 1
    return start

def binary_insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        # Tìm vị trí chèn bằng Binary Search
        pos = binary_search(arr, key, 0, i - 1)
        
        # Dịch chuyển các phần tử
        arr = arr[:pos] + [key] + arr[pos:i] + arr[i+1:]
    
    return arr
```

Giảm số lần so sánh từ O(n²) xuống O(n log n), nhưng số lần dịch chuyển vẫn là O(n²).

---

### 5. So sánh các thuật toán cơ bản

| Thuật toán | Best | Average | Worst | Space | Stable | Adaptive |
|------------|------|---------|-------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ❌ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |

#### 5.1. Khi nào sử dụng?

**Bubble Sort:**
- Mảng nhỏ và gần như đã sắp xếp
- Mục đích giáo dục
- Khi cần thuật toán đơn giản nhất

**Selection Sort:**
- Khi chi phí hoán đổi cao (ít hoán đổi nhất)
- Mảng nhỏ
- Khi bộ nhớ phụ bị hạn chế

**Insertion Sort:**
- Mảng nhỏ (< 50 phần tử)
- Mảng gần như đã sắp xếp
- Dữ liệu đến theo thời gian thực (online)
- Kết hợp với Merge Sort hoặc Quick Sort cho mảng con nhỏ

#### 5.2. Code so sánh hiệu năng

```python
import time
import random

def compare_sorting_algorithms(size=1000):
    # Tạo mảng ngẫu nhiên
    arr = [random.randint(1, 1000) for _ in range(size)]
    
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort
    }
    
    results = {}
    
    for name, func in algorithms.items():
        test_arr = arr.copy()
        start_time = time.time()
        func(test_arr)
        end_time = time.time()
        results[name] = end_time - start_time
    
    # In kết quả
    print(f"\nThời gian thực thi với mảng {size} phần tử:")
    for name, exec_time in sorted(results.items(), key=lambda x: x[1]):
        print(f"{name:20s}: {exec_time:.6f} giây")

# Test với các kích thước khác nhau
for size in [100, 500, 1000]:
    compare_sorting_algorithms(size)
```

#### 5.3. Ứng dụng thực tế

**1. Sắp xếp trong Database:**
- Sử dụng Insertion Sort cho dữ liệu nhỏ
- Kết hợp với các thuật toán nâng cao

**2. Sắp xếp trong thư viện:**
```python
# Python's sorted() và list.sort() sử dụng Timsort
# (kết hợp Merge Sort và Insertion Sort)

# Sắp xếp cơ bản
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)

# Sắp xếp với key function
students = [
    {'name': 'An', 'score': 85},
    {'name': 'Bình', 'score': 92},
    {'name': 'Chi', 'score': 78}
]
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
```

**3. Sắp xếp custom objects:**
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __lt__(self, other):
        return self.grade < other.grade
    
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

students = [Student("An", 85), Student("Bình", 92), Student("Chi", 78)]
sorted_students = insertion_sort(students)
print(sorted_students)
```

---

### 6. Tối ưu hóa và Thủ thuật

#### 6.1. Early termination (Dừng sớm)

```python
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Dừng nếu không có hoán đổi
            break
    return arr
```

#### 6.2. Giảm số lần hoán đổi

```python
def optimized_insertion_sort(arr):
    """Sử dụng shifting thay vì swapping"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift thay vì swap
            j -= 1
        arr[j + 1] = key
    return arr
```

#### 6.3. Hybrid approach

```python
def hybrid_sort(arr, threshold=10):
    """Sử dụng Insertion Sort cho mảng nhỏ"""
    if len(arr) <= threshold:
        return insertion_sort(arr)
    else:
        # Sử dụng thuật toán khác cho mảng lớn
        return sorted(arr)  # Placeholder
```

---

## Basic Sorting Algorithms

---

## Mergesort

### 1. Giới thiệu

#### 1.1. Khái niệm

Merge Sort là một thuật toán sắp xếp hiệu quả sử dụng kỹ thuật **Chia để trị (Divide and Conquer)**. Thuật toán chia mảng thành các phần nhỏ hơn, sắp xếp chúng, sau đó gộp (merge) các phần đã sắp xếp lại với nhau.

**Nguyên lý Divide and Conquer:**
1. **Divide (Chia):** Chia bài toán thành các bài toán con nhỏ hơn
2. **Conquer (Chinh phục):** Giải quyết các bài toán con (đệ quy)
3. **Combine (Kết hợp):** Gộp các lời giải của bài toán con

#### 1.2. Ý tưởng chính

```
Mảng: [38, 27, 43, 3, 9, 82, 10]

Bước 1 - Chia:
[38, 27, 43, 3] | [9, 82, 10]

Bước 2 - Chia tiếp:
[38, 27] | [43, 3] | [9, 82] | [10]

Bước 3 - Chia đến mức cơ sở:
[38] | [27] | [43] | [3] | [9] | [82] | [10]

Bước 4 - Gộp:
[27, 38] | [3, 43] | [9, 82] | [10]

Bước 5 - Gộp tiếp:
[3, 27, 38, 43] | [9, 10, 82]

Bước 6 - Gộp cuối:
[3, 9, 10, 27, 38, 43, 82]
```

---

### 2. Thuật toán Merge Sort

#### 2.1. Cài đặt cơ bản

```python
def merge_sort(arr):
    """
    Sắp xếp mảng sử dụng Merge Sort
    """
    if len(arr) <= 1:
        return arr
    
    # Chia mảng thành 2 nửa
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Đệ quy sắp xếp 2 nửa
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Gộp 2 nửa đã sắp xếp
    return merge(left, right)

def merge(left, right):
    """
    Gộp 2 mảng đã sắp xếp thành 1 mảng sắp xếp
    """
    result = []
    i = j = 0
    
    # So sánh từng phần tử và thêm phần tử nhỏ hơn vào result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Thêm các phần tử còn lại (nếu có)
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print("Mảng ban đầu:", arr)
print("Mảng sau khi sắp xếp:", merge_sort(arr))
```

#### 2.2. Cài đặt In-place (tối ưu bộ nhớ)

```python
def merge_sort_inplace(arr, left, right):
    """
    Merge Sort in-place để tiết kiệm bộ nhớ
    """
    if left < right:
        mid = (left + right) // 2
        
        # Sắp xếp 2 nửa
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        
        # Gộp 2 nửa
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr, left, mid, right):
    """
    Gộp 2 phần đã sắp xếp trong mảng
    """
    # Tạo mảng tạm
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Gộp vào mảng gốc
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy phần tử còn lại
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_inplace(arr, 0, len(arr) - 1)
print("Mảng sau khi sắp xếp:", arr)
```

#### 2.3. Cài đặt với iteration (không đệ quy)

```python
def merge_sort_iterative(arr):
    """
    Merge Sort sử dụng vòng lặp thay vì đệ quy
    """
    n = len(arr)
    current_size = 1
    
    # Bắt đầu với kích thước 1, tăng gấp đôi mỗi lần
    while current_size < n:
        left = 0
        
        while left < n - 1:
            # Tìm điểm giữa và điểm cuối
            mid = min(left + current_size - 1, n - 1)
            right = min(left + 2 * current_size - 1, n - 1)
            
            # Gộp các phần con
            merge_inplace(arr, left, mid, right)
            
            # Di chuyển đến phần con tiếp theo
            left += 2 * current_size
        
        # Tăng kích thước gấp đôi
        current_size *= 2
    
    return arr

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print("Mảng sau khi sắp xếp:", merge_sort_iterative(arr))
```

---

### 3. Phân tích thuật toán

#### 3.1. Độ phức tạp thời gian

**Phân tích bằng Master Theorem:**
- Công thức đệ quy: T(n) = 2T(n/2) + O(n)
- Trong đó:
  - 2T(n/2): Chi phí sắp xếp 2 nửa
  - O(n): Chi phí gộp

**Độ cao cây đệ quy:** log₂(n)
**Chi phí mỗi tầng:** O(n)
**Tổng chi phí:** O(n log n)

**Kết quả:**
- **Best case:** O(n log n)
- **Average case:** O(n log n)
- **Worst case:** O(n log n)

**Đặc điểm độ phức tạp:**
- Luôn là O(n log n), không phụ thuộc vào dữ liệu đầu vào
- Tốt hơn các thuật toán O(n²)
- Là thuật toán optimal cho comparison-based sorting trong worst case

#### 3.2. Độ phức tạp không gian

**Space Complexity:** O(n)
- Cần thêm bộ nhớ để lưu các mảng tạm trong quá trình merge
- Với đệ quy: O(n) cho mảng tạm + O(log n) cho stack
- Tổng: O(n)

**Cải thiện bộ nhớ:**
```python
def merge_sort_optimized(arr):
    """
    Sử dụng một mảng phụ duy nhất cho toàn bộ quá trình
    """
    n = len(arr)
    temp = [0] * n
    
    def sort_helper(left, right):
        if left < right:
            mid = (left + right) // 2
            sort_helper(left, mid)
            sort_helper(mid + 1, right)
            merge_with_temp(left, mid, right)
    
    def merge_with_temp(left, mid, right):
        # Copy vào mảng tạm
        for i in range(left, right + 1):
            temp[i] = arr[i]
        
        i, j = left, mid + 1
        k = left
        
        while i <= mid and j <= right:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1
            k += 1
        
        while i <= mid:
            arr[k] = temp[i]
            i += 1
            k += 1
    
    sort_helper(0, n - 1)
    return arr
```

#### 3.3. Đặc điểm

**Ưu điểm:**
- ✅ **Stable:** Giữ nguyên thứ tự tương đối của các phần tử bằng nhau
- ✅ **Predictable:** Luôn O(n log n) cho mọi trường hợp
- ✅ **Parallelizable:** Có thể song song hóa dễ dàng
- ✅ **External sorting:** Thích hợp cho sắp xếp dữ liệu lớn không fit trong RAM

**Nhược điểm:**
- ❌ **Space:** Cần O(n) bộ nhớ phụ
- ❌ **Not in-place:** (Phiên bản chuẩn)
- ❌ **Overhead:** Chi phí đệ quy và copy dữ liệu

---

### 4. Các biến thể và tối ưu hóa

#### 4.1. Natural Merge Sort

Tận dụng các phần đã sắp xếp tự nhiên trong mảng.

```python
def natural_merge_sort(arr):
    """
    Tận dụng các dãy con đã được sắp xếp sẵn
    """
    n = len(arr)
    
    def get_runs():
        """Tìm các dãy con đã sắp xếp"""
        runs = []
        i = 0
        
        while i < n:
            start = i
            # Tìm dãy tăng dần
            while i < n - 1 and arr[i] <= arr[i + 1]:
                i += 1
            runs.append((start, i))
            i += 1
        
        return runs
    
    while True:
        runs = get_runs()
        if len(runs) <= 1:
            break
        
        # Gộp các runs liên tiếp
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                left_start, left_end = runs[i]
                right_start, right_end = runs[i + 1]
                merge_inplace(arr, left_start, left_end, right_end)
                new_runs.append((left_start, right_end))
            else:
                new_runs.append(runs[i])
    
    return arr
```

#### 4.2. Bottom-up Merge Sort

```python
def bottom_up_merge_sort(arr):
    """
    Merge sort không dùng đệ quy, gộp từ dưới lên
    """
    n = len(arr)
    width = 1
    
    while width < n:
        left = 0
        while left < n:
            mid = min(left + width - 1, n - 1)
            right = min(left + 2 * width - 1, n - 1)
            
            if mid < right:
                merge_inplace(arr, left, mid, right)
            
            left += 2 * width
        
        width *= 2
    
    return arr
```

#### 4.3. Hybrid Merge Sort (Tim Sort inspired)

Kết hợp với Insertion Sort cho các mảng con nhỏ.

```python
def hybrid_merge_sort(arr, threshold=10):
    """
    Sử dụng Insertion Sort cho mảng nhỏ
    """
    def insertion_sort_range(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    
    def merge_sort_helper(left, right):
        if right - left + 1 <= threshold:
            insertion_sort_range(arr, left, right)
        elif left < right:
            mid = (left + right) // 2
            merge_sort_helper(left, mid)
            merge_sort_helper(mid + 1, right)
            merge_inplace(arr, left, mid, right)
    
    merge_sort_helper(0, len(arr) - 1)
    return arr
```

#### 4.4. 3-way Merge Sort

Chia mảng thành 3 phần thay vì 2.

```python
def three_way_merge_sort(arr):
    """
    Chia mảng thành 3 phần
    """
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    third = n // 3
    
    # Chia thành 3 phần
    left = merge_sort(arr[:third])
    middle = merge_sort(arr[third:2*third])
    right = merge_sort(arr[2*third:])
    
    # Gộp 3 phần
    return merge_three(left, middle, right)

def merge_three(left, middle, right):
    """
    Gộp 3 mảng đã sắp xếp
    """
    result = []
    i = j = k = 0
    
    while i < len(left) and j < len(middle) and k < len(right):
        if left[i] <= middle[j] and left[i] <= right[k]:
            result.append(left[i])
            i += 1
        elif middle[j] <= left[i] and middle[j] <= right[k]:
            result.append(middle[j])
            j += 1
        else:
            result.append(right[k])
            k += 1
    
    # Gộp 2 mảng còn lại
    while i < len(left) and j < len(middle):
        if left[i] <= middle[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(middle[j])
            j += 1
    
    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[k])
            k += 1
    
    while j < len(middle) and k < len(right):
        if middle[j] <= right[k]:
            result.append(middle[j])
            j += 1
        else:
            result.append(right[k])
            k += 1
    
    # Thêm phần tử còn lại
    result.extend(left[i:])
    result.extend(middle[j:])
    result.extend(right[k:])
    
    return result
```

---

### 5. Ứng dụng thực tế

#### 5.1. External Sorting (Sắp xếp file lớn)

```python
import os
import heapq

def external_merge_sort(input_file, output_file, chunk_size=1000):
    """
    Sắp xếp file lớn không fit trong RAM
    """
    # Bước 1: Chia file thành các chunk nhỏ và sắp xếp
    temp_files = []
    with open(input_file, 'r') as f:
        chunk = []
        for line in f:
            chunk.append(int(line.strip()))
            
            if len(chunk) >= chunk_size:
                chunk.sort()
                temp_file = f"temp_{len(temp_files)}.txt"
                with open(temp_file, 'w') as tf:
                    tf.writelines(f"{x}\n" for x in chunk)
                temp_files.append(temp_file)
                chunk = []
        
        # Xử lý chunk cuối
        if chunk:
            chunk.sort()
            temp_file = f"temp_{len(temp_files)}.txt"
            with open(temp_file, 'w') as tf:
                tf.writelines(f"{x}\n" for x in chunk)
            temp_files.append(temp_file)
    
    # Bước 2: Merge các file tạm sử dụng heap
    with open(output_file, 'w') as outf:
        # Mở tất cả file tạm
        files = [open(f, 'r') for f in temp_files]
        
        # Heap chứa (giá trị, index file)
        heap = []
        for i, f in enumerate(files):
            line = f.readline()
            if line:
                heapq.heappush(heap, (int(line.strip()), i))
        
        # Merge
        while heap:
            value, file_idx = heapq.heappop(heap)
            outf.write(f"{value}\n")
            
            # Đọc phần tử tiếp theo từ file
            line = files[file_idx].readline()
            if line:
                heapq.heappush(heap, (int(line.strip()), file_idx))
        
        # Đóng các file
        for f in files:
            f.close()
    
    # Xóa file tạm
    for temp_file in temp_files:
        os.remove(temp_file)
```

#### 5.2. Đếm số lần đảo ngược (Inversion Count)

```python
def count_inversions(arr):
    """
    Đếm số cặp (i, j) mà i < j nhưng arr[i] > arr[j]
    Sử dụng merge sort: O(n log n)
    """
    def merge_count(arr, temp, left, mid, right):
        i = left    # Index cho mảng trái
        j = mid + 1 # Index cho mảng phải
        k = left    # Index cho mảng kết quả
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                # Tất cả phần tử từ i đến mid đều lớn hơn arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        
        # Copy phần tử còn lại
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        # Copy từ temp về arr
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv_count
    
    def merge_sort_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            
            inv_count += merge_sort_count(arr, temp, left, mid)
            inv_count += merge_sort_count(arr, temp, mid + 1, right)
            inv_count += merge_count(arr, temp, left, mid, right)
        
        return inv_count
    
    n = len(arr)
    temp = [0] * n
    return merge_sort_count(arr, temp, 0, n - 1)

# Test
arr = [8, 4, 2, 1]
print(f"Số lần đảo ngược: {count_inversions(arr.copy())}")  # 6
```

#### 5.3. Tìm điểm giao nhau của các đoạn thẳng

```python
class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"[{self.start}, {self.end}]"

def merge_intervals(intervals):
    """
    Gộp các đoạn giao nhau
    """
    if not intervals:
        return []
    
    # Sắp xếp theo điểm bắt đầu
    intervals.sort(key=lambda x: x.start)
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current.start <= last.end:
            # Gộp đoạn
            last.end = max(last.end, current.end)
        else:
            merged.append(current)
    
    return merged

# Test
segments = [
    Segment(1, 3),
    Segment(2, 6),
    Segment(8, 10),
    Segment(15, 18)
]
result = merge_intervals(segments)
print("Các đoạn sau khi gộp:", result)
```

#### 5.4. K-way Merge

```python
import heapq

def k_way_merge(lists):
    """
    Gộp k danh sách đã sắp xếp thành 1 danh sách
    Ứng dụng: Merge output từ nhiều sorted files
    """
    heap = []
    result = []
    
    # Thêm phần tử đầu tiên của mỗi list vào heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    # Extract min và thêm phần tử tiếp theo
    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)
        
        # Thêm phần tử tiếp theo từ cùng list
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_value, list_idx, element_idx + 1))
    
    return result

# Test
lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
print("K-way merge:", k_way_merge(lists))
```

---

### 6. So sánh với các thuật toán khác

| Thuật toán | Best | Average | Worst | Space | Stable | In-place |
|------------|------|---------|-------|-------|--------|----------|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | ✅ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |

#### 6.1. Khi nào sử dụng Merge Sort?

**Nên sử dụng khi:**
- ✅ Cần thuật toán stable
- ✅ Cần độ phức tạp guaranteed O(n log n)
- ✅ Sắp xếp linked list (không cần bộ nhớ phụ)
- ✅ External sorting (dữ liệu không fit trong RAM)
- ✅ Parallel/distributed sorting
- ✅ Counting inversions
- ✅ Dữ liệu đến dần dần (online)

**Không nên sử dụng khi:**
- ❌ Bộ nhớ bị hạn chế nghiêm ngặt
- ❌ Cần in-place sorting
- ❌ Mảng nhỏ (overhead đệ quy cao)

---

### 7. Merge Sort cho Linked List

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort_linked_list(head):
    """
    Merge sort cho linked list - O(1) space!
    """
    if not head or not head.next:
        return head
    
    # Tìm điểm giữa
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Chia list thành 2 phần
    prev.next = None
    
    # Sắp xếp đệ quy
    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(slow)
    
    # Merge
    return merge_linked_lists(left, right)

def merge_linked_lists(l1, l2):
    """
    Gộp 2 linked lists đã sắp xếp
    """
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    
    return dummy.next

# Helper function
def print_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Test
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print("Trước khi sắp xếp:")
print_list(head)
sorted_head = merge_sort_linked_list(head)
print("Sau khi sắp xếp:")
print_list(sorted_head)
```

---

### 8. Parallel Merge Sort

```python
from concurrent.futures import ThreadPoolExecutor
import threading

def parallel_merge_sort(arr, depth=0, max_depth=3):
    """
    Merge sort song song sử dụng threads
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Sử dụng parallel khi depth nhỏ
    if depth < max_depth:
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_left = executor.submit(parallel_merge_sort, left, depth + 1, max_depth)
            future_right = executor.submit(parallel_merge_sort, right, depth + 1, max_depth)
            
            left = future_left.result()
            right = future_right.result()
    else:
        # Sequential cho các phần nhỏ
        left = merge_sort(left)
        right = merge_sort(right)
    
    return merge(left, right)

# Test
import time
arr = list(range(10000, 0, -1))

start = time.time()
sorted_arr = merge_sort(arr.copy())
sequential_time = time.time() - start

start = time.time()
sorted_arr = parallel_merge_sort(arr.copy())
parallel_time = time.time() - start

print(f"Sequential: {sequential_time:.4f}s")
print(f"Parallel: {parallel_time:.4f}s")
print(f"Speedup: {sequential_time/parallel_time:.2f}x")
```

---

## Quicksort

### 1. Giới thiệu

#### 1.1. Khái niệm

Quick Sort là một thuật toán sắp xếp hiệu quả sử dụng kỹ thuật **Chia để trị (Divide and Conquer)**. Thuật toán chọn một phần tử làm "pivot" (chốt), phân hoạch mảng sao cho các phần tử nhỏ hơn pivot ở bên trái và các phần tử lớn hơn ở bên phải, sau đó đệ quy sắp xếp hai phần.

**Đặc điểm nổi bật:**
- Được phát minh bởi Tony Hoare năm 1960
- Là thuật toán sắp xếp phổ biến nhất trong thực tế
- Average case O(n log n), nhưng worst case O(n²)
- In-place sorting (không cần bộ nhớ phụ nhiều)

#### 1.2. Ý tưởng chính

**Nguyên lý:**
1. **Chọn Pivot:** Chọn một phần tử làm pivot (có thể là đầu, cuối, giữa, hoặc random)
2. **Partition:** Sắp xếp lại mảng sao cho:
   - Tất cả phần tử < pivot ở bên trái
   - Tất cả phần tử > pivot ở bên phải
   - Pivot ở đúng vị trí cuối cùng
3. **Đệ quy:** Áp dụng quick sort cho phần trái và phần phải

**Ví dụ trực quan:**
```
Mảng: [10, 7, 8, 9, 1, 5]
Pivot: 5 (phần tử cuối)

Sau partition:
[1] [5] [7, 8, 9, 10]
 ^   ^   ^
 Trái  Pivot  Phải

Đệ quy sắp xếp [7, 8, 9, 10]:
Pivot: 10
[7, 8, 9] [10] []

Tiếp tục...
Kết quả: [1, 5, 7, 8, 9, 10]
```

---

### 2. Thuật toán Quick Sort

#### 2.1. Cài đặt cơ bản (Lomuto Partition)

```python
def quick_sort(arr, low=0, high=None):
    """
    Quick Sort sử dụng Lomuto partition scheme
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition và lấy vị trí pivot
        pivot_index = partition(arr, low, high)
        
        # Đệ quy sắp xếp 2 phần
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    """
    Lomuto partition: Chọn phần tử cuối làm pivot
    """
    pivot = arr[high]
    i = low - 1  # Index của phần tử nhỏ hơn
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Đặt pivot vào vị trí đúng
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test
arr = [10, 7, 8, 9, 1, 5]
print("Mảng ban đầu:", arr)
print("Mảng sau khi sắp xếp:", quick_sort(arr.copy()))
```

#### 2.2. Hoare Partition Scheme (Hiệu quả hơn)

```python
def quick_sort_hoare(arr, low=0, high=None):
    """
    Quick Sort sử dụng Hoare partition scheme
    Hiệu quả hơn Lomuto (ít swap hơn 3 lần)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, pivot_index)
        quick_sort_hoare(arr, pivot_index + 1, high)
    
    return arr

def hoare_partition(arr, low, high):
    """
    Hoare partition: Pivot ở giữa, 2 con trỏ từ 2 đầu
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        # Tìm phần tử >= pivot từ trái
        i += 1
        while arr[i] < pivot:
            i += 1
        
        # Tìm phần tử <= pivot từ phải
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        # Nếu 2 con trỏ gặp nhau
        if i >= j:
            return j
        
        # Swap
        arr[i], arr[j] = arr[j], arr[i]

# Test
arr = [10, 7, 8, 9, 1, 5]
print("Hoare Partition:", quick_sort_hoare(arr.copy()))
```

---

### 3. Phân tích thuật toán

#### 3.1. Độ phức tạp thời gian

**Best Case: O(n log n)**
- Xảy ra khi pivot luôn chia mảng thành 2 phần bằng nhau
- Độ cao cây đệ quy: log n
- Mỗi tầng: O(n) cho partition
- Tổng: O(n log n)

**Average Case: O(n log n)**
- Với pivot ngẫu nhiên, expected time là O(n log n)
- Ngay cả khi không chia đều (tỉ lệ 9:1), vẫn là O(n log n)

**Worst Case: O(n²)**
- Xảy ra khi pivot luôn là phần tử nhỏ nhất hoặc lớn nhất
- Ví dụ: Mảng đã sắp xếp với pivot là phần tử đầu/cuối
- Độ cao cây đệ quy: n
- Tổng: O(n²)

**Minh họa Worst Case:**
```
Mảng: [1, 2, 3, 4, 5] (pivot = cuối)

Lần 1: [1,2,3,4] | 5 | []       - n operations
Lần 2: [1,2,3] | 4 | []         - (n-1) operations
Lần 3: [1,2] | 3 | []           - (n-2) operations
...
Tổng: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = O(n²)
```

#### 3.2. Độ phức tạp không gian

**Space Complexity:**
- **Best/Average case:** O(log n) - Chiều cao cây đệ quy
- **Worst case:** O(n) - Cây đệ quy thoái hóa

**In-place:** ✅ (không cần mảng phụ, chỉ dùng stack cho đệ quy)

#### 3.3. Đặc điểm

**Ưu điểm:**
- ✅ Rất nhanh trong thực tế (cache-friendly)
- ✅ In-place (O(log n) space)
- ✅ Dễ song song hóa
- ✅ Có thể tối ưu cho nhiều trường hợp

**Nhược điểm:**
- ❌ Unstable (không giữ thứ tự tương đối)
- ❌ Worst case O(n²) (có thể tránh với random pivot)
- ❌ Không tốt với dữ liệu đã sắp xếp (nếu không tối ưu)

---

### 4. Tối ưu hóa Quick Sort

#### 4.1. Random Pivot (Tránh worst case)

```python
import random

def randomized_partition(arr, low, high):
    """
    Chọn pivot ngẫu nhiên
    """
    # Chọn random index và đổi về cuối
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)

def randomized_quick_sort(arr, low=0, high=None):
    """
    Randomized Quick Sort - Tránh worst case O(n²)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)
    
    return arr
```

#### 4.2. Median-of-Three (Tối ưu)

```python
def median_of_three(arr, low, high):
    """
    Chọn median của 3 phần tử làm pivot
    """
    mid = (low + high) // 2
    
    # Sắp xếp 3 phần tử
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Đặt median (arr[mid]) vào vị trí high-1
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    return arr[high - 1]
```

#### 4.3. Three-Way Partitioning (Dutch National Flag)

Xử lý tốt khi có nhiều phần tử trùng lặp.

```python
def three_way_partition(arr, low, high):
    """
    Chia mảng thành 3 phần: < pivot, = pivot, > pivot
    """
    if high <= low:
        return low, high
    
    pivot = arr[low]
    lt = low       # arr[low..lt-1] < pivot
    i = low + 1    # arr[lt..i-1] == pivot
    gt = high      # arr[gt+1..high] > pivot
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt

def quick_sort_3way(arr, low=0, high=None):
    """
    Quick Sort với 3-way partitioning
    Tối ưu cho mảng có nhiều phần tử trùng
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        lt, gt = three_way_partition(arr, low, high)
        quick_sort_3way(arr, low, lt - 1)
        quick_sort_3way(arr, gt + 1, high)
    
    return arr

# Test với mảng có nhiều phần tử trùng
arr = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
print("Mảng có nhiều phần tử trùng:", arr)
print("Sau 3-way quick sort:", quick_sort_3way(arr.copy()))
```

---

### 5. Ứng dụng thực tế

#### 5.1. Quick Select - Tìm phần tử thứ k

```python
def quick_select(arr, k):
    """
    Tìm phần tử thứ k nhỏ nhất (0-indexed)
    Average: O(n), Worst: O(n²)
    """
    def select(arr, low, high, k):
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(arr, low, pivot_index - 1, k)
        else:
            return select(arr, pivot_index + 1, high, k)
    
    return select(arr, 0, len(arr) - 1, k)

# Test
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(f"Phần tử thứ {k+1} nhỏ nhất:", quick_select(arr.copy(), k))

# Tìm median
def find_median(arr):
    n = len(arr)
    if n % 2 == 1:
        return quick_select(arr, n // 2)
    else:
        return (quick_select(arr.copy(), n // 2 - 1) + 
                quick_select(arr.copy(), n // 2)) / 2

print("Median:", find_median([3, 2, 1, 5, 6, 4]))
```

#### 5.2. Kth Largest Element

```python
def find_kth_largest(arr, k):
    """
    Tìm phần tử lớn thứ k
    """
    # Phần tử lớn thứ k = phần tử thứ (n-k) từ trái
    return quick_select(arr, len(arr) - k)

# Test
arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(f"Phần tử lớn thứ 4:", find_kth_largest(arr, 4))
```

---

### 6. So sánh với các thuật toán khác

| Đặc điểm | Quick Sort | Merge Sort | Heap Sort |
|----------|------------|------------|-----------|
| **Average Time** | O(n log n) | O(n log n) | O(n log n) |
| **Worst Time** | O(n²) | O(n log n) | O(n log n) |
| **Space** | O(log n) | O(n) | O(1) |
| **Stable** | ❌ | ✅ | ❌ |
| **In-place** | ✅ | ❌ | ✅ |
| **Cache-friendly** | ✅ | ❌ | ⚠️ |

#### 6.1. Khi nào dùng Quick Sort?

**Nên dùng:**
- ✅ Mảng trong RAM (in-memory sorting)
- ✅ Cần sorting nhanh nhất average case
- ✅ Bộ nhớ hạn chế
- ✅ Random access data (array)
- ✅ Không cần stable sort

**Không nên dùng:**
- ❌ Cần đảm bảo O(n log n) worst case
- ❌ Cần stable sorting
- ❌ Linked list (Merge Sort tốt hơn)
- ❌ Dữ liệu đã gần sắp xếp (trừ khi dùng random pivot)

---

### 7. Quick Sort trong thư viện chuẩn

#### 7.1. Python's sorted() và sort()

Python sử dụng **Timsort** (hybrid của Merge Sort và Insertion Sort), không phải Quick Sort, vì:
- Stable sorting
- Tốt với dữ liệu có pattern
- Worst case O(n log n) đảm bảo

#### 7.2. C++ std::sort()

C++ sử dụng **Introsort** (Introspective Sort):
- Bắt đầu với Quick Sort
- Chuyển sang Heap Sort nếu đệ quy quá sâu (tránh O(n²))
- Dùng Insertion Sort cho mảng nhỏ

#### 7.3. Java's Arrays.sort()

- **Primitive types:** Dual-Pivot Quick Sort
- **Object types:** Timsort (stable)

---

## Priority Queue & Binary Heap

### 1. Giới thiệu Priority Queue

#### 1.1. Khái niệm

**Priority Queue (Hàng đợi ưu tiên)** là một cấu trúc dữ liệu trừu tượng trong đó mỗi phần tử có một độ ưu tiên (priority) được gán cho nó. Phần tử có độ ưu tiên cao nhất được xử lý trước, bất kể thứ tự chèn vào.

**Khác với Queue thông thường:**
- Queue thông thường: FIFO (First In First Out)
- Priority Queue: Phần tử có priority cao nhất ra trước

**Ví dụ thực tế:**
- **Hệ thống cấp cứu:** Bệnh nhân nguy kịch được ưu tiên khám trước
- **CPU Scheduling:** Process có priority cao được xử lý trước
- **Dijkstra Algorithm:** Chọn đỉnh có khoảng cách nhỏ nhất
- **A* Search:** Chọn node có f(n) nhỏ nhất
- **Huffman Coding:** Xây dựng cây mã hóa

#### 1.2. Các thao tác cơ bản

**a) Insert/Enqueue:** Thêm phần tử với priority
**b) Extract-Max/Min:** Lấy và xóa phần tử có priority cao/thấp nhất
**c) Peek/Top:** Xem phần tử có priority cao/thấp nhất
**d) Change Priority:** Thay đổi priority của phần tử
**e) Delete:** Xóa phần tử bất kỳ

#### 1.3. Các cách cài đặt

| Cài đặt | Insert | Extract-Max | Peek |
|---------|--------|-------------|------|
| Array (unsorted) | O(1) | O(n) | O(n) |
| Array (sorted) | O(n) | O(1) | O(1) |
| Linked List | O(n) | O(1) | O(1) |
| **Binary Heap** | **O(log n)** | **O(log n)** | **O(1)** |
| Fibonacci Heap | O(1) | O(log n) | O(1) |

**Binary Heap là cài đặt phổ biến nhất** vì cân bằng tốt giữa các thao tác.

---

### 2. Binary Heap

#### 2.1. Khái niệm

**Binary Heap** là một cây nhị phân hoàn chỉnh (complete binary tree) thỏa mãn tính chất heap:

**Max Heap:**
- Giá trị của mỗi node ≥ giá trị của các node con
- Node gốc có giá trị lớn nhất

**Min Heap:**
- Giá trị của mỗi node ≤ giá trị của các node con
- Node gốc có giá trị nhỏ nhất

#### 2.2. Tính chất

**a) Complete Binary Tree:**
- Tất cả các level đều đầy, trừ level cuối
- Level cuối được điền từ trái sang phải

**b) Biểu diễn bằng mảng:**
Với node tại index `i`:
- Parent: `(i - 1) // 2`
- Left child: `2 * i + 1`
- Right child: `2 * i + 2`

**Ví dụ Max Heap:**
```
        50
       /  \
      30   40
     / \   /
    10 20 35

Mảng: [50, 30, 40, 10, 20, 35]
Index: 0   1   2   3   4   5
```

#### 2.3. Ưu điểm của Binary Heap

- ✅ Không cần con trỏ (dùng mảng)
- ✅ Cache-friendly (truy cập liên tiếp)
- ✅ Cân bằng tự động
- ✅ Dễ cài đặt
- ✅ Hiệu quả: O(log n) cho insert và extract

---

### 3. Cài đặt Min Heap

#### 3.1. Cấu trúc cơ bản

```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def has_left_child(self, i):
        return self.left_child(i) < len(self.heap)
    
    def has_right_child(self, i):
        return self.right_child(i) < len(self.heap)
    
    def has_parent(self, i):
        return self.parent(i) >= 0
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
```

#### 3.2. Heapify Up (Bubble Up)

Dùng khi insert phần tử mới vào cuối heap.

```python
    def heapify_up(self, i):
        """
        Di chuyển phần tử lên trên cho đến khi thỏa mãn heap property
        """
        while self.has_parent(i) and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
```

**Minh họa:**
```
Thêm 5 vào heap:

Bước 1: Thêm vào cuối
      10
     /  \
    20  15
   / \  /
  30 25 5*  <- Thêm ở đây

Bước 2: So sánh với parent (15), swap
      10
     /  \
    20  5*
   / \  /
  30 25 15

Bước 3: So sánh với parent (10), swap
      5*
     /  \
    20  10
   / \  /
  30 25 15
```

#### 3.3. Heapify Down (Bubble Down)

Dùng khi extract phần tử root.

```python
    def heapify_down(self, i):
        """
        Di chuyển phần tử xuống dưới cho đến khi thỏa mãn heap property
        """
        while self.has_left_child(i):
            # Tìm con nhỏ hơn
            smaller_child_index = self.left_child(i)
            
            if (self.has_right_child(i) and 
                self.heap[self.right_child(i)] < self.heap[smaller_child_index]):
                smaller_child_index = self.right_child(i)
            
            # Nếu phần tử hiện tại nhỏ hơn cả 2 con, dừng
            if self.heap[i] <= self.heap[smaller_child_index]:
                break
            
            # Swap với con nhỏ hơn
            self.swap(i, smaller_child_index)
            i = smaller_child_index
```

**Minh họa:**
```
Extract min (5):

Bước 1: Thay thế root bằng phần tử cuối
      15*
     /  \
    20  10
   / \
  30 25

Bước 2: Heapify down, swap với 10
      10
     /  \
    20  15*
   / \
  30 25

Dừng: 15 < 30 và 15 < 25 (không có con phải)
```

#### 3.4. Insert (Thêm phần tử)

```python
    def insert(self, value):
        """
        Thêm phần tử vào heap
        Time Complexity: O(log n)
        """
        # Thêm vào cuối
        self.heap.append(value)
        # Heapify up
        self.heapify_up(len(self.heap) - 1)
```

#### 3.5. Extract Min (Lấy phần tử nhỏ nhất)

```python
    def extract_min(self):
        """
        Lấy và xóa phần tử nhỏ nhất
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise Exception("Heap is empty")
        
        # Lấy phần tử root
        min_value = self.heap[0]
        
        # Thay thế root bằng phần tử cuối
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Heapify down nếu heap không rỗng
        if not self.is_empty():
            self.heapify_down(0)
        
        return min_value
```

#### 3.6. Peek (Xem phần tử nhỏ nhất)

```python
    def peek(self):
        """
        Xem phần tử nhỏ nhất mà không xóa
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Exception("Heap is empty")
        return self.heap[0]
```

#### 3.7. Build Heap (Xây dựng heap từ mảng)

```python
    def build_heap(self, arr):
        """
        Xây dựng heap từ mảng cho trước
        Time Complexity: O(n)
        """
        self.heap = arr.copy()
        
        # Heapify từ node cuối cùng có con (từ dưới lên trên)
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)
```

**Tại sao O(n) chứ không phải O(n log n)?**
- Các node ở level cuối không cần heapify
- Các node gần root có ít hơn, nhưng chi phí heapify cao hơn
- Tổng chi phí: Σ(h * nodes_at_level_h) ≈ O(n)

---

### 4. Cài đặt Max Heap

```python
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        """Max Heap: parent phải lớn hơn con"""
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        """Max Heap: parent phải lớn hơn con"""
        while self.left_child(i) < len(self.heap):
            larger_child = self.left_child(i)
            
            if (self.right_child(i) < len(self.heap) and
                self.heap[self.right_child(i)] > self.heap[larger_child]):
                larger_child = self.right_child(i)
            
            if self.heap[i] >= self.heap[larger_child]:
                break
            
            self.swap(i, larger_child)
            i = larger_child
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        if not self.heap:
            raise Exception("Heap is empty")
        
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self.heapify_down(0)
        
        return max_value
    
    def peek(self):
        if not self.heap:
            raise Exception("Heap is empty")
        return self.heap[0]
```

---

### 5. Test và Demo

```python
# Test Min Heap
print("=== MIN HEAP ===")
min_heap = MinHeap()

# Insert elements
elements = [5, 3, 8, 1, 9, 2, 7]
print(f"Inserting: {elements}")
for elem in elements:
    min_heap.insert(elem)
    print(f"After inserting {elem}: {min_heap.heap}")

print(f"\nMin element (peek): {min_heap.peek()}")

# Extract min
print("\nExtracting min elements:")
while not min_heap.is_empty():
    min_val = min_heap.extract_min()
    print(f"Extracted: {min_val}, Remaining: {min_heap.heap}")

# Test Max Heap
print("\n=== MAX HEAP ===")
max_heap = MaxHeap()

print(f"Inserting: {elements}")
for elem in elements:
    max_heap.insert(elem)
    print(f"After inserting {elem}: {max_heap.heap}")

print(f"\nMax element (peek): {max_heap.peek()}")

# Extract max
print("\nExtracting max elements:")
while max_heap.heap:
    max_val = max_heap.extract_max()
    print(f"Extracted: {max_val}, Remaining: {max_heap.heap}")

# Test Build Heap
print("\n=== BUILD HEAP ===")
arr = [9, 5, 6, 2, 3, 7, 1, 4, 8]
print(f"Original array: {arr}")

min_heap2 = MinHeap()
min_heap2.build_heap(arr)
print(f"Min Heap: {min_heap2.heap}")

max_heap2 = MaxHeap()
max_heap2.heap = arr.copy()
for i in range(len(max_heap2.heap) // 2 - 1, -1, -1):
    max_heap2.heapify_down(i)
print(f"Max Heap: {max_heap2.heap}")
```

---

### 6. Ứng dụng thực tế

#### 6.1. Heap Sort

```python
def heap_sort(arr):
    """
    Sắp xếp mảng sử dụng heap
    Time Complexity: O(n log n)
    Space Complexity: O(1) - in-place
    """
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap root (max) với phần tử cuối
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify root với heap size giảm dần
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """Heapify subtree rooted at index i"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Test
arr = [12, 11, 13, 5, 6, 7]
print("Original:", arr)
print("Sorted:", heap_sort(arr.copy()))
```

#### 6.2. K Largest/Smallest Elements

```python
def k_largest_elements(arr, k):
    """
    Tìm k phần tử lớn nhất
    Sử dụng Min Heap với size k
    Time: O(n log k)
    """
    import heapq
    
    # Duy trì min heap với k phần tử lớn nhất
    heap = arr[:k]
    heapq.heapify(heap)
    
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return sorted(heap, reverse=True)

def k_smallest_elements(arr, k):
    """
    Tìm k phần tử nhỏ nhất
    Sử dụng Max Heap với size k
    Time: O(n log k)
    """
    import heapq
    
    # Python heapq là min heap, dùng số âm để làm max heap
    heap = [-x for x in arr[:k]]
    heapq.heapify(heap)
    
    for num in arr[k:]:
        if num < -heap[0]:
            heapq.heapreplace(heap, -num)
    
    return sorted([-x for x in heap])

# Test
arr = [3, 2, 1, 5, 6, 4, 8, 9, 7]
print(f"3 largest: {k_largest_elements(arr, 3)}")
print(f"3 smallest: {k_smallest_elements(arr, 3)}")
```

#### 6.3. Merge K Sorted Lists

```python
import heapq

def merge_k_sorted_lists(lists):
    """
    Gộp k danh sách đã sắp xếp
    Time: O(n log k) với n là tổng số phần tử
    """
    heap = []
    result = []
    
    # Thêm phần tử đầu tiên của mỗi list vào heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    # Extract min và thêm phần tử tiếp theo
    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)
        
        # Thêm phần tử tiếp theo từ cùng list
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_value, list_idx, element_idx + 1))
    
    return result

# Test
lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
print("Merged:", merge_k_sorted_lists(lists))
```

#### 6.4. Median of Running Stream

```python
class MedianFinder:
    """
    Tìm median của dòng số liệu
    Sử dụng 2 heap: max heap (nửa trái) và min heap (nửa phải)
    """
    def __init__(self):
        self.max_heap = []  # Nửa nhỏ hơn (dùng số âm)
        self.min_heap = []  # Nửa lớn hơn
    
    def add_num(self, num):
        """Time: O(log n)"""
        # Thêm vào max heap (nửa trái)
        heapq.heappush(self.max_heap, -num)
        
        # Đảm bảo mọi phần tử trong max_heap <= min_heap
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # Cân bằng kích thước 2 heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def find_median(self):
        """Time: O(1)"""
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# Test
mf = MedianFinder()
stream = [5, 15, 1, 3, 8]
for num in stream:
    mf.add_num(num)
    print(f"Added {num}, Median: {mf.find_median()}")
```

#### 6.5. Task Scheduler

```python
import heapq
from collections import Counter, deque

def least_interval(tasks, n):
    """
    Lập lịch task với cooling time
    Time: O(N) với N là số task
    """
    # Đếm số lần xuất hiện của mỗi task
    task_counts = Counter(tasks)
    
    # Max heap để chọn task có count lớn nhất
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)
    
    time = 0
    queue = deque()  # (count, available_time)
    
    while max_heap or queue:
        time += 1
        
        if max_heap:
            count = -heapq.heappop(max_heap)
            count -= 1
            
            if count > 0:
                # Task này cần làm lại, thêm vào queue
                queue.append((count, time + n))
        
        # Kiểm tra task nào đã sẵn sàng
        if queue and queue[0][1] == time:
            count, _ = queue.popleft()
            heapq.heappush(max_heap, -count)
    
    return time

# Test
tasks = ['A', 'A', 'A', 'B', 'B', 'B']
n = 2  # Cooling time
print(f"Minimum intervals: {least_interval(tasks, n)}")
```

---

### 7. Python heapq Module

Python cung cấp module `heapq` cho Min Heap:

```python
import heapq

# Tạo heap
heap = []

# Thêm phần tử
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)
print("Heap:", heap)  # [3, 5, 8]

# Lấy min
min_val = heapq.heappop(heap)
print("Min:", min_val)  # 3

# Build heap từ list
arr = [5, 7, 9, 1, 3]
heapq.heapify(arr)
print("Heapified:", arr)  # [1, 3, 9, 7, 5]

# N smallest/largest
arr = [3, 2, 1, 5, 6, 4]
print("3 smallest:", heapq.nsmallest(3, arr))  # [1, 2, 3]
print("3 largest:", heapq.nlargest(3, arr))    # [6, 5, 4]

# Replace (pop và push trong 1 operation)
heapq.heapreplace(heap, 10)

# Push và pop
heapq.heappushpop(heap, 2)

# Max Heap trick (dùng số âm)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
max_val = -heapq.heappop(max_heap)
print("Max:", max_val)  # 8
```

---

### 8. So sánh độ phức tạp

| Thao tác | Min/Max Heap | Binary Search Tree | Sorted Array |
|----------|--------------|-------------------|--------------|
| Insert | O(log n) | O(log n) avg, O(n) worst | O(n) |
| Extract Min/Max | O(log n) | O(log n) avg, O(n) worst | O(1) |
| Peek | O(1) | O(log n) avg, O(n) worst | O(1) |
| Search | O(n) | O(log n) avg, O(n) worst | O(log n) |
| Delete | O(log n) | O(log n) avg, O(n) worst | O(n) |
| Build | O(n) | O(n log n) | O(n log n) |

**Khi nào dùng Heap?**
- ✅ Cần extract min/max nhiều lần
- ✅ Priority Queue
- ✅ Tìm k largest/smallest elements
- ✅ Median trong stream
- ✅ Scheduling problems

**Khi nào không dùng Heap?**
- ❌ Cần search phần tử cụ thể (dùng BST)
- ❌ Cần duyệt theo thứ tự (dùng BST)
- ❌ Cần truy cập ngẫu nhiên (dùng array)

---

## Binary Search Tree 

### 1. Giới thiệu

#### 1.1. Khái niệm

**Binary Search Tree (BST)** là một cây nhị phân có tính chất đặc biệt:
- Tất cả các node trong cây con trái có giá trị **< node gốc**
- Tất cả các node trong cây con phải có giá trị **> node gốc**
- Cây con trái và cây con phải cũng là BST

**Ví dụ BST hợp lệ:**
```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \  /
      4  7 13
```

**Không phải BST:**
```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \  /
      4  9 13    <- 9 > 8, không thể ở cây con trái
```

#### 1.2. Tính chất quan trọng

**a) Duyệt Inorder cho thứ tự tăng dần:**
- Duyệt BST theo Inorder (Left-Root-Right) cho dãy số tăng dần
- Ví dụ trên: 1, 3, 4, 6, 7, 8, 10, 13, 14

**b) Tìm kiếm hiệu quả:**
- Có thể loại bỏ 1 nửa cây ở mỗi bước
- Average case: O(log n)
- Worst case: O(n) - cây thoái hóa thành linked list

**c) Dynamic data structure:**
- Dễ dàng insert và delete
- Không cần biết trước kích thước

#### 1.3. Ứng dụng

- **Database indexing:** B-Tree, B+ Tree (biến thể của BST)
- **File system:** Tổ chức thư mục
- **Expression parsing:** Cây biểu thức
- **Priority Queue:** Có thể implement bằng BST
- **Auto-complete:** Trie (dạng đặc biệt của cây)

---

### 2. Cấu trúc Node và BST

#### 2.1. Định nghĩa Node

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node({self.val})"
```

#### 2.2. Lớp BST

```python
class BST:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root is None
    
    def get_root(self):
        return self.root
```

---

### 3. Các thao tác cơ bản

#### 3.1. Search (Tìm kiếm)

```python
    def search(self, val):
        """
        Tìm node có giá trị val
        Time: O(h) với h là chiều cao cây
        Average: O(log n), Worst: O(n)
        """
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        # Base case
        if node is None or node.val == val:
            return node
        
        # Tìm trong cây con trái
        if val < node.val:
            return self._search_recursive(node.left, val)
        
        # Tìm trong cây con phải
        return self._search_recursive(node.right, val)
    
    # Cách 2: Iterative
    def search_iterative(self, val):
        """Tìm kiếm không đệ quy"""
        current = self.root
        
        while current is not None:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        
        return None
```

**Minh họa:**
```
Tìm 6 trong BST:
        8
       / \
      3   10
     / \    \
    1   6   14

Bước 1: 6 < 8, đi sang trái
Bước 2: 6 > 3, đi sang phải
Bước 3: 6 == 6, tìm thấy!
```

#### 3.2. Insert (Thêm node)

```python
    def insert(self, val):
        """
        Thêm node mới với giá trị val
        Time: O(h)
        """
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        # Nếu giá trị nhỏ hơn, chèn vào trái
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        
        # Nếu giá trị lớn hơn, chèn vào phải
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)
        
        # Nếu bằng, không làm gì (hoặc update)
    
    # Cách 2: Iterative
    def insert_iterative(self, val):
        """Thêm node không đệ quy"""
        new_node = TreeNode(val)
        
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif val > current.val:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                break  # Đã tồn tại
```

**Minh họa:**
```
Insert 5 vào BST:
        8
       / \
      3   10
     / \    \
    1   6   14

Bước 1: 5 < 8, đi trái
Bước 2: 5 > 3, đi phải
Bước 3: 5 < 6, chèn vào trái của 6

Kết quả:
        8
       / \
      3   10
     / \    \
    1   6   14
       /
      5
```

#### 3.3. Find Min và Find Max

```python
    def find_min(self, node=None):
        """
        Tìm node có giá trị nhỏ nhất
        Đi sang trái cho đến hết
        Time: O(h)
        """
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        while node.left is not None:
            node = node.left
        
        return node
    
    def find_max(self, node=None):
        """
        Tìm node có giá trị lớn nhất
        Đi sang phải cho đến hết
        Time: O(h)
        """
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        while node.right is not None:
            node = node.right
        
        return node
```

#### 3.4. Delete (Xóa node)

Xóa node là thao tác phức tạp nhất, có 3 trường hợp:

```python
    def delete(self, val):
        """
        Xóa node có giá trị val
        Time: O(h)
        """
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        # Base case
        if node is None:
            return None
        
        # Tìm node cần xóa
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Tìm thấy node cần xóa
            
            # Trường hợp 1: Node lá (không có con)
            if node.left is None and node.right is None:
                return None
            
            # Trường hợp 2a: Chỉ có con phải
            if node.left is None:
                return node.right
            
            # Trường hợp 2b: Chỉ có con trái
            if node.right is None:
                return node.left
            
            # Trường hợp 3: Có cả 2 con
            # Tìm successor (node nhỏ nhất trong cây con phải)
            successor = self.find_min(node.right)
            
            # Copy giá trị successor vào node hiện tại
            node.val = successor.val
            
            # Xóa successor
            node.right = self._delete_recursive(node.right, successor.val)
        
        return node
```

**Minh họa 3 trường hợp:**

**Trường hợp 1: Xóa node lá (1)**
```
Before:          After:
    8               8
   / \             / \
  3   10          3   10
 / \    \          \    \
1   6   14          6   14
```

**Trường hợp 2: Xóa node có 1 con (10)**
```
Before:          After:
    8               8
   / \             / \
  3   10          3   14
 / \    \        / \
1   6   14      1   6
```

**Trường hợp 3: Xóa node có 2 con (3)**
```
Before:          After:
    8               8
   / \             / \
  3   10          4   10
 / \    \        / \    \
1   6   14      1   6   14
   / \             /
  4  7            7

Bước 1: Tìm successor = 4 (min của cây con phải)
Bước 2: Copy 4 vào vị trí 3
Bước 3: Xóa 4 ở vị trí cũ
```

---

### 4. Các phép duyệt cây (Tree Traversal)

#### 4.1. Inorder Traversal (Left-Root-Right)

```python
    def inorder(self, node=None, result=None):
        """
        Duyệt Inorder: Trái - Gốc - Phải
        BST: cho thứ tự tăng dần
        """
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node is not None:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)
        
        return result
    
    # Iterative với stack
    def inorder_iterative(self):
        """Inorder không đệ quy"""
        result = []
        stack = []
        current = self.root
        
        while current or stack:
            # Đi sang trái hết cỡ
            while current:
                stack.append(current)
                current = current.left
            
            # Xử lý node
            current = stack.pop()
            result.append(current.val)
            
            # Đi sang phải
            current = current.right
        
        return result
```

#### 4.2. Preorder Traversal (Root-Left-Right)

```python
    def preorder(self, node=None, result=None):
        """
        Duyệt Preorder: Gốc - Trái - Phải
        Dùng để copy cây, serialize
        """
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node is not None:
            result.append(node.val)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        
        return result
    
    # Iterative
    def preorder_iterative(self):
        """Preorder không đệ quy"""
        if self.root is None:
            return []
        
        result = []
        stack = [self.root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push phải trước, trái sau (vì stack LIFO)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
```

#### 4.3. Postorder Traversal (Left-Right-Root)

```python
    def postorder(self, node=None, result=None):
        """
        Duyệt Postorder: Trái - Phải - Gốc
        Dùng để xóa cây, tính expression tree
        """
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node is not None:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)
        
        return result
```

#### 4.4. Level Order Traversal (BFS)

```python
    def level_order(self):
        """
        Duyệt theo từng level (BFS)
        Sử dụng queue
        """
        if self.root is None:
            return []
        
        from collections import deque
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    # Level by level
    def level_order_by_level(self):
        """Duyệt theo level, trả về list của list"""
        if self.root is None:
            return []
        
        from collections import deque
        
        result = []
        queue = deque([self.root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result
```

**Ví dụ các phép duyệt:**
```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \
      4  7

Inorder:    1, 3, 4, 6, 7, 8, 10, 14
Preorder:   8, 3, 1, 6, 4, 7, 10, 14
Postorder:  1, 4, 7, 6, 3, 14, 10, 8
Level Order: 8, 3, 10, 1, 6, 14, 4, 7
```

---

### 5. Các thao tác nâng cao

#### 5.1. Validate BST

```python
    def is_valid_bst(self):
        """
        Kiểm tra cây có phải BST hợp lệ không
        """
        def validate(node, min_val, max_val):
            if node is None:
                return True
            
            # Kiểm tra ràng buộc
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Kiểm tra đệ quy cây con
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(self.root, float('-inf'), float('inf'))
```

#### 5.2. Height của cây

```python
    def height(self, node=None):
        """
        Tính chiều cao của cây
        Chiều cao = số cạnh dài nhất từ root đến lá
        """
        if node is None:
            node = self.root
        
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return max(left_height, right_height) + 1
```

#### 5.3. Count nodes

```python
    def count_nodes(self, node=None):
        """Đếm số node trong cây"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
```

#### 5.4. Lowest Common Ancestor (LCA)

```python
    def lca(self, val1, val2):
        """
        Tìm node tổ tiên chung thấp nhất của 2 node
        """
        def find_lca(node, val1, val2):
            if node is None:
                return None
            
            # Cả 2 đều nhỏ hơn root, LCA ở bên trái
            if val1 < node.val and val2 < node.val:
                return find_lca(node.left, val1, val2)
            
            # Cả 2 đều lớn hơn root, LCA ở bên phải
            if val1 > node.val and val2 > node.val:
                return find_lca(node.right, val1, val2)
            
            # Một bên trái, một bên phải hoặc một trong hai là root
            return node
        
        return find_lca(self.root, val1, val2)
```

#### 5.5. Kth Smallest Element

```python
    def kth_smallest(self, k):
        """
        Tìm phần tử nhỏ thứ k
        Sử dụng inorder traversal
        """
        def inorder(node):
            if node is None:
                return
            
            # Duyệt trái
            inorder(node.left)
            
            # Xử lý node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # Duyệt phải
            inorder(node.right)
        
        self.count = 0
        self.result = None
        inorder(self.root)
        return self.result
```

#### 5.6. Range Sum

```python
    def range_sum(self, low, high):
        """
        Tính tổng các node có giá trị trong [low, high]
        """
        def sum_range(node):
            if node is None:
                return 0
            
            total = 0
            
            # Nếu node trong range
            if low <= node.val <= high:
                total += node.val
            
            # Tìm trong cây con trái nếu cần
            if node.val > low:
                total += sum_range(node.left)
            
            # Tìm trong cây con phải nếu cần
            if node.val < high:
                total += sum_range(node.right)
            
            return total
        
        return sum_range(self.root)
```

---

### 6. Ứng dụng thực tế

#### 6.1. Build BST từ Array

```python
def build_bst_from_array(arr):
    """Xây dựng BST từ mảng"""
    bst = BST()
    for val in arr:
        bst.insert(val)
    return bst

# Test
arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
bst = build_bst_from_array(arr)
print("Inorder:", bst.inorder())
```

#### 6.2. Build Balanced BST từ Sorted Array

```python
def sorted_array_to_bst(arr):
    """
    Xây dựng BST cân bằng từ mảng đã sắp xếp
    Chọn phần tử giữa làm root
    """
    def build(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(arr[mid])
        
        node.left = build(left, mid - 1)
        node.right = build(mid + 1, right)
        
        return node
    
    bst = BST()
    bst.root = build(0, len(arr) - 1)
    return bst

# Test
arr = [1, 2, 3, 4, 5, 6, 7]
bst = sorted_array_to_bst(arr)
print("Level order:", bst.level_order())  # [4, 2, 6, 1, 3, 5, 7]
```

#### 6.3. Serialize và Deserialize BST

```python
def serialize(root):
    """Chuyển BST thành string"""
    def preorder(node):
        if node is None:
            result.append('#')
            return
        result.append(str(node.val))
        preorder(node.left)
        preorder(node.right)
    
    result = []
    preorder(root)
    return ','.join(result)

def deserialize(data):
    """Xây dựng lại BST từ string"""
    def build():
        val = next(vals)
        if val == '#':
            return None
        
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node
    
    vals = iter(data.split(','))
    return build()

# Test
bst = build_bst_from_array([8, 3, 10, 1, 6, 14])
serialized = serialize(bst.root)
print("Serialized:", serialized)

root = deserialize(serialized)
bst2 = BST()
bst2.root = root
print("Inorder after deserialize:", bst2.inorder())
```

---

### 7. Phân tích độ phức tạp

| Thao tác | Average | Worst | Best |
|----------|---------|-------|------|
| Search | O(log n) | O(n) | O(1) |
| Insert | O(log n) | O(n) | O(1) |
| Delete | O(log n) | O(n) | O(1) |
| Find Min/Max | O(log n) | O(n) | O(1) |
| Inorder | O(n) | O(n) | O(n) |
| Space | O(n) | O(n) | O(n) |

**Worst case xảy ra khi:** Cây thoái hóa thành linked list (insert các phần tử đã sắp xếp)

```
Cây cân bằng:        Cây thoái hóa:
      4                   1
     / \                   \
    2   6                   2
   / \ / \                   \
  1  3 5  7                   3
                               \
                                4
Height: log n              Height: n
```

**Giải pháp:** Sử dụng **Self-balancing BST** như AVL Tree, Red-Black Tree

---

### 8. So sánh với các cấu trúc khác

| Cấu trúc | Search | Insert | Delete | Sorted | Space |
|----------|--------|--------|--------|--------|-------|
| Array (unsorted) | O(n) | O(1) | O(n) | ❌ | O(n) |
| Array (sorted) | O(log n) | O(n) | O(n) | ✅ | O(n) |
| Linked List | O(n) | O(1) | O(n) | ❌ | O(n) |
| BST | O(log n) | O(log n) | O(log n) | ✅ | O(n) |
| Hash Table | O(1) | O(1) | O(1) | ❌ | O(n) |

**Khi nào dùng BST?**
- ✅ Cần duy trì thứ tự sorted
- ✅ Cần range query (tìm trong khoảng)
- ✅ Cần tìm successor/predecessor
- ✅ Dynamic data (thêm/xóa thường xuyên)
- ✅ Cần kth smallest/largest

**Khi nào không dùng BST?**
- ❌ Chỉ cần search nhanh → Hash Table
- ❌ Truy cập theo index → Array
- ❌ Dữ liệu đã sắp xếp → Sorted Array

---

## Hash Table 

### 1. Giới thiệu

#### 1.1. Khái niệm

**Hash Table (Bảng băm)** là một cấu trúc dữ liệu cho phép lưu trữ và truy xuất dữ liệu với độ phức tạp trung bình **O(1)**. Hash Table sử dụng **hash function** để chuyển đổi key thành index trong mảng.

**Thành phần chính:**
- **Key:** Khóa duy nhất để truy cập giá trị
- **Value:** Giá trị được lưu trữ
- **Hash Function:** Hàm chuyển key thành index
- **Bucket/Slot:** Vị trí trong mảng để lưu cặp key-value

**Ví dụ:**
```
Key: "apple"  → Hash("apple") → Index: 5
Key: "banana" → Hash("banana") → Index: 2
Key: "cherry" → Hash("cherry") → Index: 8

Array: [_, _, "banana", _, _, "apple", _, _, "cherry", _]
Index:  0  1     2      3  4     5     6  7     8      9
```

#### 1.2. Hash Function

**Yêu cầu của hash function tốt:**
1. **Deterministic:** Cùng input luôn cho cùng output
2. **Uniform distribution:** Phân bố đều các key
3. **Fast to compute:** Tính toán nhanh O(1)
4. **Minimize collisions:** Giảm xung đột

**Các phương pháp hash phổ biến:**

**a) Division Method:**
```python
def hash_division(key, table_size):
    """h(k) = k mod m"""
    return key % table_size
```

**b) Multiplication Method:**
```python
def hash_multiplication(key, table_size):
    """h(k) = floor(m * (k*A mod 1))"""
    A = 0.6180339887  # (√5 - 1) / 2
    return int(table_size * ((key * A) % 1))
```

**c) String Hash (Polynomial Rolling Hash):**
```python
def hash_string(key, table_size):
    """Hash cho string"""
    hash_value = 0
    prime = 31
    
    for char in key:
        hash_value = (hash_value * prime + ord(char)) % table_size
    
    return hash_value
```

**d) Universal Hashing:**
```python
import random

def universal_hash(key, table_size):
    """Chọn ngẫu nhiên từ họ hash functions"""
    p = 1000000007  # Số nguyên tố lớn
    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)
    
    return ((a * key + b) % p) % table_size
```

#### 1.3. Collision (Xung đột)

**Collision xảy ra khi:** 2 key khác nhau có cùng hash value.

```
hash("apple") = 5
hash("avocado") = 5  ← Collision!
```

**Hai phương pháp xử lý collision chính:**
1. **Chaining (Open Hashing)**
2. **Open Addressing (Closed Hashing)**

---

### 2. Chaining (Separate Chaining)

#### 2.1. Ý tưởng

Mỗi slot trong bảng băm chứa một **linked list** (hoặc dynamic array) các phần tử có cùng hash value.

**Minh họa:**
```
Hash Table với Chaining:

Index 0: → [("apple", 5)]
Index 1: → []
Index 2: → [("banana", 3)] → [("blueberry", 7)]
Index 3: → [("cherry", 2)]
Index 4: → []
Index 5: → [("date", 8)] → [("durian", 9)]
```

#### 2.2. Cài đặt

```python
class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
    
    def hash_function(self, key):
        """Hash function đơn giản"""
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.size
            return hash_value
        return key % self.size
    
    def insert(self, key, value):
        """
        Thêm hoặc cập nhật key-value
        Time: O(1) average, O(n) worst
        """
        index = self.hash_function(key)
        
        # Kiểm tra key đã tồn tại chưa
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                # Update giá trị
                self.table[index][i] = (key, value)
                return
        
        # Thêm mới
        self.table[index].append((key, value))
        self.count += 1
        
        # Resize nếu load factor quá cao
        if self.load_factor() > 0.7:
            self._resize()
    
    def search(self, key):
        """
        Tìm giá trị theo key
        Time: O(1) average, O(n) worst
        """
        index = self.hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """
        Xóa key-value
        Time: O(1) average, O(n) worst
        """
        index = self.hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                self.count -= 1
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """Kiểm tra key có tồn tại không"""
        try:
            self.search(key)
            return True
        except KeyError:
            return False
    
    def load_factor(self):
        """Tính load factor = n / m"""
        return self.count / self.size
    
    def _resize(self):
        """Tăng kích thước bảng khi load factor cao"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        
        # Rehash tất cả phần tử
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
    
    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"Index {i}: {bucket}")
        return "\n".join(result) if result else "Empty hash table"
```

#### 2.3. Test Chaining

```python
# Test
ht = HashTableChaining(size=5)

# Insert
ht.insert("apple", 5)
ht.insert("banana", 3)
ht.insert("cherry", 2)
ht.insert("date", 8)
ht.insert("elderberry", 7)

print("Hash Table:")
print(ht)
print(f"\nLoad factor: {ht.load_factor():.2f}")

# Search
print(f"\nSearch 'apple': {ht.search('apple')}")
print(f"Contains 'grape': {ht.contains('grape')}")

# Update
ht.insert("apple", 10)
print(f"Updated 'apple': {ht.search('apple')}")

# Delete
ht.delete("banana")
print(f"\nAfter deleting 'banana':")
print(ht)
```

---

### 3. Open Addressing

#### 3.1. Ý tưởng

Khi collision xảy ra, tìm slot trống khác trong cùng bảng băm bằng **probing**.

**Các phương pháp probing:**
1. **Linear Probing:** h(k, i) = (h(k) + i) mod m
2. **Quadratic Probing:** h(k, i) = (h(k) + c₁·i + c₂·i²) mod m
3. **Double Hashing:** h(k, i) = (h₁(k) + i·h₂(k)) mod m

#### 3.2. Linear Probing

```python
class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
        self.DELETED = "DELETED"  # Marker cho phần tử đã xóa
    
    def hash_function(self, key):
        """Hash function"""
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.size
            return hash_value
        return key % self.size
    
    def insert(self, key, value):
        """
        Thêm key-value với linear probing
        Time: O(1) average
        """
        if self.load_factor() >= 0.7:
            self._resize()
        
        index = self.hash_function(key)
        original_index = index
        i = 0
        
        while self.table[index] is not None:
            # Nếu key đã tồn tại, update
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            # Linear probing
            i += 1
            index = (original_index + i) % self.size
            
            # Nếu đã duyệt hết bảng
            if i >= self.size:
                raise Exception("Hash table is full")
        
        # Tìm được slot trống
        self.table[index] = (key, value)
        self.count += 1
    
    def search(self, key):
        """
        Tìm giá trị theo key
        Time: O(1) average
        """
        index = self.hash_function(key)
        original_index = index
        i = 0
        
        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
            
            i += 1
            index = (original_index + i) % self.size
            
            if i >= self.size:
                break
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """
        Xóa key-value
        Đánh dấu DELETED thay vì xóa thật
        """
        index = self.hash_function(key)
        original_index = index
        i = 0
        
        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                value = self.table[index][1]
                self.table[index] = self.DELETED
                self.count -= 1
                return value
            
            i += 1
            index = (original_index + i) % self.size
            
            if i >= self.size:
                break
        
        raise KeyError(f"Key '{key}' not found")
    
    def load_factor(self):
        return self.count / self.size
    
    def _resize(self):
        """Resize bảng"""
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        
        for item in old_table:
            if item is not None and item != self.DELETED:
                self.insert(item[0], item[1])
    
    def __str__(self):
        result = []
        for i, item in enumerate(self.table):
            if item is not None and item != self.DELETED:
                result.append(f"Index {i}: {item}")
        return "\n".join(result) if result else "Empty hash table"
```

#### 3.3. Quadratic Probing

```python
class HashTableQuadraticProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def hash_function(self, key):
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.size
            return hash_value
        return key % self.size
    
    def insert(self, key, value):
        """
        Quadratic probing: h(k, i) = (h(k) + i²) mod m
        """
        index = self.hash_function(key)
        original_index = index
        i = 0
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            i += 1
            index = (original_index + i * i) % self.size
            
            if i >= self.size:
                raise Exception("Hash table is full")
        
        self.table[index] = (key, value)
        self.count += 1
```

#### 3.4. Double Hashing

```python
class HashTableDoubleHashing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def hash1(self, key):
        """Primary hash function"""
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.size
            return hash_value
        return key % self.size
    
    def hash2(self, key):
        """Secondary hash function"""
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 37 + ord(char))
            return 1 + (hash_value % (self.size - 1))
        return 1 + (key % (self.size - 1))
    
    def insert(self, key, value):
        """
        Double hashing: h(k, i) = (h1(k) + i*h2(k)) mod m
        """
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            i += 1
            index = (self.hash1(key) + i * step) % self.size
            
            if i >= self.size:
                raise Exception("Hash table is full")
        
        self.table[index] = (key, value)
        self.count += 1
```

---

### 4. So sánh Chaining vs Open Addressing

| Đặc điểm | Chaining | Open Addressing |
|----------|----------|-----------------|
| **Collision** | Dùng linked list | Tìm slot khác |
| **Memory** | Thêm memory cho pointers | Chỉ dùng array |
| **Load factor** | Có thể > 1 | Phải < 1 |
| **Cache** | Kém (pointers) | Tốt (locality) |
| **Delete** | Dễ | Phức tạp (cần marker) |
| **Resize** | Ít cần | Cần thường xuyên |
| **Performance** | Ổn định | Giảm khi đầy |

**Khi nào dùng:**
- **Chaining:** Không biết trước số phần tử, collision rate cao
- **Open Addressing:** Biết trước size, cần tối ưu cache

---

### 5. Ứng dụng thực tế

#### 5.1. Two Sum Problem

```python
def two_sum(nums, target):
    """
    Tìm 2 số có tổng = target
    Time: O(n), Space: O(n)
    """
    hash_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[num] = i
    
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

#### 5.2. Group Anagrams

```python
def group_anagrams(words):
    """
    Nhóm các từ là anagram của nhau
    Time: O(n * k log k) với k là độ dài từ
    """
    from collections import defaultdict
    
    anagram_map = defaultdict(list)
    
    for word in words:
        # Sort chữ cái làm key
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())

# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

#### 5.3. Longest Consecutive Sequence

```python
def longest_consecutive(nums):
    """
    Tìm độ dài dãy liên tiếp dài nhất
    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Chỉ bắt đầu từ đầu dãy
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Đếm độ dài
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

# Test
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 (1,2,3,4)
```

#### 5.4. LRU Cache

```python
class LRUCache:
    """
    Least Recently Used Cache
    Sử dụng Hash Table + Doubly Linked List
    """
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Dummy head và tail
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_front(self, node):
        """Thêm node vào đầu (sau head)"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Xóa node khỏi linked list"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key):
        """
        Get giá trị và đánh dấu recently used
        Time: O(1)
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Di chuyển lên đầu
        self._remove_node(node)
        self._add_to_front(node)
        
        return node.value
    
    def put(self, key, value):
        """
        Thêm/cập nhật key-value
        Time: O(1)
        """
        if key in self.cache:
            # Update
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_front(node)
        else:
            # Insert
            node = self.Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)
            
            # Evict nếu vượt capacity
            if len(self.cache) > self.capacity:
                # Xóa node cuối (least recently used)
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]

# Test
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)        # Evict key 2
print(cache.get(2))    # -1 (not found)
```

#### 5.5. Design HashMap

```python
class MyHashMap:
    """
    Custom HashMap implementation
    """
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        """Time: O(n/k) với k là số buckets"""
        index = self._hash(key)
        
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        
        self.buckets[index].append((key, value))
    
    def get(self, key):
        """Time: O(n/k)"""
        index = self._hash(key)
        
        for k, v in self.buckets[index]:
            if k == key:
                return v
        
        return -1
    
    def remove(self, key):
        """Time: O(n/k)"""
        index = self._hash(key)
        
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index].pop(i)
                return

# Test
hashmap = MyHashMap()
hashmap.put(1, 1)
hashmap.put(2, 2)
print(hashmap.get(1))    # 1
hashmap.put(2, 1)
print(hashmap.get(2))    # 1
hashmap.remove(2)
print(hashmap.get(2))    # -1
```

---

### 6. Python Dictionary

Python's `dict` là hash table được tối ưu cao:

```python
# Tạo dictionary
d = {}
d = dict()
d = {'apple': 5, 'banana': 3}

# Thao tác cơ bản
d['cherry'] = 2        # Insert/Update - O(1)
value = d['apple']     # Get - O(1)
del d['banana']        # Delete - O(1)
exists = 'apple' in d  # Contains - O(1)

# Methods
keys = d.keys()        # Tất cả keys
values = d.values()    # Tất cả values
items = d.items()      # Tất cả (key, value) pairs

# Get với default
value = d.get('grape', 0)  # Trả về 0 nếu không tìm thấy

# Duyệt
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# Counter
from collections import Counter
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
count = Counter(words)
print(count)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# DefaultDict
from collections import defaultdict
dd = defaultdict(int)  # Default value = 0
dd['apple'] += 1

dd_list = defaultdict(list)  # Default value = []
dd_list['fruits'].append('apple')
```

---

### 7. Phân tích độ phức tạp

| Thao tác | Average | Worst | Space |
|----------|---------|-------|-------|
| Insert | O(1) | O(n) | O(n) |
| Search | O(1) | O(n) | O(n) |
| Delete | O(1) | O(n) | O(n) |

**Worst case:** Khi tất cả keys hash về cùng index (collision)

**Load factor ảnh hưởng:**
- α < 0.7: Performance tốt
- α > 0.7: Nên resize

---

### 8. Khi nào dùng Hash Table?

**Nên dùng:**
- ✅ Cần lookup/insert/delete nhanh O(1)
- ✅ Không cần thứ tự
- ✅ Unique keys
- ✅ Counting, frequency
- ✅ Caching

**Không nên dùng:**
- ❌ Cần duy trì thứ tự → BST, Sorted Array
- ❌ Cần range query → BST
- ❌ Cần min/max → Heap
- ❌ Memory bị hạn chế → Array

---

## Graph Algorithms – Shortest Path

### 1. Giới thiệu về Graph (Đồ thị)

#### 1.1. Khái niệm cơ bản

**Graph (Đồ thị)** là một cấu trúc dữ liệu bao gồm:
- **Vertices (V):** Tập các đỉnh (nodes)
- **Edges (E):** Tập các cạnh kết nối các đỉnh

**Ký hiệu:** G = (V, E)

**Các loại graph:**

**a) Directed vs Undirected:**
```
Undirected:           Directed (Digraph):
    A --- B               A → B
    |     |               ↓   ↓
    C --- D               C → D
```

**b) Weighted vs Unweighted:**
```
Unweighted:           Weighted:
    A --- B               A --5-- B
    |     |               |       |
    C --- D               3       7
                          |       |
                          C --2-- D
```

**c) Connected vs Disconnected:**
```
Connected:            Disconnected:
    A --- B               A --- B    E --- F
    |     |                          
    C --- D               C --- D    
```

#### 1.2. Biểu diễn Graph

**a) Adjacency Matrix (Ma trận kề):**
```python
# Không gian: O(V²)
graph = [
    [0, 1, 1, 0],  # A kết nối với B, C
    [1, 0, 0, 1],  # B kết nối với A, D
    [1, 0, 0, 1],  # C kết nối với A, D
    [0, 1, 1, 0]   # D kết nối với B, C
]
```

**b) Adjacency List (Danh sách kề):**
```python
# Không gian: O(V + E)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Weighted graph
weighted_graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('D', 7)],
    'C': [('A', 3), ('D', 2)],
    'D': [('B', 7), ('C', 2)]
}
```

**So sánh:**

| Đặc điểm | Adjacency Matrix | Adjacency List |
|----------|------------------|----------------|
| Space | O(V²) | O(V + E) |
| Check edge (u,v) | O(1) | O(degree(u)) |
| Iterate neighbors | O(V) | O(degree(u)) |
| Add vertex | O(V²) | O(1) |
| Add edge | O(1) | O(1) |

---

### 2. Bài toán Shortest Path (Đường đi ngắn nhất)

**Phân loại:**

1. **Single Source Shortest Path (SSSP):**
   - Từ 1 đỉnh nguồn đến tất cả đỉnh khác
   - Algorithms: BFS, Dijkstra, Bellman-Ford

2. **All Pairs Shortest Path (APSP):**
   - Giữa mọi cặp đỉnh
   - Algorithm: Floyd-Warshall

**Đặc điểm:**
- **Unweighted:** BFS
- **Non-negative weights:** Dijkstra
- **Negative weights:** Bellman-Ford
- **Negative cycles:** Bellman-Ford (detect)

---

### 3. BFS (Breadth-First Search) - Unweighted

#### 3.1. Ý tưởng

BFS tìm đường đi ngắn nhất trong **unweighted graph** bằng cách duyệt theo từng level.

**Thuật toán:**
1. Dùng queue, bắt đầu từ đỉnh nguồn
2. Đánh dấu khoảng cách từ nguồn = 0
3. Duyệt các đỉnh kề, cập nhật khoảng cách
4. Lặp lại cho đến khi queue rỗng

#### 3.2. Cài đặt

```python
from collections import deque

def bfs_shortest_path(graph, start):
    """
    Tìm đường đi ngắn nhất từ start đến tất cả đỉnh
    Chỉ dùng cho unweighted graph
    Time: O(V + E), Space: O(V)
    """
    # Khởi tạo
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    parent = {vertex: None for vertex in graph}
    
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        # Duyệt các đỉnh kề
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)
    
    return distances, parent

def reconstruct_path(parent, start, end):
    """Tái tạo đường đi từ start đến end"""
    if parent[end] is None and start != end:
        return None  # Không có đường đi
    
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = parent[current]
    
    path.reverse()
    return path

# Test
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

distances, parent = bfs_shortest_path(graph, 'A')
print("Distances from A:", distances)
print("Path A to F:", reconstruct_path(parent, 'A', 'F'))
```

**Minh họa:**
```
Graph:
    A --- B --- D
    |     |
    C --- F --- E

BFS từ A:
Level 0: A (distance = 0)
Level 1: B, C (distance = 1)
Level 2: D, E, F (distance = 2)

Shortest paths from A:
A → B: 1
A → C: 1
A → D: 2 (A → B → D)
A → E: 2 (A → B → E)
A → F: 2 (A → C → F)
```

---

### 4. Dijkstra's Algorithm

#### 4.1. Ý tưởng

**Dijkstra** tìm đường đi ngắn nhất từ nguồn đến tất cả đỉnh trong **weighted graph với trọng số không âm**.

**Thuật toán (Greedy):**
1. Khởi tạo khoảng cách nguồn = 0, còn lại = ∞
2. Dùng min-heap (priority queue)
3. Chọn đỉnh có khoảng cách nhỏ nhất chưa xét
4. **Relaxation:** Cập nhật khoảng cách các đỉnh kề
5. Lặp lại cho đến khi tất cả đỉnh được xét

**Relaxation:**
```
if dist[u] + weight(u, v) < dist[v]:
    dist[v] = dist[u] + weight(u, v)
    parent[v] = u
```

#### 4.2. Cài đặt

```python
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm cho weighted graph
    Time: O((V + E) log V) với binary heap
    Space: O(V)
    
    graph: dict of dict
    graph[u][v] = weight of edge (u, v)
    """
    # Khởi tạo
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    parent = {vertex: None for vertex in graph}
    
    # Min heap: (distance, vertex)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # Đã xét rồi (vì có thể có nhiều entry trong heap)
        if current in visited:
            continue
        
        visited.add(current)
        
        # Không cần xét nếu distance đã lớn hơn
        if current_dist > distances[current]:
            continue
        
        # Relaxation
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, parent

# Test
weighted_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

distances, parent = dijkstra(weighted_graph, 'A')
print("\nDijkstra from A:")
for vertex in distances:
    print(f"A → {vertex}: {distances[vertex]}")
    path = reconstruct_path(parent, 'A', vertex)
    print(f"  Path: {' → '.join(path) if path else 'No path'}")
```

**Minh họa từng bước:**
```
Graph:
    A --4-- B --5-- D
    |  \    |  \    |  \
    2   1   1   8   2   6
    |    \  |    \  |    \
    C --8-- + --10- E --3-- F

Step by step từ A:

Initial: A=0, B=∞, C=∞, D=∞, E=∞, F=∞

1. Chọn A (dist=0)
   Relax: B=4, C=2
   Heap: [(2,C), (4,B)]

2. Chọn C (dist=2)
   Relax: B=min(4,2+1)=3, D=10, E=12
   Heap: [(3,B), (4,B), (10,D), (12,E)]

3. Chọn B (dist=3)
   Relax: D=min(10,3+5)=8
   Heap: [(4,B), (8,D), (10,D), (12,E)]

4. Chọn B (dist=4) - Skip (visited)

5. Chọn D (dist=8)
   Relax: E=min(12,8+2)=10, F=14
   Heap: [(10,D), (10,E), (12,E), (14,F)]

6. Chọn D (dist=10) - Skip

7. Chọn E (dist=10)
   Relax: F=min(14,10+3)=13
   Heap: [(12,E), (13,F), (14,F)]

8. Continue...

Final distances:
A → A: 0
A → B: 3 (A → C → B)
A → C: 2 (A → C)
A → D: 8 (A → C → B → D)
A → E: 10 (A → C → B → D → E)
A → F: 13 (A → C → B → D → E → F)
```

#### 4.3. Dijkstra với Path Reconstruction

```python
def dijkstra_with_path(graph, start, end):
    """
    Tìm đường đi ngắn nhất từ start đến end
    """
    distances, parent = dijkstra(graph, start)
    
    if distances[end] == float('inf'):
        return None, float('inf')
    
    path = reconstruct_path(parent, start, end)
    return path, distances[end]

# Test
path, dist = dijkstra_with_path(weighted_graph, 'A', 'F')
print(f"\nShortest path A → F: {' → '.join(path)}")
print(f"Distance: {dist}")
```

---

### 5. Bellman-Ford Algorithm

#### 5.1. Ý tưởng

**Bellman-Ford** tìm đường đi ngắn nhất từ nguồn trong **weighted graph có thể có trọng số âm**.

**Khác với Dijkstra:**
- ✅ Xử lý được trọng số âm
- ✅ Phát hiện được negative cycle
- ❌ Chậm hơn: O(VE) vs O((V+E) log V)

**Thuật toán:**
1. Khởi tạo distance nguồn = 0, còn lại = ∞
2. Lặp (V-1) lần:
   - Relax tất cả các cạnh
3. Kiểm tra negative cycle (lặp lần thứ V)

#### 5.2. Cài đặt

```python
def bellman_ford(graph, start):
    """
    Bellman-Ford algorithm
    Time: O(VE), Space: O(V)
    
    graph: list of edges [(u, v, weight)]
    Returns: (distances, parent, has_negative_cycle)
    """
    # Lấy tất cả vertices
    vertices = set()
    for u, v, _ in graph:
        vertices.add(u)
        vertices.add(v)
    
    # Khởi tạo
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    parent = {v: None for v in vertices}
    
    # Relax tất cả edges (V-1) lần
    for _ in range(len(vertices) - 1):
        updated = False
        
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parent[v] = u
                updated = True
        
        # Early termination nếu không có update
        if not updated:
            break
    
    # Kiểm tra negative cycle
    has_negative_cycle = False
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break
    
    return distances, parent, has_negative_cycle

# Test
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 3)
]

distances, parent, has_neg_cycle = bellman_ford(edges, 'A')
print("\nBellman-Ford from A:")
print(f"Has negative cycle: {has_neg_cycle}")
for vertex in sorted(distances.keys()):
    print(f"A → {vertex}: {distances[vertex]}")
```

#### 5.3. Phát hiện Negative Cycle

```python
def detect_negative_cycle(graph):
    """
    Phát hiện negative cycle trong graph
    """
    # Thử từ mỗi vertex (cho disconnected graph)
    vertices = set()
    for u, v, _ in graph:
        vertices.add(u)
        vertices.add(v)
    
    for start in vertices:
        _, _, has_cycle = bellman_ford(graph, start)
        if has_cycle:
            return True
    
    return False

# Test với negative cycle
edges_with_cycle = [
    ('A', 'B', 1),
    ('B', 'C', -3),
    ('C', 'A', 1)  # Cycle A→B→C→A có tổng = -1
]

print(f"\nHas negative cycle: {detect_negative_cycle(edges_with_cycle)}")
```

**Minh họa Negative Cycle:**
```
Graph with negative cycle:
    A --1-→ B
    ↑       |
    1       -3
    |       ↓
    +←------C

Cycle: A → B → C → A
Weight: 1 + (-3) + 1 = -1 (negative!)

Mỗi lần đi qua cycle, distance giảm → không có shortest path
```

---

### 6. Floyd-Warshall Algorithm (All Pairs)

#### 6.1. Ý tưởng

**Floyd-Warshall** tìm đường đi ngắn nhất giữa **mọi cặp đỉnh**.

**Dynamic Programming:**
- `dp[k][i][j]` = shortest path từ i đến j qua các đỉnh {1, 2, ..., k}
- `dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])`

**Có thể tối ưu:** Dùng 2D array thay vì 3D

#### 6.2. Cài đặt

```python
def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm
    Time: O(V³), Space: O(V²)
    
    graph: adjacency matrix (2D list)
    graph[i][j] = weight of edge (i, j)
    Use float('inf') for no edge
    """
    n = len(graph)
    
    # Copy graph để không thay đổi input
    dist = [row[:] for row in graph]
    
    # next[i][j] = đỉnh tiếp theo trên đường đi từ i đến j
    next_vertex = [[None] * n for _ in range(n)]
    
    # Khởi tạo next_vertex
    for i in range(n):
        for j in range(n):
            if graph[i][j] != float('inf') and i != j:
                next_vertex[i][j] = j
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]
    
    return dist, next_vertex

def reconstruct_path_floyd(next_vertex, i, j):
    """Tái tạo đường đi từ i đến j"""
    if next_vertex[i][j] is None:
        return None
    
    path = [i]
    while i != j:
        i = next_vertex[i][j]
        path.append(i)
    
    return path

# Test
INF = float('inf')
adj_matrix = [
    [0,   4,   2,   INF, INF, INF],  # A
    [4,   0,   1,   5,   INF, INF],  # B
    [2,   1,   0,   8,   10,  INF],  # C
    [INF, 5,   8,   0,   2,   6],    # D
    [INF, INF, 10,  2,   0,   3],    # E
    [INF, INF, INF, 6,   3,   0]     # F
]

dist, next_v = floyd_warshall(adj_matrix)

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
print("\nFloyd-Warshall (All Pairs):")
print("\nDistance Matrix:")
for i in range(len(vertices)):
    for j in range(len(vertices)):
        if dist[i][j] == INF:
            print("INF", end="\t")
        else:
            print(f"{dist[i][j]}", end="\t")
    print(f"  ({vertices[i]})")

# Ví dụ một vài đường đi
print("\nSample paths:")
for i in range(3):
    for j in range(3, 6):
        path = reconstruct_path_floyd(next_v, i, j)
        if path:
            path_str = ' → '.join(vertices[k] for k in path)
            print(f"{vertices[i]} → {vertices[j]}: {dist[i][j]} ({path_str})")
```

---

### 7. So sánh các thuật toán

| Algorithm | Graph Type | Time | Space | Negative Weight | Negative Cycle |
|-----------|-----------|------|-------|-----------------|----------------|
| BFS | Unweighted | O(V+E) | O(V) | N/A | N/A |
| Dijkstra | Non-negative weight | O((V+E)logV) | O(V) | ❌ | ❌ |
| Bellman-Ford | Any weight | O(VE) | O(V) | ✅ | Detect |
| Floyd-Warshall | Any weight | O(V³) | O(V²) | ✅ | Detect |

**Khi nào dùng:**
- **BFS:** Unweighted graph, đơn giản nhất
- **Dijkstra:** Weighted graph, không có cạnh âm, nhanh nhất
- **Bellman-Ford:** Có cạnh âm, hoặc cần detect negative cycle
- **Floyd-Warshall:** Cần tất cả cặp shortest paths, graph nhỏ

---

### 8. Ứng dụng thực tế

#### 8.1. Network Routing

```python
def find_shortest_route(network, source, destination):
    """
    Tìm tuyến đường ngắn nhất trong mạng
    network: weighted graph (router graph)
    """
    distances, parent = dijkstra(network, source)
    
    if distances[destination] == float('inf'):
        return None, "No route available"
    
    path = reconstruct_path(parent, source, destination)
    return path, distances[destination]
```

#### 8.2. Map Navigation (GPS)

```python
def gps_navigation(map_graph, start, end):
    """
    Tìm đường đi ngắn nhất trên bản đồ
    Có thể mở rộng với A* algorithm
    """
    path, distance = dijkstra_with_path(map_graph, start, end)
    
    if path is None:
        return "No route found"
    
    return {
        'path': path,
        'distance': distance,
        'estimated_time': distance / 60  # Giả sử 60km/h
    }
```

#### 8.3. Currency Arbitrage Detection

```python
def detect_arbitrage(exchange_rates):
    """
    Phát hiện cơ hội arbitrage trong tỷ giá
    Sử dụng negative cycle detection
    
    Chuyển đổi: weight = -log(exchange_rate)
    Negative cycle = arbitrage opportunity
    """
    import math
    
    edges = []
    for source, targets in exchange_rates.items():
        for target, rate in targets.items():
            # Chuyển multiplication thành addition
            weight = -math.log(rate)
            edges.append((source, target, weight))
    
    return detect_negative_cycle(edges)
```

#### 8.4. Network Delay Time

```python
def network_delay_time(times, n, k):
    """
    Thời gian để tín hiệu đến tất cả nodes
    times: [[u, v, w]] - từ u đến v mất w thời gian
    n: số nodes
    k: node nguồn
    """
    # Build graph
    graph = {i: {} for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u][v] = w
    
    # Dijkstra
    distances, _ = dijkstra(graph, k)
    
    # Max distance = thời gian cần
    max_dist = max(distances.values())
    
    return max_dist if max_dist != float('inf') else -1

# Test
times = [[2,1,1], [2,3,1], [3,4,1]]
print(f"Network delay: {network_delay_time(times, 4, 2)}")
```

#### 8.5. Cheapest Flights Within K Stops

```python
def cheapest_flights_k_stops(n, flights, src, dst, k):
    """
    Tìm chuyến bay rẻ nhất với tối đa k điểm dừng
    Modified Bellman-Ford
    """
    # prices[i] = chi phí rẻ nhất đến đỉnh i
    prices = [float('inf')] * n
    prices[src] = 0
    
    # Lặp k+1 lần (tối đa k stops)
    for _ in range(k + 1):
        temp_prices = prices.copy()
        
        for u, v, price in flights:
            if prices[u] != float('inf'):
                temp_prices[v] = min(temp_prices[v], prices[u] + price)
        
        prices = temp_prices
    
    return prices[dst] if prices[dst] != float('inf') else -1

# Test
flights = [[0,1,100], [1,2,100], [0,2,500]]
print(f"Cheapest: {cheapest_flights_k_stops(3, flights, 0, 2, 1)}")
```

---

### 9. Tối ưu hóa và Biến thể

#### 9.1. A* Algorithm

Cải tiến Dijkstra với heuristic function:

```python
def a_star(graph, start, goal, heuristic):
    """
    A* algorithm - Dijkstra + heuristic
    heuristic(node, goal) = ước lượng khoảng cách đến goal
    
    f(n) = g(n) + h(n)
    g(n) = cost từ start đến n
    h(n) = heuristic từ n đến goal
    """
    import heapq
    
    open_set = [(0 + heuristic(start, goal), 0, start)]
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal]
        
        for neighbor, weight in graph[current].items():
            tentative_g = current_g + weight
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
    
    return None, float('inf')
```

#### 9.2. Bidirectional Dijkstra

Chạy Dijkstra từ cả 2 phía (start và end):

```python
def bidirectional_dijkstra(graph, start, end):
    """
    Dijkstra từ cả 2 phía
    Nhanh hơn khi chỉ cần tìm 1 đường đi
    """
    # Implement tương tự Dijkstra nhưng:
    # - Chạy 2 searches song song
    # - Dừng khi 2 searches gặp nhau
    # - Kết hợp 2 paths
    pass
```
