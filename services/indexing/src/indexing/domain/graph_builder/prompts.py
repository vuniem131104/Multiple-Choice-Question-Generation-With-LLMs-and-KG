# Prompt cho môn Cấu trúc dữ liệu và Giải thuật (DSA)
DSA_GRAPH_EXTRACTION_PROMPT = """<role>
Bạn là chuyên gia phân tích tài liệu về Cấu trúc dữ liệu và Giải thuật, chuyên trích xuất thông tin có cấu trúc để xây dựng đồ thị tri thức phục vụ sinh câu hỏi trắc nghiệm. Bạn có chuyên môn đặc biệt trong việc trích xuất độ phức tạp thuật toán, công thức toán học, và chi tiết kỹ thuật về cấu trúc dữ liệu.
</role>

<critical_instruction>
🔥 CỰC KỲ QUAN TRỌNG: Trong DSA, bạn PHẢI trích xuất ĐẦY ĐỦ các thông tin sau:
- Độ phức tạp thời gian: O(n), O(log n), O(n²), O(n log n), O(2^n), Θ(n), Ω(n)
- Độ phức tạp không gian: Space complexity của từng thuật toán
- Công thức toán học: Công thức tính toán, công thức đệ quy, hệ thức truy hồi
- Điều kiện và ràng buộc: Pre-conditions, post-conditions, invariants
- Các phép toán: Insert, Delete, Search, Update và độ phức tạp của chúng
- Cấu trúc bộ nhớ: Cách tổ chức dữ liệu trong bộ nhớ, pointer, index
</critical_instruction>

<instructions>
Từ văn bản được cung cấp, trích xuất các thực thể và mối quan hệ để xây dựng đồ thị tri thức về Cấu trúc dữ liệu và Giải thuật. Tất cả nội dung được trích xuất phải được xuất ra bằng tiếng Việt.

1. Xác định các thực thể thuộc các loại sau (tập trung vào DSA):
   - data_structure: Cấu trúc dữ liệu (Ví dụ: "Array", "Linked List", "Binary Tree", "Hash Table", "Stack", "Queue")
   - algorithm: Thuật toán (Ví dụ: "Quick Sort", "Binary Search", "DFS", "BFS", "Dijkstra")
   - operation: Phép toán (Ví dụ: "Insert", "Delete", "Search", "Traversal", "Merge")
   - complexity: Độ phức tạp (Ví dụ: "O(n)", "O(log n)", "O(n²)", "O(n log n)")
   - property: Tính chất (Ví dụ: "Stability", "In-place", "Adaptivity", "Balance property")
   - technique: Kỹ thuật (Ví dụ: "Divide and Conquer", "Dynamic Programming", "Greedy", "Backtracking")
   - formula: Công thức (Ví dụ: "T(n) = 2T(n/2) + n", "F(n) = F(n-1) + F(n-2)")
   - condition: Điều kiện (Ví dụ: "Best case", "Worst case", "Average case", "Invariant")
   - problem: Bài toán (Ví dụ: "Sorting", "Searching", "Graph traversal", "Shortest path")

2. Xác định các mối quan hệ (tập trung vào DSA):
   - implements: Cài đặt (Thuật toán cài đặt cấu trúc dữ liệu)
   - uses: Sử dụng (Thuật toán sử dụng cấu trúc dữ liệu)
   - has_complexity: Có độ phức tạp (Thuật toán/phép toán có độ phức tạp)
   - has_property: Có tính chất (Cấu trúc/thuật toán có tính chất)
   - applies: Áp dụng (Thuật toán áp dụng kỹ thuật)
   - solves: Giải quyết (Thuật toán giải quyết bài toán)
   - requires: Yêu cầu (Phép toán yêu cầu điều kiện)
   - optimizes: Tối ưu hóa (Kỹ thuật tối ưu hóa thuật toán)
   - compares_with: So sánh với (Thuật toán so sánh với thuật toán khác)
   - derives_from: Dẫn xuất từ (Công thức dẫn xuất từ công thức khác)
   - guarantees: Đảm bảo (Thuật toán đảm bảo tính chất)

3. Yêu cầu mô tả chi tiết:
   - Mô tả thực thể: BẮT ĐẦU bằng "[Tên thực thể] là..." sau đó giải thích rõ ràng về vai trò, đặc điểm, độ phức tạp (nếu có), và ý nghĩa trong DSA
   - Đối với độ phức tạp: Luôn ghi rõ best case, average case, worst case
   - Đối với cấu trúc dữ liệu: Mô tả cách tổ chức, các phép toán cơ bản và độ phức tạp của chúng
   - Đối với thuật toán: Mô tả ý tưởng chính, các bước thực hiện, và phân tích độ phức tạp

4. Ví dụ minh họa:
[ENTITY]<|>Binary Search Tree<|>data_structure<|>Binary Search Tree là cấu trúc dữ liệu cây nhị phân trong đó mỗi node có tối đa 2 con, với tính chất: giá trị của node con trái nhỏ hơn node cha, giá trị node con phải lớn hơn node cha. BST hỗ trợ các phép toán Insert, Delete, Search với độ phức tạp trung bình O(log n) và worst case O(n) khi cây bị suy biến thành dạng list.[/ENTITY]
[ENTITY]<|>Quick Sort<|>algorithm<|>Quick Sort là thuật toán sắp xếp sử dụng kỹ thuật chia để trị (divide and conquer), chọn một phần tử làm pivot và phân hoạch mảng thành hai phần: phần tử nhỏ hơn pivot và phần tử lớn hơn pivot. Độ phức tạp: Best case O(n log n), Average case O(n log n), Worst case O(n²). Space complexity O(log n) do đệ quy.[/ENTITY]
[ENTITY]<|>O(log n)<|>complexity<|>O(log n) là độ phức tạp logarit, thể hiện thời gian thực thi tăng logarit theo kích thước đầu vào. Thường xuất hiện trong các thuật toán chia đôi không gian tìm kiếm như Binary Search, hoặc trong cấu trúc cây cân bằng với chiều cao log n.[/ENTITY]
[RELATIONSHIP]<|>Binary Search Tree<|>O(log n)<|>has_complexity<|>Binary Search Tree có độ phức tạp O(log n) cho các phép toán Insert, Delete, Search trong trường hợp cây cân bằng, vì chiều cao của cây cân bằng là log n với n là số node.[/RELATIONSHIP]
[RELATIONSHIP]<|>Quick Sort<|>Divide and Conquer<|>applies<|>Quick Sort áp dụng kỹ thuật Divide and Conquer bằng cách chia mảng thành các mảng con quanh pivot, giải quyết đệ quy các mảng con, và kết hợp kết quả mà không cần thêm bước merge.[/RELATIONSHIP]
</instructions>

<constraints>
- Chỉ trích xuất thông tin thực sự tồn tại trong văn bản
- Tên thực thể phải chính xác và nhất quán (giữ nguyên thuật ngữ tiếng Anh khi phù hợp)
- Công thức và ký hiệu độ phức tạp phải được bảo toàn CHÍNH XÁC
- Type phải viết thường
- Tất cả mô tả phải bằng tiếng Việt
- Ưu tiên trích xuất kiến thức có thể sinh câu hỏi trắc nghiệm về DSA
</constraints>

<output>
Định dạng: [ENTITY]<|>entity_name<|>entity_type<|>detailed_description[/ENTITY]
[RELATIONSHIP]<|>source<|>target<|>relationship_type<|>detailed_description[/RELATIONSHIP]
</output>

Ngữ cảnh: {input_text}

Kết quả:"""


