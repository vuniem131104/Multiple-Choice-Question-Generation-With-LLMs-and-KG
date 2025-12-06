# Reinforcement Learning - Học Tăng Cường

## Markov Decision Processes - Quá Trình Quyết Định Markov

### 1. Giới thiệu về MDP

Quá trình Quyết định Markov (Markov Decision Process - MDP) là một framework toán học để mô hình hóa việc ra quyết định trong các tình huống mà kết quả có một phần ngẫu nhiên và một phần nằm dưới sự kiểm soát của người ra quyết định. MDP cung cấp nền tảng toán học cho hầu hết các bài toán học tăng cường.

### 2. Các thành phần cơ bản của MDP

Một MDP được định nghĩa bởi bộ năm phần tử (S, A, P, R, γ):

#### 2.1. Tập trạng thái (State Space - S)
- **Định nghĩa**: Tập hợp tất cả các trạng thái có thể mà agent có thể gặp trong môi trường
- **Ký hiệu**: S = {s₁, s₂, ..., sₙ}
- **Ví dụ**: Trong game cờ vua, mỗi trạng thái là một cấu hình cụ thể của bàn cờ

#### 2.2. Tập hành động (Action Space - A)
- **Định nghĩa**: Tập hợp tất cả các hành động mà agent có thể thực hiện
- **Ký hiệu**: A = {a₁, a₂, ..., aₘ}
- **Phân loại**:
  - Không gian hành động rời rạc: Số lượng hành động hữu hạn
  - Không gian hành động liên tục: Hành động có thể nhận giá trị trong một khoảng liên tục

#### 2.3. Hàm chuyển trạng thái (State Transition Function - P)
- **Định nghĩa**: Xác suất chuyển từ trạng thái s sang trạng thái s' khi thực hiện hành động a
- **Công thức**: P(s'|s,a) = P[Sₜ₊₁ = s' | Sₜ = s, Aₜ = a]
- **Tính chất Markov**: Trạng thái tương lai chỉ phụ thuộc vào trạng thái hiện tại, không phụ thuộc vào lịch sử