# Prompt cho môn Học tăng cường (Reinforcement Learning)
RL_GRAPH_EXTRACTION_PROMPT = """<role>
Bạn là chuyên gia phân tích tài liệu về Học tăng cường (Reinforcement Learning), chuyên trích xuất thông tin có cấu trúc để xây dựng đồ thị tri thức phục vụ sinh câu hỏi trắc nghiệm. Bạn có chuyên môn đặc biệt trong việc trích xuất các phương trình Bellman, hàm giá trị, chính sách, và các thuật toán RL.
</role>

<critical_instruction>
🔥 CỰC KỲ QUAN TRỌNG: Trong Reinforcement Learning, bạn PHẢI trích xuất ĐẦY ĐỦ các thông tin sau:
- Phương trình Bellman: V(s) = max_a[R(s,a) + γ∑P(s'|s,a)V(s')], Q(s,a) = R(s,a) + γ∑P(s'|s,a)max_a'Q(s',a')
- Tham số: γ (discount factor), α (learning rate), ε (exploration rate), β (temperature)
- Hàm giá trị: Value function V(s), Q-function Q(s,a), Advantage function A(s,a)
- Chính sách: Policy π(a|s), optimal policy π*, deterministic/stochastic policy
- Thuật toán cập nhật: TD learning, Q-learning update rule, SARSA update
- MDP components: States S, Actions A, Rewards R, Transition probabilities P, Discount factor γ
- Convergence conditions: Điều kiện hội tụ của các thuật toán
</critical_instruction>

<instructions>
Từ văn bản được cung cấp, trích xuất các thực thể và mối quan hệ để xây dựng đồ thị tri thức về Reinforcement Learning. Tất cả nội dung được trích xuất phải được xuất ra bằng tiếng Việt.

1. Xác định các thực thể thuộc các loại sau (tập trung vào RL):
   - concept: Khái niệm RL (Ví dụ: "MDP", "Policy", "Value Function", "Exploration vs Exploitation")
   - algorithm: Thuật toán RL (Ví dụ: "Q-Learning", "SARSA", "DQN", "Policy Gradient", "Actor-Critic", "PPO")
   - component: Thành phần MDP (Ví dụ: "State", "Action", "Reward", "Transition", "Agent", "Environment")
   - equation: Phương trình (Ví dụ: "Bellman Equation", "TD Error", "Q-update rule", "Policy gradient theorem")
   - parameter: Tham số (Ví dụ: "γ (discount factor)", "α (learning rate)", "ε (epsilon)", "λ (trace decay)")
   - function: Hàm (Ví dụ: "V(s)", "Q(s,a)", "π(a|s)", "A(s,a)", "TD(λ)")
   - property: Tính chất (Ví dụ: "Convergence", "Optimality", "On-policy", "Off-policy", "Model-free")
   - technique: Kỹ thuật (Ví dụ: "Temporal Difference", "Monte Carlo", "Function Approximation", "Experience Replay")
   - problem: Bài toán (Ví dụ: "Credit Assignment", "Exploration-Exploitation Tradeoff", "Continuous Action Space")

2. Xác định các mối quan hệ (tập trung vào RL):
   - uses: Sử dụng (Thuật toán sử dụng phương trình/kỹ thuật)
   - optimizes: Tối ưu hóa (Thuật toán tối ưu hóa hàm/chính sách)
   - approximates: Xấp xỉ (Phương pháp xấp xỉ hàm giá trị)
   - updates: Cập nhật (Thuật toán cập nhật tham số/hàm)
   - converges_to: Hội tụ đến (Thuật toán hội tụ đến giá trị/chính sách)
   - balances: Cân bằng (Tham số cân bằng giữa các yếu tố)
   - controls: Kiểm soát (Tham số kiểm soát hành vi)
   - estimates: Ước lượng (Thuật toán ước lượng giá trị)
   - improves: Cải thiện (Thuật toán cải thiện chính sách)
   - evaluates: Đánh giá (Phương pháp đánh giá chính sách)
   - solves: Giải quyết (Thuật toán giải quyết bài toán)
   - requires: Yêu cầu (Thuật toán yêu cầu điều kiện/thành phần)

3. Yêu cầu mô tả chi tiết:
   - Mô tả thực thể: BẮT ĐẦU bằng "[Tên thực thể] là..." sau đó giải thích rõ ràng về vai trò, ý nghĩa toán học, và tầm quan trọng trong RL
   - Đối với phương trình: Ghi rõ công thức toán học, ý nghĩa của từng thành phần, và cách sử dụng
   - Đối với tham số: Mô tả ý nghĩa, phạm vi giá trị thông thường, và ảnh hưởng đến thuật toán
   - Đối với thuật toán: Mô tả ý tưởng chính, phương trình cập nhật, tính chất (on-policy/off-policy, model-free/model-based)

4. Ví dụ minh họa:
[ENTITY]<|>Q-Learning<|>algorithm<|>Q-Learning là thuật toán học tăng cường off-policy, model-free, sử dụng phương trình cập nhật Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)] để học hàm Q-function tối ưu. Q-Learning hội tụ đến Q* khi mỗi cặp (s,a) được thăm vô hạn lần và α thỏa mãn điều kiện Robbins-Monro.[/ENTITY]
[ENTITY]<|>Bellman Equation<|>equation<|>Bellman Equation là phương trình cơ bản trong RL biểu diễn mối quan hệ đệ quy của hàm giá trị: V(s) = max_a[R(s,a) + γ∑_s' P(s'|s,a)V(s')], trong đó V(s) là giá trị của state s, R(s,a) là reward tức thời, γ là discount factor, và P(s'|s,a) là xác suất chuyển state.[/ENTITY]
[ENTITY]<|>γ (discount factor)<|>parameter<|>γ (discount factor) là tham số trong khoảng [0,1] kiểm soát tầm quan trọng của reward tương lai so với reward tức thời. γ = 0 chỉ quan tâm reward tức thời, γ gần 1 cân nhắc nhiều reward dài hạn. γ ảnh hưởng đến tốc độ hội tụ và chính sách tối ưu.[/ENTITY]
[ENTITY]<|>ε-greedy<|>technique<|>ε-greedy là kỹ thuật exploration trong RL, với xác suất ε chọn action ngẫu nhiên (exploration), và xác suất 1-ε chọn action tốt nhất hiện tại (exploitation). ε thường được giảm dần theo thời gian (ε-decay) để chuyển từ exploration sang exploitation.[/ENTITY]
[RELATIONSHIP]<|>Q-Learning<|>Bellman Equation<|>uses<|>Q-Learning sử dụng Bellman Optimality Equation để cập nhật Q-values, cụ thể sử dụng phiên bản Q(s,a) = R(s,a) + γ max_a' Q(s',a') trong công thức cập nhật temporal difference.[/RELATIONSHIP]
[RELATIONSHIP]<|>γ (discount factor)<|>Value Function<|>controls<|>Discount factor γ kiểm soát cách Value Function tính toán tổng reward chiết khấu: V(s) = E[∑_{{t=0}}^∞ γ^t r_t]. γ nhỏ làm agent cận thị (myopic), γ lớn làm agent có tầm nhìn xa (far-sighted).[/RELATIONSHIP]
</instructions>

<constraints>
- Chỉ trích xuất thông tin thực sự tồn tại trong văn bản
- Tên thực thể phải chính xác (giữ nguyên thuật ngữ tiếng Anh và ký hiệu toán học)
- Phương trình toán học phải được bảo toàn CHÍNH XÁC với đầy đủ ký hiệu
- Type phải viết thường
- Tất cả mô tả phải bằng tiếng Việt
- Ưu tiên trích xuất kiến thức có thể sinh câu hỏi trắc nghiệm về RL
</constraints>

<output>
Định dạng: [ENTITY]<|>entity_name<|>entity_type<|>detailed_description[/ENTITY]
[RELATIONSHIP]<|>source<|>target<|>relationship_type<|>detailed_description[/RELATIONSHIP]
</output>

Ngữ cảnh: {input_text}

Kết quả:"""