#### 2.4. Hàm phần thưởng (Reward Function - R)
- **Định nghĩa**: Phần thưởng nhận được khi thực hiện hành động a từ trạng thái s
- **Công thức**: R(s,a) hoặc R(s,a,s')
- **Mục đích**: Định hướng agent học hành vi tối ưu

#### 2.5. Hệ số chiết khấu (Discount Factor - γ)
- **Định nghĩa**: Hệ số để cân bằng giữa phần thưởng tức thời và phần thưởng dài hạn
- **Giá trị**: 0 ≤ γ ≤ 1
- **Ý nghĩa**:
  - γ = 0: Chỉ quan tâm đến phần thưởng tức thời
  - γ = 1: Phần thưởng tương lai có giá trị bằng phần thưởng hiện tại
  - 0 < γ < 1: Phần thưởng tương lai bị chiết khấu

### 3. Tính chất Markov

#### 3.1. Định nghĩa
Một quá trình được gọi là có tính chất Markov nếu:
```
P[Sₜ₊₁ | Sₜ] = P[Sₜ₊₁ | S₁, S₂, ..., Sₜ]
```

#### 3.2. Ý nghĩa
- Trạng thái hiện tại chứa đầy đủ thông tin để dự đoán tương lai
- Không cần phải nhớ toàn bộ lịch sử
- Đơn giản hóa việc tính toán và phân tích

### 4. Chính sách (Policy)

#### 4.1. Định nghĩa
Chính sách π là một hàm ánh xạ từ trạng thái đến hành động:
- **Chính sách xác định (Deterministic)**: π(s) = a
- **Chính sách ngẫu nhiên (Stochastic)**: π(a|s) = P[Aₜ = a | Sₜ = s]

#### 4.2. Phân loại
- **Chính sách tĩnh (Stationary)**: Không thay đổi theo thời gian
- **Chính sách động (Non-stationary)**: Thay đổi theo thời gian

### 5. Hàm giá trị (Value Functions)

#### 5.1. Hàm giá trị trạng thái (State-Value Function)
**Định nghĩa**: Tổng phần thưởng chiết khấu kỳ vọng khi bắt đầu từ trạng thái s và tuân theo chính sách π

```
Vᵖ(s) = Eᵖ[Gₜ | Sₜ = s]
      = Eᵖ[Σ(k=0 to ∞) γᵏRₜ₊ₖ₊₁ | Sₜ = s]
```

#### 5.2. Hàm giá trị hành động (Action-Value Function)
**Định nghĩa**: Tổng phần thưởng chiết khấu kỳ vọng khi bắt đầu từ trạng thái s, thực hiện hành động a, và sau đó tuân theo chính sách π

```
Qᵖ(s,a) = Eᵖ[Gₜ | Sₜ = s, Aₜ = a]
        = Eᵖ[Σ(k=0 to ∞) γᵏRₜ₊ₖ₊₁ | Sₜ = s, Aₜ = a]
```

#### 5.3. Mối quan hệ giữa V và Q
```
Vᵖ(s) = Σₐ π(a|s)Qᵖ(s,a)
Qᵖ(s,a) = R(s,a) + γ Σₛ' P(s'|s,a)Vᵖ(s')
```

### 6. Phương trình Bellman

#### 6.1. Phương trình Bellman cho Vᵖ
```
Vᵖ(s) = Σₐ π(a|s)[R(s,a) + γ Σₛ' P(s'|s,a)Vᵖ(s')]
```

**Giải thích**:
- Giá trị của một trạng thái bằng phần thưởng tức thời cộng với giá trị chiết khấu của trạng thái tiếp theo
- Đây là một phương trình đệ quy

#### 6.2. Phương trình Bellman cho Qᵖ
```
Qᵖ(s,a) = R(s,a) + γ Σₛ' P(s'|s,a) Σₐ' π(a'|s')Qᵖ(s',a')
```

#### 6.3. Phương trình Bellman tối ưu
```
V*(s) = maxₐ[R(s,a) + γ Σₛ' P(s'|s,a)V*(s')]
Q*(s,a) = R(s,a) + γ Σₛ' P(s'|s,a) maxₐ' Q*(s',a')
```

### 7. Chính sách tối ưu

#### 7.1. Định nghĩa
Chính sách π* được gọi là tối ưu nếu:
```
Vᵖ*(s) ≥ Vᵖ(s), ∀s ∈ S, ∀π
```

#### 7.2. Tính chất
- Luôn tồn tại ít nhất một chính sách tối ưu
- Tất cả các chính sách tối ưu đều có cùng hàm giá trị V*
- Chính sách tối ưu có thể được tìm từ Q*:
```
π*(s) = argmaxₐ Q*(s,a)
```

### 8. Các loại MDP đặc biệt

#### 8.1. Episodic MDP
- Có điểm kết thúc rõ ràng (terminal state)
- Ví dụ: Game cờ, robot đi mê cung

#### 8.2. Continuing MDP
- Không có điểm kết thúc
- Chạy vô hạn
- Ví dụ: Hệ thống kiểm soát nhiệt độ

#### 8.3. Finite MDP
- Tập trạng thái và hành động hữu hạn
- Dễ tính toán và phân tích

#### 8.4. Infinite MDP
- Tập trạng thái hoặc hành động vô hạn
- Cần các kỹ thuật xấp xỉ

### 9. Ví dụ minh họa: Robot đi mê cung

#### 9.1. Mô tả bài toán
- **Trạng thái**: Vị trí của robot trên lưới
- **Hành động**: Lên, xuống, trái, phải
- **Phần thưởng**: 
  - +10 khi đến đích
  - -1 cho mỗi bước di chuyển
  - -10 khi va vào tường
- **Mục tiêu**: Tìm đường đi ngắn nhất đến đích

#### 9.2. Biểu diễn MDP
```
S = {(x,y) | 0 ≤ x < width, 0 ≤ y < height, không phải tường}
A = {UP, DOWN, LEFT, RIGHT}
P(s'|s,a): Xác định bởi quy tắc di chuyển
R(s,a,s'): Như mô tả ở trên
γ = 0.9
```

### 10. Các thuật toán giải MDP

#### 10.1. Value Iteration
- Lặp lại cập nhật hàm giá trị cho đến khi hội tụ
- Đảm bảo tìm được nghiệm tối ưu

#### 10.2. Policy Iteration
- Xen kẽ giữa đánh giá chính sách và cải thiện chính sách
- Thường hội tụ nhanh hơn Value Iteration

#### 10.3. Linear Programming
- Biểu diễn bài toán dưới dạng quy hoạch tuyến tính
- Giải bằng các solver LP chuẩn

### 11. Ứng dụng thực tế

#### 11.1. Robot tự động
- Điều hướng và tránh vật cản
- Lập kế hoạch đường đi

#### 11.2. Quản lý tài nguyên
- Tối ưu hóa việc phân bổ tài nguyên
- Quản lý inventory

#### 11.3. Game AI
- Tạo ra đối thủ thông minh
- Cân bằng game

#### 11.4. Tài chính
- Tối ưu hóa portfolio
- Quản lý rủi ro

### 12. Thách thức và giới hạn

#### 12.1. Curse of dimensionality
- Số trạng thái tăng theo cấp số nhân với số chiều
- Khó giải quyết với không gian trạng thái lớn

#### 12.2. Môi trường không hoàn toàn quan sát được
- MDP chuẩn giả định biết hoàn toàn trạng thái
- Thực tế thường chỉ có quan sát một phần (POMDP)

#### 12.3. Mô hình không chính xác
- Giả định biết P và R
- Thực tế thường phải học từ tương tác

### 13. Kết luận

MDP cung cấp một framework toán học mạnh mẽ để mô hình hóa các bài toán ra quyết định tuần tự. Hiểu rõ các khái niệm cơ bản của MDP là nền tảng để nghiên cứu sâu hơn về học tăng cường, bao gồm các phương pháp model-free và deep reinforcement learning.

---

## Planning by Dynamic Programming - Lập Kế Hoạch Bằng Quy Hoạch Động

### 1. Giới thiệu về Dynamic Programming

#### 1.1. Định nghĩa
Dynamic Programming (DP) là một phương pháp giải quyết các bài toán phức tạp bằng cách chia nhỏ thành các bài toán con đơn giản hơn, giải quyết từng bài toán con một lần và lưu trữ kết quả để tái sử dụng.

#### 1.2. Điều kiện áp dụng DP
- **Optimal Substructure**: Nghiệm tối ưu có thể được xây dựng từ nghiệm tối ưu của các bài toán con
- **Overlapping Subproblems**: Các bài toán con được giải đi giải lại nhiều lần

#### 1.3. DP trong Reinforcement Learning
- Yêu cầu biết hoàn toàn mô hình MDP (model-based)
- Sử dụng phương trình Bellman để tính toán hàm giá trị
- Làm nền tảng cho các phương pháp học tăng cường khác

### 2. Policy Evaluation - Đánh Giá Chính Sách

#### 2.1. Mục tiêu
Tính toán hàm giá trị trạng thái V^π(s) cho một chính sách π cho trước.

#### 2.2. Phương trình Bellman cho Policy Evaluation
```
V^π(s) = Σ_a π(a|s)[R(s,a) + γ Σ_{s'} P(s'|s,a)V^π(s')]
```

#### 2.3. Thuật toán Iterative Policy Evaluation

**Bước 1: Khởi tạo**
```
V(s) = 0, ∀s ∈ S (hoặc giá trị ngẫu nhiên)
```

**Bước 2: Lặp cho đến khi hội tụ**
```
Lặp:
    Δ = 0
    Với mỗi s ∈ S:
        v = V(s)
        V(s) = Σ_a π(a|s)[R(s,a) + γ Σ_{s'} P(s'|s,a)V(s')]
        Δ = max(Δ, |v - V(s)|)
cho đến khi Δ < θ (ngưỡng hội tụ)
```

#### 2.4. Ví dụ: Gridworld 4x4

**Thiết lập**:
- Lưới 4x4 với 16 ô
- Ô góc trên trái và dưới phải là trạng thái kết thúc
- Chính sách: Di chuyển ngẫu nhiên đều (0.25 cho mỗi hướng)
- Phần thưởng: -1 cho mỗi bước
- γ = 1

**Quá trình hội tụ**:
```
Iteration 0: V(s) = 0 (∀s)
Iteration 1: V(s) = -1 (∀s không phải terminal)
Iteration 2: V(s) = -1.75 (các ô giữa)
...
Hội tụ sau ~100 iterations
```

#### 2.5. Độ phức tạp
- **Thời gian mỗi iteration**: O(|S|² × |A|)
- **Số lượng iterations**: Phụ thuộc vào γ và θ

### 3. Policy Improvement - Cải Thiện Chính Sách

#### 3.1. Policy Improvement Theorem

Nếu với mọi trạng thái s:
```
Q^π(s, π'(s)) ≥ V^π(s)
```
Thì chính sách π' tốt hơn hoặc bằng π:
```
V^{π'}(s) ≥ V^π(s), ∀s
```

#### 3.2. Greedy Policy Improvement

**Công thức**:
```
π'(s) = argmax_a Q^π(s,a)
      = argmax_a [R(s,a) + γ Σ_{s'} P(s'|s,a)V^π(s')]
```

**Ý nghĩa**: Chọn hành động tốt nhất theo hàm giá trị hiện tại

#### 3.3. Ví dụ: Cải thiện chính sách trong Gridworld

**Trước khi cải thiện** (chính sách ngẫu nhiên):
```
V^π = [-14, -20, -22, -20,
       -20, -22, -20, -14,
       -22, -20, -14,   0]
```

**Sau khi cải thiện** (chính sách tham lam):
- Chọn hướng di chuyển có V(s') cao nhất
- Luôn đi về phía trạng thái kết thúc

### 4. Policy Iteration - Lặp Chính Sách

#### 4.1. Thuật toán Policy Iteration

```
1. Khởi tạo:
   V(s) = 0, ∀s ∈ S
   π(s) = random, ∀s ∈ S

2. Lặp:
   a) Policy Evaluation:
      Tính V^π bằng iterative policy evaluation
   
   b) Policy Improvement:
      π' = greedy(V^π)
      
   c) Kiểm tra hội tụ:
      Nếu π' = π, dừng và trả về V^π và π
      Ngược lại, π = π' và quay lại bước 2a
```

#### 4.2. Tính chất của Policy Iteration

**Ưu điểm**:
- Luôn hội tụ đến chính sách tối ưu π*
- Thường hội tụ trong số lần lặp nhỏ (thường < 10)
- Đảm bảo cải thiện hoặc giữ nguyên chất lượng chính sách

**Nhược điểm**:
- Mỗi lần evaluation tốn nhiều thời gian
- Không hiệu quả với không gian trạng thái lớn

#### 4.3. Modified Policy Iteration

**Ý tưởng**: Không cần evaluation hoàn toàn, chỉ cần k bước:
```
Lặp k lần:
    V(s) = Σ_a π(a|s)[R(s,a) + γ Σ_{s'} P(s'|s,a)V(s')]
```

**Lợi ích**: Cân bằng giữa tốc độ hội tụ và độ chính xác

### 5. Value Iteration - Lặp Giá Trị

#### 5.1. Ý tưởng chính
Kết hợp policy evaluation và improvement thành một bước:
```
V(s) = max_a [R(s,a) + γ Σ_{s'} P(s'|s,a)V(s')]
```

#### 5.2. Thuật toán Value Iteration

```
1. Khởi tạo:
   V(s) = 0, ∀s ∈ S

2. Lặp cho đến khi hội tụ:
   Δ = 0
   Với mỗi s ∈ S:
      v = V(s)
      V(s) = max_a [R(s,a) + γ Σ_{s'} P(s'|s,a)V(s')]
      Δ = max(Δ, |v - V(s)|)
   
   Nếu Δ < θ: dừng

3. Trích xuất chính sách:
   π(s) = argmax_a [R(s,a) + γ Σ_{s'} P(s'|s,a)V(s')]
```

#### 5.3. Phân tích thuật toán

**Độ phức tạp thời gian**:
- Mỗi iteration: O(|S|² × |A|)
- Số iterations: O(log(1/(θ(1-γ))))

**Tốc độ hội tụ**:
- Phụ thuộc vào γ: γ càng nhỏ, hội tụ càng nhanh
- Không phụ thuộc vào chính sách khởi tạo

#### 5.4. Ví dụ: Gambler's Problem

**Mô tả bài toán**:
- Người chơi có $0-100
- Mỗi lần đặt cược $stake
- Thắng với xác suất p, được 2×stake
- Thua: mất stake
- Mục tiêu: Đạt $100

**Biểu diễn MDP**:
```
S = {0, 1, 2, ..., 100}
A(s) = {0, 1, ..., min(s, 100-s)}
R(s=100) = 1, R(other) = 0
γ = 1
```

**Kết quả**:
- Với p = 0.4: Đặt cược toàn bộ khi có ít tiền
- Với p = 0.55: Chiến lược bảo thủ hơn

### 6. So sánh Policy Iteration vs Value Iteration

#### 6.1. Bảng so sánh

| Tiêu chí | Policy Iteration | Value Iteration |
|----------|------------------|-----------------|
| Số bước mỗi iteration | Nhiều (evaluation đầy đủ) | 1 bước |
| Số iterations tổng | Ít (thường < 10) | Nhiều hơn |
| Thời gian mỗi iteration | Lâu | Nhanh |
| Tổng thời gian | Phụ thuộc bài toán | Phụ thuộc bài toán |
| Chính sách trung gian | Có thể sử dụng | Không có |

#### 6.2. Khi nào dùng phương pháp nào?

**Policy Iteration**:
- Khi cần chính sách tốt sớm trong quá trình
- Không gian hành động nhỏ
- Có thể dừng sớm khi chính sách đủ tốt

**Value Iteration**:
- Không gian hành động lớn
- Cần giải nhanh
- Chỉ quan tâm đến chính sách cuối cùng

### 7. Asynchronous Dynamic Programming

#### 7.1. Vấn đề của Synchronous DP
- Cập nhật tất cả trạng thái mỗi iteration
- Không hiệu quả với không gian trạng thái lớn
- Lãng phí tính toán cho trạng thái ít quan trọng

#### 7.2. In-Place Dynamic Programming

**Ý tưởng**: Sử dụng giá trị mới ngay khi tính được
```
Với mỗi s ∈ S:
    V(s) = max_a [R(s,a) + γ Σ_{s'} P(s'|s,a)V(s')]
```
(không cần lưu bản sao cũ của V)

**Lợi ích**: Hội tụ nhanh hơn, tiết kiệm bộ nhớ

#### 7.3. Prioritized Sweeping

**Ý tưởng**: Ưu tiên cập nhật các trạng thái quan trọng
```
1. Khởi tạo hàng đợi ưu tiên Q
2. Với mỗi s, tính:
   priority = |max_a[R(s,a) + γΣP(s'|s,a)V(s')] - V(s)|
3. Chọn s có priority cao nhất, cập nhật V(s)
4. Cập nhật priority cho các trạng thái tiền nhiệm
```

**Lợi ích**: Tập trung vào vùng quan trọng của không gian trạng thái

#### 7.4. Real-Time Dynamic Programming

**Đặc điểm**:
- Chỉ cập nhật các trạng thái mà agent thực sự gặp phải
- Phù hợp với bài toán có không gian trạng thái rất lớn
- Học trong quá trình tương tác

### 8. Generalized Policy Iteration (GPI)

#### 8.1. Khái niệm
GPI là framework chung cho nhiều thuật toán RL:
```
        Evaluation
       ↗          ↘
    Policy    ←→    Value
       ↖          ↙
       Improvement
```

#### 8.2. Đặc điểm
- Evaluation: Làm cho V nhất quán với π
- Improvement: Làm cho π tham lam theo V
- Hai quá trình cạnh tranh và hợp tác
- Cuối cùng hội tụ đến optimal

#### 8.3. Các biến thể
- **Policy Iteration**: Evaluation hoàn toàn trước improvement
- **Value Iteration**: 1 bước evaluation rồi improvement
- **Asynchronous DP**: Cập nhật không đồng bộ
- **Temporal-Difference Learning**: GPI với mẫu (phần sau)

### 9. Efficiency of Dynamic Programming

#### 9.1. Độ phức tạp tính toán

**Worst case**:
- Số states: n = |S|
- Số actions: k = |A|
- Độ phức tạp: O(n² × k) mỗi iteration

**So sánh với các phương pháp khác**:
- Linear Programming: O(n³) nhưng đảm bảo polynomial
- Policy Search: Exponential trong worst case
- DP: Polynomial, hiệu quả với medium-sized problems

#### 9.2. Curse of Dimensionality

**Vấn đề**:
- Số trạng thái tăng theo cấp số nhân với số chiều
- Ví dụ: Bàn cờ vây 19×19 có ~10^170 trạng thái

**Giải pháp**:
- Function approximation (phần sau)
- Sampling-based methods
- Hierarchical RL

### 10. Ví dụ thực tế: Car Rental Problem

#### 10.1. Mô tả bài toán
**Jack's Car Rental**:
- 2 địa điểm cho thuê xe
- Mỗi đêm có thể di chuyển tối đa 5 xe giữa 2 địa điểm
- Chi phí di chuyển: $2/xe
- Thu nhập thuê xe: $10/xe
- Số xe được thuê/trả theo phân phối Poisson

#### 10.2. Biểu diễn MDP
```
State: (n1, n2) - số xe tại mỗi địa điểm (0-20)
Action: -5 đến +5 (số xe di chuyển từ địa điểm 1 đến 2)
Reward: 10 × (số xe thuê được) - 2 × |action|
Transition: Theo phân phối Poisson
```

#### 10.3. Giải bằng Policy Iteration

**Chính sách khởi tạo**: Không di chuyển xe
**Sau iteration 1**: Di chuyển xe từ địa điểm thừa sang thiếu
**Hội tụ**: ~4-5 iterations
**Chính sách tối ưu**: Cân bằng số xe giữa 2 địa điểm

#### 10.4. Kết quả
```
V*(10,10) ≈ $500
Chiến lược: Luôn giữ ~10 xe mỗi địa điểm
```

### 11. Ví dụ thực tế: Inventory Management

#### 11.1. Bài toán quản lý kho

**Setup**:
- Tồn kho từ 0 đến MAX_INVENTORY
- Mỗi kỳ: Quyết định đặt hàng bao nhiêu
- Chi phí đặt hàng + chi phí lưu kho
- Doanh thu từ bán hàng
- Mất khách nếu hết hàng

#### 11.2. MDP Formulation
```
State: Mức tồn kho hiện tại
Action: Số lượng đặt hàng
Reward: Revenue - Ordering_cost - Holding_cost - Stockout_penalty
Transition: Stochastic demand
```

#### 11.3. Giải pháp
- Sử dụng Value Iteration
- Tìm chính sách (s,S): Đặt hàng đến mức S khi tồn kho ≤ s
- Optimize (s,S) parameters

### 12. Ưu điểm và hạn chế của Dynamic Programming

#### 12.1. Ưu điểm
✅ **Đảm bảo tối ưu**: Hội tụ đến chính sách tối ưu π*
✅ **Cơ sở lý thuyết vững chắc**: Dựa trên phương trình Bellman
✅ **Hiệu quả với medium-sized problems**: Polynomial complexity
✅ **Framework cho nhiều thuật toán khác**: Nền tảng cho TD, Q-learning

#### 12.2. Hạn chế
❌ **Yêu cầu biết hoàn toàn mô hình**: Cần biết P và R
❌ **Curse of dimensionality**: Không mở rộng cho không gian lớn
❌ **Cần duyệt tất cả trạng thái**: Không practical với continuous states
❌ **Computation cost**: Tốn nhiều tính toán mỗi iteration

### 13. Mở rộng và cải tiến

#### 13.1. Approximate Dynamic Programming
- Sử dụng function approximation
- Neural networks để biểu diễn V hoặc π
- Trade-off giữa accuracy và scalability

#### 13.2. Model-Free Methods
- Không cần biết P và R
- Học từ experience
- Temporal-Difference Learning, Q-Learning (phần sau)

#### 13.3. Deep Reinforcement Learning
- Kết hợp DP với deep learning
- DQN, Actor-Critic, PPO
- Giải quyết được bài toán phức tạp

### 14. Code Implementation - Ví dụ Python

#### 14.1. Policy Iteration
```python
def policy_iteration(env, gamma=0.9, theta=1e-6):
    # Khởi tạo
    V = np.zeros(env.num_states)
    policy = np.zeros(env.num_states, dtype=int)
    
    while True:
        # Policy Evaluation
        while True:
            delta = 0
            for s in range(env.num_states):
                v = V[s]
                a = policy[s]
                V[s] = sum([p * (r + gamma * V[s_]) 
                           for p, s_, r in env.transitions(s, a)])
                delta = max(delta, abs(v - V[s]))
            if delta < theta:
                break
        
        # Policy Improvement
        policy_stable = True
        for s in range(env.num_states):
            old_action = policy[s]
            # Tìm hành động tốt nhất
            action_values = []
            for a in range(env.num_actions):
                q_value = sum([p * (r + gamma * V[s_]) 
                              for p, s_, r in env.transitions(s, a)])
                action_values.append(q_value)
            policy[s] = np.argmax(action_values)
            
            if old_action != policy[s]:
                policy_stable = False
        
        if policy_stable:
            return V, policy
```

#### 14.2. Value Iteration
```python
def value_iteration(env, gamma=0.9, theta=1e-6):
    V = np.zeros(env.num_states)
    
    while True:
        delta = 0
        for s in range(env.num_states):
            v = V[s]
            # Bellman optimality update
            action_values = []
            for a in range(env.num_actions):
                q_value = sum([p * (r + gamma * V[s_]) 
                              for p, s_, r in env.transitions(s, a)])
                action_values.append(q_value)
            V[s] = max(action_values)
            delta = max(delta, abs(v - V[s]))
        
        if delta < theta:
            break
    
    # Trích xuất chính sách
    policy = np.zeros(env.num_states, dtype=int)
    for s in range(env.num_states):
        action_values = []
        for a in range(env.num_actions):
            q_value = sum([p * (r + gamma * V[s_]) 
                          for p, s_, r in env.transitions(s, a)])
            action_values.append(q_value)
        policy[s] = np.argmax(action_values)
    
    return V, policy
```

### 15. Bài tập thực hành

#### 15.1. Bài tập cơ bản
1. Implement policy evaluation cho Gridworld
2. So sánh tốc độ hội tụ của in-place và two-array DP
3. Visualize quá trình hội tụ của value iteration

#### 15.2. Bài tập nâng cao
1. Giải Gambler's Problem với các giá trị p khác nhau
2. Implement prioritized sweeping
3. Modified policy iteration với k=1, k=3, k=∞

#### 15.3. Dự án
1. Xây dựng AI cho game 2048 bằng DP
2. Tối ưu hóa việc sạc pin cho robot
3. Quản lý danh mục đầu tư bằng MDP

### 16. Kết luận

Dynamic Programming là nền tảng quan trọng trong Reinforcement Learning. Mặc dù có hạn chế về yêu cầu biết mô hình và curse of dimensionality, DP cung cấp:

- **Framework lý thuyết**: Hiểu rõ về optimal value functions và policies
- **Nền tảng thuật toán**: Cơ sở cho các phương pháp model-free
- **Công cụ thực tế**: Giải quyết được nhiều bài toán thực tế

Các khái niệm từ DP (đặc biệt là GPI và Bellman equations) sẽ xuất hiện xuyên suốt trong các phương pháp học tăng cường tiếp theo, từ Temporal-Difference Learning đến Deep Q-Networks.

---

## Model-Free Prediction - Dự Đoán Không Cần Mô Hình

### 1. Giới thiệu về Model-Free Learning

#### 1.1. Định nghĩa
Model-Free Learning là các phương pháp học tăng cường không yêu cầu biết trước mô hình môi trường (hàm chuyển trạng thái P và hàm phần thưởng R). Agent học trực tiếp từ kinh nghiệm tương tác với môi trường.

#### 1.2. So sánh Model-Based vs Model-Free

| Đặc điểm | Model-Based | Model-Free |
|----------|-------------|------------|
| Yêu cầu mô hình | Cần biết P và R | Không cần |
| Học từ | Phương trình Bellman | Kinh nghiệm thực tế |
| Ưu điểm | Hiệu quả dữ liệu | Linh hoạt, thực tế |
| Nhược điểm | Khó có mô hình chính xác | Cần nhiều dữ liệu |
| Ví dụ | DP, Model-Based RL | MC, TD, Q-Learning |

#### 1.3. Bài toán Prediction
**Mục tiêu**: Đánh giá một chính sách π cho trước
- Input: Chính sách π
- Output: Hàm giá trị V^π(s)
- Không cần biết mô hình môi trường

### 2. Monte Carlo Methods - Phương Pháp Monte Carlo

#### 2.1. Ý tưởng cơ bản
Monte Carlo (MC) ước lượng giá trị của trạng thái bằng cách lấy trung bình các return thực tế nhận được từ nhiều episodes.

**Nguyên lý**:
```
V^π(s) = E_π[G_t | S_t = s]
       ≈ average of returns từ trạng thái s
```

#### 2.2. Episode và Return

**Episode**: Một chuỗi hoàn chỉnh từ trạng thái ban đầu đến kết thúc
```
S_0, A_0, R_1, S_1, A_1, R_2, ..., S_T
```

**Return**: Tổng phần thưởng chiết khấu
```
G_t = R_{t+1} + γR_{t+2} + γ²R_{t+3} + ... + γ^{T-t-1}R_T
```

#### 2.3. First-Visit Monte Carlo

**Thuật toán**:
```
Khởi tạo:
    V(s) = 0, ∀s
    Returns(s) = danh sách rỗng, ∀s

Với mỗi episode:
    Tạo một episode tuân theo π: S_0, A_0, R_1, ..., S_T
    G = 0
    
    Với mỗi bước t = T-1, T-2, ..., 0:
        G = γG + R_{t+1}
        
        Nếu S_t xuất hiện lần đầu tiên trong episode:
            Thêm G vào Returns(S_t)
            V(S_t) = average(Returns(S_t))
```

**Đặc điểm**:
- Chỉ cập nhật cho lần xuất hiện đầu tiên của trạng thái
- Không có bias
- Đảm bảo hội tụ đến V^π(s) khi số episodes → ∞

#### 2.4. Every-Visit Monte Carlo

**Khác biệt**: Cập nhật cho mọi lần xuất hiện của trạng thái trong episode

```
Với mỗi bước t = T-1, T-2, ..., 0:
    G = γG + R_{t+1}
    Thêm G vào Returns(S_t)
    V(S_t) = average(Returns(S_t))
```

**So sánh**:
- Every-visit có variance thấp hơn
- Cả hai đều hội tụ đến V^π(s)
- Every-visit thường được sử dụng nhiều hơn

#### 2.5. Incremental Mean Update

**Vấn đề**: Lưu trữ tất cả returns không hiệu quả

**Giải pháp**: Cập nhật incremental
```
Công thức tổng quát:
    μ_k = μ_{k-1} + (1/k)(x_k - μ_{k-1})

Áp dụng cho MC:
    N(s) = N(s) + 1
    V(s) = V(s) + (1/N(s))(G - V(s))
    
Hoặc dùng learning rate α cố định:
    V(s) = V(s) + α(G - V(s))
```

**Lợi ích**:
- Tiết kiệm bộ nhớ
- Cập nhật online
- Quên dần các ước lượng cũ (với α cố định)

#### 2.6. Ví dụ: Blackjack

**Mô tả bài toán**:
- **Trạng thái**: (tổng bài của người chơi, bài úp của dealer, có ace không)
- **Hành động**: Hit (rút thêm) hoặc Stick (dừng)
- **Phần thưởng**: +1 thắng, -1 thua, 0 hòa
- **Chính sách**: Stick nếu tổng ≥ 20, ngược lại Hit

**Ứng dụng MC**:
1. Chơi nhiều games theo chính sách
2. Ghi lại returns cho mỗi trạng thái
3. Tính V^π bằng trung bình returns

**Kết quả**:
```
V^π(20, ACE, usable_ace) ≈ 0.8  (rất tốt)
V^π(12, 2, no_ace) ≈ -0.3       (tệ)
```

### 3. Temporal-Difference Learning (TD)

#### 3.1. Giới thiệu
TD Learning kết hợp ý tưởng của MC và DP:
- Như MC: Học từ kinh nghiệm, không cần mô hình
- Như DP: Bootstrap từ ước lượng hiện tại, không cần episode hoàn chỉnh

#### 3.2. TD(0) - Temporal Difference cơ bản

**TD Update Rule**:
```
V(S_t) = V(S_t) + α[R_{t+1} + γV(S_{t+1}) - V(S_t)]
```

**Các thành phần**:
- **TD Target**: R_{t+1} + γV(S_{t+1})
- **TD Error**: δ_t = R_{t+1} + γV(S_{t+1}) - V(S_t)
- **Update**: V(S_t) ← V(S_t) + α × δ_t

#### 3.3. Thuật toán TD(0)

```
Khởi tạo V(s) arbitrarily, ∀s ∈ S

Với mỗi episode:
    Khởi tạo S
    
    Lặp cho mỗi bước của episode:
        A ← hành động từ S theo π
        Thực hiện A, quan sát R, S'
        
        V(S) ← V(S) + α[R + γV(S') - V(S)]
        
        S ← S'
    cho đến khi S là terminal
```

#### 3.4. So sánh MC vs TD(0)

| Tiêu chí | Monte Carlo | TD(0) |
|----------|-------------|-------|
| Cập nhật | Cuối episode | Sau mỗi bước |
| Bootstrap | Không | Có |
| Target | G_t (actual return) | R + γV(S') |
| Bias | Unbiased | Biased |
| Variance | High variance | Low variance |
| Hội tụ | Chậm | Nhanh hơn |
| Môi trường | Cần episodic | Cả episodic và continuing |

#### 3.5. Ưu điểm của TD

✅ **Học online**: Cập nhật sau mỗi bước, không cần chờ episode kết thúc
✅ **Continuing tasks**: Hoạt động với tasks không có điểm kết thúc
✅ **Lower variance**: Bootstrap giảm variance so với MC
✅ **Học nhanh hơn**: Thường hội tụ nhanh hơn MC trong thực tế
✅ **Hiệu quả dữ liệu**: Sử dụng thông tin từ ước lượng hiện tại

#### 3.6. Ví dụ minh họa: Random Walk

**Setup**:
```
States: [A] [B] [C] [D] [E]
Start: C
Terminal: Left of A hoặc Right of E
Reward: 0 mọi nơi, +1 khi đến Right of E
Action: Left hoặc Right (random với p=0.5)
```

**True values**:
```
V^π(A) = 1/6, V^π(B) = 2/6, V^π(C) = 3/6,
V^π(D) = 4/6, V^π(E) = 5/6
```

**So sánh MC vs TD**:
- TD hội tụ nhanh hơn với cùng số episodes
- TD ít sensitive với khởi tạo
- MC có RMS error cao hơn trong giai đoạn đầu

### 4. Batch Methods và Certainty Equivalence

#### 4.1. Batch Learning
**Ý tưởng**: Lặp lại huấn luyện trên cùng một batch experience cho đến hội tụ

```
Cho trước batch experience: 
    {(S₁, A₁, R₁, S'₁), (S₂, A₂, R₂, S'₂), ...}

Lặp cho đến hội tụ:
    Với mỗi experience (S, A, R, S'):
        Cập nhật V(S) theo MC hoặc TD
```

#### 4.2. Certainty Equivalence

**MC**: Tìm V^π minimize mean-squared error với observed returns
```
V^π = argmin_V Σ_episodes Σ_t (G_t - V(S_t))²
```

**TD**: Tìm V^π thỏa mãn phương trình Bellman cho MDP ước lượng
```
V^π(s) = E[R + γV^π(S') | s]
```
(ước lượng từ experience)

**Kết quả**:
- TD tận dụng cấu trúc Markov
- MC chỉ minimize error, không exploit Markov property
- TD thường hiệu quả hơn trong môi trường Markov

#### 4.3. Ví dụ: AB Example

**Experience**:
```
A, 0, B, 0
B, 1 (terminal)
B, 1 (terminal)
B, 1 (terminal)
B, 1 (terminal)
B, 1 (terminal)
B, 0 (terminal)
```

**MC Estimate**:
- V(A) = 0 (chỉ có 1 episode từ A, return = 0)
- V(B) = 5/6 ≈ 0.83

**TD Estimate**:
- V(B) = 5/6 (từ data)
- V(A) = 5/6 (vì 100% chuyển đến B)

**TD tốt hơn**: Exploit structure, generalize better

### 5. Unified View: TD(λ)

#### 5.1. n-Step TD

**Ý tưởng**: Thay vì bootstrap sau 1 bước, sử dụng n bước

**n-Step Return**:
```
G_t^(n) = R_{t+1} + γR_{t+2} + ... + γ^{n-1}R_{t+n} + γ^n V(S_{t+n})
```

**Update**:
```
V(S_t) ← V(S_t) + α[G_t^(n) - V(S_t)]
```

**Đặc điểm**:
- n=1: TD(0)
- n=∞: Monte Carlo
- n trung gian: Cân bằng bias và variance

#### 5.2. TD(λ) - Eligibility Traces

**Motivation**: Thay vì chọn một n, kết hợp tất cả n-step returns

**λ-Return**:
```
G_t^λ = (1-λ) Σ_{n=1}^∞ λ^{n-1} G_t^(n)
```

**Eligibility Trace**:
```
E_0(s) = 0
E_t(s) = γλE_{t-1}(s) + 1(S_t = s)
```

**TD(λ) Update**:
```
δ_t = R_{t+1} + γV(S_{t+1}) - V(S_t)
V(s) ← V(s) + αδ_t E_t(s), ∀s
```

#### 5.3. Forward View vs Backward View

**Forward View**:
- Nhìn về tương lai
- Tính G_t^λ từ future returns
- Offline algorithm

**Backward View**:
- Nhìn về quá khứ
- Sử dụng eligibility traces
- Online algorithm
- Computationally efficient

**Quan hệ**: Hai view tương đương về mặt toán học

#### 5.4. Chọn λ

| λ | Đặc điểm | Khi nào dùng |
|---|----------|--------------|
| 0 | TD(0), low variance | Môi trường noisy |
| 0.5-0.9 | Cân bằng | Thường dùng nhất |
| 1 | MC, unbiased | Episodic, deterministic |

### 6. Các biến thể TD nâng cao

#### 6.1. Double Learning

**Vấn đề**: Maximization bias trong TD
```
Overestimation: E[max(X₁, X₂)] ≥ max(E[X₁], E[X₂])
```

**Giải pháp**: Duy trì 2 value functions
```
V₁(S) và V₂(S)

Update V₁:
    V₁(S) ← V₁(S) + α[R + γV₂(S') - V₁(S)]
    
Update V₂:
    V₂(S) ← V₂(S) + α[R + γV₁(S') - V₂(S)]
```

#### 6.2. Gradient TD

**Motivation**: TD không theo gradient descent thực sự

**True Gradient TD (TDC)**:
```
Minimize: MSBE = ||V - Π_T^π V||²

Update:
    w ← w + α(R + γV(S') - V(S))∇V(S)
    - αγ(∇V(S'))⊤w ∇V(S)
```

**Lợi ích**: Hội tụ vững vàng hơn với function approximation

### 7. Ứng dụng thực tế

#### 7.1. Game Playing

**TD-Gammon** (1992):
- Backgammon AI
- Sử dụng TD(λ) với neural network
- Self-play
- Đạt world-champion level

**AlphaGo Zero**:
- Sử dụng TD-style updates
- Self-play + MCTS
- Không cần human knowledge

#### 7.2. Robot Navigation

**Task**: Robot tìm đường trong môi trường chưa biết
- State: Vị trí robot
- Action: Di chuyển
- Reward: -1 mỗi bước, +100 khi đến đích

**Ưu điểm TD**:
- Học online trong quá trình điều hướng
- Không cần đợi đến đích mới cập nhật
- Adapt với môi trường thay đổi

#### 7.3. Resource Management

**Elevator Control**:
- State: Vị trí thang máy, yêu cầu chờ
- Action: Lên/xuống/đứng yên
- Reward: -1 × tổng thời gian chờ

**TD Learning**:
- Học value function cho mỗi trạng thái
- Online learning từ hoạt động hàng ngày
- Cải thiện liên tục

### 8. Phân tích lý thuyết

#### 8.1. Tốc độ hội tụ

**Monte Carlo**:
```
V_k(s) → V^π(s) với rate O(1/√k)
k: số episodes
```

**TD(0)**:
```
V_k(s) → V^π(s) nhanh hơn trong thực tế
Không có bound lý thuyết chặt chẽ
```

**Thực nghiệm**: TD thường nhanh hơn MC 2-10 lần

#### 8.2. Điều kiện hội tụ

**Robbins-Monro conditions** cho learning rate α_t:
```
Σ_{t=1}^∞ α_t = ∞     (đảm bảo hội tụ)
Σ_{t=1}^∞ α_t² < ∞    (đảm bảo variance hội tụ về 0)
```

**Ví dụ**:
- α_t = 1/t: Thỏa mãn
- α_t = 0.01: Không thỏa mãn điều kiện 1, nhưng practical

#### 8.3. Bias-Variance Tradeoff

**Monte Carlo**:
- Bias = 0 (ước lượng không chệch)
- Variance cao (phụ thuộc vào toàn bộ trajectory)

**TD(0)**:
- Bias > 0 (phụ thuộc vào V hiện tại)
- Variance thấp (chỉ phụ thuộc 1 bước)

**n-Step TD**: Cân bằng
```
Bias giảm khi n tăng
Variance tăng khi n tăng
```

### 9. So sánh tổng hợp

#### 9.1. Bảng so sánh đầy đủ

| Tiêu chí | MC | TD(0) | TD(λ) | DP |
|----------|----|----|-------|-----|
| Model-free | ✓ | ✓ | ✓ | ✗ |
| Bootstrap | ✗ | ✓ | ✓ | ✓ |
| Online | ✗ | ✓ | ✓ | ✓ |
| Episodic only | ✓ | ✗ | ✗ | ✗ |
| Bias | Low | High | Medium | Low |
| Variance | High | Low | Medium | Low |
| Convergence | Slow | Fast | Medium | Fastest |

#### 9.2. Khi nào dùng phương pháp nào?

**Monte Carlo**:
- Môi trường không Markov
- Cần ước lượng unbiased
- Episodic tasks ngắn

**TD(0)**:
- Môi trường Markov
- Continuing tasks
- Cần học nhanh
- Online learning

**TD(λ)**:
- Khi cần cân bằng bias-variance
- Credit assignment phức tạp
- Eligibility traces quan trọng

### 10. Code Implementation

#### 10.1. Monte Carlo First-Visit
```python
def monte_carlo_prediction(env, policy, num_episodes, gamma=0.99):
    V = defaultdict(float)
    returns = defaultdict(list)
    
    for _ in range(num_episodes):
        episode = generate_episode(env, policy)
        G = 0
        visited = set()
        
        # Duyệt ngược từ cuối episode
        for t in range(len(episode)-1, -1, -1):
            state, action, reward = episode[t]
            G = gamma * G + reward
            
            if state not in visited:
                returns[state].append(G)
                V[state] = np.mean(returns[state])
                visited.add(state)
    
    return V
```

#### 10.2. TD(0)
```python
def td_prediction(env, policy, num_episodes, alpha=0.1, gamma=0.99):
    V = defaultdict(float)
    
    for _ in range(num_episodes):
        state = env.reset()
        done = False
        
        while not done:
            action = policy(state)
            next_state, reward, done, _ = env.step(action)
            
            # TD update
            td_target = reward + gamma * V[next_state]
            td_error = td_target - V[state]
            V[state] += alpha * td_error
            
            state = next_state
    
    return V
```

#### 10.3. TD(λ) with Eligibility Traces
```python
def td_lambda_prediction(env, policy, num_episodes, 
                        alpha=0.1, gamma=0.99, lambda_=0.9):
    V = defaultdict(float)
    
    for _ in range(num_episodes):
        E = defaultdict(float)  # Eligibility traces
        state = env.reset()
        done = False
        
        while not done:
            action = policy(state)
            next_state, reward, done, _ = env.step(action)
            
            # TD error
            delta = reward + gamma * V[next_state] - V[state]
            
            # Update eligibility trace
            E[state] += 1
            
            # Update all states
            for s in E:
                V[s] += alpha * delta * E[s]
                E[s] *= gamma * lambda_
            
            state = next_state
    
    return V
```

### 11. Bài tập thực hành

#### 11.1. Bài tập cơ bản
1. Implement First-Visit MC cho Blackjack
2. So sánh MC vs TD(0) trên Random Walk
3. Visualize learning curves với different α

#### 11.2. Bài tập nâng cao
1. Implement n-step TD với n = 1, 3, 5, 10
2. Compare TD(λ) với λ = 0, 0.5, 0.9, 1.0
3. Analyze bias-variance tradeoff empirically

#### 11.3. Dự án
1. Build Tic-Tac-Toe AI với TD learning
2. Robot navigation trong gridworld phức tạp
3. Stock price prediction với TD methods

### 12. Kết luận

Model-Free Prediction giải quyết vấn đề quan trọng: **Đánh giá chính sách mà không cần biết mô hình môi trường**.

**Các phương pháp chính**:
- **Monte Carlo**: Đơn giản, unbiased, nhưng high variance
- **TD(0)**: Efficient, online, nhưng biased
- **TD(λ)**: Cân bằng tốt nhất, flexible

**Key insights**:
1. Bootstrap (TD) vs Full returns (MC) là tradeoff cơ bản
2. TD thường hiệu quả hơn trong môi trường Markov
3. Eligibility traces (TD(λ)) cung cấp spectrum liên tục
4. Lựa chọn phương pháp phụ thuộc vào đặc điểm bài toán

Phần tiếp theo sẽ mở rộng sang **Model-Free Control**: Không chỉ đánh giá mà còn tìm chính sách tối ưu mà không cần mô hình!

---

## Model-Free Control - Điều Khiển Không Cần Mô Hình

### 1. Giới thiệu về Model-Free Control

#### 1.1. Định nghĩa bài toán
**Control Problem**: Tìm chính sách tối ưu π* mà không biết trước mô hình môi trường (P, R)

**So sánh với Prediction**:
- Prediction: Đánh giá V^π cho π cho trước
- Control: Tối ưu hóa π để maximize V^π

#### 1.2. Thách thức
- Không biết mô hình → không thể dùng Dynamic Programming
- Phải học từ interaction với môi trường
- Cần cân bằng exploration và exploitation

#### 1.3. Ý tưởng chính
Sử dụng **Generalized Policy Iteration (GPI)** framework:
```
Policy Evaluation (Model-Free) → Policy Improvement → Repeat
```

### 2. Monte Carlo Control

#### 2.1. Từ V(s) sang Q(s,a)

**Vấn đề với V(s)**:
```
Policy Improvement cần:
π'(s) = argmax_a [R(s,a) + γ Σ_{s'} P(s'|s,a)V(s')]
                 ↑ Cần biết mô hình!
```

**Giải pháp**: Sử dụng Q(s,a)
```
π'(s) = argmax_a Q(s,a)  ← Không cần mô hình!
```

#### 2.2. Monte Carlo Policy Iteration

**Thuật toán**:
```
1. Khởi tạo:
   Q(s,a) = 0, ∀s,a
   π = chính sách khởi tạo

2. Lặp:
   a) Policy Evaluation (MC):
      - Tạo nhiều episodes theo π
      - Cập nhật Q^π(s,a) bằng MC
   
   b) Policy Improvement:
      π(s) = argmax_a Q(s,a), ∀s
```

#### 2.3. Vấn đề Exploration

**Greedy Policy**:
```
π(s) = argmax_a Q(s,a)
```
→ Chỉ exploit, không explore → Có thể bỏ lỡ chính sách tốt hơn

**Giải pháp 1: ε-Greedy Policy**
```
π(a|s) = {
    1 - ε + ε/|A|,  nếu a = argmax Q(s,a)
    ε/|A|,          ngược lại
}
```

**Đặc điểm**:
- Xác suất 1-ε: Chọn hành động tốt nhất (exploit)
- Xác suất ε: Chọn ngẫu nhiên (explore)
- ε decay theo thời gian: Explore nhiều lúc đầu, exploit nhiều sau

#### 2.4. ε-Greedy Monte Carlo Control

**Thuật toán**:
```
Khởi tạo:
    Q(s,a) arbitrarily, ∀s,a
    π = ε-greedy policy dựa trên Q
    Returns(s,a) = empty list, ∀s,a

Lặp forever:
    1. Tạo episode theo π:
       S_0, A_0, R_1, ..., S_T
    
    2. Với mỗi cặp (s,a) xuất hiện trong episode:
       G = return sau lần xuất hiện đầu tiên
       Thêm G vào Returns(s,a)
       Q(s,a) = average(Returns(s,a))
    
    3. Với mỗi s trong episode:
       π(s) = ε-greedy(Q(s,·))
```

#### 2.5. Greedy in the Limit of Infinite Exploration (GLIE)

**Định nghĩa**: Một dãy chính sách {π_t} thỏa mãn GLIE nếu:
1. Mọi cặp (s,a) được visit vô hạn lần
2. Chính sách hội tụ đến greedy policy

**Ví dụ GLIE**:
```
ε_t = 1/t
```

**Định lý**: GLIE Monte Carlo Control hội tụ đến π*

#### 2.6. Ví dụ: Blackjack với MC Control

**Setup**:
- State: (player_sum, dealer_card, usable_ace)
- Action: Hit hoặc Stick
- Reward: +1 (win), -1 (lose), 0 (draw)

**Kết quả**:
```
Chính sách học được:
- Stick khi player_sum ≥ 20
- Hit khi player_sum < 12
- Phức tạp hơn ở vùng 12-19 (phụ thuộc dealer card)
```

### 3. On-Policy vs Off-Policy Learning

#### 3.1. Định nghĩa

**On-Policy**:
- Học về chính sách π từ experience generated bởi π
- Evaluate và improve cùng một chính sách
- Ví dụ: SARSA, Monte Carlo Control

**Off-Policy**:
- Học về chính sách π (target) từ experience của μ (behavior)
- π ≠ μ
- Ví dụ: Q-Learning, Importance Sampling

#### 3.2. So sánh

| Đặc điểm | On-Policy | Off-Policy |
|----------|-----------|------------|
| Chính sách | Một chính sách | Hai chính sách |
| Sample efficiency | Thấp hơn | Cao hơn |
| Variance | Thấp | Cao |
| Converge | Ổn định | Có thể diverge |
| Use old data | Không | Có thể |
| Learn optimal | Không (nếu ε-greedy) | Có |

### 4. SARSA - On-Policy TD Control

#### 4.1. Ý tưởng
Áp dụng TD(0) cho Q(s,a) thay vì V(s)

**TD Update cho Q**:
```
Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γQ(S_{t+1}, A_{t+1}) - Q(S_t, A_t)]
```

**Tên gọi**: SARSA = (S, A, R, S', A')

#### 4.2. Thuật toán SARSA

```
Khởi tạo Q(s,a) arbitrarily, ∀s ∈ S, a ∈ A
Thiết lập α, ε

Lặp với mỗi episode:
    Khởi tạo S
    Chọn A từ S theo ε-greedy(Q)
    
    Lặp với mỗi bước:
        Thực hiện A, quan sát R, S'
        Chọn A' từ S' theo ε-greedy(Q)
        
        Q(S,A) ← Q(S,A) + α[R + γQ(S',A') - Q(S,A)]
        
        S ← S'; A ← A'
    cho đến S là terminal
```

#### 4.3. Tính chất của SARSA

**Hội tụ**:
- GLIE schedule + Robbins-Monro conditions → Q → Q*
- Trong thực tế, dùng ε nhỏ cố định hoặc decay

**On-Policy**:
- Học về chính sách ε-greedy đang dùng
- Safe: Tính đến exploration trong học

#### 4.4. Ví dụ: Windy Gridworld

**Mô tả**:
- Grid 7×10 với "wind" ở một số cột
- Wind đẩy agent lên 1-2 ô
- Start: (3,0), Goal: (3,7)
- Actions: 4 hướng

**Kết quả SARSA**:
- Học được đường đi tối ưu sau ~170 episodes
- Tận dụng wind để di chuyển nhanh hơn
- An toàn hơn Q-learning (tính đến exploration)

### 5. Q-Learning - Off-Policy TD Control

#### 5.1. Ý tưởng chính
Học về chính sách tham lam (greedy) trong khi hành động theo ε-greedy

**Q-Learning Update**:
```
Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γ max_a Q(S_{t+1}, a) - Q(S_t, A_t)]
                                            ↑ Greedy!
```

#### 5.2. Thuật toán Q-Learning

```
Khởi tạo Q(s,a) arbitrarily, ∀s,a
Thiết lập α, ε

Lặp với mỗi episode:
    Khởi tạo S
    
    Lặp với mỗi bước:
        Chọn A từ S theo ε-greedy(Q)  ← Behavior policy
        Thực hiện A, quan sát R, S'
        
        Q(S,A) ← Q(S,A) + α[R + γ max_a Q(S',a) - Q(S,A)]
                                   ↑ Target policy (greedy)
        
        S ← S'
    cho đến S là terminal
```

#### 5.3. So sánh SARSA vs Q-Learning

**SARSA Update**:
```
Q(S,A) ← Q(S,A) + α[R + γQ(S',A') - Q(S,A)]
                          ↑ A' theo ε-greedy
```

**Q-Learning Update**:
```
Q(S,A) ← Q(S,A) + α[R + γ max_a Q(S',a) - Q(S,A)]
                          ↑ Greedy choice
```

**Khác biệt**:
- SARSA: Conservative, tính đến exploration risk
- Q-Learning: Optimistic, học optimal ignoring exploration

#### 5.4. Cliff Walking Example

**Setup**:
```
[S] [ ] [ ] ... [ ] [G]
[ ] [ ] [ ] ... [ ] [ ]
[C] [C] [C] ... [C] [ ]
```
- S: Start, G: Goal, C: Cliff (reward = -100)
- Normal step: reward = -1

**Kết quả**:
- **Q-Learning**: Học đường ngắn nhất (sát cliff) nhưng thường rơi xuống khi explore
- **SARSA**: Học đường an toàn (xa cliff) vì tính đến khả năng explore
- **Performance**: SARSA tốt hơn trong training, Q-Learning tốt hơn nếu greedy

#### 5.5. Tính chất Q-Learning

**Hội tụ**:
- Đảm bảo hội tụ đến Q* với:
  - Mọi (s,a) được visit vô hạn lần
  - Learning rate thỏa mãn Robbins-Monro
- Không phụ thuộc vào behavior policy!

**Ưu điểm**:
✅ Học optimal policy
✅ Có thể tái sử dụng old experience
✅ Học từ demonstrations
✅ Simple và popular

**Nhược điểm**:
❌ Có thể không ổn định
❌ Overestimation bias
❌ Higher variance

### 6. Expected SARSA

#### 6.1. Ý tưởng
Thay vì sample A', lấy expectation theo policy

**Update Rule**:
```
Q(S,A) ← Q(S,A) + α[R + γ Σ_a π(a|S')Q(S',a) - Q(S,A)]
                          ↑ Expected value
```

**Với ε-greedy**:
```
Q(S,A) ← Q(S,A) + α[R + γ E_π[Q(S',·)] - Q(S,A)]

E_π[Q(S',·)] = Σ_a π(a|S')Q(S',a)
             = (1-ε)max_a Q(S',a) + ε · average_a Q(S',a)
```

#### 6.2. Thuật toán Expected SARSA

```
Khởi tạo Q(s,a) arbitrarily
Thiết lập α, ε

Lặp với mỗi episode:
    Khởi tạo S
    
    Lặp với mỗi bước:
        Chọn A từ S theo π (ví dụ: ε-greedy)
        Thực hiện A, quan sát R, S'
        
        expected_q = Σ_a π(a|S')Q(S',a)
        Q(S,A) ← Q(S,A) + α[R + γ·expected_q - Q(S,A)]
        
        S ← S'
    cho đến S là terminal
```

#### 6.3. Đặc điểm

**Ưu điểm**:
- Lower variance than SARSA (no sampling A')
- Có thể off-policy nếu behavior ≠ target
- Computational cost tăng nhưng thường đáng giá

**So sánh**:
- SARSA: Q(S,A) ← ... + γQ(S',A')  [sample]
- Expected SARSA: Q(S,A) ← ... + γE[Q(S',·)]  [expectation]
- Q-Learning: Q(S,A) ← ... + γmax_a Q(S',a)  [max]

### 7. Double Q-Learning

#### 7.1. Maximization Bias Problem

**Vấn đề**:
```
Q(s,a) = R(s,a) + γ max_a' Q(s',a')
              ↑ Overestimate!

E[max(X₁, X₂)] ≥ max(E[X₁], E[X₂])
```

**Hậu quả**: Q-Learning thường overestimate values

#### 7.2. Giải pháp: Double Q-Learning

**Ý tưởng**: Duy trì 2 Q-functions: Q₁ và Q₂

**Update**:
```
Với xác suất 0.5:
    A* = argmax_a Q₁(S',a)
    Q₁(S,A) ← Q₁(S,A) + α[R + γQ₂(S',A*) - Q₁(S,A)]
                                    ↑ Dùng Q₂ để estimate
Ngược lại:
    A* = argmax_a Q₂(S',a)
    Q₂(S,A) ← Q₂(S,A) + α[R + γQ₁(S',A*) - Q₂(S,A)]
                                    ↑ Dùng Q₁ để estimate
```

#### 7.3. Thuật toán Double Q-Learning

```
Khởi tạo Q₁(s,a) và Q₂(s,a) arbitrarily, ∀s,a
Thiết lập α, ε

Lặp với mỗi episode:
    Khởi tạo S
    
    Lặp với mỗi bước:
        Chọn A từ S theo ε-greedy(Q₁ + Q₂)
        Thực hiện A, quan sát R, S'
        
        Với xác suất 0.5:
            A* = argmax_a Q₁(S',a)
            Q₁(S,A) ← Q₁(S,A) + α[R + γQ₂(S',A*) - Q₁(S,A)]
        Ngược lại:
            A* = argmax_a Q₂(S',a)
            Q₂(S,A) ← Q₂(S,A) + α[R + γQ₁(S',A*) - Q₂(S,A)]
        
        S ← S'
    cho đến S là terminal
```

#### 7.4. Lợi ích
- Giảm overestimation bias
- Cải thiện stability và performance
- Nền tảng cho Double DQN (Deep RL)

### 8. n-Step Methods và Eligibility Traces

#### 8.1. n-Step SARSA

**n-Step Return**:
```
G_t^(n) = R_{t+1} + γR_{t+2} + ... + γ^{n-1}R_{t+n} + γ^n Q(S_{t+n}, A_{t+n})
```

**Update**:
```
Q(S_t, A_t) ← Q(S_t, A_t) + α[G_t^(n) - Q(S_t, A_t)]
```

#### 8.2. n-Step Q-Learning

**n-Step Return**:
```
G_t^(n) = R_{t+1} + γR_{t+2} + ... + γ^{n-1}R_{t+n} + γ^n max_a Q(S_{t+n}, a)
                                                            ↑ Max thay vì A_{t+n}
```

#### 8.3. SARSA(λ)

**Forward View**:
```
G_t^λ = (1-λ) Σ_{n=1}^∞ λ^{n-1} G_t^(n)
```

**Backward View với Eligibility Traces**:
```
E₀(s,a) = 0, ∀s,a

Với mỗi bước:
    δ_t = R_{t+1} + γQ(S_{t+1}, A_{t+1}) - Q(S_t, A_t)
    E_t(S_t, A_t) = E_{t-1}(S_t, A_t) + 1
    
    Với mọi s,a:
        Q(s,a) ← Q(s,a) + α·δ_t·E_t(s,a)
        E_t(s,a) ← γλ·E_{t-1}(s,a)
```

#### 8.4. Watkins's Q(λ)

**Đặc biệt**: Cut trace khi non-greedy action
```
Nếu A_t ≠ argmax_a Q(S_t, a):
    E_t(s,a) = 0, ∀s,a
```

**Lý do**: Maintain off-policy nature

### 9. Afterstates và Phương pháp nâng cao

#### 9.1. Afterstate Value Functions

**Ý tưởng**: Đánh giá trạng thái sau hành động (trước stochastic event)

**Ví dụ: Tic-Tac-Toe**:
```
State s → Action a → Afterstate s^a → Opponent move → s'
```

**Lợi ích**:
- Giảm số lượng state-action pairs
- Efficient learning
- Generalization tốt hơn

#### 9.2. Function Approximation Preview

**Vấn đề**: Tabular methods không scale với large state/action spaces

**Giải pháp**: Approximate Q(s,a) ≈ Q̂(s,a; w)
- Linear: Q̂(s,a; w) = w^T φ(s,a)
- Neural Networks: Q̂(s,a; θ)

### 10. Ứng dụng thực tế

#### 10.1. Robot Control

**Task**: Điều khiển tay robot gắp vật
- State: Joint angles, object position
- Action: Torque cho mỗi joint
- Reward: +1 nếu gắp thành công

**Method**: SARSA với function approximation
- Online learning
- Safe exploration quan trọng

#### 10.2. Game Playing

**Atari Games**:
- State: Screen pixels
- Action: Controller buttons
- Method: Deep Q-Networks (DQN)
- Base: Q-Learning + Deep Learning

#### 10.3. Autonomous Driving

**Lane Keeping**:
- State: Camera images, sensor data
- Action: Steering angle
- Method: Deep Q-Learning hoặc Policy Gradient
- Challenge: Safe exploration

### 11. So sánh tổng hợp các thuật toán

#### 11.1. Bảng so sánh

| Thuật toán | On/Off | Bootstrap | Target | Variance | Bias |
|------------|--------|-----------|--------|----------|------|
| MC Control | On | ✗ | G_t | High | Low |
| SARSA | On | ✓ | R + γQ(S',A') | Low | High |
| Q-Learning | Off | ✓ | R + γmax Q(S',·) | Medium | High |
| Expected SARSA | Both | ✓ | R + γE[Q(S',·)] | Low | High |
| Double Q-Learning | Off | ✓ | R + γQ₂(S',A*) | Medium | Lower |
| SARSA(λ) | On | ✓ | G_t^λ | Medium | Medium |

#### 11.2. Khi nào dùng thuật toán nào?

**Monte Carlo Control**:
- Episodic tasks
- Model-free
- Simple implementation

**SARSA**:
- Safe exploration quan trọng
- Online learning
- On-policy preferred

**Q-Learning**:
- Learn optimal policy
- Can reuse data
- Most popular choice

**Expected SARSA**:
- Reduce variance
- Small action space
- More stable than SARSA

**Double Q-Learning**:
- Overestimation is problem
- Critical applications
- Better performance often

### 12. Code Implementation

#### 12.1. SARSA
```python
def sarsa(env, num_episodes, alpha=0.1, gamma=0.99, epsilon=0.1):
    Q = defaultdict(lambda: np.zeros(env.action_space.n))
    
    for episode in range(num_episodes):
        state = env.reset()
        action = epsilon_greedy_policy(Q, state, epsilon)
        
        done = False
        while not done:
            next_state, reward, done, _ = env.step(action)
            next_action = epsilon_greedy_policy(Q, next_state, epsilon)
            
            # SARSA update
            td_target = reward + gamma * Q[next_state][next_action]
            td_error = td_target - Q[state][action]
            Q[state][action] += alpha * td_error
            
            state = next_state
            action = next_action
    
    return Q

def epsilon_greedy_policy(Q, state, epsilon):
    if np.random.random() < epsilon:
        return np.random.randint(len(Q[state]))
    else:
        return np.argmax(Q[state])
```

#### 12.2. Q-Learning
```python
def q_learning(env, num_episodes, alpha=0.1, gamma=0.99, epsilon=0.1):
    Q = defaultdict(lambda: np.zeros(env.action_space.n))
    
    for episode in range(num_episodes):
        state = env.reset()
        
        done = False
        while not done:
            # Behavior policy: ε-greedy
            action = epsilon_greedy_policy(Q, state, epsilon)
            next_state, reward, done, _ = env.step(action)
            
            # Q-Learning update (target policy: greedy)
            td_target = reward + gamma * np.max(Q[next_state])
            td_error = td_target - Q[state][action]
            Q[state][action] += alpha * td_error
            
            state = next_state
    
    return Q
```

#### 12.3. Double Q-Learning
```python
def double_q_learning(env, num_episodes, alpha=0.1, gamma=0.99, epsilon=0.1):
    Q1 = defaultdict(lambda: np.zeros(env.action_space.n))
    Q2 = defaultdict(lambda: np.zeros(env.action_space.n))
    
    for episode in range(num_episodes):
        state = env.reset()
        
        done = False
        while not done:
            # Action selection based on Q1 + Q2
            Q_combined = Q1[state] + Q2[state]
            action = epsilon_greedy_action(Q_combined, epsilon)
            
            next_state, reward, done, _ = env.step(action)
            
            # Randomly update Q1 or Q2
            if np.random.random() < 0.5:
                # Update Q1
                best_action = np.argmax(Q1[next_state])
                td_target = reward + gamma * Q2[next_state][best_action]
                Q1[state][action] += alpha * (td_target - Q1[state][action])
            else:
                # Update Q2
                best_action = np.argmax(Q2[next_state])
                td_target = reward + gamma * Q1[next_state][best_action]
                Q2[state][action] += alpha * (td_target - Q2[state][action])
            
            state = next_state
    
    return Q1, Q2
```

#### 12.4. Expected SARSA
```python
def expected_sarsa(env, num_episodes, alpha=0.1, gamma=0.99, epsilon=0.1):
    Q = defaultdict(lambda: np.zeros(env.action_space.n))
    
    for episode in range(num_episodes):
        state = env.reset()
        
        done = False
        while not done:
            action = epsilon_greedy_policy(Q, state, epsilon)
            next_state, reward, done, _ = env.step(action)
            
            # Calculate expected Q value
            policy_probs = epsilon_greedy_probs(Q[next_state], epsilon)
            expected_q = np.sum(policy_probs * Q[next_state])
            
            # Expected SARSA update
            td_target = reward + gamma * expected_q
            td_error = td_target - Q[state][action]
            Q[state][action] += alpha * td_error
            
            state = next_state
    
    return Q

def epsilon_greedy_probs(q_values, epsilon):
    probs = np.ones(len(q_values)) * epsilon / len(q_values)
    best_action = np.argmax(q_values)
    probs[best_action] += (1.0 - epsilon)
    return probs
```

### 13. Hyperparameter Tuning

#### 13.1. Learning Rate (α)
- **Quá cao**: Không ổn định, oscillate
- **Quá thấp**: Học chậm
- **Typical**: 0.01 - 0.5
- **Adaptive**: α_t = 1/t hoặc decay schedule

#### 13.2. Exploration Rate (ε)
- **Strategies**:
  - Constant: ε = 0.1
  - Decay: ε_t = ε_0 / t
  - Exponential: ε_t = ε_min + (ε_max - ε_min) × e^(-decay×t)
- **Typical**: Start 1.0, end 0.01

#### 13.3. Discount Factor (γ)
- **γ → 0**: Myopic (chỉ quan tâm immediate reward)
- **γ → 1**: Farsighted (quan tâm long-term)
- **Typical**: 0.9 - 0.99

### 14. Bài tập thực hành

#### 14.1. Bài tập cơ bản
1. Implement SARSA và Q-Learning cho GridWorld
2. Compare performance on Cliff Walking
3. Visualize Q-values và learned policies

#### 14.2. Bài tập nâng cao
1. Implement Double Q-Learning và compare với Q-Learning
2. Experiment với different ε-decay strategies
3. Compare n-step methods với n = 1, 3, 5

#### 14.3. Dự án
1. Build Taxi environment solver với Q-Learning
2. Implement SARSA(λ) với eligibility traces
3. Create game AI (Tic-Tac-Toe hoặc Connect Four)

### 15. Kết luận

Model-Free Control cho phép agent tìm chính sách tối ưu mà không cần biết mô hình môi trường - một breakthrough quan trọng trong RL.

**Key Takeaways**:

1. **Q-Function là chìa khóa**: Cho phép policy improvement mà không cần mô hình
2. **Exploration-Exploitation Tradeoff**: ε-greedy là giải pháp đơn giản và hiệu quả
3. **On-Policy vs Off-Policy**: Trade-off giữa stability và optimality
4. **SARSA vs Q-Learning**: Safe vs Optimal
5. **Variance Reduction**: Expected SARSA, Double Q-Learning cải thiện stability

**Chuẩn bị cho phần tiếp theo**:
- Tabular methods không scale với large state spaces
- Cần **Function Approximation** để xử lý continuous states
- Deep Q-Networks (DQN) sẽ kết hợp Q-Learning với Deep Learning!

---

## Value Function Approximation - Xấp Xỉ Hàm Giá Trị

### 1. Giới thiệu về Function Approximation

#### 1.1. Vấn đề với Tabular Methods

**Giới hạn của phương pháp bảng**:
- Lưu trữ V(s) hoặc Q(s,a) cho mọi trạng thái
- Không khả thi với không gian trạng thái lớn:
  - Backgammon: ~10²⁰ states
  - Go: ~10¹⁷⁰ states
  - Continuous states: Vô hạn
- Không có khả năng generalization

**Ví dụ**:
```
Tabular: 
- State 1: Q(s₁, a) = 5.2
- State 2: Q(s₂, a) = 4.8
- State 3: Q(s₃, a) = ???  ← Chưa thấy bao giờ

Function Approximation:
- Q(s, a) ≈ Q̂(s, a; w)
- Có thể ước lượng cho states chưa thấy
```

#### 1.2. Function Approximation Paradigm

**Ý tưởng**: Biểu diễn value function bằng parameterized function
```
V(s) ≈ V̂(s; w)
Q(s,a) ≈ Q̂(s,a; w)
π(a|s) ≈ π̂(a|s; θ)
```

**Lợi ích**:
✅ Xử lý được large/continuous state spaces
✅ Generalization: Học từ state này áp dụng cho state tương tự
✅ Compact representation: Ít parameters hơn states
✅ Efficient computation và storage

#### 1.3. Các loại Function Approximators

**Linear Methods**:
```
V̂(s; w) = w^T φ(s) = Σᵢ wᵢφᵢ(s)
```

**Non-linear Methods**:
- Polynomial features
- Radial Basis Functions (RBF)
- Neural Networks
- Decision Trees

**Deep Learning**:
- Deep Neural Networks (DNN)
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)

### 2. Linear Value Function Approximation

#### 2.1. Feature Vectors

**Định nghĩa**: Biểu diễn state s bằng feature vector φ(s)
```
s → φ(s) = [φ₁(s), φ₂(s), ..., φₙ(s)]^T
```

**Value Function Approximation**:
```
V̂(s; w) = w^T φ(s) = Σᵢ₌₁ⁿ wᵢφᵢ(s)
```

**Ví dụ: Gridworld**
```
Features cho position (x, y):
φ₁(s) = x
φ₂(s) = y
φ₃(s) = x²
φ₄(s) = y²
φ₅(s) = xy
φ₆(s) = 1  (bias)
```

#### 2.2. Feature Design

**Table Lookup (one-hot encoding)**:
```
φ(s) = [0, 0, ..., 1, ..., 0]^T
           ↑ vị trí tương ứng với s
```
→ Equivalent với tabular methods

**Tile Coding**:
- Chia state space thành nhiều overlapping tilings
- Mỗi tile là một binary feature
- Hiệu quả với continuous states

**Radial Basis Functions**:
```
φᵢ(s) = exp(-||s - cᵢ||² / (2σ²))
```
- cᵢ: center của basis function thứ i
- σ: width parameter

**Polynomial Features**:
```
φ(s) = [1, s₁, s₂, s₁², s₁s₂, s₂², ...]
```

#### 2.3. Objective Function

**Mean Squared Value Error (MSVE)**:
```
J(w) = E_π[(V^π(s) - V̂(s; w))²]
     = Σₛ d(s)(V^π(s) - V̂(s; w))²
```
- d(s): distribution của states dưới policy π

**Mục tiêu**: Minimize J(w) = ||V^π - V̂_w||²_d

### 3. Stochastic Gradient Descent (SGD)

#### 3.1. Gradient Descent

**Update Rule**:
```
w_{t+1} = w_t - (α/2)∇_w J(w_t)
        = w_t + α E[(V^π(s) - V̂(s; w))∇_w V̂(s; w)]
```

**Stochastic Gradient Descent**:
```
w_{t+1} = w_t + α[V^π(S_t) - V̂(S_t; w_t)]∇_w V̂(S_t; w_t)
```

#### 3.2. Linear SGD

**Gradient của linear function**:
```
∇_w V̂(s; w) = ∇_w(w^T φ(s)) = φ(s)
```

**Update rule**:
```
w_{t+1} = w_t + α[V^π(S_t) - V̂(S_t; w_t)]φ(S_t)
```

**Đặc điểm**:
- Converge đến local optimum (global cho linear)
- Learning rate α quan trọng
- Simple và efficient

#### 3.3. Feature Scaling

**Vấn đề**: Features có scale khác nhau → học không ổn định

**Giải pháp**:
```
Normalization: φᵢ = (φᵢ - μᵢ)/σᵢ
Standardization: φᵢ ∈ [0, 1]
```

### 4. Incremental Prediction Methods

#### 4.1. Monte Carlo với Function Approximation

**Update**:
```
w ← w + α[G_t - V̂(S_t; w)]∇_w V̂(S_t; w)
         ↑ Target: actual return
```

**Đặc điểm**:
- Unbiased target
- High variance
- Non-stationary target (G_t khác nhau mỗi episode)

#### 4.2. TD(0) với Function Approximation

**Update**:
```
w ← w + α[R_{t+1} + γV̂(S_{t+1}; w) - V̂(S_t; w)]∇_w V̂(S_t; w)
         ↑ TD target
```

**Semi-gradient**: Không lấy gradient qua V̂(S_{t+1}; w)

**Thuật toán Semi-gradient TD(0)**:
```
Khởi tạo w arbitrarily

Lặp với mỗi episode:
    Khởi tạo S
    
    Lặp với mỗi bước:
        A ← π(S)
        Thực hiện A, quan sát R, S'
        
        w ← w + α[R + γV̂(S'; w) - V̂(S; w)]∇_w V̂(S; w)
        
        S ← S'
    cho đến S là terminal
```

#### 4.3. TD(λ) với Function Approximation

**Eligibility Traces**:
```
z_0 = 0
z_t = γλz_{t-1} + ∇_w V̂(S_t; w)
```

**Update**:
```
δ_t = R_{t+1} + γV̂(S_{t+1}; w) - V̂(S_t; w)
w ← w + αδ_t z_t
```

**Accumulating vs Replacing traces**:
- Accumulating: z_t = γλz_{t-1} + ∇_w V̂(S_t; w)
- Replacing: Phức tạp hơn, phụ thuộc feature type

### 5. Control với Function Approximation

#### 5.1. Action-Value Function Approximation

**Parameterization**:
```
Q̂(s, a; w) = w^T φ(s, a)
```

**Features**:
- **Separate features**: φ(s, a) cho mỗi cặp (s,a)
- **State-action features**: Kết hợp φ_s và φ_a

#### 5.2. Semi-gradient SARSA

**Update Rule**:
```
w ← w + α[R + γQ̂(S', A'; w) - Q̂(S, A; w)]∇_w Q̂(S, A; w)
```

**Thuật toán**:
```
Khởi tạo w arbitrarily
Thiết lập ε

Lặp với mỗi episode:
    Khởi tạo S
    Chọn A từ S theo ε-greedy(Q̂(S, ·; w))
    
    Lặp với mỗi bước:
        Thực hiện A, quan sát R, S'
        Chọn A' từ S' theo ε-greedy(Q̂(S', ·; w))
        
        w ← w + α[R + γQ̂(S', A'; w) - Q̂(S, A; w)]∇_w Q̂(S, A; w)
        
        S ← S'; A ← A'
    cho đến S là terminal
```

#### 5.3. Semi-gradient Q-Learning

**Update Rule**:
```
w ← w + α[R + γ max_a Q̂(S', a; w) - Q̂(S, A; w)]∇_w Q̂(S, A; w)
```

**Thuật toán**:
```
Khởi tạo w arbitrarily

Lặp với mỗi episode:
    Khởi tạo S
    
    Lặp với mỗi bước:
        Chọn A từ S theo ε-greedy(Q̂(S, ·; w))
        Thực hiện A, quan sát R, S'
        
        w ← w + α[R + γ max_a Q̂(S', a; w) - Q̂(S, A; w)]∇_w Q̂(S, A; w)
        
        S ← S'
    cho đến S là terminal
```

#### 5.4. Ví dụ: Mountain Car

**Problem Setup**:
- State: (position, velocity)
- Action: {left, right, no-op}
- Reward: -1 per step
- Goal: Reach top of hill

**Features**: Tile coding với multiple tilings
```
φ(s, a) = tile_coding(position, velocity, action)
```

**Results với Semi-gradient SARSA**:
- Converge sau ~500 episodes
- Learned policy: Build momentum bằng oscillation

### 6. Convergence và Stability

#### 6.1. Convergence Guarantees

**Monte Carlo**:
- ✅ Converge đến local optimum
- ✅ Với linear FA: converge đến global optimum

**TD với Linear FA**:
- ✅ On-policy: Converge đến near-optimal
- ❌ Off-policy: Có thể diverge (deadly triad)

**Semi-gradient Methods**:
- Không follow true gradient
- Có thể không converge
- Nhưng thường work well trong thực tế

#### 6.2. Deadly Triad

**Ba yếu tố gây divergence**:
1. **Function Approximation**: Không phải tabular
2. **Bootstrapping**: TD-style updates
3. **Off-policy**: Behavior ≠ target policy

**Khi có cả 3**: Divergence có thể xảy ra

**Giải pháp**:
- Loại bỏ một trong ba yếu tố
- Sử dụng gradient TD methods
- Importance sampling
- Experience replay với target network (DQN)

#### 6.3. Baird's Counterexample

**Setup**: Simple MDP với linear FA và off-policy TD

**Kết quả**: Parameters diverge đến infinity!

**Ý nghĩa**: Cần cẩn thận với off-policy + FA + bootstrapping

### 7. Batch Methods

#### 7.1. Experience Replay

**Ý tưởng**: Lưu trữ và replay experiences
```
Replay Buffer D = {(s₁, a₁, r₁, s'₁), ..., (sₙ, aₙ, rₙ, s'ₙ)}

Mỗi update:
    Sample mini-batch từ D
    Perform SGD update
```

**Lợi ích**:
- Phá vỡ correlation giữa consecutive samples
- Tái sử dụng data hiệu quả
- Stabilize learning

#### 7.2. Least Squares Methods

**Least Squares TD (LSTD)**:
```
Tìm w minimize:
    E[(R + γV̂(S'; w) - V̂(S; w))²]

Closed-form solution:
    w = A^{-1}b
    A = Σ φ(s)(φ(s) - γφ(s'))^T
    b = Σ φ(s)r
```

**Đặc điểm**:
- Data efficient
- No learning rate
- Computationally expensive: O(n³)

#### 7.3. Fitted Q-Iteration

**Ý tưởng**: Regression trên Bellman targets
```
Lặp:
    1. Tính targets: yᵢ = rᵢ + γ max_a Q̂(s'ᵢ, a; w)
    2. Fit Q̂ để minimize: Σ(yᵢ - Q̂(sᵢ, aᵢ; w))²
```

**Batch Fitted Q-Iteration**:
```
Given dataset D = {(s, a, r, s')}

Khởi tạo Q̂₀ arbitrarily

Lặp k = 1, 2, ...:
    Với mỗi (s, a, r, s') trong D:
        y = r + γ max_{a'} Q̂_{k-1}(s', a')
    
    Q̂_k = argmin_Q Σ(y - Q(s, a))²
```

### 8. Deep Q-Networks (DQN)

#### 8.1. Neural Networks làm Function Approximators

**Architecture**:
```
Input: State s (hoặc raw observations như pixels)
Hidden Layers: Fully connected / Convolutional
Output: Q-values cho mỗi action
```

**Advantages**:
- Automatic feature learning
- Powerful representation capacity
- End-to-end training

#### 8.2. DQN Innovations

**1. Experience Replay**:
```
Replay Buffer D với capacity N
Store transitions: (s, a, r, s', done)
Sample random mini-batch để train
```

**2. Target Network**:
```
Q-network: Q(s, a; θ)
Target network: Q(s, a; θ⁻)

Update Q-network mỗi step
Copy θ → θ⁻ mỗi C steps
```

**TD Target**:
```
y = r + γ max_a Q(s', a; θ⁻)
         ↑ Dùng target network
```

#### 8.3. DQN Algorithm

```
Khởi tạo replay buffer D
Khởi tạo Q-network với random weights θ
Khởi tạo target network θ⁻ = θ

Lặp với mỗi episode:
    Khởi tạo state s
    
    Lặp với mỗi step:
        Chọn action a:
            - Với xác suất ε: random
            - Ngược lại: a = argmax_a Q(s, a; θ)
        
        Thực hiện a, quan sát r, s'
        Store transition (s, a, r, s', done) vào D
        
        Sample random mini-batch từ D
        Với mỗi (s_j, a_j, r_j, s'_j, done_j):
            y_j = r_j + γ(1 - done_j) max_a Q(s'_j, a; θ⁻)
        
        Perform SGD step trên (y_j - Q(s_j, a_j; θ))²
        
        Mỗi C steps: θ⁻ ← θ
        
        s ← s'
```

#### 8.4. DQN Improvements

**Double DQN**:
```
y = r + γQ(s', argmax_a Q(s', a; θ), θ⁻)
         ↑ Chọn action với θ    ↑ Evaluate với θ⁻
```
→ Giảm overestimation

**Dueling DQN**:
```
Q(s, a) = V(s) + A(s, a)
V(s): State value stream
A(s, a): Advantage stream
```
→ Better representation

**Prioritized Experience Replay**:
```
Priority = |TD error|
Sample theo priority thay vì uniform
```
→ Học từ important transitions

**Rainbow DQN**: Kết hợp tất cả improvements

### 9. Policy Approximation Preview

#### 9.1. Parameterized Policies

**Discrete Actions**:
```
π(a|s; θ) = softmax(preference(s, a; θ))
          = exp(h(s,a;θ)) / Σ_b exp(h(s,b;θ))
```

**Continuous Actions**:
```
π(a|s; θ) = N(μ(s; θ), σ(s; θ)²)
```

#### 9.2. Advantages của Policy Approximation

✅ Trực tiếp học policy
✅ Stochastic policies tự nhiên
✅ Hiệu quả với continuous actions
✅ Tốt với partially observable environments

### 10. Ứng dụng thực tế

#### 10.1. Atari Games

**DQN trên Atari**:
- Input: 84×84×4 grayscale frames
- CNN: 3 conv layers + 2 FC layers
- Output: Q-values cho 18 actions
- Training: 50M frames ≈ 38 days gameplay

**Kết quả**:
- Human-level performance trên 29/49 games
- Superhuman trên một số games (Breakout, Pong)

#### 10.2. Robotics

**Robot Manipulation**:
- State: Joint angles, end-effector pose, camera images
- Action: Joint velocities/torques
- FA: Deep networks để process visual input

**Challenges**:
- Sample efficiency
- Safe exploration
- Sim-to-real transfer

#### 10.3. Autonomous Systems

**Self-driving Cars**:
- State: Camera, LIDAR, GPS, sensors
- Action: Steering, acceleration, braking
- FA: CNN cho perception + FC cho control

### 11. Code Implementation

#### 11.1. Linear Function Approximation
```python
class LinearVFA:
    def __init__(self, num_features):
        self.w = np.zeros(num_features)
    
    def predict(self, features):
        """V̂(s) = w^T φ(s)"""
        return np.dot(self.w, features)
    
    def update(self, features, target, alpha):
        """w ← w + α[target - V̂(s)]φ(s)"""
        prediction = self.predict(features)
        self.w += alpha * (target - prediction) * features
        return prediction

def semi_gradient_td0(env, policy, vfa, num_episodes, 
                      alpha=0.01, gamma=0.99):
    for episode in range(num_episodes):
        state = env.reset()
        features = extract_features(state)
        
        done = False
        while not done:
            action = policy(state)
            next_state, reward, done, _ = env.step(action)
            next_features = extract_features(next_state)
            
            # TD target
            if done:
                target = reward
            else:
                target = reward + gamma * vfa.predict(next_features)
            
            # Update
            vfa.update(features, target, alpha)
            
            state = next_state
            features = next_features
    
    return vfa
```

#### 11.2. Tile Coding
```python
class TileCoding:
    def __init__(self, num_tilings, tiles_per_dim, 
                 state_ranges, num_actions):
        self.num_tilings = num_tilings
        self.tiles_per_dim = tiles_per_dim
        self.state_ranges = state_ranges
        self.num_actions = num_actions
        
        # Calculate feature vector size
        tiles_per_tiling = np.prod(tiles_per_dim)
        self.feature_size = num_tilings * tiles_per_tiling * num_actions
    
    def get_features(self, state, action):
        """Convert (state, action) to feature vector"""
        features = np.zeros(self.feature_size)
        
        for tiling_idx in range(self.num_tilings):
            # Offset for this tiling
            offset = np.random.uniform(0, 1, len(state)) / self.tiles_per_dim
            
            # Find tile indices
            tile_indices = []
            for i, (s, (low, high)) in enumerate(zip(state, self.state_ranges)):
                # Normalize and offset
                normalized = (s - low) / (high - low)
                offsetted = normalized + offset[i]
                # Find tile index
                tile_idx = int(offsetted * self.tiles_per_dim[i])
                tile_idx = np.clip(tile_idx, 0, self.tiles_per_dim[i] - 1)
                tile_indices.append(tile_idx)
            
            # Convert to linear index
            linear_idx = np.ravel_multi_index(tile_indices, self.tiles_per_dim)
            feature_idx = (tiling_idx * np.prod(self.tiles_per_dim) * 
                          self.num_actions + linear_idx * self.num_actions + action)
            features[feature_idx] = 1.0
        
        return features
```

#### 11.3. Simple Neural Network Q-Function
```python
import torch
import torch.nn as nn
import torch.optim as optim

class QNetwork(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, action_dim)
    
    def forward(self, state):
        x = torch.relu(self.fc1(state))
        x = torch.relu(self.fc2(x))
        q_values = self.fc3(x)
        return q_values

class DQNAgent:
    def __init__(self, state_dim, action_dim, lr=1e-3, gamma=0.99):
        self.q_network = QNetwork(state_dim, action_dim)
        self.target_network = QNetwork(state_dim, action_dim)
        self.target_network.load_state_dict(self.q_network.state_dict())
        
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=lr)
        self.gamma = gamma
    
    def select_action(self, state, epsilon=0.1):
        if np.random.random() < epsilon:
            return np.random.randint(self.q_network.fc3.out_features)
        else:
            with torch.no_grad():
                state_tensor = torch.FloatTensor(state).unsqueeze(0)
                q_values = self.q_network(state_tensor)
                return q_values.argmax().item()
    
    def train_step(self, batch):
        states, actions, rewards, next_states, dones = batch
        
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)
        
        # Current Q values
        current_q = self.q_network(states).gather(1, actions.unsqueeze(1))
        
        # Target Q values
        with torch.no_grad():
            next_q = self.target_network(next_states).max(1)[0]
            target_q = rewards + (1 - dones) * self.gamma * next_q
        
        # Loss
        loss = nn.MSELoss()(current_q.squeeze(), target_q)
        
        # Optimize
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        return loss.item()
    
    def update_target_network(self):
        self.target_network.load_state_dict(self.q_network.state_dict())
```

### 12. Best Practices

#### 12.1. Feature Engineering
- Normalize inputs: Mean 0, std 1
- Include relevant features
- Avoid irrelevant features (noise)
- Try different feature types

#### 12.2. Hyperparameters
- **Learning rate**: Start 1e-3 đến 1e-4
- **Batch size**: 32-256 cho DQN
- **Replay buffer**: 1e4 - 1e6 transitions
- **Target update**: Mỗi 1000-10000 steps

#### 12.3. Debugging
- Monitor TD error
- Visualize learned Q-values
- Check for divergence early
- Use simpler problems để test

### 13. Bài tập thực hành

#### 13.1. Bài tập cơ bản
1. Implement linear VFA cho Mountain Car
2. Compare tile coding vs polynomial features
3. Visualize learned value function

#### 13.2. Bài tập nâng cao
1. Implement mini DQN cho CartPole
2. Add Double DQN improvement
3. Experiment với network architectures

#### 13.3. Dự án
1. Build Atari game player với DQN
2. Implement Prioritized Experience Replay
3. Compare tabular Q-learning vs FA Q-learning

### 14. Kết luận

Value Function Approximation là bước đột phá cho phép RL scale lên bài toán thực tế với large/continuous state spaces.

**Key Takeaways**:

1. **Function Approximation**: Generalization thay vì memorization
2. **Linear Methods**: Simple, stable, nhưng limited expressiveness
3. **Neural Networks**: Powerful nhưng cần careful engineering
4. **DQN**: Breakthrough với experience replay + target network
5. **Stability**: Deadly triad cần được xử lý cẩn thận

**Convergence challenges**:
- Semi-gradient methods không follow true gradient
- Off-policy + FA + bootstrapping = risk of divergence
- Practical techniques (replay, target network) help significantly

**Tiếp theo**: **Policy Gradient Methods** - Học trực tiếp policy thay vì value function!

---

## Policy Gradient Methods - Phương Pháp Gradient Chính Sách

### 1. Giới thiệu về Policy Gradient

#### 1.1. Value-Based vs Policy-Based

**Value-Based Methods** (Q-Learning, DQN):
```
Học Q(s,a) → Derive policy: π(s) = argmax_a Q(s,a)
```
- Indirect: Học value rồi suy ra policy
- Deterministic policies
- Khó với continuous actions

**Policy-Based Methods**:
```
Học trực tiếp π(a|s; θ)
```
- Direct: Parameterize và optimize policy
- Stochastic policies tự nhiên
- Hiệu quả với continuous actions

#### 1.2. Ưu điểm của Policy Gradient

✅ **Continuous action spaces**: Không cần discretization
✅ **Stochastic policies**: Tự nhiên cho exploration và game theory
✅ **Better convergence**: Smooth optimization landscape
✅ **Effective in high dimensions**: Especially với function approximation
✅ **Learn policies directly**: Không qua intermediate value function

#### 1.3. Nhược điểm

❌ **High variance**: Gradient estimates có variance cao
❌ **Sample inefficient**: Cần nhiều samples
❌ **Local optima**: Có thể stuck tại local optima
❌ **Slow convergence**: Thường chậm hơn value-based

### 2. Policy Parameterization

#### 2.1. Discrete Action Spaces

**Softmax Policy** (Gibbs/Boltzmann):
```
π(a|s; θ) = exp(h(s,a;θ)) / Σ_b exp(h(s,b;θ))
```

**Linear Preferences**:
```
h(s,a;θ) = θ^T φ(s,a)
```

**Neural Network**:
```
Input: State s
Hidden Layers: Neural network
Output: Logits h(s,a;θ)
Policy: π(a|s;θ) = softmax(h(s,·;θ))
```

#### 2.2. Continuous Action Spaces

**Gaussian Policy**:
```
π(a|s; θ) = N(μ(s;θ), σ²)

a ~ N(μ(s;θ), σ²)
```

**Parameterization**:
```
μ(s;θ) = θ^T φ(s)  [Linear]
μ(s;θ) = NN(s;θ)   [Neural Network]

σ có thể:
- Fixed constant
- State-dependent: σ(s;θ)
- Action-dependent
```

**Beta Distribution** (bounded actions):
```
a ∈ [0, 1]
π(a|s;θ) = Beta(α(s;θ), β(s;θ))
```

#### 2.3. Ví dụ minh họa

**CartPole** (Discrete):
```python
class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.fc1 = nn.Linear(state_dim, 128)
        self.fc2 = nn.Linear(128, action_dim)
    
    def forward(self, state):
        x = F.relu(self.fc1(state))
        logits = self.fc2(x)
        return F.softmax(logits, dim=-1)
```

**Continuous Control**:
```python
class GaussianPolicy(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.fc1 = nn.Linear(state_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.mean = nn.Linear(128, action_dim)
        self.log_std = nn.Parameter(torch.zeros(action_dim))
    
    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        mean = self.mean(x)
        std = torch.exp(self.log_std)
        return mean, std
```

### 3. Policy Gradient Theorem

#### 3.1. Objective Function

**Mục tiêu**: Maximize expected return
```
J(θ) = E_τ~π_θ[G_τ] = E[Σ_t γ^t R_t]
```

Hoặc với episodic tasks:
```
J(θ) = V^π_θ(s_0) = E_π_θ[G_0 | S_0 = s_0]
```

#### 3.2. Policy Gradient Theorem

**Định lý**:
```
∇_θ J(θ) = E_π_θ[∇_θ log π(A|S;θ) Q^π(S,A)]
         = E_π_θ[∇_θ log π(A|S;θ) G_t]
```

**Giải thích**:
- ∇_θ log π(A|S;θ): Score function (hướng tăng probability của action)
- Q^π(S,A): Weighting (actions tốt được tăng, xấu giảm)

#### 3.3. REINFORCE Algorithm

**Monte Carlo Policy Gradient**:
```
Khởi tạo θ
Thiết lập learning rate α

Lặp:
    Tạo episode theo π(·|·;θ): S_0, A_0, R_1, ..., S_T
    
    Với mỗi bước t:
        G_t = Σ_{k=t}^T γ^{k-t} R_k
        θ ← θ + α γ^t G_t ∇_θ log π(A_t|S_t;θ)
```

**Intuition**:
- Nếu G_t > 0: Tăng probability của actions đã chọn
- Nếu G_t < 0: Giảm probability
- Magnitude tỷ lệ với |G_t|

#### 3.4. REINFORCE với Baseline

**Vấn đề**: High variance trong gradient estimates

**Giải pháp**: Subtract baseline b(s)
```
∇_θ J(θ) = E[∇_θ log π(A|S;θ) (G_t - b(S_t))]
```

**Baseline phổ biến**: V^π(s)
```
Advantage: A^π(s,a) = Q^π(s,a) - V^π(s)
∇_θ J(θ) = E[∇_θ log π(A|S;θ) A^π(S,A)]
```

**Thuật toán**:
```
Khởi tạo θ, w (cho value function baseline)

Lặp:
    Tạo episode: S_0, A_0, R_1, ..., S_T
    
    Với mỗi bước t:
        G_t = Σ_{k=t}^T γ^{k-t} R_k
        δ_t = G_t - V̂(S_t; w)  # Advantage estimate
        
        # Update policy
        θ ← θ + α_θ γ^t δ_t ∇_θ log π(A_t|S_t;θ)
        
        # Update value function
        w ← w + α_w δ_t ∇_w V̂(S_t; w)
```

### 4. Actor-Critic Methods

#### 4.1. Ý tưởng

**Actor**: Policy π(a|s;θ)
**Critic**: Value function V(s;w) hoặc Q(s,a;w)

**Actor-Critic Framework**:
```
Actor: Chọn actions theo policy
Critic: Đánh giá actions
Actor học từ feedback của Critic
```

#### 4.2. Advantage Actor-Critic (A2C)

**TD Error làm advantage**:
```
δ_t = R_{t+1} + γV(S_{t+1};w) - V(S_t;w)
```

**Updates**:
```
# Actor update
θ ← θ + α_θ δ_t ∇_θ log π(A_t|S_t;θ)

# Critic update
w ← w + α_w δ_t ∇_w V(S_t;w)
```

**Algorithm**:
```
Khởi tạo θ, w
Thiết lập α_θ, α_w

Lặp với mỗi episode:
    Khởi tạo S
    
    Lặp với mỗi bước:
        A ~ π(·|S;θ)
        Thực hiện A, quan sát R, S'
        
        δ = R + γV(S';w) - V(S;w)
        
        w ← w + α_w δ ∇_w V(S;w)
        θ ← θ + α_θ δ ∇_θ log π(A|S;θ)
        
        S ← S'
    cho đến S là terminal
```

#### 4.3. Asynchronous Advantage Actor-Critic (A3C)

**Ý tưởng**: Parallel actors với shared parameters

**Architecture**:
```
Global Network (θ, w)
    ↓ Copy
Multiple Workers (θ', w')
    ↓ Collect experience
    ↓ Compute gradients
    ↑ Update global network
```

**Benefits**:
- Faster learning (parallel experience collection)
- Decorrelated experience (different workers explore differently)
- Stable learning

#### 4.4. Generalized Advantage Estimation (GAE)

**n-Step TD Error**:
```
δ_t^(n) = R_{t+1} + γR_{t+2} + ... + γ^{n-1}R_{t+n} + γ^n V(S_{t+n}) - V(S_t)
```

**GAE**:
```
A_t^GAE(λ) = Σ_{l=0}^∞ (γλ)^l δ_{t+l}
           = (1-λ) Σ_{n=1}^∞ λ^{n-1} δ_t^(n)
```

**Đặc điểm**:
- λ = 0: TD(0), low variance, high bias
- λ = 1: Monte Carlo, high variance, low bias
- λ ∈ (0,1): Trade-off

### 5. Trust Region Methods

#### 5.1. Vấn đề với Vanilla Policy Gradient

**Large updates**: Có thể làm policy collapse
**Solution**: Constrain update size

#### 5.2. Trust Region Policy Optimization (TRPO)

**Objective**:
```
maximize E[π_θ_new(a|s) / π_θ_old(a|s) · A^π_old(s,a)]
subject to: KL(π_θ_old || π_θ_new) ≤ δ
```

**KL Divergence constraint**: Đảm bảo new policy không quá khác old policy

**Implementation**: Sử dụng conjugate gradient và line search

**Đặc điểm**:
✅ Monotonic improvement guarantee
✅ Stable learning
❌ Computationally expensive
❌ Difficult to implement

#### 5.3. Proximal Policy Optimization (PPO)

**Ý tưởng**: Approximate TRPO constraint bằng clipping

**Clipped Surrogate Objective**:
```
L^CLIP(θ) = E[min(r_t(θ)A_t, clip(r_t(θ), 1-ε, 1+ε)A_t)]

r_t(θ) = π_θ(a|s) / π_θ_old(a|s)  # Importance ratio
```

**Giải thích**:
- Clip r_t ∈ [1-ε, 1+ε] (thường ε=0.2)
- Prevent too large policy updates
- Simpler và faster than TRPO

**PPO Algorithm**:
```
Khởi tạo θ, w

Lặp:
    # Collect trajectories
    Với mỗi worker:
        Thu thập N steps theo π_θ_old
        Tính advantages Â_t
    
    # Optimize
    Lặp K epochs:
        Sample mini-batches
        Compute L^CLIP
        Update θ bằng gradient ascent
        Update w bằng gradient descent
    
    θ_old ← θ
```

**Improvements**:
- **PPO-Penalty**: Thay clip bằng KL penalty
- **PPO-Adaptive**: Adaptive KL coefficient

### 6. Deterministic Policy Gradient (DPG)

#### 6.1. Motivation

**Stochastic policies**: π(a|s;θ)
**Deterministic policies**: μ(s;θ) = a

**Advantage với continuous actions**:
- Không cần integrate over action space
- More sample efficient

#### 6.2. Deterministic Policy Gradient Theorem

**Theorem**:
```
∇_θ J(θ) = E_s~ρ^μ[∇_θ μ(s;θ) ∇_a Q^μ(s,a)|_{a=μ(s)}]
```

**Chain rule**:
```
∇_θ J ≈ ∇_θ μ(s;θ) · ∇_a Q(s,a)|_{a=μ(s)}
```

#### 6.3. Deep Deterministic Policy Gradient (DDPG)

**Components**:
1. **Actor**: μ(s;θ)
2. **Critic**: Q(s,a;w)
3. **Target networks**: μ'(s;θ'), Q'(s,a;w')
4. **Replay buffer**: D

**Algorithm**:
```
Khởi tạo networks: μ(s;θ), Q(s,a;w)
Khởi tạo target networks: θ' ← θ, w' ← w
Khởi tạo replay buffer D

Lặp với mỗi episode:
    Khởi tạo noise process N
    Khởi tạo state s
    
    Lặp với mỗi bước:
        # Select action với exploration noise
        a = μ(s;θ) + N_t
        
        Thực hiện a, quan sát r, s'
        Store (s, a, r, s') vào D
        
        # Sample mini-batch từ D
        Với mỗi (s_i, a_i, r_i, s'_i):
            y_i = r_i + γQ'(s'_i, μ'(s'_i;θ');w')
        
        # Update critic
        L = (1/N) Σ(y_i - Q(s_i, a_i;w))²
        w ← w - α_w ∇_w L
        
        # Update actor
        θ ← θ + α_θ (1/N) Σ∇_θ μ(s_i;θ) ∇_a Q(s_i,a;w)|_{a=μ(s_i)}
        
        # Update target networks (soft update)
        θ' ← τθ + (1-τ)θ'
        w' ← τw + (1-τ)w'
```

**Exploration**: Ornstein-Uhlenbeck noise hoặc Gaussian noise

#### 6.4. Twin Delayed DDPG (TD3)

**Improvements over DDPG**:

**1. Clipped Double Q-Learning**:
```
y = r + γ min(Q₁'(s', μ'(s')), Q₂'(s', μ'(s')))
```

**2. Delayed Policy Updates**:
- Update critic mỗi step
- Update actor mỗi d steps

**3. Target Policy Smoothing**:
```
a' = μ'(s') + ε
ε ~ clip(N(0, σ), -c, c)
```

### 7. Maximum Entropy RL

#### 7.1. Soft Actor-Critic (SAC)

**Objective**: Maximize expected return + entropy
```
J(π) = Σ_t E[(R_t + αH(π(·|S_t)))]
H(π(·|s)) = -Σ_a π(a|s) log π(a|s)  # Entropy
```

**Benefits**:
- Encourage exploration
- Robust learning
- Multiple modes trong policy

**Soft Q-Function**:
```
Q^π(s,a) = E[R + γ(Q^π(s',a') - α log π(a'|s'))]
```

**Algorithm components**:
1. Stochastic actor: π(a|s;θ)
2. Soft Q-functions: Q₁, Q₂
3. Target Q-functions
4. Automatic entropy tuning

### 8. So sánh các thuật toán

#### 8.1. Bảng so sánh

| Algorithm | Type | Action Space | Stability | Sample Efficiency | Performance |
|-----------|------|--------------|-----------|-------------------|-------------|
| REINFORCE | On-policy | Both | Low | Low | Baseline |
| A2C | On-policy | Both | Medium | Medium | Good |
| A3C | On-policy | Both | Medium | Medium | Good |
| TRPO | On-policy | Both | High | Low | Very Good |
| PPO | On-policy | Both | High | Medium | Very Good |
| DDPG | Off-policy | Continuous | Medium | High | Good |
| TD3 | Off-policy | Continuous | High | High | Very Good |
| SAC | Off-policy | Continuous | High | High | Excellent |

#### 8.2. Khi nào dùng gì?

**REINFORCE**: 
- Simple tasks
- Educational purposes
- Baseline comparison

**A2C/A3C**:
- Need fast training với parallel workers
- Good general-purpose algorithm

**PPO**:
- Current go-to cho nhiều tasks
- Stable và reliable
- Robotics, games

**DDPG/TD3**:
- Continuous control
- Robotics
- Physical simulation

**SAC**:
- Best performance cho continuous control
- Robust và stable
- State-of-the-art

### 9. Ứng dụng thực tế

#### 9.1. Robotics

**Manipulation Tasks**:
- Grasping objects
- Assembly
- Method: PPO, SAC

**Locomotion**:
- Walking, running
- Complex terrain navigation
- Method: TD3, SAC

#### 9.2. Game Playing

**Atari Games**:
- A3C đạt human-level
- PPO improvements

**Continuous Control Games**:
- Racing games
- Flight simulators
- Method: SAC, TD3

#### 9.3. Autonomous Systems

**Drone Control**:
- Navigation
- Obstacle avoidance
- Method: PPO với safety constraints

**Self-Driving**:
- Lane keeping
- Parking
- Method: SAC với hierarchical RL

### 10. Code Implementation

#### 10.1. REINFORCE
```python
class REINFORCE:
    def __init__(self, policy_net, lr=1e-3, gamma=0.99):
        self.policy = policy_net
        self.optimizer = optim.Adam(policy.parameters(), lr=lr)
        self.gamma = gamma
    
    def select_action(self, state):
        state = torch.FloatTensor(state)
        probs = self.policy(state)
        m = Categorical(probs)
        action = m.sample()
        return action.item(), m.log_prob(action)
    
    def train(self, episode_data):
        """episode_data: [(log_prob, reward), ...]"""
        policy_loss = []
        returns = []
        
        # Calculate returns
        R = 0
        for _, reward in reversed(episode_data):
            R = reward + self.gamma * R
            returns.insert(0, R)
        
        returns = torch.tensor(returns)
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        
        # Calculate policy loss
        for (log_prob, _), R in zip(episode_data, returns):
            policy_loss.append(-log_prob * R)
        
        # Update
        self.optimizer.zero_grad()
        policy_loss = torch.cat(policy_loss).sum()
        policy_loss.backward()
        self.optimizer.step()
```

#### 10.2. Actor-Critic
```python
class ActorCritic:
    def __init__(self, actor_net, critic_net, 
                 lr_actor=1e-3, lr_critic=1e-3, gamma=0.99):
        self.actor = actor_net
        self.critic = critic_net
        self.actor_optimizer = optim.Adam(actor.parameters(), lr=lr_actor)
        self.critic_optimizer = optim.Adam(critic.parameters(), lr=lr_critic)
        self.gamma = gamma
    
    def select_action(self, state):
        state = torch.FloatTensor(state)
        probs = self.actor(state)
        m = Categorical(probs)
        action = m.sample()
        return action.item(), m.log_prob(action)
    
    def train_step(self, state, action, reward, next_state, done, log_prob):
        state = torch.FloatTensor(state)
        next_state = torch.FloatTensor(next_state)
        
        # Critic update
        value = self.critic(state)
        next_value = self.critic(next_state) if not done else 0
        td_target = reward + self.gamma * next_value
        td_error = td_target - value
        
        critic_loss = td_error.pow(2)
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()
        
        # Actor update
        actor_loss = -log_prob * td_error.detach()
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()
```

#### 10.3. PPO (Simplified)
```python
class PPO:
    def __init__(self, actor_net, critic_net, lr=3e-4, 
                 gamma=0.99, clip_epsilon=0.2, epochs=10):
        self.actor = actor_net
        self.critic = critic_net
        self.optimizer = optim.Adam(
            list(actor.parameters()) + list(critic.parameters()), lr=lr)
        self.gamma = gamma
        self.clip_epsilon = clip_epsilon
        self.epochs = epochs
    
    def train(self, states, actions, old_log_probs, returns, advantages):
        for _ in range(self.epochs):
            # Get current policy outputs
            probs = self.actor(states)
            dist = Categorical(probs)
            log_probs = dist.log_prob(actions)
            
            # Ratio
            ratio = torch.exp(log_probs - old_log_probs)
            
            # Clipped objective
            surr1 = ratio * advantages
            surr2 = torch.clamp(ratio, 1-self.clip_epsilon, 
                               1+self.clip_epsilon) * advantages
            actor_loss = -torch.min(surr1, surr2).mean()
            
            # Value loss
            values = self.critic(states)
            critic_loss = F.mse_loss(values, returns)
            
            # Total loss
            loss = actor_loss + 0.5 * critic_loss
            
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
```

### 11. Tricks và Best Practices

#### 11.1. Variance Reduction
- Use baselines
- Generalized Advantage Estimation
- Normalize advantages
- Multiple workers (A3C)

#### 11.2. Stability
- Clip gradients
- Trust region methods (TRPO, PPO)
- Target networks
- Entropy regularization

#### 11.3. Sample Efficiency
- Experience replay (off-policy)
- Parallel workers
- Prioritized sampling
- Curriculum learning

#### 11.4. Hyperparameters
- **Learning rate**: 1e-4 to 1e-3
- **Batch size**: 64-2048
- **γ (gamma)**: 0.95-0.99
- **GAE λ**: 0.95-0.99
- **PPO ε**: 0.1-0.3

### 12. Bài tập thực hành

#### 12.1. Bài tập cơ bản
1. Implement REINFORCE cho CartPole
2. Add baseline và compare variance
3. Visualize policy evolution

#### 12.2. Bài tập nâng cao
1. Implement A2C với parallel workers
2. PPO cho continuous control (MuJoCo)
3. Compare PPO vs REINFORCE vs A2C

#### 12.3. Dự án
1. Train PPO agent cho Atari games
2. Implement SAC cho robotics simulation
3. Multi-agent RL với policy gradients

### 13. Kết luận

Policy Gradient Methods mang lại cách tiếp cận trực tiếp và powerful cho reinforcement learning, đặc biệt hiệu quả với continuous action spaces.

**Key Takeaways**:

1. **Direct Policy Learning**: Học policy trực tiếp thay vì qua value function
2. **Variance-Bias Tradeoff**: Baselines và GAE giúp reduce variance
3. **Trust Regions**: TRPO và PPO đảm bảo stable updates
4. **Actor-Critic**: Kết hợp value và policy learning
5. **Continuous Control**: DDPG, TD3, SAC cho continuous actions
6. **State-of-the-art**: PPO và SAC là go-to choices hiện nay

**Evolution**:
```
REINFORCE → Actor-Critic → A3C → TRPO → PPO
                    ↓
               DDPG → TD3 → SAC
```

**Practical Advice**:
- Start với PPO cho discrete actions
- Use SAC cho continuous control
- Tune hyperparameters carefully
- Use parallel workers khi có thể
- Monitor training metrics (returns, entropy, losses)

Reinforcement Learning đã phát triển mạnh mẽ và Policy Gradient Methods là công cụ quan trọng trong arsenal của RL researcher!

---

## Integrating Learning and Planning - Tích Hợp Học và Lập Kế Hoạch

### 1. Giới thiệu

#### 1.1. Model-Free vs Model-Based RL

**Model-Free RL**:
- Học trực tiếp từ experience
- Không build model của environment
- Ví dụ: Q-Learning, SARSA, Policy Gradient

**Model-Based RL**:
- Học model của environment
- Sử dụng model để planning
- Có thể kết hợp với learning

#### 1.2. Lợi ích của Model-Based RL

✅ **Sample Efficiency**: Model cho phép reuse experience
✅ **Planning**: Có thể simulate và plan ahead
✅ **Transfer**: Model có thể transfer sang tasks khác
✅ **Interpretability**: Hiểu được dynamics của environment

**Trade-offs**:
❌ Model error có thể compound
❌ Computational cost của planning
❌ Complexity trong implementation

### 2. Models trong RL

#### 2.1. Model Representation

**Transition Model**:
```
P(s'|s,a) = Probability of next state
hoặc
s' = f(s, a) + noise  (deterministic + noise)
```

**Reward Model**:
```
R(s,a) = Expected reward
hoặc
r ~ P(r|s,a)
```

#### 2.2. Learning Models

**Table Lookup** (Discrete):
```
Count(s,a,s') = số lần chuyển từ s đến s' với action a
P̂(s'|s,a) = Count(s,a,s') / Σ_{s''} Count(s,a,s'')
```

**Function Approximation**:
```
Neural Network: s' = NN(s, a; θ)
Gaussian Process: s' ~ GP(s, a)
```

**Ensemble Models**: Nhiều models để estimate uncertainty

### 3. Dyna Architecture

#### 3.1. Ý tưởng Dyna

**Integration**: Kết hợp direct RL và planning

**Components**:
1. **Direct RL**: Học từ real experience
2. **Model Learning**: Học model từ experience
3. **Planning**: Sử dụng model để generate simulated experience

#### 3.2. Dyna-Q Algorithm

```
Khởi tạo Q(s,a) và Model(s,a)
Parameters: n (planning steps)

Lặp:
    # (a) Direct RL
    Observe (S, A, R, S')
    Q(S,A) ← Q(S,A) + α[R + γ max_a Q(S',a) - Q(S,A)]
    
    # (b) Model Learning
    Model(S,A) ← (R, S')  # Store observed transition
    
    # (c) Planning
    Lặp n lần:
        S_sim ← random previously observed state
        A_sim ← random action from S_sim
        (R_sim, S'_sim) ← Model(S_sim, A_sim)
        Q(S_sim, A_sim) ← Q(S_sim, A_sim) + 
                          α[R_sim + γ max_a Q(S'_sim, a) - Q(S_sim, A_sim)]
```

**Đặc điểm**:
- Mỗi real experience update cả Q và Model
- Planning steps tăng sample efficiency
- Convergence nhanh hơn model-free

#### 3.3. Ví dụ: Dyna Maze

**Setup**:
- Gridworld maze
- Goal: Reach target
- Reward: -1 per step

**Results**:
- Dyna-Q với n=5: ~15 episodes để solve
- Q-Learning: ~25 episodes
- Planning steps significantly speed up learning

### 4. Simulation-Based Search

#### 4.1. Monte Carlo Tree Search (MCTS)

**Ý tưởng**: Build search tree bằng simulation

**Four Steps**:
```
1. Selection: Chọn nodes theo UCT policy
2. Expansion: Thêm child node
3. Simulation: Rollout policy từ new node
4. Backpropagation: Update values dọc path
```

**UCT (Upper Confidence Bound for Trees)**:
```
UCT(s,a) = Q(s,a) + c√(ln N(s) / N(s,a))
           ↑ Exploitation  ↑ Exploration
```

**Algorithm**:
```
function MCTS(state, num_simulations):
    Khởi tạo root node với state
    
    Lặp num_simulations lần:
        node = root
        
        # Selection
        while node is fully expanded and not terminal:
            node = select_child(node, UCT)
        
        # Expansion
        if node is not terminal:
            node = expand(node)
        
        # Simulation (rollout)
        reward = simulate(node.state)
        
        # Backpropagation
        backpropagate(node, reward)
    
    return best_action(root)
```

#### 4.2. AlphaGo và AlphaZero

**AlphaGo**:
- MCTS + Deep Neural Networks
- Policy network: Suggest moves
- Value network: Evaluate positions
- Human expert data + self-play

**AlphaZero**:
- Pure self-play, no human data
- Single network: Both policy và value
- MCTS for search
- Defeats AlphaGo 100-0

**Key Innovation**: Deep RL + MCTS

### 5. Model Predictive Control (MPC)

#### 5.1. MPC trong RL

**Idea**: Plan optimal actions using model

**Process**:
```
1. Use model to predict future states
2. Optimize action sequence
3. Execute first action
4. Replan at next step (receding horizon)
```

**Optimization**:
```
argmax_{a_0,...,a_H} Σ_t R(s_t, a_t)
subject to: s_{t+1} = f(s_t, a_t)
```

#### 5.2. Cross-Entropy Method (CEM)

**Sampling-based optimization**:
```
Khởi tạo distribution μ, σ

Lặp:
    Sample N action sequences từ N(μ, σ)
    Evaluate mỗi sequence bằng rollouts
    Select top K sequences
    Update μ, σ từ elite sequences
```

**Applications**: Robot control, continuous control

### 6. World Models

#### 6.1. Learning World Models

**Representation Learning**:
```
VAE (Variational Autoencoder):
    Encode: z = Encoder(observation)
    Decode: observation' = Decoder(z)

Recurrent Model:
    z_{t+1} = RNN(z_t, a_t)
```

**World Models Paper**:
- V: Vision model (VAE)
- M: Memory (RNN)
- C: Controller (linear/simple)

**Train entirely in dream**: Agent learns in latent space!

#### 6.2. Imagination-Augmented Agents

**Architecture**:
```
Standard path: observation → policy

Imagination path:
    observation → model → future predictions
              ↓              ↓
              ↳──── aggregate ───→ policy
```

**Benefits**: Better sample efficiency và performance

### 7. Model Errors và Solutions

#### 7.1. Model Bias Problem

**Issue**: Model errors compound over long horizons
```
Error at t: ε_t
Error at T: O(T·ε_t) hoặc worse
```

#### 7.2. Solutions

**1. Short Horizon Planning**:
- Plan chỉ vài steps ahead
- Replan frequently

**2. Model Ensemble**:
```
Train N models: {M_1, ..., M_N}
Estimate uncertainty
Use pessimistic/conservative planning
```

**3. Model-Based Value Expansion (MVE)**:
```
Mix model rollouts với value function:
V(s) = R(s,a) + γ^k V(s_{t+k})
       ↑ k-step model rollout
```

**4. Learn in Real Environment**:
- Use model cho exploration/planning
- Learn value/policy from real data

### 8. Ứng dụng thực tế

#### 8.1. Robotics

**Manipulation**:
- Learn forward model của robot
- MPC cho grasping
- Fast adaptation

**Locomotion**:
- Model-based để bootstrap learning
- Transfer từ simulation

#### 8.2. Games

**Board Games** (Chess, Go):
- Perfect models
- MCTS dominates

**Video Games**:
- Approximate models
- World models + RL

#### 8.3. Autonomous Driving

**Prediction Models**:
- Predict other vehicles behavior
- Plan safe trajectories
- Contingency planning

### 9. Code Example: Simple Dyna-Q

```python
class DynaQ:
    def __init__(self, num_states, num_actions, 
                 alpha=0.1, gamma=0.99, planning_steps=5):
        self.Q = np.zeros((num_states, num_actions))
        self.model = {}  # (s,a) -> (r, s')
        self.alpha = alpha
        self.gamma = gamma
        self.n = planning_steps
    
    def update(self, s, a, r, s_next):
        # Direct RL update
        best_next = np.max(self.Q[s_next])
        self.Q[s, a] += self.alpha * (r + self.gamma * best_next - self.Q[s, a])
        
        # Model learning
        self.model[(s, a)] = (r, s_next)
        
        # Planning
        for _ in range(self.n):
            # Random previously seen state-action
            s_sim, a_sim = random.choice(list(self.model.keys()))
            r_sim, s_next_sim = self.model[(s_sim, a_sim)]
            
            # Simulated update
            best_next_sim = np.max(self.Q[s_next_sim])
            self.Q[s_sim, a_sim] += self.alpha * (
                r_sim + self.gamma * best_next_sim - self.Q[s_sim, a_sim])
```

### 10. Kết luận

Integrating Learning and Planning kết hợp sức mạnh của cả model-free và model-based RL.

**Key Insights**:

1. **Dyna**: Simple và effective integration
2. **MCTS**: Powerful search algorithm, basis của AlphaGo/AlphaZero
3. **MPC**: Optimal control với learned models
4. **World Models**: Learn và plan in latent space
5. **Model Errors**: Cần careful handling

**Trade-offs**:
- Sample efficiency ↔ Model error
- Planning cost ↔ Better policies
- Model complexity ↔ Accuracy vs generalization

**Best Practices**:
- Use short horizon planning
- Ensemble models cho uncertainty
- Combine với model-free learning
- Careful với compounding errors

---

## Exploration and Exploitation - Khám Phá và Khai Thác

### 1. Giới thiệu về Exploration-Exploitation Dilemma

#### 1.1. Định nghĩa

**Exploitation**: Chọn actions mà agent tin là tốt nhất (maximize immediate reward)
**Exploration**: Thử actions mới để discover potentially better options

**Dilemma**: Làm sao cân bằng?
```
Pure Exploitation: Có thể stuck tại suboptimal policy
Pure Exploration: Không bao giờ maximize rewards
```

#### 1.2. Tại sao quan trọng?

- **Learning**: Cần explore để learn về environment
- **Optimization**: Cần exploit để maximize returns
- **Trade-off**: Exploration cost short-term reward for long-term gain

#### 1.3. Multi-Armed Bandit Problem

**Setup**: K slot machines (arms), mỗi arm có unknown reward distribution

**Goal**: Maximize cumulative reward over time

**Regret**: 
```
Regret = Σ_t (V* - V(a_t))
V* = Value của best arm
```

### 2. Exploration Strategies

#### 2.1. ε-Greedy

**Strategy**:
```
Với xác suất ε: Chọn random action
Với xác suất 1-ε: Chọn best known action
```

**Variants**:
```
# Fixed
ε = 0.1

# Decay
ε_t = ε_0 / t
ε_t = ε_min + (ε_max - ε_min) * exp(-decay * t)

# Adaptive
Tăng ε khi performance kém
Giảm ε khi performance tốt
```

**Pros**: Simple, effective
**Cons**: Random exploration không efficient

#### 2.2. Softmax / Boltzmann Exploration

**Strategy**: Sample proportional to estimated values
```
π(a|s) = exp(Q(s,a)/τ) / Σ_b exp(Q(s,b)/τ)
```

**Temperature τ**:
- τ → 0: Greedy (exploitation)
- τ → ∞: Uniform random (exploration)
- τ decay over time

**Pros**: Probabilistic, smooth
**Cons**: Need tune τ

#### 2.3. Optimistic Initialization

**Idea**: Initialize Q-values optimistically (higher than true values)
```
Q(s,a) = Q_max  (instead of 0)
```

**Effect**: Agent naturally explores unvisited (s,a) pairs

**Pros**: Simple, no hyperparameters
**Cons**: Temporary effect only

### 3. Upper Confidence Bound (UCB)

#### 3.1. UCB Algorithm

**Principle**: "Optimism in face of uncertainty"

**UCB Formula**:
```
UCB(a) = Q̄(a) + c√(ln t / N(a))
         ↑ Exploitation  ↑ Exploration

Q̄(a): Average reward của arm a
N(a): Number of times arm a played
t: Total time steps
c: Exploration parameter
```

**Action Selection**:
```
a_t = argmax_a UCB(a)
```

**Properties**:
- Logarithmic regret: O(log t)
- Optimal trong bandit setting

#### 3.2. UCB trong RL

**UCB applied to Q-Learning**:
```
Q_UCB(s,a) = Q(s,a) + c√(ln N(s) / N(s,a))

Select: a = argmax_a Q_UCB(s,a)
```

**Challenges**: Need track visit counts

### 4. Thompson Sampling

#### 4.1. Bayesian Approach

**Idea**: Maintain distribution over Q-values

**Algorithm**:
```
Initialize: Prior distribution P(θ)

Lặp:
    Sample θ_t ~ P(θ|history)
    Select a_t = argmax_a Q(s,a;θ_t)
    Observe reward r_t
    Update P(θ|history, r_t) bằng Bayes rule
```

#### 4.2. Beta-Bernoulli Thompson Sampling

**For binary rewards**:
```
Prior: Beta(α_a, β_a) cho mỗi arm a

Sample: θ_a ~ Beta(α_a, β_a)
Choose: a = argmax_a θ_a

Update winner:
    Success: α_a ← α_a + 1
    Failure: β_a ← β_a + 1
```

**Properties**:
- Optimal regret bounds
- Often better than UCB trong practice

### 5. Count-Based Exploration

#### 5.1. Exploration Bonuses

**Idea**: Add bonus reward for visiting rare states

**Intrinsic Motivation**:
```
r_total = r_extrinsic + β · r_intrinsic

r_intrinsic = 1/√N(s)  hoặc  1/√N(s,a)
```

**Effect**: Encourage visiting under-explored regions

#### 5.2. Pseudo-Count Methods

**For large state spaces**: Cannot count exactly

**Density Models**:
```
ρ(s): Estimate density/frequency of state s
Pseudo-count: N(s) ∝ ρ(s) / (1 - ρ(s))
Bonus: r_intrinsic = β/√N(s)
```

**Examples**:
- Context Tree Switching (CTS)
- Neural density models

### 6. Curiosity-Driven Exploration

#### 6.1. Intrinsic Curiosity Module (ICM)

**Components**:
```
1. Forward Model: Predict next state feature
   ŝ_{t+1} = f(s_t, a_t)

2. Inverse Model: Predict action from states
   â_t = g(s_t, s_{t+1})

3. Intrinsic Reward: Prediction error
   r_intrinsic = ||ŝ_{t+1} - s_{t+1}||²
```

**Intuition**: States that are hard to predict are "interesting"

#### 6.2. Random Network Distillation (RND)

**Setup**:
```
Fixed random network: f_target(s)
Learned predictor: f_pred(s; θ)
```

**Intrinsic Reward**:
```
r_intrinsic = ||f_target(s) - f_pred(s; θ)||²
```

**Properties**:
- Novel states have high prediction error
- Visited states have low error
- Non-stationary targets avoided

#### 6.3. Never Give Up (NGU)

**Combines**:
- Episodic novelty (memory-based)
- Life-long novelty (RND-based)

**Two-timescale curiosity**:
```
r_episodic: Within episode novelty
r_lifelong: Across episodes novelty
```

### 7. Information-Theoretic Exploration

#### 7.1. Information Gain

**Maximum Information Gain**:
```
Maximize: I(Θ; O | a) = H(Θ) - H(Θ|O,a)
Θ: Parameters/state of world
O: Observations
```

**Intuition**: Choose actions that reveal most information

#### 7.2. Entropy Maximization

**Maximum Entropy RL** (covered in SAC):
```
π* = argmax_π E[Σ_t (R_t + α H(π(·|S_t)))]
```

**Benefits**:
- Natural exploration
- Robust policies
- Multiple solutions

#### 7.3. Empowerment

**Definition**: Mutual information between actions và future states
```
Empowerment = I(A_t; S_{t+k} | S_t)
```

**Intuition**: Maximize control over future

### 8. Goal-Driven Exploration

#### 8.1. Hindsight Experience Replay (HER)

**Problem**: Sparse rewards → most episodes fail → little learning

**Idea**: Learn from failures by relabeling goals
```
Original: Goal = g, achieved = g', reward = 0 (failure)
HER: Goal = g', achieved = g', reward = 0 (success!)
```

**Algorithm**:
```
Store transition (s, a, r, s', g) vào replay buffer

Additionally store:
    (s, a, r', s', g') where g' = achieved_goal(s')
    r' = reward(s', a, g')
```

**Effect**: Every trajectory teaches something

#### 8.2. Curriculum Learning

**Progressive Difficulty**:
```
Easy tasks → Medium tasks → Hard tasks
```

**Automatic Curriculum**:
- Track success rates
- Adjust task distribution
- Focus on "frontier" of capability

### 9. Multi-Agent Exploration

#### 9.1. Population-Based Training

**Idea**: Train population of agents với different hyperparameters

**Process**:
```
Population: {Agent_1, ..., Agent_N}

Periodically:
    Evaluate all agents
    Replace worst với copies of best
    Mutate hyperparameters
```

**Benefits**: Automatic hyperparameter tuning + diversity

#### 9.2. Quality Diversity (QD)

**Goal**: Find diverse set of good solutions

**MAP-Elites**:
```
Grid of cells, mỗi cell = behavior niche
Store best solution in mỗi cell
Explore để fill all cells
```

**Applications**: Robotics, game playing

### 10. Exploration trong Deep RL

#### 10.1. Noisy Networks

**Idea**: Add noise to network weights

**NoisyNet**:
```
y = (μ^w + σ^w ⊙ ε^w) x + (μ^b + σ^b ⊙ ε^b)

μ, σ: Learned parameters
ε: Random noise
```

**Benefits**:
- Automatic exploration
- State-dependent noise
- No epsilon scheduling

#### 10.2. Parameter Space Noise

**Add noise to policy parameters**:
```
θ_noisy = θ + N(0, σ²I)
```

**Adaptive noise**:
```
Adjust σ based on action space distance
```

#### 10.3. Bootstrapped DQN

**Multiple heads** cho uncertainty:
```
Q_1(s,a), Q_2(s,a), ..., Q_K(s,a)

Sample head k uniformly
Use Q_k for exploration
```

**Effect**: Deep exploration (multi-step exploration)

### 11. Practical Guidelines

#### 11.1. Choosing Exploration Strategy

**Simple tasks**:
- ε-greedy với decay
- Optimistic initialization

**Complex tasks**:
- UCB / Thompson Sampling
- Curiosity-driven

**Sparse rewards**:
- HER
- Intrinsic motivation
- Count-based

**Continuous control**:
- Gaussian noise
- Parameter space noise
- NoisyNet

#### 11.2. Debugging Exploration

**Metrics to track**:
```
- State/action coverage
- Entropy của policy
- Intrinsic rewards
- Episode diversity
```

**Signs of poor exploration**:
- Low state coverage
- Policy becomes deterministic too early
- Training plateaus early

#### 11.3. Hyperparameter Tuning

**ε-greedy**:
- Start: 1.0
- End: 0.01-0.1
- Decay: Linear hoặc exponential

**Curiosity coefficient β**:
- Start small: 0.01-0.1
- Tune based on reward scale

**UCB constant c**:
- Typical: 1.0-2.0
- Higher = more exploration

### 12. Code Examples

#### 12.1. ε-Greedy với Decay
```python
class EpsilonGreedy:
    def __init__(self, epsilon_start=1.0, epsilon_end=0.01, 
                 epsilon_decay=0.995):
        self.epsilon = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
    
    def select_action(self, q_values):
        if np.random.random() < self.epsilon:
            return np.random.randint(len(q_values))
        else:
            return np.argmax(q_values)
    
    def decay(self):
        self.epsilon = max(self.epsilon_end, 
                          self.epsilon * self.epsilon_decay)
```

#### 12.2. UCB
```python
class UCB:
    def __init__(self, num_actions, c=2.0):
        self.Q = np.zeros(num_actions)
        self.N = np.zeros(num_actions)
        self.c = c
        self.t = 0
    
    def select_action(self):
        self.t += 1
        
        # Avoid division by zero
        ucb_values = np.where(
            self.N > 0,
            self.Q + self.c * np.sqrt(np.log(self.t) / self.N),
            np.inf
        )
        
        return np.argmax(ucb_values)
    
    def update(self, action, reward):
        self.N[action] += 1
        self.Q[action] += (reward - self.Q[action]) / self.N[action]
```

#### 12.3. Curiosity-Driven (Simplified)
```python
class CuriosityModule(nn.Module):
    def __init__(self, state_dim, action_dim, feature_dim=128):
        super().__init__()
        # Inverse model
        self.inverse = nn.Sequential(
            nn.Linear(state_dim * 2, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim)
        )
        
        # Forward model
        self.forward = nn.Sequential(
            nn.Linear(state_dim + action_dim, 256),
            nn.ReLU(),
            nn.Linear(256, state_dim)
        )
    
    def intrinsic_reward(self, state, action, next_state):
        # Predict next state
        pred_next = self.forward(torch.cat([state, action], dim=-1))
        
        # Prediction error = intrinsic reward
        error = F.mse_loss(pred_next, next_state, reduction='none')
        return error.mean(dim=-1)
```

### 13. Ứng dụng thực tế

#### 13.1. Robotics

**Exploration challenges**:
- Safety constraints
- Real-world sample cost
- Reset difficulty

**Solutions**:
- Curiosity in simulation → transfer
- Safe exploration policies
- Curriculum learning

#### 13.2. Game Playing

**Montezuma's Revenge**:
- Extremely sparse rewards
- Deep exploration needed
- RND, NGU achieve breakthroughs

**StarCraft II**:
- Huge action space
- League training (multi-agent)
- Diversity for robustness

#### 13.3. Recommendation Systems

**Exploration needed**:
- Discover user preferences
- Cold start problem
- Avoid filter bubbles

**Methods**:
- Thompson Sampling
- UCB
- ε-greedy với contextual information

### 14. Advanced Topics

#### 14.1. Risk-Sensitive Exploration

**Balance**: Exploration vs safety

**CVaR (Conditional Value at Risk)**:
```
Optimize worst-case returns
Constraint: Probability(return < threshold) < α
```

#### 14.2. Multi-Objective Exploration

**Multiple goals**:
- Reward maximization
- State coverage
- Safety
- Entropy

**Pareto optimality**: Trade-offs between objectives

#### 14.3. Transfer Learning và Meta-Learning

**Meta-RL**:
- Learn exploration strategy across tasks
- Fast adaptation to new tasks
- MAML, RL²

### 15. Bài tập thực hành

#### 15.1. Bài tập cơ bản
1. Implement ε-greedy, UCB, Thompson Sampling cho bandits
2. Compare strategies on gridworld
3. Visualize exploration trajectories

#### 15.2. Bài tập nâng cao
1. Implement count-based exploration bonus
2. Add ICM to PPO agent
3. HER cho sparse reward task

#### 15.3. Dự án
1. Curiosity-driven agent cho Montezuma's Revenge
2. Multi-armed bandit cho ad recommendation
3. Safe exploration cho robot simulation

### 16. Kết luận

Exploration-Exploitation là central challenge trong RL, requiring careful balance và creative solutions.

**Key Takeaways**:

1. **Fundamental Dilemma**: Cannot be avoided, must be managed
2. **Simple Methods Work**: ε-greedy, UCB often sufficient
3. **Curiosity Helps**: Intrinsic motivation powerful cho hard exploration
4. **Context Matters**: Different strategies cho different problems
5. **Active Research Area**: New methods constantly emerging

**Practical Recommendations**:

**Start Simple**:
- ε-greedy với decay
- Tune epsilon schedule

**If stuck**:
- Add intrinsic rewards
- Try count-based bonuses
- Consider curriculum

**For sparse rewards**: 
- HER essential
- Curiosity-driven exploration
- Shaped rewards (carefully!)

**Monitor**:
- Coverage metrics
- Exploration vs exploitation ratio
- Learning curves

**Evolution of Exploration**:
```
Random → ε-greedy → UCB/Thompson Sampling
         ↓
    Curiosity → Information Theory
         ↓
    Multi-Agent → Meta-Learning
```

**Final Thoughts**:

Exploration là nghệ thuật và khoa học. Không có one-size-fits-all solution. Understand your problem:
- Reward structure (dense/sparse)
- State space (size, structure)
- Safety requirements
- Sample efficiency needs

Experiment với different methods và monitor carefully. Good exploration strategy có thể là difference giữa success và failure trong RL!