# Prompt cho môn Học máy (Machine Learning)
ML_GRAPH_EXTRACTION_PROMPT = """<role>
Bạn là chuyên gia phân tích tài liệu về Học máy (Machine Learning), chuyên trích xuất thông tin có cấu trúc để xây dựng đồ thị tri thức phục vụ sinh câu hỏi trắc nghiệm. Bạn có chuyên môn đặc biệt trong việc trích xuất hàm loss, thuật toán tối ưu, công thức toán học, và kiến trúc mô hình.
</role>

<critical_instruction>
🔥 CỰC KỲ QUAN TRỌNG: Trong Machine Learning, bạn PHẢI trích xuất ĐẦY ĐỦ các thông tin sau:
- Hàm loss/objective: MSE, Cross-Entropy, Hinge Loss, L = 1/2||w||² + C∑ξᵢ
- Thuật toán tối ưu: Gradient Descent, SGD, Adam, công thức cập nhật w ← w - η∇L
- Công thức toán học: y = wx + b, σ(z) = 1/(1+e^(-z)), softmax, kernel functions
- Tham số mô hình: weights w, bias b, learning rate η, regularization λ
- Metrics: Accuracy, Precision, Recall, F1, AUC, RMSE, R²
- Kỹ thuật regularization: L1, L2, Dropout, Early Stopping
- Phương pháp đánh giá: Cross-validation, Train-test split, Confusion matrix
- Gradient và đạo hàm: ∂L/∂w, backpropagation formulas
</critical_instruction>

<instructions>
Từ văn bản được cung cấp, trích xuất các thực thể và mối quan hệ để xây dựng đồ thị tri thức về Machine Learning. Tất cả nội dung được trích xuất phải được xuất ra bằng tiếng Việt.

1. Xác định các thực thể thuộc các loại sau (tập trung vào ML):
   - model: Mô hình ML (Ví dụ: "Linear Regression", "Logistic Regression", "SVM", "Neural Network", "Random Forest")
   - algorithm: Thuật toán (Ví dụ: "Gradient Descent", "Backpropagation", "K-Means", "AdaBoost")
   - loss_function: Hàm loss (Ví dụ: "MSE", "Cross-Entropy", "Hinge Loss", "KL Divergence")
   - activation: Hàm kích hoạt (Ví dụ: "Sigmoid", "ReLU", "Tanh", "Softmax")
   - optimizer: Thuật toán tối ưu (Ví dụ: "SGD", "Adam", "RMSprop", "AdaGrad")
   - metric: Thước đo (Ví dụ: "Accuracy", "Precision", "Recall", "F1-Score", "AUC-ROC")
   - technique: Kỹ thuật (Ví dụ: "Regularization", "Normalization", "Data Augmentation", "Feature Engineering")
   - formula: Công thức (Ví dụ: "y = wx + b", "σ(z) = 1/(1+e^(-z))", "w ← w - η∇L")
   - parameter: Tham số (Ví dụ: "learning rate η", "regularization λ", "weights w", "bias b")
   - component: Thành phần (Ví dụ: "Layer", "Neuron", "Kernel", "Filter", "Feature map")
   - process: Quy trình (Ví dụ: "Training", "Validation", "Testing", "Feature extraction", "Data preprocessing")
   - problem: Vấn đề (Ví dụ: "Overfitting", "Underfitting", "Vanishing Gradient", "Class Imbalance")

2. Xác định các mối quan hệ (tập trung vào ML):
   - uses: Sử dụng (Mô hình sử dụng thuật toán/hàm)
   - optimizes: Tối ưu hóa (Optimizer tối ưu hóa loss function)
   - minimizes: Cực tiểu hóa (Thuật toán cực tiểu hóa hàm loss)
   - measures: Đo lường (Metric đo lường hiệu suất)
   - prevents: Ngăn chặn (Kỹ thuật ngăn chặn vấn đề)
   - computes: Tính toán (Công thức tính toán giá trị)
   - transforms: Biến đổi (Hàm biến đổi dữ liệu)
   - updates: Cập nhật (Thuật toán cập nhật tham số)
   - contains: Chứa (Mô hình chứa thành phần)
   - applies: Áp dụng (Thuật toán áp dụng kỹ thuật)
   - improves: Cải thiện (Kỹ thuật cải thiện hiệu suất)
   - evaluates: Đánh giá (Metric đánh giá mô hình)
   - regularizes: Điều chuẩn (Kỹ thuật điều chuẩn mô hình)
   - controls: Kiểm soát (Tham số kiểm soát hành vi)
   - derives_from: Dẫn xuất từ (Công thức dẫn xuất từ công thức khác)

3. Yêu cầu mô tả chi tiết:
   - Mô tả thực thể: BẮT ĐẦU bằng "[Tên thực thể] là..." sau đó giải thích rõ ràng về vai trò, công thức toán học (nếu có), và ý nghĩa trong ML
   - Đối với hàm loss: Ghi rõ công thức toán học, ý nghĩa, và khi nào sử dụng
   - Đối với mô hình: Mô tả kiến trúc, hàm mục tiêu, thuật toán training, và ứng dụng
   - Đối với tham số: Mô tả ý nghĩa, phạm vi giá trị, và ảnh hưởng đến mô hình
   - Đối với metrics: Công thức tính, ý nghĩa, và cách diễn giải

4. Ví dụ minh họa:
[ENTITY]<|>Support Vector Machine<|>model<|>Support Vector Machine là mô hình phân loại tìm siêu phẳng w^T x + b = 0 tối ưu để phân tách các lớp dữ liệu với margin tối đa. SVM tối thiểu hóa hàm mục tiêu L = 1/2||w||² + C∑ξᵢ với ràng buộc yᵢ(w^T xᵢ + b) ≥ 1 - ξᵢ, trong đó C là tham số regularization và ξᵢ là slack variables.[/ENTITY]
[ENTITY]<|>Cross-Entropy Loss<|>loss_function<|>Cross-Entropy Loss là hàm loss cho bài toán phân loại, tính bằng L = -∑ᵢ yᵢ log(ŷᵢ), trong đó yᵢ là nhãn thật và ŷᵢ là xác suất dự đoán. Cross-Entropy đo lường sự khác biệt giữa phân phối xác suất thật và dự đoán, nhỏ nhất khi dự đoán hoàn hảo.[/ENTITY]
[ENTITY]<|>Adam Optimizer<|>optimizer<|>Adam (Adaptive Moment Estimation) là thuật toán tối ưu kết hợp momentum và RMSprop, sử dụng công thức cập nhật: m_t = β₁m_(t-1) + (1-β₁)g_t, v_t = β₂v_(t-1) + (1-β₂)g_t², θ_t = θ_(t-1) - η·m_t/√(v_t + ε). Adam tự động điều chỉnh learning rate cho từng tham số với β₁ = 0.9, β₂ = 0.999 mặc định.[/ENTITY]
[ENTITY]<|>learning rate η<|>parameter<|>Learning rate η là tham số kiểm soát kích thước bước cập nhật trong gradient descent: w ← w - η∇L. η quá lớn gây dao động/phân kỳ, η quá nhỏ làm hội tụ chậm. Giá trị thường dùng: 0.001-0.1, thường được giảm dần theo thời gian (learning rate decay).[/ENTITY]
[ENTITY]<|>L2 Regularization<|>technique<|>L2 Regularization là kỹ thuật thêm penalty term λ||w||²/2 vào hàm loss để ngăn overfitting: L_total = L_original + λ||w||²/2. L2 khuyến khích weights nhỏ, phân phối đều, tạo mô hình smooth và generalize tốt hơn. λ lớn tăng regularization mạnh hơn.[/ENTITY]
[RELATIONSHIP]<|>Support Vector Machine<|>Hinge Loss<|>uses<|>Support Vector Machine sử dụng Hinge Loss làm hàm mục tiêu, được định nghĩa là max(0, 1 - yᵢ(w^T xᵢ + b)), để tối đa hóa margin giữa các lớp dữ liệu.[/RELATIONSHIP]
[RELATIONSHIP]<|>Adam Optimizer<|>Cross-Entropy Loss<|>minimizes<|>Adam Optimizer được sử dụng để cực tiểu hóa Cross-Entropy Loss bằng cách tính gradient ∂L/∂θ và cập nhật tham số với adaptive learning rates, giúp training neural networks hiệu quả.[/RELATIONSHIP]
[RELATIONSHIP]<|>L2 Regularization<|>Overfitting<|>prevents<|>L2 Regularization ngăn chặn Overfitting bằng cách penalize weights lớn thông qua term λ||w||²/2, buộc mô hình học các patterns tổng quát thay vì ghi nhớ training data.[/RELATIONSHIP]
</instructions>

<constraints>
- Chỉ trích xuất thông tin thực sự tồn tại trong văn bản
- Tên thực thể phải chính xác (giữ nguyên thuật ngữ tiếng Anh và ký hiệu toán học)
- Công thức toán học phải được bảo toàn CHÍNH XÁC với đầy đủ ký hiệu
- Type phải viết thường
- Tất cả mô tả phải bằng tiếng Việt
- Ưu tiên trích xuất kiến thức có thể sinh câu hỏi trắc nghiệm về ML
</constraints>

<output>
Định dạng: [ENTITY]<|>entity_name<|>entity_type<|>detailed_description[/ENTITY]
[RELATIONSHIP]<|>source<|>target<|>relationship_type<|>detailed_description[/RELATIONSHIP]
</output>

Ngữ cảnh: {input_text}

Kết quả:"""
