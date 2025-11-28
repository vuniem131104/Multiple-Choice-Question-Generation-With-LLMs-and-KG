# Học Máy (Machine Learning)

## Hồi Quy Tuyến Tính (Linear Regression)

### Giới Thiệu Về Hồi Quy Tuyến Tính

Hồi quy tuyến tính là một trong những kỹ thuật thống kê cơ bản và được sử dụng rộng rãi nhất trong học máy. Nó mô hình hóa mối quan hệ giữa một biến phụ thuộc (biến mục tiêu) và một hoặc nhiều biến độc lập (đặc trưng) bằng cách khớp một phương trình tuyến tính với dữ liệu quan sát được.

Hồi quy tuyến tính được ứng dụng rộng rãi trong nhiều lĩnh vực như:
- Dự đoán giá nhà dựa trên diện tích, vị trí, số phòng
- Dự báo doanh số bán hàng dựa trên ngân sách quảng cáo
- Phân tích tác động của các yếu tố đến kết quả kinh doanh
- Dự đoán nhiệt độ, lượng mưa trong khí tượng học
- Phân tích xu hướng thị trường chứng khoán

### Hồi Quy Tuyến Tính Đơn Giản

Hồi quy tuyến tính đơn giản liên quan đến một biến độc lập duy nhất và có thể được biểu diễn như sau:

$$y = \beta_0 + \beta_1x + \epsilon$$

Trong đó:
- $y$ là biến phụ thuộc (biến mục tiêu) - giá trị chúng ta muốn dự đoán
- $x$ là biến độc lập (đặc trưng) - biến đầu vào
- $\beta_0$ là hệ số chặn (intercept) - giao điểm với trục y
- $\beta_1$ là hệ số góc (slope) - độ dốc của đường thẳng
- $\epsilon$ là sai số ngẫu nhiên (error term)

**Các Khái Niệm Quan Trọng:**

**1. Phương Pháp Bình Phương Tối Thiểu (Ordinary Least Squares - OLS):**
- Đây là phương pháp phổ biến nhất để ước lượng các hệ số
- Mục tiêu: Tối thiểu hóa tổng bình phương của các phần dư (residuals)
- Phần dư là khoảng cách thẳng đứng giữa điểm dữ liệu thực tế và đường hồi quy

**2. Phần Dư (Residuals):**
$$e_i = y_i - \hat{y}_i$$
- Đo lường sự khác biệt giữa giá trị quan sát và giá trị dự đoán
- Phần dư nhỏ cho thấy mô hình khớp tốt với dữ liệu

**3. Hàm Chi Phí (Cost Function):**
$$J(\beta) = \frac{1}{2m}\sum_{i=1}^{m}(h_\beta(x^{(i)}) - y^{(i)})^2$$

Trong đó:
- $m$ là số lượng mẫu huấn luyện
- $h_\beta(x^{(i)})$ là giá trị dự đoán cho mẫu thứ $i$
- $y^{(i)}$ là giá trị thực tế

**4. Công Thức Tính Hệ Số:**

Hệ số góc: $\beta_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$

Hệ số chặn: $\beta_0 = \bar{y} - \beta_1\bar{x}$

Trong đó $\bar{x}$ và $\bar{y}$ là giá trị trung bình của $x$ và $y$.

**Ví Dụ Minh Họa:**
Giả sử chúng ta muốn dự đoán giá nhà (triệu đồng) dựa trên diện tích (m²):
- Dữ liệu: Diện tích [50, 60, 70, 80, 90], Giá [1500, 1800, 2100, 2400, 2700]
- Sau khi áp dụng OLS, ta có thể tìm được: $y = 300 + 30x$
- Diễn giải: Giá cơ bản là 300 triệu, mỗi m² tăng thêm 30 triệu

### Hồi Quy Tuyến Tính Bội

Khi xử lý nhiều đặc trưng, phương trình mở rộng thành:

$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n + \epsilon$$

**Ví dụ:** Dự đoán giá nhà với nhiều yếu tố:
$$Giá = \beta_0 + \beta_1 \times Diện\ tích + \beta_2 \times Số\ phòng + \beta_3 \times Khoảng\ cách\ trung\ tâm$$

**Dạng Ma Trận:**
$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

Trong đó:
- $\mathbf{y}$ là vector cột của các giá trị mục tiêu (kích thước $m \times 1$)
- $\mathbf{X}$ là ma trận đặc trưng (kích thước $m \times (n+1)$), bao gồm cột 1 cho hệ số chặn
- $\boldsymbol{\beta}$ là vector các hệ số (kích thước $(n+1) \times 1$)
- $\boldsymbol{\epsilon}$ là vector sai số

**Nghiệm Dạng Đóng (Closed-form Solution):**
$$\boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

**Ưu điểm của nghiệm dạng đóng:**
- Tính toán trực tiếp, không cần lặp
- Cho kết quả chính xác (không phụ thuộc tốc độ học)
- Phù hợp khi số lượng đặc trưng nhỏ (< 10,000)

**Nhược điểm:**
- Phức tạp tính toán: $O(n^3)$ với $n$ là số đặc trưng
- Yêu cầu $\mathbf{X}^T\mathbf{X}$ khả nghịch
- Không hiệu quả với dữ liệu lớn

### Các Giả Định Của Hồi Quy Tuyến Tính

Để hồi quy tuyến tính hoạt động tốt, cần thỏa mãn các giả định sau:

**1. Tính Tuyến Tính (Linearity):**
- Mối quan hệ giữa các đặc trưng và mục tiêu là tuyến tính
- Kiểm tra: Vẽ biểu đồ phân tán giữa $x$ và $y$
- Giải pháp nếu vi phạm: Biến đổi đặc trưng (log, căn bậc hai, đa thức)

**2. Tính Độc Lập (Independence):**
- Các quan sát độc lập với nhau
- Quan trọng với dữ liệu chuỗi thời gian
- Vi phạm: Tự tương quan (autocorrelation)
- Kiểm tra: Durbin-Watson test

**3. Phương Sai Đồng Nhất (Homoscedasticity):**
- Phương sai của phần dư không đổi theo giá trị dự đoán
- Kiểm tra: Vẽ biểu đồ phần dư vs giá trị dự đoán
- Nếu vi phạm (heteroscedasticity): Sử dụng weighted least squares hoặc biến đổi log

**4. Tính Chuẩn (Normality):**
- Phần dư tuân theo phân phối chuẩn
- Kiểm tra: Q-Q plot, Shapiro-Wilk test
- Quan trọng cho suy diễn thống kê (khoảng tin cậy, kiểm định giả thuyết)

**5. Không Có Đa Cộng Tuyến (No Multicollinearity):**
- Các đặc trưng không tương quan cao với nhau
- Kiểm tra: VIF (Variance Inflation Factor)
- VIF > 10 cho thấy đa cộng tuyến nghiêm trọng
- Giải pháp: Loại bỏ đặc trưng tương quan cao, PCA, regularization

**Công Thức VIF:**
$$VIF_j = \frac{1}{1 - R_j^2}$$
Trong đó $R_j^2$ là $R^2$ khi hồi quy $x_j$ với các đặc trưng còn lại.

### Tối Ưu Hóa Bằng Gradient Descent

Gradient Descent là phương pháp lặp để tìm hệ số tối ưu, đặc biệt hữu ích với dữ liệu lớn.

**Thuật Toán:**
$$\beta_j := \beta_j - \alpha\frac{\partial J(\beta)}{\partial\beta_j}$$

Trong đó:
- $\alpha$ là tốc độ học (learning rate)
- $\frac{\partial J(\beta)}{\partial\beta_j}$ là đạo hàm riêng của hàm chi phí

**Đạo Hàm Riêng:**
$$\frac{\partial J(\beta)}{\partial\beta_j} = \frac{1}{m}\sum_{i=1}^{m}(h_\beta(x^{(i)}) - y^{(i)})x_j^{(i)}$$

**Các Loại Gradient Descent:**

**1. Batch Gradient Descent:**
- Sử dụng toàn bộ tập dữ liệu trong mỗi lần cập nhật
- Ưu điểm: Hội tụ ổn định, tối ưu toàn cục
- Nhược điểm: Chậm với dữ liệu lớn
- Công thức cập nhật: $\beta := \beta - \alpha\nabla J(\beta)$

**2. Stochastic Gradient Descent (SGD):**
- Sử dụng từng mẫu một để cập nhật
- Ưu điểm: Nhanh, có thể thoát khỏi cực tiểu địa phương
- Nhược điểm: Dao động nhiều, không hội tụ chính xác
- Phù hợp: Dữ liệu rất lớn, học trực tuyến

**3. Mini-batch Gradient Descent:**
- Sử dụng các batch nhỏ (thường 32-256 mẫu)
- Cân bằng giữa tốc độ và độ ổn định
- Tận dụng tốt GPU/song song hóa
- Phổ biến nhất trong thực tế

**Lựa Chọn Learning Rate:**
- Quá nhỏ: Hội tụ chậm, tốn thời gian
- Quá lớn: Dao động, không hội tụ, có thể phân kỳ
- Thường bắt đầu với 0.01, 0.001, hoặc 0.0001
- Kỹ thuật: Learning rate decay (giảm dần theo thời gian)
- Learning rate schedule: $\alpha_t = \frac{\alpha_0}{1 + decay \times t}$

**Điều Kiện Dừng:**
- Số lần lặp tối đa
- Thay đổi hàm chi phí < ngưỡng
- Độ lớn gradient < ngưỡng

### Các Chỉ Số Đánh Giá Mô Hình

**1. Mean Squared Error (MSE) - Sai Số Bình Phương Trung Bình:**
$$MSE = \frac{1}{m}\sum_{i=1}^{m}(y_i - \hat{y}_i)^2$$
- Phạt nặng các lỗi lớn (do bình phương)
- Đơn vị: Bình phương của đơn vị mục tiêu
- Nhạy cảm với outliers

**2. Root Mean Squared Error (RMSE) - Căn Sai Số Bình Phương Trung Bình:**
$$RMSE = \sqrt{MSE}$$
- Cùng đơn vị với biến mục tiêu
- Dễ diễn giải hơn MSE
- Phổ biến trong các cuộc thi

**3. Mean Absolute Error (MAE) - Sai Số Tuyệt Đối Trung Bình:**
$$MAE = \frac{1}{m}\sum_{i=1}^{m}|y_i - \hat{y}_i|$$
- Ít nhạy cảm với outliers hơn MSE
- Diễn giải đơn giản: Sai số trung bình
- Không phạt nặng lỗi lớn

**4. R-squared (Hệ Số Xác Định):**
$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum_{i}(y_i - \hat{y}_i)^2}{\sum_{i}(y_i - \bar{y})^2}$$

- Tỷ lệ phương sai được giải thích bởi mô hình
- Giá trị: 0 đến 1 (hoặc âm nếu mô hình tệ hơn baseline)
- $R^2 = 1$: Mô hình hoàn hảo
- $R^2 = 0$: Mô hình không tốt hơn dự đoán bằng trung bình
- Diễn giải: $R^2 = 0.85$ nghĩa là 85% phương sai được giải thích

**5. Adjusted R-squared (R² Điều Chỉnh):**
$$R^2_{adj} = 1 - \frac{(1-R^2)(m-1)}{m-p-1}$$

Trong đó:
- $m$ là số mẫu
- $p$ là số đặc trưng
- Tính đến số lượng biến dự đoán
- Phạt việc thêm đặc trưng không cần thiết
- Tốt hơn $R^2$ khi so sánh các mô hình khác nhau

**6. Mean Absolute Percentage Error (MAPE):**
$$MAPE = \frac{100\%}{m}\sum_{i=1}^{m}\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$
- Sai số phần trăm trung bình
- Dễ diễn giải cho người không chuyên
- Vấn đề: Không xác định khi $y_i = 0$

### Kỹ Thuật Regularization

Regularization giúp giảm overfitting bằng cách thêm penalty vào hàm chi phí.

**1. Ridge Regression (L2 Regularization - Hồi Quy Ridge):**
$$J(\beta) = \frac{1}{2m}\sum_{i=1}^{m}(h_\beta(x^{(i)}) - y^{(i)})^2 + \lambda\sum_{j=1}^{n}\beta_j^2$$

**Đặc điểm:**
- Thêm penalty là tổng bình phương các hệ số
- Làm co nhỏ (shrink) các hệ số về gần 0
- Không đưa hệ số về chính xác 0
- Hiệu quả với đa cộng tuyến
- Nghiệm dạng đóng: $\boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$

**Khi nào sử dụng:**
- Nhiều đặc trưng tương quan
- Muốn giữ tất cả đặc trưng
- Dữ liệu có đa cộng tuyến

**2. Lasso Regression (L1 Regularization - Hồi Quy Lasso):**
$$J(\beta) = \frac{1}{2m}\sum_{i=1}^{m}(h_\beta(x^{(i)}) - y^{(i)})^2 + \lambda\sum_{j=1}^{n}|\beta_j|$$

**Đặc điểm:**
- Thêm penalty là tổng giá trị tuyệt đối các hệ số
- Có thể đưa một số hệ số về chính xác 0
- Thực hiện feature selection tự động
- Tạo ra mô hình sparse (thưa)
- Không có nghiệm dạng đóng

**Khi nào sử dụng:**
- Muốn loại bỏ đặc trưng không quan trọng
- Cần mô hình đơn giản, dễ diễn giải
- Có nhiều đặc trưng nhưng ít quan trọng

**3. Elastic Net:**
$$J(\beta) = \frac{1}{2m}\sum_{i=1}^{m}(h_\beta(x^{(i)}) - y^{(i)})^2 + \lambda_1\sum_{j=1}^{n}|\beta_j| + \lambda_2\sum_{j=1}^{n}\beta_j^2$$

**Đặc điểm:**
- Kết hợp L1 và L2
- Cân bằng giữa feature selection và shrinkage
- Tốt với các đặc trưng tương quan nhóm
- Ổn định hơn Lasso khi đặc trưng tương quan cao

**Tham số $\lambda$ (Lambda):**
- $\lambda = 0$: Không có regularization (hồi quy tuyến tính thông thường)
- $\lambda$ nhỏ: Ít regularization
- $\lambda$ lớn: Nhiều regularization, hệ số bị co nhỏ mạnh
- Chọn $\lambda$: Cross-validation

**So Sánh Ridge vs Lasso:**
| Tiêu chí | Ridge (L2) | Lasso (L1) |
|----------|-----------|------------|
| Feature Selection | Không | Có |
| Hệ số về 0 | Gần 0 | Chính xác 0 |
| Đa cộng tuyến | Tốt | Chọn ngẫu nhiên 1 trong nhóm |
| Nghiệm đóng | Có | Không |
| Mô hình | Dense | Sparse |

### Cân Nhắc Thực Tế

**1. Feature Scaling (Chuẩn Hóa Đặc Trưng):**

**Tại sao cần thiết:**
- Gradient descent hội tụ nhanh hơn
- Các đặc trưng có tầm ảnh hưởng công bằng
- Regularization hoạt động đúng (không thiên vị về đặc trưng có độ lớn lớn)

**Phương pháp:**

**Standardization (Z-score normalization):**
$$x_{scaled} = \frac{x - \mu}{\sigma}$$
- Kết quả: Trung bình = 0, độ lệch chuẩn = 1
- Phù hợp khi dữ liệu có phân phối gần chuẩn
- Không bị ảnh hưởng bởi outliers nhiều

**Min-Max Normalization:**
$$x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$$
- Kết quả: Giá trị trong khoảng [0, 1]
- Nhạy cảm với outliers
- Phù hợp khi cần giới hạn trong khoảng cụ thể

**2. Phát Hiện Outliers:**

**Phương pháp:**
- **Residual plots:** Vẽ biểu đồ phần dư
- **Cook's distance:** Đo lường ảnh hưởng của từng điểm
  - $D_i > \frac{4}{n}$ cho thấy điểm có ảnh hưởng cao
- **Leverage:** Điểm xa trung tâm dữ liệu
- **Studentized residuals:** Phần dư chuẩn hóa

**Xử lý outliers:**
- Kiểm tra xem có phải lỗi dữ liệu không
- Xem xét loại bỏ hoặc biến đổi
- Sử dụng robust regression (ít nhạy cảm với outliers)

**3. Feature Engineering (Kỹ Thuật Đặc Trưng):**

**Polynomial Features (Đặc trưng đa thức):**
- Tạo mối quan hệ phi tuyến từ đặc trưng tuyến tính
- Ví dụ: $x_1, x_2 \rightarrow x_1, x_2, x_1^2, x_1x_2, x_2^2$
- Tăng khả năng biểu diễn nhưng dễ overfitting

**Interaction terms (Tương tác):**
- Tích của hai đặc trưng
- Ví dụ: Diện tích × Vị trí trong dự đoán giá nhà

**Logarithmic transformation:**
- Giảm skewness (độ lệch)
- Xử lý mối quan hệ exponential
- Ví dụ: Thu nhập, giá nhà thường lệch phải

**4. Cross-Validation (Kiểm Định Chéo):**

**K-Fold Cross-Validation:**
- Chia dữ liệu thành k phần
- Lần lượt sử dụng mỗi phần làm validation set
- Trung bình kết quả từ k lần
- Thường dùng k = 5 hoặc k = 10

**Lợi ích:**
- Đánh giá chính xác hơn
- Sử dụng toàn bộ dữ liệu cho cả training và validation
- Phát hiện overfitting/underfitting
- Chọn hyperparameter tối ưu

**5. Chẩn Đoán Mô Hình:**

**Underfitting (High Bias):**
- Training error cao
- Validation error cao
- Mô hình quá đơn giản
- Giải pháp: Thêm đặc trưng, tăng độ phức tạp, giảm regularization

**Overfitting (High Variance):**
- Training error thấp
- Validation error cao (chênh lệch lớn)
- Mô hình quá phức tạp
- Giải pháp: Thêm dữ liệu, regularization, giảm đặc trưng, early stopping

**Good fit:**
- Training error thấp
- Validation error thấp
- Chênh lệch nhỏ giữa hai errors


---

## Phân Loại (Classification)

### Giới Thiệu Về Phân Loại

Phân loại là một tác vụ học có giám sát trong đó mục tiêu là dự đoán nhãn lớp rời rạc. Khác với hồi quy dự đoán giá trị liên tục, phân loại gán các đầu vào vào các danh mục được định nghĩa trước.

**Ứng dụng thực tế:**
- Phát hiện thư rác (spam/không spam)
- Chẩn đoán bệnh (bệnh/không bệnh)
- Nhận dạng chữ viết tay
- Phân tích cảm xúc (tích cực/tiêu cực/trung lập)
- Phát hiện gian lận thẻ tín dụng
- Nhận dạng khuôn mặt
- Phân loại văn bản, hình ảnh

### Các Loại Bài Toán Phân Loại

**1. Phân Loại Nhị Phân (Binary Classification):**
- Hai lớp duy nhất
- Ví dụ: Email spam/không spam, Bệnh/khỏe mạnh
- Mã hóa nhãn: 0 và 1, hoặc -1 và +1

**2. Phân Loại Đa Lớp (Multiclass Classification):**
- Nhiều hơn hai lớp
- Mỗi mẫu thuộc đúng một lớp
- Ví dụ: Nhận dạng chữ số (0-9), Phân loại loại hoa
- Mã hóa nhãn: One-hot encoding

**3. Phân Loại Đa Nhãn (Multilabel Classification):**
- Mỗi mẫu có thể thuộc nhiều lớp
- Ví dụ: Gắn thẻ bài viết (công nghệ, kinh tế, chính trị), Phân loại thể loại phim

### Hồi Quy Logistic (Logistic Regression)

Mặc dù có tên là "regression", hồi quy logistic là thuật toán phân loại mô hình hóa xác suất của kết quả nhị phân.

**Hàm Sigmoid (Logistic Function):**
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Trong đó: $z = \beta_0 + \beta_1x_1 + ... + \beta_nx_n = \beta^Tx$

**Đặc điểm hàm Sigmoid:**
- Miền giá trị: $(0, 1)$ - phù hợp để biểu diễn xác suất
- $\sigma(0) = 0.5$
- $\sigma(z) \to 1$ khi $z \to \infty$
- $\sigma(z) \to 0$ khi $z \to -\infty$
- Đạo hàm: $\sigma'(z) = \sigma(z)(1 - \sigma(z))$

**Diễn Giải:**
$$P(y=1|x) = \sigma(\beta^Tx) = \frac{1}{1 + e^{-\beta^Tx}}$$
- Dự đoán xác suất lớp dương (y=1)
- Nếu $P(y=1|x) \geq 0.5$: Dự đoán lớp 1
- Nếu $P(y=1|x) < 0.5$: Dự đoán lớp 0

**Quyết Định Ranh Giới (Decision Boundary):**
- Tuyến tính trong không gian đặc trưng: $\beta^Tx = 0$
- Phi tuyến có thể đạt được bằng polynomial features
- Ngưỡng quyết định có thể điều chỉnh (không nhất thiết 0.5)

**Hàm Chi Phí (Cross-Entropy Loss):**
$$J(\beta) = -\frac{1}{m}\sum_{i=1}^{m}[y^{(i)}\log(h_\beta(x^{(i)})) + (1-y^{(i)})\log(1-h_\beta(x^{(i)}))]$$

**Lý do không dùng MSE:**
- MSE với sigmoid tạo hàm non-convex
- Nhiều cực tiểu địa phương
- Gradient descent khó hội tụ

**Cross-entropy:**
- Hàm convex
- Gradient descent hội tụ toàn cục
- Phạt nặng dự đoán sai với confidence cao

**Tối Ưu Hóa:**
- Gradient descent (hoặc các biến thể)
- Đạo hàm: $\frac{\partial J}{\partial\beta_j} = \frac{1}{m}\sum_{i=1}^{m}(h_\beta(x^{(i)}) - y^{(i)})x_j^{(i)}$
- Giống với linear regression nhưng $h_\beta$ khác

**Regularization trong Logistic Regression:**

**L2 (Ridge):**
$$J(\beta) = -\frac{1}{m}\sum_{i=1}^{m}[y^{(i)}\log(h_\beta(x^{(i)})) + (1-y^{(i)})\log(1-h_\beta(x^{(i)}))] + \frac{\lambda}{2m}\sum_{j=1}^{n}\beta_j^2$$

**L1 (Lasso):**
$$J(\beta) = -\frac{1}{m}\sum_{i=1}^{m}[y^{(i)}\log(h_\beta(x^{(i)})) + (1-y^{(i)})\log(1-h_\beta(x^{(i)}))] + \frac{\lambda}{m}\sum_{j=1}^{n}|\beta_j|$$

### Phân Loại Đa Lớp

**1. One-vs-Rest (OvR) / One-vs-All (OvA):**
- Huấn luyện K bộ phân loại nhị phân cho K lớp
- Mỗi bộ phân loại: Một lớp vs tất cả lớp còn lại
- Dự đoán: Chọn lớp có confidence cao nhất
- Ưu điểm: Đơn giản, phù hợp với mọi thuật toán nhị phân
- Nhược điểm: Mất cân bằng lớp, K mô hình riêng biệt

**Ví dụ:** 3 lớp (A, B, C)
- Mô hình 1: A vs (B, C)
- Mô hình 2: B vs (A, C)
- Mô hình 3: C vs (A, B)

**2. One-vs-One (OvO):**
- Huấn luyện $\frac{K(K-1)}{2}$ bộ phân loại nhị phân
- Mỗi cặp lớp có một bộ phân loại
- Dự đoán: Voting - lớp thắng nhiều nhất
- Ưu điểm: Mỗi mô hình đơn giản hơn, cân bằng hơn
- Nhược điểm: Nhiều mô hình (phức tạp khi K lớn)

**Ví dụ:** 3 lớp (A, B, C)
- Mô hình 1: A vs B
- Mô hình 2: A vs C
- Mô hình 3: B vs C

**3. Softmax Regression (Multinomial Logistic Regression):**

Mở rộng trực tiếp của logistic regression cho đa lớp.

**Công thức:**
$$P(y=k|x) = \frac{e^{z_k}}{\sum_{j=1}^{K}e^{z_j}}$$

Trong đó: $z_k = \beta_k^Tx$ với $\beta_k$ là vector hệ số cho lớp $k$

**Đặc điểm:**
- Tổng các xác suất = 1: $\sum_{k=1}^{K}P(y=k|x) = 1$
- Output là phân phối xác suất trên tất cả lớp
- Huấn luyện đồng thời tất cả lớp

**Hàm chi phí (Categorical Cross-Entropy):**
$$J(\beta) = -\frac{1}{m}\sum_{i=1}^{m}\sum_{k=1}^{K}y_k^{(i)}\log(P(y=k|x^{(i)}))$$

Trong đó $y_k^{(i)}$ là one-hot encoding của nhãn.

**Lựa chọn giữa OvR, OvO, và Softmax:**
- **Softmax:** Tốt nhất khi cần xác suất, K không quá lớn
- **OvR:** Đơn giản, hiệu quả với K lớn
- **OvO:** Tốt với SVM, K nhỏ/trung bình

### Naive Bayes Classifier (Bộ Phân Loại Naive Bayes)

Dựa trên định lý Bayes với giả định "ngây thơ" (naive) về tính độc lập đặc trưng.

**Định Lý Bayes:**
$$P(C_k|x) = \frac{P(x|C_k)P(C_k)}{P(x)}$$

Trong đó:
- $P(C_k|x)$: Xác suất hậu nghiệm (posterior) - xác suất lớp $C_k$ cho trước $x$
- $P(x|C_k)$: Likelihood - xác suất của $x$ trong lớp $C_k$
- $P(C_k)$: Xác suất tiên nghiệm (prior) của lớp $C_k$
- $P(x)$: Evidence - xác suất của $x$

**Giả Định Naive (Độc Lập Điều Kiện):**
$$P(x_1, x_2, ..., x_n|C_k) = \prod_{i=1}^{n}P(x_i|C_k)$$

Các đặc trưng độc lập với nhau khi biết lớp.

**Công Thức Đầy Đủ:**
$$P(C_k|x_1,...,x_n) = \frac{P(C_k)\prod_{i=1}^{n}P(x_i|C_k)}{P(x_1,...,x_n)}$$

**Quyết Định:**
$$\hat{y} = \arg\max_{k} P(C_k)\prod_{i=1}^{n}P(x_i|C_k)$$

Không cần tính $P(x)$ vì nó giống nhau cho tất cả lớp.

**Các Biến Thể:**

**1. Gaussian Naive Bayes:**
- Cho đặc trưng liên tục
- Giả định phân phối Gaussian (chuẩn)
$$P(x_i|C_k) = \frac{1}{\sqrt{2\pi\sigma_k^2}}\exp\left(-\frac{(x_i-\mu_k)^2}{2\sigma_k^2}\right)$$
- Ước lượng $\mu_k$ (mean) và $\sigma_k^2$ (variance) từ dữ liệu
- Ứng dụng: Phân loại văn bản, nhận dạng mẫu

**2. Multinomial Naive Bayes:**
- Cho đếm rời rạc (word counts, frequencies)
- Phân phối đa thức
$$P(x_i|C_k) = \frac{N_{ki} + \alpha}{N_k + \alpha n}$$
  - $N_{ki}$: Số lần đặc trưng $i$ xuất hiện trong lớp $k$
  - $N_k$: Tổng số đếm trong lớp $k$
  - $\alpha$: Laplace smoothing (thường = 1)
- Ứng dụng: Phân loại văn bản, phân tích cảm xúc, lọc spam

**3. Bernoulli Naive Bayes:**
- Cho đặc trưng nhị phân (có/không)
- Phân phối Bernoulli
$$P(x_i|C_k) = P(i|C_k)x_i + (1-P(i|C_k))(1-x_i)$$
- Tính cả việc đặc trưng xuất hiện và không xuất hiện
- Ứng dụng: Phân loại văn bản với binary features

**Ưu Điểm:**
- Nhanh, hiệu quả
- Hoạt động tốt với dữ liệu nhỏ
- Dễ triển khai và diễn giải
- Hoạt động tốt với nhiều đặc trưng
- Không nhạy cảm với đặc trưng không liên quan

**Nhược Điểm:**
- Giả định độc lập hiếm khi đúng trong thực tế
- "Zero frequency problem" cần smoothing
- Ước lượng xác suất có thể không chính xác
- Không tốt khi đặc trưng tương quan

**Laplace Smoothing:**
Xử lý vấn đề xác suất = 0:
$$P(x_i|C_k) = \frac{count(x_i, C_k) + \alpha}{count(C_k) + \alpha \times |V|}$$

### k-Nearest Neighbors (k-NN) - K Láng Giềng Gần Nhất

Phương pháp non-parametric phân loại dựa trên đa số vote của k láng giềng gần nhất.

**Thuật Toán:**
1. Tính khoảng cách từ điểm cần phân loại đến tất cả điểm huấn luyện
2. Chọn k điểm gần nhất
3. Vote: Lớp xuất hiện nhiều nhất trong k láng giềng
4. Gán nhãn lớp đó cho điểm mới

**Các Độ Đo Khoảng Cách:**

**1. Euclidean Distance (Khoảng cách Euclid):**
$$d(x,y) = \sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}$$
- Phổ biến nhất
- Khoảng cách đường thẳng
- Nhạy cảm với scale của đặc trưng

**2. Manhattan Distance (Khoảng cách Manhattan):**
$$d(x,y) = \sum_{i=1}^{n}|x_i-y_i|$$
- Khoảng cách theo lưới đô thị
- Ít nhạy cảm với outliers
- Tốt cho dữ liệu high-dimensional

**3. Minkowski Distance:**
$$d(x,y) = \left(\sum_{i=1}^{n}|x_i-y_i|^p\right)^{1/p}$$
- Tổng quát hóa Euclidean (p=2) và Manhattan (p=1)
- p=∞: Chebyshev distance

**4. Cosine Similarity:**
$$similarity = \frac{x \cdot y}{||x|| \times ||y||}$$
- Đo góc giữa vectors
- Tốt cho văn bản, high-dimensional sparse data
- Không phụ thuộc vào độ lớn

**5. Hamming Distance:**
- Số vị trí khác nhau giữa hai chuỗi
- Cho dữ liệu categorical hoặc binary

**Chọn Giá Trị k:**

**k quá nhỏ (k=1):**
- Nhạy cảm với noise
- Overfitting
- Decision boundary phức tạp, không mượt

**k quá lớn:**
- Underfitting
- Decision boundary quá mượt
- Tính toán chậm
- Có thể bị ảnh hưởng bởi lớp đa số

**Lựa chọn k tối ưu:**
- Cross-validation
- Thử các giá trị k khác nhau (1, 3, 5, 7, 11, ...)
- Chọn k lẻ để tránh tie trong binary classification
- Thường k = √n (n là số mẫu training)
- Elbow method: Vẽ error vs k

**Weighted k-NN:**
- Gán trọng số cho láng giềng dựa trên khoảng cách
- Láng giềng gần hơn có ảnh hưởng lớn hơn
$$weight = \frac{1}{distance}$$ hoặc $$weight = e^{-distance}$$

**Ưu Điểm:**
- Đơn giản, trực quan
- Không có giai đoạn training (lazy learning)
- Tự nhiên xử lý đa lớp
- Hiệu quả với decision boundary phức tạp
- Không giả định về phân phối dữ liệu

**Nhược Điểm:**
- Dự đoán chậm (O(n) cho mỗi dự đoán)
- Yêu cầu lưu trữ toàn bộ training data
- Nhạy cảm với scale của đặc trưng (cần scaling)
- Hiệu suất giảm với high-dimensional data (curse of dimensionality)
- Không xử lý tốt imbalanced data
- Khó xử lý missing values

**Tối Ưu Hóa k-NN:**
- **KD-Tree, Ball Tree:** Cấu trúc dữ liệu để tìm kiếm nhanh
- **Approximate Nearest Neighbors:** Hy sinh chút độ chính xác để tăng tốc
- **Feature Selection:** Giảm dimensionality
- **Dimensionality Reduction:** PCA, t-SNE

### Các Chỉ Số Đánh Giá Phân Loại

**Ma Trận Nhầm Lẫn (Confusion Matrix):**

```
                    Dự Đoán
                Positive  Negative
Thực Tế  Pos      TP        FN
         Neg      FP        TN
```

- **TP (True Positive):** Dự đoán đúng lớp dương
- **TN (True Negative):** Dự đoán đúng lớp âm
- **FP (False Positive):** Dự đoán sai là dương (Type I error)
- **FN (False Negative):** Dự đoán sai là âm (Type II error)

**Các Chỉ Số Chính:**

**1. Accuracy (Độ Chính Xác):**
$$Accuracy = \frac{TP+TN}{TP+TN+FP+FN}$$

- Tỷ lệ dự đoán đúng tổng thể
- Không phù hợp với imbalanced data
- Ví dụ: 95% accuracy nghe tốt nhưng vô nghĩa nếu 95% data thuộc 1 lớp

**2. Precision (Độ Chính Xác Dương):**
$$Precision = \frac{TP}{TP+FP}$$

- Trong các dự đoán dương, bao nhiêu thực sự dương?
- Quan trọng khi cost của FP cao
- Ví dụ: Phát hiện spam (không muốn email quan trọng bị đánh dấu spam)

**3. Recall/Sensitivity/True Positive Rate (Độ Bao Phủ):**
$$Recall = \frac{TP}{TP+FN}$$

- Trong các mẫu dương thực tế, bao nhiêu được phát hiện?
- Quan trọng khi cost của FN cao
- Ví dụ: Chẩn đoán bệnh (không muốn bỏ sót bệnh nhân)

**4. Specificity/True Negative Rate (Độ Đặc Hiệu):**
$$Specificity = \frac{TN}{TN+FP}$$

- Trong các mẫu âm thực tế, bao nhiêu được phát hiện đúng?
- Bổ sung cho recall

**5. F1-Score:**
$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

- Trung bình điều hòa của Precision và Recall
- Cân bằng giữa Precision và Recall
- Tốt cho imbalanced data
- F1 = 1: Hoàn hảo, F1 = 0: Tệ nhất

**6. F-Beta Score:**
$$F_\beta = (1 + \beta^2) \times \frac{Precision \times Recall}{\beta^2 \times Precision + Recall}$$

- $\beta < 1$: Ưu tiên Precision
- $\beta > 1$: Ưu tiên Recall
- $\beta = 1$: F1-Score

**7. Matthews Correlation Coefficient (MCC):**
$$MCC = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$$

- Giá trị: -1 đến +1
- +1: Dự đoán hoàn hảo
- 0: Ngẫu nhiên
- -1: Không đồng ý hoàn toàn
- Tốt cho imbalanced data

**Đường Cong ROC và AUC:**

**ROC Curve (Receiver Operating Characteristic):**
- Trục X: False Positive Rate = $\frac{FP}{FP+TN}$ = 1 - Specificity
- Trục Y: True Positive Rate = Recall = $\frac{TP}{TP+FN}$
- Vẽ với các ngưỡng threshold khác nhau
- Cho thấy trade-off giữa TPR và FPR

**AUC (Area Under Curve):**
- Diện tích dưới đường cong ROC
- Giá trị: 0 đến 1
- AUC = 1: Phân loại hoàn hảo
- AUC = 0.5: Phân loại ngẫu nhiên
- AUC < 0.5: Tệ hơn ngẫu nhiên
- Không bị ảnh hưởng bởi threshold
- Đo khả năng phân biệt giữa các lớp

**Diễn giải AUC:**
- 0.9-1.0: Xuất sắc
- 0.8-0.9: Tốt
- 0.7-0.8: Chấp nhận được
- 0.6-0.7: Kém
- 0.5-0.6: Thất bại

**Đường Cong Precision-Recall:**
- Trục X: Recall
- Trục Y: Precision
- Tốt cho imbalanced data
- Tập trung vào lớp dương
- AUPRC (Area Under Precision-Recall Curve)

**Khi nào dùng gì:**
- **Balanced data:** ROC-AUC
- **Imbalanced data:** Precision-Recall Curve, F1-Score, MCC
- **Cost-sensitive:** Tùy chỉnh threshold, F-beta

**Lựa Chọn Threshold:**
- Default: 0.5
- Điều chỉnh dựa trên business requirements
- Tăng threshold: Tăng Precision, giảm Recall
- Giảm threshold: Tăng Recall, giảm Precision

### Xử Lý Dữ Liệu Mất Cân Bằng (Imbalanced Data)

Khi một lớp chiếm đa số (ví dụ: 95% negative, 5% positive).

**Vấn Đề:**
- Mô hình thiên vị về lớp đa số
- Accuracy cao nhưng không phát hiện được lớp thiểu số
- Mô hình có thể chỉ dự đoán lớp đa số

**1. Resampling Techniques:**

**Oversampling (Lấy Mẫu Tăng):**
- Tăng số lượng mẫu lớp thiểu số
- **Random Oversampling:** Nhân đôi mẫu thiểu số
  - Dễ triển khai
  - Nguy cơ overfitting
  
- **SMOTE (Synthetic Minority Over-sampling Technique):**
  - Tạo mẫu synthetic từ kNN
  - Nội suy giữa các mẫu thiểu số
  - Công thức: $x_{new} = x_i + \lambda \times (x_{nn} - x_i)$
  - $\lambda \in [0,1]$, $x_{nn}$ là láng giềng gần
  - Giảm overfitting hơn random oversampling

- **ADASYN (Adaptive Synthetic Sampling):**
  - Tập trung vào mẫu khó phân loại
  - Tạo nhiều mẫu hơn ở vùng khó

**Undersampling (Lấy Mẫu Giảm):**
- Giảm số lượng mẫu lớp đa số
- **Random Undersampling:** Loại bỏ ngẫu nhiên
  - Nhanh, đơn giản
  - Mất thông tin
  
- **Tomek Links:** Loại bỏ mẫu biên
- **NearMiss:** Chọn mẫu đa số gần thiểu số
- **Cluster Centroids:** K-means cho lớp đa số

**Kết Hợp Over và Under:**
- SMOTE + Tomek Links
- SMOTE + ENN (Edited Nearest Neighbors)

**2. Class Weights (Trọng Số Lớp):**
- Gán trọng số cao hơn cho lớp thiểu số
- Penalty cho misclassification của thiểu số lớn hơn
$$w_k = \frac{n_{samples}}{n_{classes} \times n_{samples\_k}}$$
- Tích hợp trong hầu hết thuật toán (sklearn: class_weight='balanced')

**3. Ensemble Methods:**

**Balanced Random Forest:**
- Bootstrap undersampling cho mỗi tree
- Cân bằng classes trong mỗi tree

**EasyEnsemble:**
- Nhiều balanced subsets
- AdaBoost trên mỗi subset

**BalancedBagging:**
- Undersampling + Bagging

**4. Anomaly Detection Approach:**
- Xem lớp thiểu số như anomaly
- One-class SVM, Isolation Forest
- Học chỉ từ lớp đa số

**5. Cost-Sensitive Learning:**
- Định nghĩa cost matrix
- Misclassification cost khác nhau cho mỗi lớp
- Tối ưu hóa total cost thay vì accuracy

**6. Ensemble of Different Techniques:**
- Kết hợp nhiều phương pháp
- Voting hoặc stacking

**Best Practices:**
- Luôn dùng stratified splits
- Đánh giá bằng F1, AUC, không phải accuracy
- Cross-validation với stratification
- Hiểu business context (cost của FP vs FN)

### Phân Loại Đa Nhãn (Multi-label Classification)

Mỗi mẫu có thể thuộc nhiều lớp đồng thời.

**Ví dụ:**
- Gắn thẻ bài viết: [Technology, Politics, Economy]
- Phân loại phim: [Action, Comedy, Romance]
- Chẩn đoán bệnh: [Diabetes, Hypertension, Obesity]

**Approaches:**

**1. Binary Relevance:**
- Huấn luyện N bộ phân loại nhị phân độc lập (N là số nhãn)
- Mỗi bộ phân loại: Nhãn có/không
- Ưu điểm: Đơn giản, dễ triển khai
- Nhược điểm: Bỏ qua tương quan giữa nhãn

**2. Classifier Chains:**
- Chuỗi các bộ phân loại nhị phân
- Mỗi bộ phân loại sử dụng dự đoán của bộ trước làm input
- Mô hình phụ thuộc giữa nhãn
- Nhược điểm: Phụ thuộc vào thứ tự nhãn

**3. Label Powerset:**
- Xem mỗi tổ hợp nhãn unique như một lớp
- Chuyển thành multiclass classification
- Ưu điểm: Mô hình tương quan nhãn
- Nhược điểm: Số lớp = $2^N$ (exponential), nhiều lớp hiếm

**4. Multi-label k-NN:**
- Mở rộng k-NN cho đa nhãn
- Tính toán tần suất nhãn trong k láng giềng
- Threshold để quyết định nhãn

**Evaluation Metrics cho Multi-label:**

**1. Hamming Loss:**
$$HammingLoss = \frac{1}{N \times L}\sum_{i=1}^{N}\sum_{j=1}^{L}XOR(y_{ij}, \hat{y}_{ij})$$
- Tỷ lệ nhãn bị phân loại sai
- Càng nhỏ càng tốt

**2. Subset Accuracy:**
- Tỷ lệ mẫu có tất cả nhãn đúng
- Strict, yêu cầu exact match

**3. Precision, Recall, F1 (Micro/Macro):**
- **Micro:** Tính toán global (tổng TP, FP, FN)
- **Macro:** Trung bình trên tất cả nhãn
- **Weighted:** Trọng số theo số lượng mẫu

**4. Jaccard Similarity:**
$$Jaccard = \frac{|Y \cap \hat{Y}|}{|Y \cup \hat{Y}|}$$
- Đo overlap giữa nhãn thực và dự đoán

---

---

## Cây Quyết Định (Decision Tree)

### Giới Thiệu Về Cây Quyết Định

Cây quyết định là thuật toán học có giám sát đa năng có thể thực hiện cả tác vụ phân loại và hồi quy. Chúng học các quy tắc quyết định từ các đặc trưng để dự đoán giá trị mục tiêu thông qua cấu trúc dạng cây.

**Ứng dụng thực tế:**
- Chẩn đoán y tế (chuỗi quyết định dựa trên triệu chứng)
- Đánh giá rủi ro tín dụng
- Dự đoán churn khách hàng
- Phát hiện gian lận
- Hệ thống chuyên gia
- Phân loại email spam

**Tại sao gọi là "cây":**
- Cấu trúc phân cấp giống cây ngược
- Gốc ở trên, lá ở dưới
- Quyết định được đưa ra tại mỗi nút nội bộ
- Kết quả cuối cùng ở nút lá

### Cấu Trúc Cây

**1. Nút Gốc (Root Node):**
- Nút trên cùng đại diện cho toàn bộ tập dữ liệu
- Chứa tất cả mẫu training
- Điểm bắt đầu của quá trình quyết định
- Có phân chia đầu tiên dựa trên đặc trưng quan trọng nhất

**2. Nút Nội Bộ (Internal Nodes):**
- Các nút quyết định dựa trên kiểm tra đặc trưng
- Mỗi nút thực hiện một câu hỏi yes/no về đặc trưng
- Ví dụ: "Tuổi > 30?", "Thu nhập < 50,000?"
- Chia dữ liệu thành các tập con

**3. Nhánh (Branches):**
- Kết quả của các quyết định
- Kết nối nút cha với nút con
- Đại diện cho giá trị hoặc phạm vi giá trị của đặc trưng

**4. Nút Lá (Leaf Nodes):**
- Nút cuối cùng không có nhánh con
- Chứa dự đoán cuối cùng
- Phân loại: Nhãn lớp
- Hồi quy: Giá trị số

**Ví dụ minh họa - Quyết định mua nhà:**
```
                 [Thu nhập > 50K?]
                /                 \
            YES                    NO
           /                         \
   [Tuổi > 30?]                [Không mua]
    /        \
  YES        NO
  /            \
[Mua]      [Thuê]
```

### Xây Dựng Cây Quyết Định

**Tiêu Chí Phân Chia (Splitting Criteria):**

Mục tiêu: Tìm phân chia tốt nhất làm tăng "độ thuần khiết" (purity) của các tập con.

**Cho Phân Loại:**

**1. Gini Impurity (Chỉ Số Gini):**
$$Gini(t) = 1 - \sum_{i=1}^{C}p_i^2$$

Trong đó:
- $p_i$ là tỷ lệ mẫu thuộc lớp $i$ tại nút $t$
- $C$ là số lớp
- Gini = 0: Nút hoàn toàn thuần khiết (tất cả mẫu cùng lớp)
- Gini = 0.5: Nút hỗn loạn nhất (phân bố đều giữa các lớp)

**Ví dụ:**
- Nút có 100 mẫu: 80 lớp A, 20 lớp B
- $Gini = 1 - (0.8^2 + 0.2^2) = 1 - (0.64 + 0.04) = 0.32$

**2. Entropy và Information Gain (Độ Lợi Thông Tin):**
$$Entropy(t) = -\sum_{i=1}^{C}p_i\log_2(p_i)$$

- Entropy đo lường độ hỗn loạn/không chắc chắn
- Entropy = 0: Thuần khiết hoàn toàn
- Entropy cao: Hỗn loạn

**Information Gain:**
$$IG(D_p, f) = Entropy(D_p) - \sum_{j=1}^{m}\frac{N_j}{N_p}Entropy(D_j)$$

Trong đó:
- $D_p$ là tập dữ liệu cha
- $D_j$ là tập con thứ $j$ sau phân chia
- $N_j$ là số mẫu trong $D_j$
- $N_p$ là tổng số mẫu trong $D_p$
- $m$ là số tập con

**Information Gain đo lường:**
- Giảm entropy sau khi phân chia
- Giá trị càng cao càng tốt
- Phân chia tốt nhất có IG cao nhất

**So sánh Gini vs Entropy:**
| Tiêu chí | Gini | Entropy |
|----------|------|---------|
| Tính toán | Nhanh hơn | Chậm hơn (có log) |
| Độ nhạy | Ít nhạy | Nhạy hơn với thay đổi |
| Kết quả | Tương tự trong thực tế | Tương tự |
| Mặc định | Sklearn default | ID3, C4.5 |

**Cho Hồi Quy:**

**3. Mean Squared Error (MSE):**
$$MSE = \frac{1}{N}\sum_{i=1}^{N}(y_i - \bar{y})^2$$

- $\bar{y}$ là giá trị trung bình của mục tiêu tại nút
- Đo lường phương sai của giá trị mục tiêu
- Mục tiêu: Giảm MSE sau phân chia

**4. Mean Absolute Error (MAE):**
$$MAE = \frac{1}{N}\sum_{i=1}^{N}|y_i - \bar{y}|$$

- Ít nhạy cảm với outliers hơn MSE
- Median thay vì mean làm giá trị dự đoán

### Thuật Toán CART (Classification and Regression Trees)

CART là thuật toán phổ biến nhất để xây dựng cây quyết định, tạo ra cây nhị phân.

**Các Bước:**

**1. Bắt đầu với tất cả dữ liệu training tại gốc:**
- Tính impurity ban đầu
- Xem xét tất cả đặc trưng và ngưỡng có thể

**2. Chọn đặc trưng và ngưỡng tốt nhất:**
- Thử tất cả đặc trưng
- Với mỗi đặc trưng, thử nhiều ngưỡng
- Tính information gain hoặc giảm Gini
- Chọn phân chia có improvement cao nhất

**3. Phân chia tập dữ liệu thành các tập con:**
- Tạo nhánh trái và phải
- Mẫu thỏa điều kiện đi trái
- Mẫu không thỏa đi phải

**4. Lặp đệ quy cho mỗi tập con:**
- Áp dụng quy trình tương tự cho nút con
- Tiếp tục cho đến khi đạt điều kiện dừng

**5. Dừng khi đạt tiêu chí dừng**

**Tiêu Chí Dừng (Stopping Criteria):**

**1. Đạt độ sâu tối đa (max_depth):**
- Giới hạn số tầng của cây
- Ngăn cây quá sâu, overfitting
- Thường: 3-10 cho cây đơn, sâu hơn cho ensemble

**2. Số mẫu tối thiểu để phân chia (min_samples_split):**
- Nút phải có ít nhất X mẫu để tiếp tục phân chia
- Nếu < X: Trở thành nút lá
- Thường: 2-100 tùy kích thước dữ liệu

**3. Số mẫu tối thiểu trong nút lá (min_samples_leaf):**
- Mỗi nút lá phải có ít nhất X mẫu
- Làm mượt decision boundary
- Thường: 1-50

**4. Cải thiện tối thiểu trong purity:**
- Phân chia phải giảm impurity ít nhất X
- Dừng nếu improvement quá nhỏ

**5. Tất cả mẫu thuộc cùng một lớp:**
- Nút hoàn toàn thuần khiết
- Không cần phân chia thêm

**6. Không còn đặc trưng để phân chia:**
- Đã sử dụng hết đặc trưng
- Tạo nút lá với nhãn đa số

### Pruning (Cắt Tỉa Cây)

Giảm overfitting bằng cách loại bỏ các nhánh có tầm quan trọng thấp.

**Tại sao cần Pruning:**
- Cây đầy đủ thường overfit
- Học cả noise trong training data
- Hiệu suất kém trên test data
- Cây phức tạp, khó diễn giải

**Pre-pruning (Early Stopping - Cắt Tỉa Sớm):**

Dừng xây dựng cây sớm bằng cách thiết lập ràng buộc:

**Tham số:**
- `max_depth`: Độ sâu tối đa (ví dụ: 5)
- `min_samples_split`: Mẫu tối thiểu để split (ví dụ: 20)
- `min_samples_leaf`: Mẫu tối thiểu trong lá (ví dụ: 10)
- `max_leaf_nodes`: Số nút lá tối đa
- `min_impurity_decrease`: Giảm impurity tối thiểu

**Ưu điểm:**
- Nhanh, không cần xây dựng cây đầy đủ
- Dễ triển khai

**Nhược điểm:**
- Có thể dừng quá sớm
- Bỏ lỡ phân chia tốt sau phân chia xấu

**Post-pruning (Cắt Tỉa Sau):**

Xây dựng cây đầy đủ, sau đó cắt bớt các nhánh.

**Cost Complexity Pruning (Weakest Link Pruning):**
$$R_\alpha(T) = R(T) + \alpha|T|$$

Trong đó:
- $R(T)$ là error rate của cây $T$
- $|T|$ là số nút lá
- $\alpha$ là tham số complexity (càng lớn càng cắt nhiều)

**Quy trình:**
1. Xây dựng cây đầy đủ
2. Tính $\alpha$ cho mỗi subtree
3. Loại bỏ subtree có $\alpha$ nhỏ nhất (đóng góp ít nhất)
4. Lặp lại cho đến khi còn gốc
5. Chọn cây tối ưu bằng cross-validation

**Ưu điểm:**
- Thường cho kết quả tốt hơn pre-pruning
- Không bỏ lỡ phân chia tốt

**Nhược điểm:**
- Tốn thời gian (xây dựng cây đầy đủ trước)
- Phức tạp hơn

### Feature Importance (Tầm Quan Trọng Đặc Trưng)

Cây quyết định tự động tính toán mức độ quan trọng của mỗi đặc trưng.

**Công Thức:**
$$Importance(f) = \sum_{t \in T} p(t) \cdot \Delta impurity(t, f)$$

Trong đó:
- $p(t)$ là tỷ lệ mẫu tại nút $t$
- $\Delta impurity(t, f)$ là giảm impurity khi phân chia theo đặc trưng $f$ tại nút $t$
- Tổng trên tất cả nút sử dụng đặc trưng $f$

**Diễn giải:**
- Giá trị càng cao, đặc trưng càng quan trọng
- Tổng tất cả importance = 1
- Đặc trưng không xuất hiện có importance = 0

**Ứng dụng:**
- Feature selection
- Hiểu mô hình
- Phát hiện đặc trưng không cần thiết
- Giải thích cho stakeholders

**Lưu ý:**
- Thiên vị về đặc trưng có nhiều giá trị unique
- Đặc trưng tương quan cao có importance phân tán
- Sử dụng permutation importance để khắc phục

### Ưu Điểm Của Cây Quyết Định

**1. Dễ hiểu và diễn giải:**
- Trực quan, giống cách con người quyết định
- Có thể vẽ và giải thích bằng lời
- Không cần kiến thức thống kê sâu
- Phù hợp cho business users

**2. Yêu cầu ít tiền xử lý dữ liệu:**
- Không cần feature scaling
- Không cần one-hot encoding cho categorical
- Xử lý được missing values (surrogate splits)
- Không cần assumption về phân phối

**3. Xử lý dữ liệu số và phân loại:**
- Linh hoạt với nhiều loại đặc trưng
- Không cần encoding phức tạp
- Mixed data types

**4. Non-parametric:**
- Không giả định về phân phối dữ liệu
- Linh hoạt với mọi dạng data
- Không cần chọn hàm phân phối

**5. Bắt được mối quan hệ phi tuyến:**
- Decision boundary phức tạp
- Tương tác giữa các đặc trưng
- Không giới hạn bởi tuyến tính

**6. Tính toán Feature Importance tự nhiên:**
- Không cần phương pháp bên ngoài
- Tích hợp trong thuật toán

**7. Nhanh với dự đoán:**
- Độ phức tạp: O(log n) với cây cân bằng
- Hiệu quả cho production

### Nhược Điểm

**1. Dễ Overfitting:**
- Cây sâu học cả noise
- Mô hình phức tạp không generalize tốt
- Cần pruning hoặc ensemble

**2. Không Ổn Định:**
- Thay đổi nhỏ trong dữ liệu → cây hoàn toàn khác
- High variance
- Giải pháp: Ensemble methods (Random Forest)

**3. Thiên Vị Về Đặc Trưng Có Nhiều Mức:**
- Đặc trưng với nhiều giá trị unique được ưu tiên
- Information Gain thiên vị
- Giải pháp: Gain Ratio (C4.5)

**4. Không Tối Ưu Cho Extrapolation:**
- Hồi quy chỉ dự đoán trong phạm vi training data
- Không thể dự đoán ngoài min/max đã thấy
- Dự đoán là hằng số ở nút lá

**5. Tạo Cây Thiên Vị Với Imbalanced Data:**
- Ưu tiên lớp đa số
- Cần class_weight hoặc resampling

**6. Greedy Algorithm:**
- Chọn phân chia tốt nhất tại thời điểm hiện tại
- Không đảm bảo cây tối ưu toàn cục
- Có thể bỏ lỡ cây tốt hơn

**7. Khó Bắt Mối Quan Hệ Tuyến Tính:**
- Cần nhiều phân chia để xấp xỉ đường thẳng
- Linear model đơn giản hơn cho quan hệ tuyến tính

### Phương Pháp Ensemble Với Cây

**1. Random Forest (Rừng Ngẫu Nhiên):**

**Nguyên lý:**
- Xây dựng nhiều cây quyết định
- Mỗi cây trên bootstrap sample khác nhau
- Random subset đặc trưng tại mỗi split
- Kết hợp dự đoán: Voting (classification) hoặc averaging (regression)

**Tham số chính:**
- `n_estimators`: Số cây (50-500)
- `max_features`: Số đặc trưng xem xét (sqrt(n) cho classification, n/3 cho regression)
- `max_depth`: Độ sâu mỗi cây
- `min_samples_split`, `min_samples_leaf`

**Ưu điểm:**
- Giảm variance, ít overfitting
- Ổn định hơn cây đơn
- Feature importance đáng tin cậy hơn
- Xử lý tốt high-dimensional data
- Out-of-bag error estimation

**2. Gradient Boosting:**

**Nguyên lý:**
- Xây dựng cây tuần tự
- Mỗi cây học sửa lỗi của cây trước
- Mỗi cây nhỏ (weak learner)
- Kết hợp có trọng số

**Công thức:**
$$F_m(x) = F_{m-1}(x) + \nu \cdot h_m(x)$$

Trong đó:
- $F_m$ là mô hình tại iteration $m$
- $h_m$ là cây mới
- $\nu$ là learning rate

**Implementations phổ biến:**
- **XGBoost:** Nhanh, regularization tốt, xử lý missing values
- **LightGBM:** Rất nhanh, hiệu quả bộ nhớ, leaf-wise growth
- **CatBoost:** Tốt cho categorical features, ít overfitting

**Ưu điểm:**
- Hiệu suất cao nhất trong nhiều competition
- Có thể đạt accuracy rất cao
- Xử lý tốt heterogeneous features

**Nhược điểm:**
- Dễ overfit nếu không tune cẩn thận
- Chậm hơn Random Forest (sequential)
- Khó tune (nhiều hyperparameters)

**3. AdaBoost (Adaptive Boosting):**

**Nguyên lý:**
- Tăng trọng số cho mẫu bị misclassified
- Mỗi cây tập trung vào mẫu khó
- Trọng số cho mô hình dựa trên accuracy

**Ưu điểm:**
- Đơn giản, hiệu quả
- Ít tham số hơn Gradient Boosting
- Tốt cho binary classification

**Nhược điểm:**
- Nhạy cảm với noise và outliers
- Có thể overfit

### Điều Chỉnh Hyperparameters

**Tham số quan trọng:**

**1. max_depth (Độ sâu tối đa):**
- Giá trị nhỏ: Underfitting, mô hình đơn giản
- Giá trị lớn: Overfitting, mô hình phức tạp
- Thường: 3-10 cho cây đơn, 5-20 cho ensemble

**2. min_samples_split:**
- Số mẫu tối thiểu để split nút
- Tăng lên: Giảm overfitting, cây đơn giản hơn
- Thường: 2-100

**3. min_samples_leaf:**
- Số mẫu tối thiểu trong mỗi lá
- Làm mượt decision boundary
- Thường: 1-50

**4. max_features:**
- Số đặc trưng xem xét cho mỗi split
- 'auto'/'sqrt': √n (cho classification)
- 'log2': log₂(n)
- None: Tất cả đặc trưng

**5. criterion:**
- 'gini': Gini impurity (mặc định, nhanh)
- 'entropy': Information gain (chậm hơn)
- 'squared_error': Cho regression

**6. splitter:**
- 'best': Chọn phân chia tốt nhất (mặc định)
- 'random': Chọn ngẫu nhiên (nhanh hơn, thêm randomness)

**Strategies cho Tuning:**
- **Grid Search:** Thử tất cả combinations
- **Random Search:** Sample ngẫu nhiên, hiệu quả hơn
- **Bayesian Optimization:** Thông minh, ít iterations
- **Cross-validation:** Luôn dùng CV để đánh giá

**Tips:**
- Bắt đầu với default parameters
- Tune max_depth trước
- Sau đó min_samples_split và min_samples_leaf
- Cuối cùng các tham số khác
- Monitor training vs validation performance

### Ứng Dụng Thực Tế

**1. Chẩn Đoán Y Tế:**
- Chuỗi quyết định dựa trên triệu chứng
- Dự đoán bệnh từ test results
- Giải thích dễ dàng cho bác sĩ

**2. Đánh Giá Rủi Ro Tín Dụng:**
- Quyết định cho vay
- Dự đoán default risk
- Tuân thủ quy định (interpretability)

**3. Dự Đoán Customer Churn:**
- Xác định khách hàng có khả năng rời đi
- Hành động marketing có mục tiêu
- Hiểu lý do churn

**4. Phát Hiện Gian Lận:**
- Phát hiện transactions đáng ngờ
- Real-time scoring
- Giải thích cho investigation team

**5. Feature Selection:**
- Xác định đặc trưng quan trọng
- Giảm dimensionality
- Chuẩn bị cho mô hình khác

**6. Hệ Thống Gợi Ý:**
- Quyết định sản phẩm recommend
- Personalization rules
- Content filtering

---

## Máy Vector Hỗ Trợ (Support Vector Machine - SVM)

### Giới Thiệu Về SVM

Support Vector Machine (SVM) là thuật toán học có giám sát mạnh mẽ cho phân loại và hồi quy. Chúng hoạt động bằng cách tìm siêu phẳng (hyperplane) tối ưu phân tách tối đa các lớp trong không gian nhiều chiều.

**Ý tưởng cốt lõi:**
- Tìm ranh giới quyết định tốt nhất giữa các lớp
- Tối đa hóa khoảng cách (margin) giữa các lớp
- Chỉ dựa vào các điểm dữ liệu quan trọng nhất (support vectors)

**Ứng dụng:**
- Phân loại văn bản (spam detection, sentiment analysis)
- Nhận dạng chữ viết tay
- Nhận dạng khuôn mặt
- Phân loại hình ảnh
- Phân tích sinh học (protein classification)
- Dự đoán chuỗi thời gian

**Ưu điểm chính:**
- Hiệu quả trong không gian nhiều chiều
- Hoạt động tốt khi có ranh giới rõ ràng
- Tiết kiệm bộ nhớ (chỉ lưu support vectors)
- Linh hoạt với nhiều kernel functions

### SVM Tuyến Tính (Linear SVM)

**Mục tiêu:** Tìm siêu phẳng có margin tối đa giữa các lớp.

**Siêu Phẳng (Hyperplane):**

Trong không gian n chiều, siêu phẳng là không gian con (n-1) chiều chia không gian thành hai nửa.

**Phương trình siêu phẳng:**
$$w^Tx + b = 0$$

Trong đó:
- $w$ là vector trọng số (weights) - vector pháp tuyến của siêu phẳng
- $x$ là vector đặc trưng
- $b$ là bias (hệ số chặn)

**Ví dụ:**
- 2D: $w_1x_1 + w_2x_2 + b = 0$ (đường thẳng)
- 3D: $w_1x_1 + w_2x_2 + w_3x_3 + b = 0$ (mặt phẳng)

**Hàm Quyết Định:**
$$f(x) = sign(w^Tx + b)$$

- Nếu $w^Tx + b > 0$: Dự đoán lớp +1
- Nếu $w^Tx + b < 0$: Dự đoán lớp -1
- Nếu $w^Tx + b = 0$: Điểm nằm trên siêu phẳng

**Margin (Lề):**

Margin là khoảng cách từ siêu phẳng đến điểm dữ liệu gần nhất.

**Công thức:**
$$margin = \frac{2}{||w||}$$

**Giải thích:**
- Khoảng cách từ điểm $x_i$ đến siêu phẳng: $\frac{|w^Tx_i + b|}{||w||}$
- Điểm support vector thỏa: $|w^Tx_i + b| = 1$
- Margin = khoảng cách từ support vector này đến support vector bên kia = $\frac{2}{||w||}$

**Tối đa hóa margin:**
- Margin lớn → Generalization tốt hơn
- Mô hình ổn định hơn với noise
- Tăng khả năng phân loại đúng trên dữ liệu mới

### Hard Margin SVM

Dành cho dữ liệu **linearly separable** (phân tách tuyến tính hoàn toàn).

**Bài toán tối ưu:**
$$\min_{w,b} \frac{1}{2}||w||^2$$

**Ràng buộc:** $y_i(w^Tx_i + b) \geq 1, \forall i$

**Giải thích:**
- Mục tiêu: Tối thiểu hóa $||w||^2$ (tương đương tối đa hóa margin $\frac{2}{||w||}$)
- Ràng buộc: Tất cả điểm phải được phân loại đúng
- $y_i \in \{-1, +1\}$: Nhãn lớp
- $y_i(w^Tx_i + b) \geq 1$: Điểm nằm đúng phía và cách siêu phẳng ít nhất 1 đơn vị

**Tại sao dùng $\frac{1}{2}||w||^2$:**
- Đạo hàm đẹp hơn (mất $\frac{1}{2}$ khi lấy đạo hàm)
- Bài toán convex quadratic programming
- Dễ giải với Lagrange multipliers

**Hạn chế:**
- Yêu cầu dữ liệu phân tách tuyến tính hoàn toàn
- Không tolerant với outliers
- Hiếm khi áp dụng trong thực tế (dữ liệu thường có noise)

### Soft Margin SVM

Dành cho dữ liệu **không phân tách tuyến tính hoàn toàn** (có overlap).

**Giới thiệu Slack Variables $\xi_i$:**
- Cho phép một số điểm vi phạm margin
- $\xi_i$ đo lường mức độ vi phạm của điểm $i$
- $\xi_i = 0$: Điểm được phân loại đúng, nằm ngoài margin
- $0 < \xi_i < 1$: Điểm nằm trong margin nhưng phân loại đúng
- $\xi_i \geq 1$: Điểm bị misclassified

**Bài toán tối ưu:**
$$\min_{w,b,\xi} \frac{1}{2}||w||^2 + C\sum_{i=1}^{m}\xi_i$$

**Ràng buộc:**
- $y_i(w^Tx_i + b) \geq 1 - \xi_i$
- $\xi_i \geq 0, \forall i$

**Tham số C (Regularization Parameter):**

C điều khiển trade-off giữa margin rộng và số lượng vi phạm.

**C lớn (C → ∞):**
- Penalty cao cho vi phạm
- Margin nhỏ hơn
- Ít misclassifications
- Low bias, high variance (overfitting)
- Gần với hard margin SVM

**C nhỏ:**
- Penalty thấp cho vi phạm
- Margin lớn hơn
- Nhiều misclassifications hơn
- High bias, low variance (underfitting)
- Mô hình đơn giản hơn

**Lựa chọn C:**
- Cross-validation
- Thường thử: 0.01, 0.1, 1, 10, 100
- Phụ thuộc vào scale của dữ liệu

**Diễn giải hàm mục tiêu:**
- $\frac{1}{2}||w||^2$: Tối đa hóa margin
- $C\sum_{i=1}^{m}\xi_i$: Tối thiểu hóa vi phạm
- C cân bằng hai mục tiêu này

### Kernel Trick (Mẹo Kernel)

Ánh xạ dữ liệu sang không gian nhiều chiều hơn nơi nó trở nên phân tách tuyến tính.

**Vấn đề:**
- Nhiều bài toán không phân tách tuyến tính trong không gian gốc
- Ví dụ: XOR problem, dữ liệu phân bố hình tròn

**Giải pháp:**
- Ánh xạ dữ liệu sang không gian đặc trưng (feature space) nhiều chiều hơn
- Trong không gian mới, dữ liệu có thể phân tách tuyến tính
- SVM tuyến tính trong không gian mới = SVM phi tuyến trong không gian gốc

**Hàm Kernel:**
$$K(x_i, x_j) = \phi(x_i)^T\phi(x_j)$$

Trong đó:
- $\phi(x)$ là hàm ánh xạ (không cần tính tường minh)
- $K(x_i, x_j)$ tính trực tiếp inner product trong không gian đặc trưng

**Ưu điểm Kernel Trick:**
- Không cần tính $\phi(x)$ tường minh
- Không cần lưu trữ trong không gian nhiều chiều
- Chỉ cần tính $K(x_i, x_j)$
- Hiệu quả tính toán

**Các Kernel Phổ Biến:**

**1. Linear Kernel (Kernel Tuyến Tính):**
$$K(x_i, x_j) = x_i^Tx_j$$

- Không ánh xạ, chỉ là inner product thông thường
- Sử dụng khi dữ liệu đã phân tách tuyến tính
- Nhanh nhất
- Tốt cho high-dimensional sparse data (text)
- Dễ diễn giải

**Khi nào dùng:**
- Số đặc trưng >> số mẫu
- Dữ liệu văn bản
- Cần tốc độ và interpretability

**2. Polynomial Kernel (Kernel Đa Thức):**
$$K(x_i, x_j) = (x_i^Tx_j + c)^d$$

Trong đó:
- $d$ là degree (bậc) của polynomial
- $c$ là constant (thường = 0 hoặc 1)

**Đặc điểm:**
- Tạo đặc trưng polynomial
- $d=2$: Bao gồm tương tác cặp
- $d$ lớn: Flexibility cao nhưng dễ overfit
- Có thể bùng nổ tính toán với $d$ lớn

**Khi nào dùng:**
- Quan hệ polynomial giữa features
- Image processing
- $d=2$ hoặc $d=3$ thường đủ

**3. RBF Kernel (Radial Basis Function / Gaussian Kernel):**
$$K(x_i, x_j) = \exp(-\gamma||x_i - x_j||^2)$$

Trong đó:
- $\gamma$ (gamma) kiểm soát ảnh hưởng của single training example
- $\gamma = \frac{1}{2\sigma^2}$ trong phân phối Gaussian

**$\gamma$ nhỏ:**
- Ảnh hưởng lan rộng
- Decision boundary mượt
- Low variance, high bias (underfitting)

**$\gamma$ lớn:**
- Ảnh hưởng hẹp
- Decision boundary phức tạp
- High variance, low bias (overfitting)

**Đặc điểm:**
- Phổ biến nhất
- Ánh xạ sang không gian vô hạn chiều
- Linh hoạt, xử lý được nhiều dạng data
- Giá trị trong [0, 1]

**Khi nào dùng:**
- Default choice khi không biết kernel nào
- Dữ liệu không có structure rõ ràng
- Hiệu quả với nhiều loại bài toán

**Lựa chọn $\gamma$:**
- Cross-validation
- `gamma='scale'`: $\gamma = \frac{1}{n_{features} \times Var(X)}$
- `gamma='auto'`: $\gamma = \frac{1}{n_{features}}$
- Thử: 0.001, 0.01, 0.1, 1

**4. Sigmoid Kernel:**
$$K(x_i, x_j) = \tanh(\alpha x_i^Tx_j + c)$$

- Giống activation function trong neural networks
- Không phải luôn positive semi-definite
- Ít được sử dụng
- Có thể không converge

**So sánh các Kernel:**

| Kernel | Khi nào dùng | Ưu điểm | Nhược điểm |
|--------|-------------|---------|------------|
| Linear | High-dim sparse data, text | Nhanh, diễn giải được | Chỉ tuyến tính |
| Polynomial | Quan hệ polynomial | Flexible | Tốn tính toán, nhiều params |
| RBF | Default, unknown structure | Rất flexible | Cần tune $\gamma$, dễ overfit |
| Sigmoid | Rare | Giống neural net | Không stable |

### Formulation Đối Ngẫu (Dual Formulation)

Bài toán tối ưu có thể được công thức hóa dưới dạng đối ngẫu sử dụng Lagrange multipliers $\alpha_i$.

**Primal Problem:**
$$\min_{w,b,\xi} \frac{1}{2}||w||^2 + C\sum_{i=1}^{m}\xi_i$$

**Dual Problem:**
$$\max_\alpha \sum_{i=1}^{m}\alpha_i - \frac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}\alpha_i\alpha_jy_iy_jK(x_i, x_j)$$

**Ràng buộc:**
- $0 \leq \alpha_i \leq C, \forall i$
- $\sum_{i=1}^{m}\alpha_iy_i = 0$

**Tại sao dùng Dual:**
- Dễ tính toán hơn với kernel
- Chỉ cần kernel function $K(x_i, x_j)$
- Không cần tính $\phi(x)$ tường minh
- Quadratic programming problem (well-studied)

**Dự Đoán:**
$$f(x) = sign\left(\sum_{i=1}^{m}\alpha_iy_iK(x_i, x) + b\right)$$

**Lưu ý:**
- Chỉ cần tính với support vectors ($\alpha_i > 0$)
- Hầu hết $\alpha_i = 0$

### Support Vectors

Các điểm dữ liệu có $\alpha_i > 0$ được gọi là support vectors.

**Đây là các điểm quan trọng:**

**1. Nằm trên margin boundary ($\alpha_i < C$):**
- $y_i(w^Tx_i + b) = 1$
- Ảnh hưởng trực tiếp đến vị trí siêu phẳng
- Điểm "support" (hỗ trợ) siêu phẳng

**2. Bị misclassified hoặc trong margin ($\alpha_i = C$):**
- $y_i(w^Tx_i + b) < 1$
- Có slack variable $\xi_i > 0$

**Đặc điểm:**
- Chỉ support vectors đóng góp vào decision function
- Các điểm khác không ảnh hưởng
- Xóa non-support vectors không thay đổi mô hình
- Thường chỉ có 10-30% điểm là support vectors

**Tầm quan trọng:**
- Giảm memory (chỉ lưu support vectors)
- Dự đoán nhanh hơn
- Robust to outliers (điểm xa không ảnh hưởng)

**Visualize:**
- Support vectors thường là các điểm gần decision boundary
- Điểm khó phân loại
- Biên giới giữa các lớp

### SVM Đa Lớp (Multi-class SVM)

SVM ban đầu cho binary classification. Mở rộng cho multi-class:

**1. One-vs-One (OvO):**
- Huấn luyện $\frac{K(K-1)}{2}$ bộ phân loại nhị phân
- Mỗi cặp lớp có một SVM
- Dự đoán: Voting - lớp thắng nhiều nhất

**Ưu điểm:**
- Mỗi SVM đơn giản hơn (chỉ 2 lớp)
- Training nhanh cho mỗi SVM
- Tốt cho SVM với kernel

**Nhược điểm:**
- Nhiều mô hình khi K lớn
- Voting có thể tie

**2. One-vs-Rest (OvR / One-vs-All):**
- Huấn luyện K bộ phân loại nhị phân
- Mỗi SVM: Một lớp vs tất cả lớp khác
- Dự đoán: Lớp có decision function score cao nhất

**Ưu điểm:**
- Ít mô hình hơn (K so với $\frac{K(K-1)}{2}$)
- Đơn giản

**Nhược điểm:**
- Imbalanced training sets
- Scores không comparable trực tiếp

**3. Crammer & Singer:**
- Giải trực tiếp multi-class SVM
- Một bài toán tối ưu duy nhất
- Phức tạp tính toán

**Sklearn default:** OvR cho hầu hết, OvO cho `SVC`

### SVM cho Hồi Quy (SVR - Support Vector Regression)

Thay vì tối đa hóa margin, SVR tìm một "ống" (tube) có độ rộng $\epsilon$ chứa hầu hết các điểm dữ liệu.

**Ý tưởng:**
- Cho phép sai số trong khoảng $\epsilon$
- Penalty cho điểm ngoài ống
- Cân bằng giữa flatness và tolerance

**Bài toán tối ưu:**
$$\min_{w,b} \frac{1}{2}||w||^2 + C\sum_{i=1}^{m}(\xi_i + \xi_i^*)$$

**Ràng buộc:**
- $y_i - (w^Tx_i + b) \leq \epsilon + \xi_i$
- $(w^Tx_i + b) - y_i \leq \epsilon + \xi_i^*$
- $\xi_i, \xi_i^* \geq 0$

**Trong đó:**
- $\epsilon$ là độ rộng của ống (epsilon-insensitive tube)
- $\xi_i, \xi_i^*$ là slack variables (trên và dưới)
- Điểm trong ống: không penalty
- Điểm ngoài ống: penalty tỷ lệ với khoảng cách

**Tham số:**

**1. Epsilon ($\epsilon$):**
- Độ rộng tube
- $\epsilon$ lớn: Ống rộng, ít support vectors, underfitting
- $\epsilon$ nhỏ: Ống hẹp, nhiều support vectors, overfitting
- Thường: 0.01, 0.1, 0.5

**2. C:**
- Trade-off margin vs vi phạm
- Giống như trong classification

**3. Kernel:**
- RBF, Linear, Polynomial
- Giống như classification

**Support Vectors trong SVR:**
- Điểm nằm trên hoặc ngoài biên ống
- Điểm trong ống không đóng góp

**Ứng dụng:**
- Time series forecasting
- Stock price prediction
- Weather prediction
- Regression với outliers

### Điều Chỉnh Hyperparameters

**Các tham số chính:**

**1. C (Regularization):**
- Kiểm soát trade-off giữa margin và errors
- Range: 0.01 đến 1000
- Grid search: [0.01, 0.1, 1, 10, 100]

**2. Kernel type:**
- Lựa chọn hàm kernel
- Try: 'linear', 'rbf', 'poly'
- Default: 'rbf'

**3. Gamma (γ) - cho RBF kernel:**
- Định nghĩa bán kính ảnh hưởng
- Range: 0.0001 đến 1
- Grid search: [0.001, 0.01, 0.1, 1]
- 'scale': $\frac{1}{n \times var(X)}$

**4. Degree (d) - cho Polynomial kernel:**
- Bậc của polynomial
- Thường: 2, 3, 4
- Tránh quá cao (overfitting, computational cost)

**5. Epsilon (ε) - cho SVR:**
- Độ rộng tube
- Range: 0.01 đến 1
- Phụ thuộc scale của target

**Chiến lược Tuning:**

**1. Coarse Grid Search:**
- Tìm vùng tốt với grid thô
- C: [0.1, 1, 10, 100]
- gamma: [0.001, 0.01, 0.1, 1]

**2. Fine Grid Search:**
- Zoom vào vùng tốt
- Grid mịn hơn

**3. Randomized Search:**
- Nhanh hơn grid search
- Sample ngẫu nhiên từ distributions

**4. Bayesian Optimization:**
- Thông minh, adaptive
- Ít iterations hơn

**Tips:**
- Luôn feature scaling trước
- Cross-validation (5-fold hoặc 10-fold)
- Monitor training time
- Tune C và gamma cùng lúc (interdependent)

### Ưu Điểm Của SVM

**1. Hiệu quả trong không gian nhiều chiều:**
- Hoạt động tốt khi $n_{features} > n_{samples}$
- Phù hợp cho text, genomics, high-dimensional data

**2. Tiết kiệm bộ nhớ:**
- Chỉ lưu support vectors
- Không cần lưu toàn bộ training data
- Sparse representation

**3. Linh hoạt với kernel functions:**
- Nhiều kernel có sẵn
- Có thể define custom kernel
- Xử lý được non-linear relationships

**4. Hoạt động tốt với margin rõ ràng:**
- Khi các lớp separated tốt
- Decision boundary rõ ràng

**5. Robust to outliers (soft margin):**
- Slack variables cho phép một số outliers
- Không bị ảnh hưởng nhiều bởi outliers xa

**6. Cơ sở toán học vững chắc:**
- Convex optimization problem
- Global optimum guaranteed
- Không bị stuck ở local minima

**7. Regularization tích hợp:**
- Tham số C control overfitting
- Không cần regularization bên ngoài

### Nhược Điểm

**1. Chi phí tính toán cao cho dữ liệu lớn:**
- Training complexity: O($n^2$) đến O($n^3$)
- Không scale tốt với >10,000 mẫu
- Memory intensive

**2. Nhạy cảm với feature scaling:**
- **Bắt buộc** phải scaling/normalization
- Đặc trưng có scale lớn sẽ dominate
- Ảnh hưởng đến kernel calculations

**3. Khó diễn giải (với kernels):**
- Đặc biệt với RBF kernel
- Không thấy được feature importance trực tiếp
- Black box (so với linear models, trees)

**4. Không có xác suất trực tiếp:**
- Decision function cho distance, không phải probability
- Cần calibration (Platt scaling, isotonic regression)
- `predict_proba()` chậm hơn và ít reliable

**5. Khó chọn kernel và parameters:**
- Nhiều choices: kernel type, C, gamma, ...
- Cần extensive tuning
- Cross-validation tốn thời gian

**6. Không xử lý trực tiếp missing values:**
- Cần imputation trước
- Không như tree-based methods

**7. Không cung cấp feature importance:**
- Khác với trees, linear models
- Cần phương pháp bên ngoài (permutation importance)

### Cân Nhắc Thực Tế

**1. Feature Scaling - BẮT BUỘC:**

**Tại sao:**
- SVM dựa trên khoảng cách (Euclidean distance trong kernel)
- Đặc trưng có scale lớn sẽ dominate
- Ảnh hưởng đến optimization

**Phương pháp:**
- StandardScaler: $(x - \mu) / \sigma$
- MinMaxScaler: Scale về [0, 1] hoặc [-1, 1]
- RobustScaler: Dùng median, robust to outliers

**Lưu ý:**
- Scale trên training set
- Apply cùng transformation cho test set
- Không scale lại test set độc lập

**2. Class Imbalance:**

**Giải pháp:**
- `class_weight='balanced'`: Tự động điều chỉnh
- `class_weight={0: w0, 1: w1}`: Custom weights
- SMOTE trước khi train
- Adjust decision threshold

**3. Large Datasets:**

**Vấn đề:**
- Standard SVM không scale tốt
- Training chậm với >10,000 mẫu

**Giải pháp:**
- **LinearSVC:** SGD-based, linear SVM nhanh hơn
- **SGDClassifier với loss='hinge':** Online learning
- Sample subset cho training
- Approximate methods

**4. Probability Estimates:**

**Vấn đề:**
- SVM cho decision values, không phải probabilities
- Cần probabilities cho many applications

**Giải pháp:**
- Platt Scaling: Fit sigmoid function
- Isotonic Regression: Non-parametric
- `probability=True` trong `SVC` (chậm hơn)

**Lưu ý:**
- Probabilities không chính xác như Logistic Regression
- Dùng cross-validation để calibrate

**5. Multi-class:**
- Sklearn tự động xử lý
- `decision_function_shape='ovr'` hoặc `'ovo'`
- Chọn dựa trên yêu cầu

**6. Kernel Selection:**

**Quy trình:**
1. Bắt đầu với Linear kernel (nhanh, baseline)
2. Nếu không tốt, thử RBF
3. Nếu biết structure, thử Polynomial
4. So sánh bằng cross-validation

**7. Early Stopping:**
- Không có early stopping trong standard SVM
- Training đến khi converge
- Có thể set `max_iter` để limit

### Ứng Dụng

**1. Text Classification:**
- Spam detection
- Sentiment analysis
- Document categorization
- Topic labeling
- Language detection

**Tại sao tốt:**
- High-dimensional sparse data
- Linear kernel hiệu quả
- Good generalization

**2. Image Recognition:**
- Face detection và recognition
- Object classification
- Handwriting recognition (MNIST)
- Medical image analysis

**Tại sao tốt:**
- RBF kernel bắt được patterns
- Robust to variations

**3. Bioinformatics:**
- Protein classification
- Gene classification
- Cancer classification từ gene expression
- Drug discovery

**Tại sao tốt:**
- High-dimensional data
- Small sample size
- Good with complex patterns

**4. Handwriting Recognition:**
- Digit recognition
- Character recognition
- Signature verification

**5. Face Detection:**
- Detect faces trong images
- Feature-based classification

**6. Time Series Prediction:**
- Stock market prediction (SVR)
- Weather forecasting
- Energy consumption prediction

**Best Practices:**

1. **Luôn scale features**
2. **Bắt đầu với linear kernel**
3. **Use cross-validation cho tuning**
4. **Monitor training time**
5. **Consider LinearSVC cho large datasets**
6. **Check support vector ratio** (nếu >50% có thể có vấn đề)
7. **Combine với ensemble methods** nếu cần

**Directed Acyclic Graph SVM (DAGSVM):** Efficient OvO approach

### SVM for Regression (SVR)

Instead of maximizing margin, SVR finds a tube of width $\epsilon$ that contains most data points.

**Objective:**
$$\min_{w,b} \frac{1}{2}||w||^2 + C\sum_{i=1}^{m}(\xi_i + \xi_i^*)$$

Subject to:
- $y_i - (w^Tx_i + b) \leq \epsilon + \xi_i$
- $(w^Tx_i + b) - y_i \leq \epsilon + \xi_i^*$
- $\xi_i, \xi_i^* \geq 0$

### Hyperparameter Tuning

**Key Parameters:**
1. **C (Regularization):** Controls trade-off between margin and errors
2. **Kernel type:** Choice of kernel function
3. **Gamma (γ):** For RBF kernel, defines influence radius
4. **Degree (d):** For polynomial kernel
5. **Epsilon (ε):** For SVR, width of tube

Use Grid Search or Randomized Search with cross-validation.

### Advantages of SVM

1. Effective in high-dimensional spaces
2. Memory efficient (uses subset of training points)
3. Versatile through different kernel functions
4. Works well with clear margin of separation
5. Robust to outliers (soft margin)

### Disadvantages

1. Computationally expensive for large datasets (O($n^2$) to O($n^3$))
2. Sensitive to feature scaling
3. Difficult to interpret (especially with kernels)
4. No probabilistic interpretation (requires additional calibration)
5. Choosing right kernel and parameters is challenging

### Practical Considerations

- **Feature Scaling:** Always standardize features
- **Class Imbalance:** Adjust class weights
- **Large Datasets:** Use SGD-based linear SVM
- **Probability Estimates:** Use Platt scaling or isotonic regression

### Applications

- Text classification
- Image recognition
- Bioinformatics (protein classification)
- Handwriting recognition
- Face detection
- Time series prediction

---

## Lựa Chọn Đặc Trưng & Tối Ưu Hóa Mô Hình

### Giới Thiệu

Lựa chọn đặc trưng (feature selection) và tối ưu hóa mô hình là các bước quan trọng trong việc xây dựng mô hình học máy hiệu quả. Chúng cải thiện hiệu suất mô hình, giảm overfitting, giảm thời gian huấn luyện và tăng khả năng diễn giải.

**Tại sao quan trọng:**

**1. Cải Thiện Hiệu Suất:**
- Loại bỏ noise và đặc trưng không liên quan
- Tăng accuracy và generalization
- Mô hình tập trung vào signal thực sự

**2. Giảm Overfitting:**
- Ít đặc trưng → mô hình đơn giản hơn
- Giảm variance
- Better generalization

**3. Giảm Thời Gian Training:**
- Ít dữ liệu để xử lý
- Training nhanh hơn
- Prediction nhanh hơn

**4. Tăng Khả Năng Diễn Giải:**
- Dễ hiểu mô hình
- Ít đặc trưng để phân tích
- Better insights

**5. Giảm Chi Phí:**
- Ít đặc trưng cần thu thập
- Tiết kiệm storage
- Giảm computational resources

### Lựa Chọn Đặc Trưng (Feature Selection)

Xác định các đặc trưng liên quan nhất cho việc xây dựng mô hình, giảm số chiều và cải thiện hiệu suất.

**Ba nhóm phương pháp chính:**
1. **Filter Methods:** Đánh giá độc lập với mô hình
2. **Wrapper Methods:** Đánh giá bằng hiệu suất mô hình
3. **Embedded Methods:** Lựa chọn trong quá trình training

### Filter Methods (Phương Pháp Lọc)

Đánh giá đặc trưng độc lập với mô hình sử dụng các đo lường thống kê.

**Đặc điểm:**
- Nhanh, hiệu quả
- Không phụ thuộc vào thuật toán học
- Tốt cho high-dimensional data
- Có thể bỏ lỡ feature interactions

**1. Correlation-Based Methods (Phương Pháp Dựa Trên Tương Quan):**

**Pearson Correlation Coefficient:**
$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

- Giá trị: -1 đến +1
- |r| gần 1: Tương quan mạnh
- |r| gần 0: Không tương quan

**Ứng dụng:**
- **Feature-Target Correlation:** Chọn features có correlation cao với target
- **Feature-Feature Correlation:** Loại bỏ features tương quan cao với nhau (multicollinearity)

**Threshold:**
- |r| > 0.8 hoặc 0.9: Multicollinearity
- |r| < 0.1: Ít liên quan với target

**Lưu ý:**
- Chỉ bắt được mối quan hệ tuyến tính
- Không phù hợp với categorical features
- Có thể bỏ lỡ quan hệ phi tuyến

**2. Statistical Tests (Kiểm Định Thống Kê):**

**Chi-squared Test ($\chi^2$) - Cho Categorical Features:**
$$\chi^2 = \sum_{i,j}\frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

Trong đó:
- $O_{ij}$ là observed frequency
- $E_{ij}$ là expected frequency

**Khi nào dùng:**
- Cả feature và target đều categorical
- Test độc lập giữa feature và target
- P-value nhỏ: Feature quan trọng

**ANOVA F-test - Cho Continuous Features, Classification:**
$$F = \frac{MS_{between}}{MS_{within}}$$

- Test khác biệt means giữa các groups
- Continuous features, categorical target
- F-statistic cao: Feature discriminative

**Mutual Information (Thông Tin Tương Hỗ):**
$$MI(X,Y) = \sum_{x \in X}\sum_{y \in Y}P(x,y)\log\frac{P(x,y)}{P(x)P(y)}$$

**Đặc điểm:**
- Đo lường phụ thuộc giữa hai biến
- Bắt được cả quan hệ phi tuyến
- Giá trị ≥ 0
- MI = 0: Độc lập
- MI cao: Phụ thuộc mạnh

**Ưu điểm:**
- Không giả định về phân phối
- Bắt được quan hệ phức tạp
- Phù hợp với mọi loại dữ liệu

**Variance Threshold:**
- Loại bỏ features có variance thấp
- Low variance → ít thông tin
- Threshold: Variance < 0.01 hoặc 0.1
- Đặc biệt hữu ích cho sparse data

**3. Information Gain (Độ Lợi Thông Tin):**
$$IG(Y|X) = H(Y) - H(Y|X)$$

Trong đó:
- $H(Y)$ là entropy của target
- $H(Y|X)$ là conditional entropy của Y cho trước X

**Diễn giải:**
- Giảm uncertainty về Y khi biết X
- Cao hơn → Feature quan trọng hơn
- Dựa trên entropy từ Decision Trees

**Ưu điểm Filter Methods:**
- Rất nhanh
- Scale tốt với nhiều features
- Độc lập với model
- Không overfit

**Nhược điểm:**
- Không xem xét feature interactions
- Bỏ qua model-specific patterns
- Có thể loại bỏ features hữu ích

### Wrapper Methods (Phương Pháp Bao)

Đánh giá subsets đặc trưng bằng hiệu suất mô hình.

**Đặc điểm:**
- Sử dụng mô hình cụ thể để đánh giá
- Xem xét feature interactions
- Chậm hơn filter methods
- Có thể overfit nếu không cẩn thận

**1. Forward Selection (Lựa Chọn Tiến):**

**Thuật toán:**
1. Bắt đầu với tập rỗng: $S = \emptyset$
2. Với mỗi feature $f$ chưa chọn:
   - Training model với $S \cup \{f\}$
   - Đánh giá performance
3. Thêm feature tốt nhất vào $S$
4. Lặp lại cho đến khi đạt điều kiện dừng

**Điều kiện dừng:**
- Đạt số features mong muốn
- Performance không cải thiện
- Tất cả features đã thêm

**Ưu điểm:**
- Đơn giản, trực quan
- Tốt khi số features quan trọng nhỏ
- Bắt đầu từ đơn giản

**Nhược điểm:**
- Không thể remove features đã thêm
- Có thể stuck với local optimum
- $O(n^2)$ complexity

**2. Backward Elimination (Loại Bỏ Lùi):**

**Thuật toán:**
1. Bắt đầu với tất cả features: $S = \{all\}$
2. Với mỗi feature $f$ trong $S$:
   - Training model với $S \setminus \{f\}$
   - Đánh giá performance
3. Loại bỏ feature ảnh hưởng ít nhất
4. Lặp lại cho đến điều kiện dừng

**Điều kiện dừng:**
- Đạt số features mong muốn
- Loại bỏ features làm giảm performance
- Chỉ còn 1 feature

**Ưu điểm:**
- Xem xét feature interactions từ đầu
- Tốt khi hầu hết features quan trọng

**Nhược điểm:**
- Chậm hơn forward (bắt đầu với nhiều features)
- Không phù hợp với high-dimensional data
- $O(n^2)$ complexity

**3. Recursive Feature Elimination (RFE):**

**Thuật toán:**
1. Training model với tất cả features
2. Rank features theo importance
3. Loại bỏ feature ít quan trọng nhất
4. Lặp lại cho đến khi đạt số features mong muốn

**Ưu điểm:**
- Efficient hơn backward elimination
- Xem xét feature importance
- Phổ biến trong sklearn
- Tốt với linear models, SVMs, trees

**Nhược điểm:**
- Cần model có feature importance
- Vẫn tốn thời gian
- Có thể loại bỏ features sớm

**Cải tiến - RFECV:**
- RFE + Cross-Validation
- Tự động chọn số features tối ưu
- Robust hơn

**4. Exhaustive Search (Tìm Kiếm Toàn Diện):**

**Thuật toán:**
- Thử tất cả possible feature combinations
- Đánh giá mỗi subset
- Chọn subset tốt nhất

**Số combinations:** $2^n - 1$

**Ưu điểm:**
- Đảm bảo tìm được optimal subset (global optimum)
- Không bỏ sót combination nào

**Nhược điểm:**
- Exponential complexity: $O(2^n)$
- Không khả thi với n > 20-25
- Rất chậm

**Khi nào dùng:**
- Số features nhỏ (< 15-20)
- Cần optimal solution
- Có đủ computational resources

**Comparison Wrapper Methods:**

| Method | Complexity | Best for | Speed |
|--------|-----------|----------|-------|
| Forward | $O(n^2)$ | Ít features quan trọng | Trung bình |
| Backward | $O(n^2)$ | Nhiều features quan trọng | Chậm |
| RFE | $O(kn)$ | Balance | Nhanh hơn |
| Exhaustive | $O(2^n)$ | Optimal solution, n nhỏ | Rất chậm |

**Ưu điểm Wrapper Methods:**
- Xem xét model-specific performance
- Capture feature interactions
- Thường cho kết quả tốt nhất

**Nhược điểm:**
- Computationally expensive
- Risk of overfitting
- Phụ thuộc vào specific model

### Embedded Methods (Phương Pháp Nhúng)

Lựa chọn đặc trưng xảy ra trong quá trình training model.

**Đặc điểm:**
- Feature selection là part của training
- Balance giữa speed và accuracy
- Model-specific
- Efficient hơn wrapper methods

**1. Lasso (L1 Regularization):**

$$J(\beta) = MSE + \lambda\sum_{j=1}^{n}|\beta_j|$$

**Đặc điểm:**
- Đưa một số coefficients về chính xác 0
- Automatic feature selection
- Sparse solutions

**Tại sao L1 tạo sparsity:**
- L1 penalty có góc nhọn tại 0
- Optimization dễ chạm đến 0
- L2 có hình tròn → không về 0

**Ưu điểm:**
- Tự động và efficient
- Feature selection + training cùng lúc
- Tốt cho high-dimensional data
- Diễn giải dễ (chỉ giữ features quan trọng)

**Nhược điểm:**
- Có thể chọn ngẫu nhiên giữa correlated features
- Không stable với correlated features
- Sensitive to scaling

**Tuning:**
- $\lambda$ (alpha trong sklearn)
- Cross-validation để chọn
- LassoCV: Automatic tuning

**2. Tree-Based Feature Importance:**

**Random Forest Feature Importance:**
$$Importance_j = \frac{1}{N_T}\sum_{T}\sum_{t \in T}\mathbb{1}_{split(t)=j} \cdot \Delta impurity(t)$$

**Đặc điểm:**
- Dựa trên giảm impurity
- Average across all trees
- Normalized to sum to 1

**Gradient Boosting Feature Importance:**
- Tương tự RF nhưng weighted
- Trees sau có ảnh hưởng khác
- Thường reliable hơn RF

**Ưu điểm:**
- Capture non-linear relationships
- Handle feature interactions
- Không cần feature scaling
- Built-in trong tree models

**Nhược điểm:**
- Thiên vị về high-cardinality features
- Không reliable với correlated features
- Khác nhau giữa random states

**Cải thiện - Permutation Importance:**
- Shuffle feature và đo impact
- Không thiên vị
- Computationally expensive

**3. Elastic Net:**
$$J(\beta) = MSE + \lambda_1\sum_{j=1}^{n}|\beta_j| + \lambda_2\sum_{j=1}^{n}\beta_j^2$$

**Đặc điểm:**
- Kết hợp L1 và L2
- Balance giữa feature selection và shrinkage
- Tốt hơn Lasso với correlated features

**Tham số:**
- $\alpha$: Tổng strength của regularization
- $l1\_ratio$: Tỷ lệ L1 vs L2
  - $l1\_ratio = 1$: Pure Lasso
  - $l1\_ratio = 0$: Pure Ridge
  - $l1\_ratio = 0.5$: Equal mix

**Khi nào dùng:**
- Correlated features
- Muốn cả feature selection và shrinkage
- Groups of correlated features (chọn cả group)

**So sánh Embedded Methods:**

| Method | Type | Feature Selection | Best for |
|--------|------|------------------|----------|
| Lasso | Linear | Strong | High-dim, independent features |
| Elastic Net | Linear | Moderate | Correlated features |
| RF Importance | Tree | Moderate | Non-linear, interactions |
| GB Importance | Tree | Strong | Complex relationships |

### Giảm Số Chiều (Dimensionality Reduction)

Biến đổi đặc trưng sang không gian ít chiều hơn.

**Feature Selection vs Dimensionality Reduction:**
- **Feature Selection:** Giữ subset features gốc
- **Dimensionality Reduction:** Tạo features mới (combinations)

**1. Principal Component Analysis (PCA):**

**Nguyên lý:**
- Biến đổi tuyến tính sang orthogonal components
- Components sắp xếp theo variance
- Component đầu tiên: Direction của maximum variance

**Toán học:**
$$X_{reduced} = X \cdot W_k$$

Trong đó $W_k$ là matrix của k eigenvectors hàng đầu.

**Thuật toán:**
1. Standardize data
2. Tính covariance matrix: $\Sigma = \frac{1}{n}X^TX$
3. Tính eigenvectors và eigenvalues
4. Sắp xếp eigenvectors theo eigenvalues
5. Chọn top k eigenvectors
6. Transform data

**Variance Explained:**
$$\frac{\lambda_k}{\sum_{i=1}^{n}\lambda_i} \times 100\%$$

**Chọn số components:**
- Cumulative variance explained (thường 95% hoặc 99%)
- Scree plot (elbow method)
- Cross-validation performance

**Ưu điểm:**
- Giảm dimensionality hiệu quả
- Remove noise
- Decorrelate features
- Visualization (2D, 3D)
- Speed up training

**Nhược điểm:**
- Features mới khó diễn giải
- Linear transformation only
- Sensitive to scaling
- Mất thông tin

**Ứng dụng:**
- Visualization
- Noise reduction
- Feature extraction
- Compression
- Preprocessing cho ML

**2. Linear Discriminant Analysis (LDA):**

**Nguyên lý:**
- Supervised dimensionality reduction
- Tối đa hóa class separability
- Tìm directions phân biệt classes tốt nhất

**Mục tiêu:**
$$\max \frac{S_B}{S_W}$$

Trong đó:
- $S_B$: Between-class scatter
- $S_W$: Within-class scatter

**So với PCA:**
- PCA: Unsupervised, maximize variance
- LDA: Supervised, maximize separability

**Số components tối đa:**
- min(n_features, n_classes - 1)

**Ưu điểm:**
- Tốt cho classification
- Xem xét labels
- Fewer components needed

**Nhược điểm:**
- Cần labels
- Giả định Gaussian distribution
- Có thể overfit với small data

**3. t-SNE (t-Distributed Stochastic Neighbor Embedding):**

**Nguyên lý:**
- Non-linear dimensionality reduction
- Bảo toàn local structure
- Visualization mạnh mẽ

**Đặc điểm:**
- Typically cho 2D hoặc 3D
- Stochastic (kết quả khác mỗi lần chạy)
- Không có transform function (không dùng cho new data)

**Perplexity parameter:**
- Cân bằng local vs global structure
- Thường: 5-50
- Larger data → larger perplexity

**Ưu điểm:**
- Visualization xuất sắc
- Reveal clusters rõ ràng
- Handle non-linear structures

**Nhược điểm:**
- Rất chậm (O(n²))
- Không scale với large data
- Không có transform cho new data
- Khoảng cách không meaningful
- Parameters sensitive

**Khi nào dùng:**
- Visualization only
- Explore data structure
- Small-medium datasets (< 10,000)

**4. UMAP (Uniform Manifold Approximation and Projection):**

**Nguyên lý:**
- Tương tự t-SNE nhưng based on manifold theory
- Preserve both local và global structure

**Ưu điểm:**
- Nhanh hơn t-SNE nhiều
- Scale tốt hơn
- Preserve global structure
- Có transform function

**Nhược điểm:**
- Vẫn stochastic
- Parameters cần tuning

**So với t-SNE:**
- UMAP nhanh hơn 10-100x
- UMAP preserve global structure tốt hơn
- t-SNE có thể tốt hơn cho local structure

**5. Autoencoders:**

**Nguyên lý:**
- Neural network học compress và reconstruct data
- Bottleneck layer là reduced representation

**Architecture:**
```
Input → Encoder → Bottleneck → Decoder → Output
```

**Loss:** Reconstruction error
$$L = ||X - \hat{X}||^2$$

**Ưu điểm:**
- Non-linear transformations
- Flexible architecture
- Can be deep
- Learn complex patterns

**Nhược điểm:**
- Cần nhiều data
- Training phức tạp
- Hyperparameter tuning
- Computational expensive

**Variants:**
- Sparse Autoencoders
- Denoising Autoencoders
- Variational Autoencoders (VAE)

### Kỹ Thuật Đặc Trưng (Feature Engineering)

Tạo đặc trưng mới từ đặc trưng hiện có.

**"Feature engineering is the key to success in machine learning"**

**1. Polynomial Features (Đặc Trưng Đa Thức):**
$$\phi(x_1, x_2) = [1, x_1, x_2, x_1^2, x_1x_2, x_2^2]$$

**Ví dụ:** Với degree=2, 2 features → 6 features

**Khi nào dùng:**
- Quan hệ phi tuyến
- Regression models
- SVM với linear kernel

**Cảnh báo:**
- Exponential growth số features
- Easy overfit
- Cần regularization

**2. Interaction Features (Đặc Trưng Tương Tác):**
- Tích của hai hoặc nhiều features
- Capture relationships

**Ví dụ:**
- Area = Length × Width
- BMI = Weight / Height²
- Price per SqFt = Price / Area

**Khi tạo:**
- Domain knowledge
- Feature importance từ trees
- Feature interactions từ models

**3. Binning/Discretization (Rời Rạc Hóa):**

Chuyển continuous → categorical

**Methods:**
- **Equal Width:** Chia thành bins có width bằng nhau
- **Equal Frequency (Quantile):** Mỗi bin có số lượng bằng nhau
- **Custom Bins:** Domain-specific

**Ví dụ:**
- Age → Age groups (0-18, 19-35, 36-60, 60+)
- Income → Income brackets

**Ưu điểm:**
- Handle outliers
- Capture non-linear patterns
- Easier interpretation

**Nhược điểm:**
- Loss of information
- Arbitrary boundaries
- Increase dimensionality (one-hot encoding)

**4. Mathematical Transformations:**

**Log Transformation:**
$$x' = \log(x + 1)$$
- Giảm right skewness
- Compress large values
- Ví dụ: Income, population, prices

**Square Root:**
$$x' = \sqrt{x}$$
- Mild transformation
- Dành cho count data

**Box-Cox Transformation:**
$$x' = \begin{cases} \frac{x^\lambda - 1}{\lambda} & \lambda \neq 0 \\ \log(x) & \lambda = 0 \end{cases}$$
- Automatic tìm optimal $\lambda$
- Make distribution more Gaussian

**Power Transformation:**
- $x^2$, $x^3$ cho left skew
- $\frac{1}{x}$ cho extreme skew

**Khi nào dùng:**
- Skewed distributions
- Để thỏa model assumptions
- Improve normality

**5. Domain-Specific Features:**

**Date/Time Features:**
- Hour of day, Day of week, Month, Quarter
- Is weekend, Is holiday
- Time since event
- Cyclical encoding (sin/cos for hour)

**Text Features:**
- TF-IDF
- Word embeddings (Word2Vec, GloVe)
- Sentence length, Word count
- Sentiment scores

**Image Features:**
- Edges (Sobel, Canny)
- Textures (Gabor filters)
- Colors (histograms)
- Shapes (contours)

**Geospatial Features:**
- Distance to landmarks
- Density of points
- Cluster memberships
- Postal codes, City, Country

### Tối Ưu Hóa Mô Hình

### Điều Chỉnh Hyperparameters (Hyperparameter Tuning)

**Hyperparameters vs Parameters:**
- **Parameters:** Học từ data (weights, biases)
- **Hyperparameters:** Set trước training (learning rate, tree depth)

**1. Grid Search (Tìm Kiếm Lưới):**

**Nguyên lý:**
- Tìm kiếm exhaustive over parameter grid
- Thử tất cả combinations

**Ví dụ:**
```python
param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['rbf', 'linear'],
    'gamma': [0.001, 0.01, 0.1, 1]
}
# Total combinations: 4 × 2 × 4 = 32
```

**Ưu điểm:**
- Thorough, không bỏ sót
- Parallelizable
- Reproducible

**Nhược điểm:**
- Computationally expensive: $O(\prod n_i)$
- Chậm với nhiều parameters
- Không efficient

**Khi nào dùng:**
- Ít parameters
- Small/medium grid
- Muốn comprehensive search

**2. Random Search (Tìm Kiếm Ngẫu Nhiên):**

**Nguyên lý:**
- Sample ngẫu nhiên từ parameter distributions
- Không thử tất cả combinations

**Ưu điểm:**
- Hiệu quả hơn Grid Search
- Tốt cho large parameter spaces
- Often finds good solutions faster
- Cover more ranges

**Nhược điểm:**
- Không guarantee optimal
- Có thể miss best combination

**Best practices:**
- Use n_iter = 50-100
- Define reasonable distributions
- Use with cross-validation

**So sánh Grid vs Random:**
- Random: 10x faster, 95% performance
- Grid: Thorough nhưng chậm
- **Chiến lược:** Random Search → Grid Search trong vùng tốt

**3. Bayesian Optimization:**

**Nguyên lý:**
- Sử dụng probability model để guide search
- Learn từ previous evaluations
- Balance exploration vs exploitation

**Surrogate Model:**
- Gaussian Process hoặc Tree-based
- Model objective function
- Predict promising regions

**Acquisition Function:**
- Quyết định next point to try
- Expected Improvement (EI)
- Probability of Improvement (PI)
- Upper Confidence Bound (UCB)

**Ưu điểm:**
- Intelligent, adaptive
- Ít evaluations hơn
- Tốt cho expensive evaluations
- Handle continuous và categorical

**Nhược điểm:**
- Phức tạp hơn
- Overhead cho simple problems
- Cần tuning acquisition function

**Tools:**
- Hyperopt
- Optuna (modern, flexible)
- Scikit-Optimize (skopt)
- BayesSearchCV

**4. Genetic Algorithms (Thuật Toán Di Truyền):**

**Nguyên lý:**
- Evolution-based optimization
- Population of solutions
- Selection, Crossover, Mutation

**Bước:**
1. Initialize population
2. Evaluate fitness
3. Select best individuals
4. Crossover (combine solutions)
5. Mutate (random changes)
6. Repeat

**Ưu điểm:**
- Good for complex search spaces
- Không cần gradients
- Explore diverse solutions

**Nhược điểm:**
- Chậm
- Many hyperparameters (population size, mutation rate)
- Không guarantee optimal

**Khi nào dùng:**
- Very complex optimization
- Discrete + continuous parameters
- Multiple objectives

**5. Gradient-Based Optimization:**

**Nguyên lý:**
- Cho differentiable hyperparameters
- Compute gradients
- Update parameters

**Ứng dụng:**
- Learning rate
- Neural Architecture Search
- Meta-learning

**Ưu điểm:**
- Efficient với differentiable params
- Fast convergence

**Nhược điểm:**
- Chỉ cho differentiable
- Có thể stuck ở local minima

**So sánh các phương pháp:**

| Method | Speed | Efficiency | Best for |
|--------|-------|-----------|----------|
| Grid Search | Slow | Low | Small grids |
| Random Search | Medium | Medium | Large spaces |
| Bayesian Opt | Medium | High | Expensive evaluations |
| Genetic Alg | Slow | Medium | Complex spaces |
| Gradient | Fast | High | Differentiable |

### Chiến Lược Cross-Validation

**Tại sao Cross-Validation:**
- Single train-test split không đủ
- High variance in performance estimate
- May not be representative
- CV cho stable estimate

**1. K-Fold Cross-Validation:**

**Thuật toán:**
1. Chia data thành k folds
2. For i = 1 to k:
   - Use fold i làm validation
   - Use k-1 folds còn lại làm training
   - Train và evaluate
3. Average metrics across k folds

**Chọn k:**
- k=5: Standard, good balance
- k=10: More stable, more computational
- Larger k: Less bias, more variance, more expensive

**Ưu điểm:**
- Sử dụng toàn bộ data
- Stable estimate
- Reduce variance

**Nhược điểm:**
- k lần training (expensive)
- Có thể chậm

**2. Stratified K-Fold:**

**Nguyên lý:**
- Maintain class distribution trong mỗi fold
- Each fold representative

**Khi nào dùng:**
- Imbalanced datasets
- Classification tasks
- Đảm bảo mỗi fold có đủ samples mỗi class

**Ưu điểm:**
- Fair evaluation với imbalanced data
- Consistent class proportions

**3. Leave-One-Out (LOO):**

**Nguyên lý:**
- k = n (n = số samples)
- Mỗi sample là một fold

**Ưu điểm:**
- Maximum data cho training
- No randomness
- Deterministic

**Nhược điểm:**
- Rất chậm (n iterations)
- High variance
- Chỉ khả thi với small datasets (< 1000)

**Khi nào dùng:**
- Very small datasets
- Need maximum training data
- Computational resources available

**4. Time Series Cross-Validation:**

**Nguyên lý:**
- Respect temporal order
- Train on past, validate on future
- No data leakage from future

**Expanding Window:**
```
Fold 1: Train [1:100] → Test [101:120]
Fold 2: Train [1:120] → Test [121:140]
Fold 3: Train [1:140] → Test [141:160]
```

**Rolling Window:**
```
Fold 1: Train [1:100] → Test [101:120]
Fold 2: Train [21:120] → Test [121:140]
Fold 3: Train [41:140] → Test [141:160]
```

**Quan trọng:**
- **KHÔNG shuffle data**
- Maintain temporal order
- Avoid look-ahead bias

**5. Nested Cross-Validation:**

**Nguyên lý:**
- Outer loop: Model evaluation
- Inner loop: Hyperparameter tuning
- Prevents overfitting in parameter selection

**Structure:**
```
Outer CV (5-fold):
  For each outer fold:
    Inner CV (5-fold):
      Hyperparameter tuning
    Train with best params
    Evaluate on outer fold
```

**Ưu điểm:**
- Unbiased performance estimate
- Proper hyperparameter tuning
- Gold standard

**Nhược điểm:**
- Very expensive (k_outer × k_inner trainings)
- Overkill cho simple problems

**Khi nào dùng:**
- Need unbiased estimate
- Publishing results
- Critical applications
- Have computational resources

### Learning Curves (Đường Cong Học)

Phân tích hiệu suất mô hình vs kích thước training set.

**Vẽ gì:**
- X-axis: Training set size
- Y-axis: Error (hoặc Score)
- Two curves: Training error & Validation error

**Chẩn Đoán:**

**1. High Bias (Underfitting):**
```
Training error: Cao
Validation error: Cao
Gap: Nhỏ
Both plateau at high error
```
**Dấu hiệu:**
- Cả hai curves plateau
- Performance kém ngay cả với nhiều data
- Thêm data không giúp

**Giải pháp:**
- Increase model complexity
- Add features
- Reduce regularization
- Try complex model

**2. High Variance (Overfitting):**
```
Training error: Thấp
Validation error: Cao
Gap: Lớn
Gap doesn't close with more data
```
**Dấu hiệu:**
- Large gap giữa curves
- Training error tiếp tục giảm
- Validation error không cải thiện

**Giải pháp:**
- Get more training data
- Reduce model complexity
- Increase regularization
- Feature selection
- Dropout, early stopping

**3. Good Fit:**
```
Training error: Thấp
Validation error: Thấp
Gap: Nhỏ
Both converge
```
**Dấu hiệu:**
- Small gap
- Both errors low
- Converged performance

**4. More Data Helps:**
```
Validation error giảm khi tăng data
Gap đang đóng lại
Chưa plateau
```
**Hành động:** Get more data!

**5. More Data Doesn't Help:**
```
Both curves plateau
Adding data không cải thiện
```
**Hành động:** Improve features hoặc model

### Bias-Variance Tradeoff (Sự Đánh Đổi Bias-Variance)

**Công thức:**
$$Expected\ Error = Bias^2 + Variance + Irreducible\ Error$$

**Bias (Thiên Lệch):**
- Error từ giả định đơn giản hóa
- Underfitting
- Model không capture được patterns
- High bias → Systematic errors

**Variance (Phương Sai):**
- Error từ sensitivity to training data
- Overfitting
- Model learns noise
- High variance → Different results với different data

**Irreducible Error:**
- Noise trong data
- Không thể giảm
- Comes from data collection

**Tradeoff:**
- Decrease bias → Increase variance
- Decrease variance → Increase bias
- Cần balance

**Strategies:**

**Giảm High Bias:**
1. Increase model complexity
2. Add more features/polynomial features
3. Decrease regularization
4. Train longer
5. Use ensemble methods

**Giảm High Variance:**
1. Get more training data
2. Reduce model complexity
3. Increase regularization (L1, L2, dropout)
4. Feature selection
5. Early stopping
6. Ensemble methods (bagging)

**Sweet Spot:**
- Minimize total error
- Balance bias và variance
- Depends on problem và data

**Visualize:**
```
Total Error
    |     \
    |      \___Bias²
    |___________\
    |            \___
    |Variance_____\___Total
    |________________\___
    |___________________\___
    +----------------------->
    Simple          Complex
            Model Complexity
```

### Phương Pháp Ensemble

Kết hợp nhiều models để cải thiện hiệu suất.

**"Wisdom of crowds"**

**Tại sao hoạt động:**
- Errors của individual models cancel out
- Diverse models capture different patterns
- Reduce variance
- More robust

**1. Bagging (Bootstrap Aggregating):**

**Nguyên lý:**
- Train multiple models trên bootstrap samples
- Average predictions (regression) hoặc vote (classification)

**Bootstrap Sampling:**
- Sample with replacement
- Same size as original
- ~63% unique samples mỗi bootstrap

**Thuật toán:**
1. For i = 1 to M:
   - Create bootstrap sample $D_i$
   - Train model $M_i$ on $D_i$
2. Combine:
   - Regression: $\hat{y} = \frac{1}{M}\sum_{i=1}^{M}M_i(x)$
   - Classification: Majority vote

**Ưu điểm:**
- Reduce variance
- Parallel training
- Works với high-variance models

**Nhược điểm:**
- Không giảm bias
- Có thể chậm (many models)

**Ví dụ:** Random Forest

**2. Boosting:**

**Nguyên lý:**
- Sequential training
- Each model corrects errors của previous models
- Weighted combination

**Thuật toán (general):**
1. Initialize equal weights
2. For i = 1 to M:
   - Train model $M_i$ on weighted data
   - Tính error
   - Update weights (increase for misclassified)
   - Calculate model weight
3. Combine: Weighted vote/average

**Variants:**
- **AdaBoost:** Adjust sample weights
- **Gradient Boosting:** Fit residuals
- **XGBoost:** Optimized GBM
- **LightGBM:** Leaf-wise GBM
- **CatBoost:** Handle categorical

**Ưu điểm:**
- Reduce bias và variance
- Often best performance
- Handle complex patterns

**Nhược điểm:**
- Sequential (không parallel)
- Sensitive to noise
- Easy overfit
- Nhiều hyperparameters

**3. Stacking (Stacked Generalization):**

**Nguyên lý:**
- Train meta-model trên predictions của base models
- Combine diverse models

**Architecture:**
```
Base Models: Model1, Model2, Model3, ...
    ↓          ↓       ↓        ↓
Predictions: pred1, pred2, pred3, ...
    ↓
Meta-Model: Learns to combine predictions
    ↓
Final Prediction
```

**Thuật toán:**
1. Split data: Train + Holdout
2. Train base models trên Train set
3. Generate predictions trên Holdout set
4. Train meta-model:
   - Input: Base model predictions
   - Output: True labels
5. Final prediction: Meta-model(base predictions)

**Base Models:**
- Diverse algorithms (RF, SVM, NN, etc.)
- Different architectures
- Different feature sets

**Meta-Model:**
- Usually simple (Linear, Logistic Regression)
- Can be any model

**Ưu điểm:**
- Combine strengths của different models
- Often best performance
- Flexible

**Nhược điểm:**
- Complex pipeline
- Risk overfitting
- Computationally expensive
- Hard to interpret

**4. Voting:**

**Hard Voting (Classification):**
- Each model votes
- Majority class wins
- Simple democracy

**Soft Voting (Classification):**
- Average predicted probabilities
- More nuanced
- Usually better than hard

**Averaging (Regression):**
- Simple average
- Weighted average possible

**Ưu điểm:**
- Simple
- Reduce variance
- No additional training

**Nhược điểm:**
- All models equal weight (hard voting)
- Không learn to combine

**Best Practices Ensemble:**
1. **Diverse models:** Different algorithms, features, architectures
2. **Not too many:** 5-10 models often enough
3. **Strong individual models:** Garbage in, garbage out
4. **Cross-validation:** Avoid overfitting in stacking
5. **Computational cost:** Consider inference time

### Tiêu Chí Lựa Chọn Mô Hình

**1. Akaike Information Criterion (AIC):**
$$AIC = 2k - 2\ln(\hat{L})$$

Trong đó:
- $k$ là số parameters
- $\hat{L}$ là maximized likelihood

**Diễn giải:**
- Lower AIC = better model
- Penalizes model complexity
- Trade-off fit vs complexity

**2. Bayesian Information Criterion (BIC):**
$$BIC = k\ln(n) - 2\ln(\hat{L})$$

Trong đó $n$ là số observations.

**So với AIC:**
- BIC penalizes complexity nhiều hơn
- Prefers simpler models
- Better với large $n$

**3. Adjusted R-squared:**
$$R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}$$

**Đặc điểm:**
- Penalizes thêm predictors
- Không tăng khi thêm useless features
- Tốt hơn $R^2$ cho model comparison

**Khi nào dùng:**
- AIC/BIC: Model comparison, likelihood-based
- Adjusted R²: Linear regression
- Cross-validation: General, most reliable

### Tối Ưu Pipeline

**1. Pipeline Construction:**

**Sklearn Pipeline:**
```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('classifier', RandomForestClassifier())
])
```

**Ưu điểm:**
- Consistent transformations
- Avoid data leakage
- Easy to deploy
- Grid search toàn pipeline

**2. Feature Union:**

```python
from sklearn.pipeline import FeatureUnion

feature_union = FeatureUnion([
    ('numeric', numeric_pipeline),
    ('text', text_pipeline),
    ('categorical', categorical_pipeline)
])
```

**Đặc điểm:**
- Parallel processing
- Combine different feature types
- Modular design

**3. Caching:**

```python
pipeline = Pipeline([...], memory='cache_folder')
```

**Ưu điểm:**
- Cache intermediate results
- Speed up grid search
- Reuse computations

### Early Stopping

Cho iterative algorithms (gradient descent, boosting).

**Nguyên lý:**
- Monitor validation performance
- Stop khi performance degrades
- Prevents overfitting

**Thuật toán:**
1. Set patience (số epochs không cải thiện)
2. Track best validation score
3. Each epoch:
   - Evaluate validation
   - If improved: Reset counter, save model
   - If not: Increment counter
4. If counter > patience: Stop

**Ưu điểm:**
- Automatic regularization
- Save training time
- Prevent overfitting

**Tham số:**
- **patience:** Số epochs chờ (5-20)
- **min_delta:** Minimum improvement (0.001-0.01)
- **restore_best_weights:** Restore model tốt nhất

**Áp dụng:**
- Neural Networks (most common)
- Gradient Boosting
- Iterative algorithms

### Chiến Lược Regularization

**1. L1 (Lasso):**
- Feature selection
- Sparse solutions
- $\lambda||w||_1$

**2. L2 (Ridge):**
- Shrinks coefficients
- Handles multicollinearity
- $\lambda||w||_2^2$

**3. Elastic Net:**
- Combines L1 và L2
- $\lambda_1||w||_1 + \lambda_2||w||_2^2$

**4. Dropout (Neural Networks):**
- Randomly drop units during training
- Rate: 0.2-0.5
- Forces redundancy
- Reduces co-adaptation

**5. Data Augmentation:**
- Artificially expand training set
- Transformations:
  - Images: Rotation, flip, crop, brightness
  - Text: Synonym replacement, back-translation
  - Audio: Time stretch, pitch shift, noise

**Ưu điểm:**
- More data without collecting
- Improve generalization
- Reduce overfitting

### AutoML

Automated machine learning systems.

**Tools:**
- **Auto-sklearn:** Automated sklearn
- **H2O AutoML:** Enterprise-grade
- **Google AutoML:** Cloud-based
- **TPOT:** Genetic programming
- **AutoKeras:** Automated deep learning

**Tự động hóa:**
1. **Feature preprocessing:**
   - Scaling, encoding, imputation
   - Feature engineering

2. **Algorithm selection:**
   - Try multiple algorithms
   - Ensemble automatically

3. **Hyperparameter tuning:**
   - Bayesian optimization
   - Meta-learning

4. **Model ensembling:**
   - Combine best models
   - Stacking, voting

**Ưu điểm:**
- Save time
- Good baseline
- Accessible to non-experts
- Try many approaches

**Nhược điểm:**
- Black box
- Computational expensive
- May not find best solution
- Limited customization
- Overkill cho simple problems

**Khi nào dùng:**
- Starting point
- Baseline comparison
- Limited ML expertise
- Have computational resources

**Best practices:**
- Set time/resource limits
- Understand results
- Use as starting point, tune further
- Validate on hold-out set

### Best Practices

**1. Start Simple:**
- Begin với simple model (Linear, Logistic)
- Establish baseline
- Increase complexity nếu cần

**2. Establish Baseline:**
- Random prediction
- Mean/Mode prediction
- Simple rule-based
- Must beat baseline

**3. Feature Importance:**
- Understand which features matter
- Remove useless features
- Focus effort on important features

**4. Iterate:**
- Continuous improvement cycle
- Experiment → Analyze → Refine
- Keep track of experiments

**5. Monitor Multiple Metrics:**
- Không chỉ một metric
- Precision, Recall, F1, AUC
- Business metrics

**6. Avoid Data Leakage:**
- **Proper CV:** Fit preprocessors trên train folds only
- **Time-based splits:** cho time series
- **No target leakage:** Features không chứa info về target
- **Test set untouched:** Cho đến cuối

**7. Document Everything:**
- Experiments log
- Model versions
- Hyperparameters
- Results và insights

**8. Reproducibility:**
- Set random seeds
- Version control code
- Save data versions
- Document environment
- Use containers (Docker)

**9. Model Versioning:**
- MLflow, DVC
- Track models
- Compare versions
- Rollback nếu cần

**10. Validation Strategy:**
- Robust CV
- Hold-out test set
- Temporal validation cho time series

**11. Feature Engineering First:**
- "Data > Algorithms"
- Good features > Complex models
- Domain knowledge valuable

**12. Monitor Training:**
- Training vs validation
- Learning curves
- Early signs of overfitting

**13. Consider Production:**
- Inference time
- Model size
- Dependencies
- Maintenance
- Explainability

**14. Test on Real Data:**
- Not just metrics
- Qualitative analysis
- Edge cases
- Failure modes

---

---

## Học Không Giám Sát (Unsupervised Learning)

### Giới Thiệu Về Học Không Giám Sát

Học không giám sát khám phá các mẫu ẩn trong dữ liệu không có nhãn mà không cần biến mục tiêu tường minh. Nó được sử dụng cho phân tích dữ liệu khám phá, nhận dạng mẫu và nén dữ liệu.

**Đặc điểm chính:**
- Không có labels (y)
- Chỉ có features (X)
- Tìm structure trong data
- Exploratory analysis

**So với Supervised Learning:**
| Tiêu chí | Supervised | Unsupervised |
|----------|-----------|--------------|
| Labels | Có | Không |
| Mục tiêu | Dự đoán | Khám phá |
| Feedback | Có (accuracy) | Không rõ ràng |
| Ứng dụng | Classification, Regression | Clustering, Dimensionality Reduction |

**Các tác vụ chính:**
1. **Clustering:** Nhóm dữ liệu tương tự
2. **Dimensionality Reduction:** Giảm số chiều
3. **Anomaly Detection:** Phát hiện bất thường
4. **Association Rule Learning:** Tìm mối quan hệ

**Thách thức:**
- Không có ground truth để đánh giá
- Khó xác định số clusters/components
- Kết quả có thể subjective
- Cần domain knowledge để interpret

### Clustering (Phân Cụm)

Nhóm các điểm dữ liệu tương tự lại với nhau.

**Mục tiêu:**
- High intra-cluster similarity (trong cùng cluster)
- Low inter-cluster similarity (giữa các clusters)

**Ứng dụng:**
- Customer segmentation
- Document clustering
- Image segmentation
- Anomaly detection
- Data compression

### K-Means Clustering

Thuật toán phân cụm phổ biến nhất, chia dữ liệu thành K clusters.

**Thuật toán:**

**Bước 1: Initialization**
- Chọn K centroids ngẫu nhiên
- Có thể từ data points hoặc random positions

**Bước 2: Assignment**
- Gán mỗi điểm đến centroid gần nhất
- Sử dụng Euclidean distance:
$$d(x, \mu_k) = ||x - \mu_k|| = \sqrt{\sum_{j=1}^{n}(x_j - \mu_{kj})^2}$$

**Bước 3: Update**
- Cập nhật centroids = mean của các điểm assigned
$$\mu_k = \frac{1}{|C_k|}\sum_{x \in C_k}x$$

**Bước 4: Repeat**
- Lặp lại Steps 2-3 cho đến khi convergence

**Convergence khi:**
- Centroids không đổi
- Assignments không đổi
- Đạt max iterations

**Objective Function (WCSS - Within-Cluster Sum of Squares):**
$$J = \sum_{k=1}^{K}\sum_{x \in C_k}||x - \mu_k||^2$$

Mục tiêu: Minimize J

**Chọn K (Số Clusters):**

**1. Elbow Method:**
- Vẽ WCSS vs K
- Tìm "khuỷu tay" (elbow) - điểm mà WCSS giảm chậm lại
- Tradeoff giữa số clusters và fit

**Ví dụ:**
```
WCSS
  |  \
  |    \
  |      \___
  |          ----___
  +----------------->
  1  2  3  4  5  6  K
       ↑ Elbow ~ K=3
```

**2. Silhouette Score:**
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

Trong đó:
- $a(i)$: Average distance đến các điểm trong cùng cluster
- $b(i)$: Average distance đến các điểm trong nearest cluster
- Score: -1 đến 1
  - ~1: Tốt, điểm xa cluster khác
  - ~0: Gần boundary
  - Negative: Có thể assign sai

**Average Silhouette Score:**
- Trung bình trên tất cả điểm
- Chọn K có score cao nhất

**3. Gap Statistic:**
- So sánh WCSS với expected WCSS dưới null distribution
- Chọn K where gap lớn nhất

**4. Domain Knowledge:**
- Business requirements
- Interpretability
- Practical constraints

**Ưu Điểm:**
- Đơn giản, dễ implement
- Nhanh, scalable
- Hoạt động tốt với spherical clusters
- Dễ interpret

**Nhược Điểm:**

**1. Phải chỉ định K trước:**
- Không biết K optimal
- Cần thử nhiều giá trị

**2. Nhạy cảm với initialization:**
- Different initializations → different results
- Có thể stuck ở local minima

**3. Giả định spherical clusters:**
- Không tốt với elongated/irregular shapes
- Equal-sized clusters

**4. Nhạy cảm với outliers:**
- Outliers ảnh hưởng đến centroids
- Có thể tạo clusters cho outliers

**5. Phụ thuộc vào scale:**
- Features có scale lớn dominate
- Cần scaling trước

**Cải Tiến:**

**K-Means++:**
- Better initialization strategy
- Chọn centroids xa nhau
- Giảm chance của bad initialization
- Convergence nhanh hơn

**Mini-batch K-Means:**
- Sử dụng random mini-batches
- Nhanh hơn nhiều với large datasets
- Trade-off: Hơi kém chính xác
- Good cho online learning

**Practical Tips:**
- Luôn standardize features
- Run multiple times với different initializations
- Use K-Means++ initialization
- Try different K values
- Visualize results nếu có thể

### Hierarchical Clustering (Phân Cụm Phân Cấp)

Xây dựng hierarchy của clusters mà không cần chỉ định K trước.

**Đặc điểm:**
- Tạo tree structure (dendrogram)
- Có thể chọn số clusters sau
- Two approaches: Agglomerative và Divisive

**1. Agglomerative (Bottom-Up - Tích Tụ):**

**Thuật toán:**
1. Start: Mỗi điểm là một cluster (N clusters)
2. Repeat:
   - Tìm 2 clusters gần nhất
   - Merge chúng thành 1 cluster
3. Until: Chỉ còn 1 cluster

**Steps chi tiết:**
- Initialize: N clusters
- Iteration 1: N-1 clusters
- Iteration 2: N-2 clusters
- ...
- Final: 1 cluster

**2. Divisive (Top-Down - Phân Chia):**

**Thuật toán:**
1. Start: Tất cả điểm trong 1 cluster
2. Repeat:
   - Chọn cluster để split
   - Chia thành 2 sub-clusters
3. Until: Mỗi điểm là 1 cluster

**Ít phổ biến:** Computationally expensive hơn

**Linkage Methods (Cách Đo Khoảng Cách Giữa Clusters):**

**1. Single Linkage (Minimum):**
$$d(C_i, C_j) = \min_{x \in C_i, y \in C_j}d(x,y)$$
- Khoảng cách giữa 2 điểm gần nhất
- Tạo long, chain-like clusters
- Sensitive to noise và outliers

**2. Complete Linkage (Maximum):**
$$d(C_i, C_j) = \max_{x \in C_i, y \in C_j}d(x,y)$$
- Khoảng cách giữa 2 điểm xa nhất
- Tạo compact, spherical clusters
- Ít sensitive to outliers

**3. Average Linkage:**
$$d(C_i, C_j) = \frac{1}{|C_i||C_j|}\sum_{x \in C_i}\sum_{y \in C_j}d(x,y)$$
- Trung bình tất cả pairwise distances
- Balance giữa single và complete
- Phổ biến choice

**4. Ward's Method:**
- Minimize within-cluster variance sau khi merge
- Maximize between-cluster variance
- Tạo balanced, compact clusters
- Thường cho kết quả tốt nhất
- Phổ biến nhất trong thực tế

**Dendrogram (Biểu Đồ Cây):**

Tree diagram showing cluster hierarchy.

**Đọc Dendrogram:**
- Vertical axis: Distance/dissimilarity
- Horizontal axis: Samples
- Height của merge: Distance giữa clusters
- Càng cao merge càng dissimilar

**Cutting Dendrogram:**
- Vẽ horizontal line
- Number of intersections = Number of clusters
- Height của cut = dissimilarity threshold

**Ưu Điểm:**
- Không cần specify K trước
- Dendrogram provides insights
- Flexible - có thể chọn K sau
- Deterministic (no randomness)

**Nhược Điểm:**
- Computationally expensive: O(N²log N) or O(N³)
- Không scale với large datasets
- Một khi merge không thể undo
- Memory intensive

**Khi Nào Dùng:**
- Small-medium datasets (< 10,000)
- Cần understand hierarchy
- Không biết K optimal
- Exploratory analysis

### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

Nhóm các điểm có mật độ cao, robust to outliers và arbitrary shapes.

**Tham Số:**

**1. ε (epsilon):**
- Maximum distance giữa 2 điểm để được coi là neighbors
- Định nghĩa neighborhood radius
- Quá nhỏ: Nhiều noise points
- Quá lớn: Merge nhiều clusters

**2. MinPts (Minimum Points):**
- Minimum số điểm trong ε-neighborhood để là core point
- Thường: 4, 5, hoặc 2×dim
- Larger MinPts: Ít core points, stricter

**Các Loại Điểm:**

**1. Core Point:**
- Có ≥ MinPts điểm khác trong ε-neighborhood (bao gồm cả chính nó)
- Trung tâm của clusters
- Can form clusters

**2. Border Point:**
- Nằm trong ε-neighborhood của core point
- Có < MinPts neighbors
- Thuộc cluster nhưng không core
- Ở biên của cluster

**3. Noise Point (Outlier):**
- Không phải core point
- Không nằm trong ε của bất kỳ core point nào
- Isolated points

**Thuật Toán:**

1. For each unvisited point:
   - Mark as visited
   - Tìm ε-neighbors
   - If neighbors < MinPts: Mark as noise
   - Else: Start new cluster
     - Add point và neighbors to cluster
     - For each neighbor:
       - If unvisited: Visit và expand cluster
       - If noise: Add to cluster

**Ưu Điểm:**

**1. Arbitrary shapes:**
- Không giả định spherical
- Handle complex geometries
- Non-convex clusters

**2. Robust to outliers:**
- Outliers = noise points
- Không ảnh hưởng clusters

**3. Không cần specify K:**
- Tự động determine số clusters
- Dựa trên density

**4. Deterministic:**
- Same parameters → same results (mostly)

**Nhược Điểm:**

**1. Sensitive to parameters:**
- ε và MinPts khó chọn
- Cần domain knowledge hoặc tuning

**2. Varying densities:**
- Một cặp (ε, MinPts) không phù hợp cho tất cả
- Clusters với different densities problematic

**3. High-dimensional data:**
- Distance metrics less meaningful
- Curse of dimensionality

**4. Memory và computation:**
- O(N²) worst case
- Index structures help (KD-tree, Ball-tree)

**Chọn Parameters:**

**ε (epsilon):**
- **K-distance graph:**
  - Vẽ sorted k-distances (k=MinPts-1)
  - Tìm "knee" - nơi tăng đột ngột
  - ε = distance tại knee

**MinPts:**
- Rule of thumb: MinPts ≥ dim + 1
- Thường: 4 hoặc 5
- Larger for noisy data
- Smaller for cleaner data

**Variants:**

**HDBSCAN (Hierarchical DBSCAN):**
- Hierarchical approach
- Không cần specify ε
- Better với varying densities
- Extract clusters ở different density levels

**OPTICS:**
- Ordering points to identify clustering structure
- Tạo reachability plot
- Flexible extraction

**Khi Nào Dùng:**
- Non-spherical clusters
- Outliers present
- Không biết K
- Arbitrary shaped regions

### Gaussian Mixture Models (GMM) - Mô Hình Hỗn Hợp Gaussian

Mô hình xác suất giả định data đến từ hỗn hợp các phân phối Gaussian.

**Khái Niệm:**
- Data generated từ K Gaussian distributions
- Mỗi Gaussian = một cluster
- Soft assignment (probabilities)

**Model:**
$$P(x) = \sum_{k=1}^{K}\pi_k\mathcal{N}(x|\mu_k, \Sigma_k)$$

Trong đó:
- $\pi_k$: Mixing coefficient (weight) của component k
  - $\sum_{k=1}^{K}\pi_k = 1$
  - $0 \leq \pi_k \leq 1$
- $\mu_k$: Mean vector của Gaussian k
- $\Sigma_k$: Covariance matrix của Gaussian k
- $\mathcal{N}(x|\mu_k, \Sigma_k)$: Gaussian distribution

**Gaussian Distribution:**
$$\mathcal{N}(x|\mu, \Sigma) = \frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}\exp\left(-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\right)$$

**Expectation-Maximization (EM) Algorithm:**

Iterative algorithm để estimate parameters.

**E-Step (Expectation):**
Tính responsibility (xác suất mềm) của mỗi component cho mỗi điểm:

$$\gamma_{ik} = \frac{\pi_k\mathcal{N}(x_i|\mu_k, \Sigma_k)}{\sum_{j=1}^{K}\pi_j\mathcal{N}(x_i|\mu_j, \Sigma_j)}$$

- $\gamma_{ik}$: Probability điểm $i$ belongs to cluster $k$
- $\sum_{k=1}^{K}\gamma_{ik} = 1$ for each $i$

**M-Step (Maximization):**
Update parameters dựa trên responsibilities:

**Mixing coefficients:**
$$\pi_k = \frac{1}{N}\sum_{i=1}^{N}\gamma_{ik}$$

**Means:**
$$\mu_k = \frac{\sum_{i=1}^{N}\gamma_{ik}x_i}{\sum_{i=1}^{N}\gamma_{ik}}$$

**Covariances:**
$$\Sigma_k = \frac{\sum_{i=1}^{N}\gamma_{ik}(x_i-\mu_k)(x_i-\mu_k)^T}{\sum_{i=1}^{N}\gamma_{ik}}$$

**Repeat E-Step và M-Step** cho đến convergence.

**Convergence:**
- Log-likelihood không thay đổi nhiều
- Parameters stable
- Đạt max iterations

**Ưu Điểm:**

**1. Soft clustering:**
- Probability of membership cho mỗi cluster
- Captures uncertainty
- More nuanced than hard assignment

**2. Flexible cluster shapes:**
- Elliptical clusters
- Different sizes
- Different orientations

**3. Probabilistic framework:**
- Sound mathematical foundation
- Can compute likelihoods
- Model selection với BIC/AIC

**4. Generative model:**
- Có thể generate new samples
- Understand data distribution

**Nhược Điểm:**

**1. Cần specify K:**
- Không tự động determine
- Use BIC/AIC để chọn

**2. Sensitive to initialization:**
- EM có thể converge to local optima
- Run multiple times

**3. Assumes Gaussian:**
- Không phù hợp nếu data không Gaussian
- Limited to elliptical shapes

**4. Computationally expensive:**
- Covariance matrix inversion
- Slower than K-Means

**5. Singular covariance matrices:**
- Có thể xảy ra với small clusters
- Need regularization

**So Sánh K-Means vs GMM:**

| Tiêu chí | K-Means | GMM |
|----------|---------|-----|
| Assignment | Hard | Soft (probabilistic) |
| Cluster shape | Spherical | Elliptical |
| Parameters | Centroids | Means + Covariances |
| Speed | Nhanh | Chậm hơn |
| Flexibility | Ít | Nhiều |
| Probabilistic | Không | Có |

**Chọn K:**
- Bayesian Information Criterion (BIC)
- Akaike Information Criterion (AIC)
- Cross-validation
- Silhouette score

### Các Thuật Toán Clustering Khác

**1. Mean Shift:**

**Nguyên lý:**
- Density-based, no need chỉ định số clusters
- Shift points toward mode (density maxima)

**Thuật toán:**
1. Khởi tạo window around each point
2. Tính mean của points trong window
3. Shift center đến mean
4. Repeat until convergence
5. Points converging to same mode = same cluster

**Ưu điểm:**
- Không cần specify K
- Arbitrary shapes
- Automatic K

**Nhược điểm:**
- Slow (O(N²))
- Bandwidth parameter critical

**2. Spectral Clustering:**

**Nguyên lý:**
- Uses graph theory
- Eigenvalues của similarity matrix
- Good cho non-convex clusters

**Steps:**
1. Construct similarity graph
2. Compute Laplacian matrix
3. Eigenvalue decomposition
4. K-Means trên eigenvectors

**Ưu điểm:**
- Handle complex shapes
- Thường tốt hơn K-Means
- Based on graph cuts

**Nhược điểm:**
- Computationally expensive
- Cần tune similarity function
- Sensitive to parameters

**3. Affinity Propagation:**

**Nguyên lý:**
- Message passing between data points
- Points "vote" on their exemplars
- Automatically determines K

**Messages:**
- **Responsibility:** Điểm $i$ chọn điểm $k$ làm exemplar
- **Availability:** Điểm $k$ available làm exemplar cho $i$

**Ưu điểm:**
- Không cần specify K
- Flexible
- Finds exemplars (representative points)

**Nhược điểm:**
- Slow (O(N²T), T = iterations)
- Memory intensive
- Sensitive to preferences

**4. OPTICS (Ordering Points To Identify Clustering Structure):**

**Nguyên lý:**
- Extension của DBSCAN
- Tạo ordering của points
- Handle varying densities better

**Output:**
- Reachability plot
- Extract clusters ở different density levels

**Ưu điểm:**
- Varying densities
- Không cần ε cụ thể
- Hierarchical view

**Nhược điểm:**
- Complex interpretation
- Still need MinPts

**So Sánh Các Thuật Toán:**

| Algorithm | K needed | Shape | Outliers | Speed | Best for |
|-----------|----------|-------|----------|-------|----------|
| K-Means | Yes | Spherical | Sensitive | Fast | Large, simple |
| Hierarchical | No | Any | Sensitive | Slow | Small, hierarchy |
| DBSCAN | No | Arbitrary | Robust | Medium | Spatial, noise |
| GMM | Yes | Elliptical | Sensitive | Slow | Probabilistic |
| Mean Shift | No | Arbitrary | Robust | Slow | Non-uniform |
| Spectral | Yes | Complex | Sensitive | Slow | Graph-like |

### Giảm Số Chiều (Dimensionality Reduction)

Đã được cover chi tiết trong phần Feature Selection & Model Optimization, đây là summary.

### Principal Component Analysis (PCA)

**Nguyên lý:**
- Linear transformation sang orthogonal components
- Components ordered by variance
- Maximize variance retained

**Công thức:**
$$Z = XW_k$$

Trong đó $W_k$ là matrix của k eigenvectors.

**Steps:**
1. Standardize data: $X' = \frac{X - \mu}{\sigma}$
2. Covariance matrix: $\Sigma = \frac{1}{n}X'^TX'$
3. Eigendecomposition: $\Sigma = V\Lambda V^T$
4. Chọn top k eigenvectors
5. Transform: $Z = X'W_k$

**Variance Explained:**
$$\frac{\lambda_k}{\sum_{i=1}^{n}\lambda_i} \times 100\%$$

**Chọn số components:**
- Cumulative variance ≥ 95% hoặc 99%
- Scree plot (elbow)
- Kaiser criterion (eigenvalue > 1)

**Ứng dụng:**
- Visualization (2D/3D)
- Noise reduction
- Feature extraction
- Speed up learning
- Preprocessing

### Singular Value Decomposition (SVD)

**Matrix factorization:**
$$X = U\Sigma V^T$$

- $U$: Left singular vectors (m × m)
- $\Sigma$: Singular values (m × n, diagonal)
- $V^T$: Right singular vectors (n × n)

**Quan hệ với PCA:**
- PCA eigenvectors = right singular vectors
- PCA eigenvalues = squared singular values

**Ứng dụng:**
- PCA computation
- Latent Semantic Analysis (LSA)
- Recommender systems (matrix completion)
- Image compression
- Data compression

**Truncated SVD:**
- Giữ top k components
- Approximation: $X \approx U_k\Sigma_kV_k^T$

### Independent Component Analysis (ICA)

**Nguyên lý:**
- Tách signal thành independent components
- Maximize statistical independence
- Non-Gaussian components

**Model:**
$$X = AS$$

Trong đó:
- $X$: Observed signals (mixed)
- $A$: Mixing matrix (unknown)
- $S$: Source signals (independent, unknown)

**Mục tiêu:** Estimate $A$ và $S$ from $X$

**Cocktail Party Problem:**
- Multiple people talking simultaneously
- Multiple microphones recording
- ICA separates individual voices

**So với PCA:**
- PCA: Decorrelation, orthogonal, Gaussian assumption
- ICA: Independence, not orthogonal, non-Gaussian

**Ứng dụng:**
- Blind source separation
- Signal processing (audio, EEG, fMRI)
- Feature extraction
- Artifact removal

### Non-negative Matrix Factorization (NMF)

**Nguyên lý:**
- Factorize matrix into non-negative factors
- Parts-based representation

**Model:**
$$X \approx WH$$

**Constraints:**
- $X \geq 0$: Input non-negative
- $W \geq 0$: Basis matrix non-negative
- $H \geq 0$: Coefficient matrix non-negative

**Interpretation:**
- $W$: Basis vectors (features, topics)
- $H$: Coefficients (weights, memberships)
- Each column của $X$ = linear combination của columns của $W$

**Optimization:**
Minimize: $||X - WH||^2$ with constraints

**Ứng dụng:**

**1. Topic Modeling:**
- $X$: Document-term matrix
- $W$: Term-topic matrix
- $H$: Topic-document matrix

**2. Image Processing:**
- Learn parts of faces
- $W$: Facial features
- $H$: How to combine them

**3. Recommender Systems:**
- $X$: User-item matrix
- $W$: User factors
- $H$: Item factors

**Ưu điểm:**
- Interpretable (non-negativity)
- Parts-based representation
- Sparse solutions

**Nhược điểm:**
- Non-convex (local minima)
- Slower than PCA
- Requires non-negative data

### Manifold Learning

Khám phá non-linear structure trong high-dimensional data.

**Manifold:**
- Low-dimensional surface embedded trong high-dimensional space
- Ví dụ: Swiss roll (2D manifold trong 3D)

**1. Isomap (Isometric Feature Mapping):**

**Nguyên lý:**
- Preserve geodesic distances (shortest path trên manifold)
- Global structure preservation

**Steps:**
1. Construct neighborhood graph
2. Compute shortest path distances (Dijkstra)
3. Apply MDS (Multi-Dimensional Scaling)

**Ưu điểm:**
- Global structure
- Theoretical foundation

**Nhược điểm:**
- Expensive (shortest paths)
- Sensitive to noise
- Cần connected graph

**2. Locally Linear Embedding (LLE):**

**Nguyên lý:**
- Preserve local relationships
- Each point reconstructed từ neighbors

**Steps:**
1. Find k nearest neighbors
2. Compute reconstruction weights
3. Embed với same weights trong low-dim

**Ưu điểm:**
- Fast
- Non-iterative
- Good local preservation

**Nhược điểm:**
- Sensitive to k
- Can produce distorted results

**3. t-SNE:**
Đã cover chi tiết trước đó.

**4. UMAP:**
Đã cover chi tiết trước đó.

**So sánh:**
- **Isomap:** Global, geodesic distances
- **LLE:** Local, linear reconstruction
- **t-SNE:** Local, visualization, stochastic
- **UMAP:** Both local & global, faster than t-SNE

### Phát Hiện Bất Thường (Anomaly Detection)

Xác định các items, events, hoặc observations hiếm.

**Anomaly types:**
- **Point anomalies:** Single data point
- **Contextual anomalies:** Trong specific context
- **Collective anomalies:** Collection của points

**1. Statistical Methods:**

**Z-score:**
$$z = \frac{x - \mu}{\sigma}$$

- |z| > 3: Anomaly (99.7% rule)
- Giả định Gaussian distribution

**Modified Z-score (Robust):**
$$M = \frac{0.6745(x - median)}{MAD}$$

- MAD = Median Absolute Deviation
- Robust to outliers

**Interquartile Range (IQR):**
- IQR = Q3 - Q1
- Outliers: < Q1 - 1.5×IQR hoặc > Q3 + 1.5×IQR

**2. Isolation Forest:**

**Nguyên lý:**
- Anomalies are few và different
- Easier to isolate than normal points
- Random partitioning

**Path length:**
- Normal points: Longer paths
- Anomalies: Shorter paths

**Thuật toán:**
1. Build ensemble of isolation trees
2. Each tree: Random splits
3. Compute average path length
4. Shorter paths → Higher anomaly score

**Ưu điểm:**
- Fast, scalable
- High-dimensional data
- Không cần distribution assumption

**Nhược điểm:**
- Không giải thích tại sao anomaly
- Random (need multiple trees)

**3. One-Class SVM:**

**Nguyên lý:**
- Learn boundary around normal data
- Separate normal from origin
- Points outside boundary = anomalies

**Objective:**
Maximize margin from origin to hyperplane

**Ưu điểm:**
- Kernel trick for non-linear
- Theoretical foundation
- Good cho high-dim

**Nhược điểm:**
- Expensive với large data
- Sensitive to ν parameter
- Cần feature scaling

**4. Local Outlier Factor (LOF):**

**Nguyên lý:**
- Compare local density với neighbors
- Anomaly có density thấp hơn neighbors

**LOF Score:**
- ~1: Normal
- <<1: Denser than neighbors (inlier)
- >>1: Less dense (outlier)

**Ưu điểm:**
- Local anomalies
- Varying densities

**Nhược điểm:**
- Expensive (O(N²))
- Sensitive to k

**5. Autoencoders:**

**Nguyên lý:**
- Neural network học reconstruct normal data
- Anomalies have high reconstruction error

**Reconstruction error:**
$$Error = ||x - \hat{x}||^2$$

- Threshold: Mean + k × std
- Points above threshold = anomalies

**Ưu điểm:**
- Non-linear patterns
- High-dimensional
- Deep representations

**Nhược điểm:**
- Need training data (mostly normal)
- Computationally expensive
- Hyperparameter tuning

**Ứng dụng:**
- Fraud detection
- Network intrusion
- Manufacturing defects
- Medical diagnosis
- System monitoring

### Association Rule Learning

Khám phá mối quan hệ giữa các biến.

**Market Basket Analysis:**
Tìm sản phẩm thường được mua cùng nhau.

**Terminology:**
- **Itemset:** Tập hợp items {Milk, Bread}
- **Transaction:** Một lần mua hàng
- **Rule:** A → B (If buy A, then buy B)

**Metrics:**

**1. Support:**
$$Support(A) = \frac{\text{Transactions containing A}}{\text{Total transactions}}$$

- Tỷ lệ transactions có itemset
- Popular items có support cao

**2. Confidence:**
$$Confidence(A \rightarrow B) = \frac{Support(A \cup B)}{Support(A)} = P(B|A)$$

- Tỷ lệ transactions có B trong số có A
- Strength của rule

**3. Lift:**
$$Lift(A \rightarrow B) = \frac{Confidence(A \rightarrow B)}{Support(B)} = \frac{P(A \cap B)}{P(A)P(B)}$$

- Measure of association
- Lift = 1: Independent
- Lift > 1: Positive correlation
- Lift < 1: Negative correlation

**Ví dụ:**
- Rule: {Milk} → {Bread}
- Support({Milk, Bread}) = 0.3 (30% transactions)
- Confidence = 0.6 (60% người mua Milk cũng mua Bread)
- Lift = 1.2 (Buying Milk tăng 20% khả năng mua Bread)

**Algorithms:**

**1. Apriori Algorithm:**

**Nguyên lý:**
- If itemset frequent → all subsets frequent
- If itemset infrequent → all supersets infrequent

**Steps:**
1. Find frequent 1-itemsets (support ≥ min_support)
2. Generate candidate k-itemsets from frequent (k-1)-itemsets
3. Prune candidates using apriori property
4. Count support và find frequent k-itemsets
5. Repeat until no more frequent itemsets
6. Generate rules từ frequent itemsets

**Ưu điểm:**
- Guaranteed to find all frequent itemsets
- Pruning reduces candidates

**Nhược điểm:**
- Multiple database scans
- Expensive với large datasets
- Chậm với low support threshold

**2. FP-Growth (Frequent Pattern Growth):**

**Nguyên lý:**
- Compress database into FP-tree
- Mine directly từ tree
- Chỉ 2 database scans

**Steps:**
1. Scan database, find frequent items
2. Build FP-tree (compressed representation)
3. Mine frequent patterns từ FP-tree

**Ưu điểm:**
- Nhanh hơn Apriori nhiều
- Không generate candidates
- Memory efficient (tree compression)

**Nhược điểm:**
- Complex implementation
- FP-tree construction overhead

**Thresholds:**
- **min_support:** 0.01 - 0.1 (1% - 10%)
- **min_confidence:** 0.5 - 0.8 (50% - 80%)
- **min_lift:** > 1

**Ứng dụng:**

**1. Retail:**
- Product recommendations
- Store layout optimization
- Cross-selling strategies

**2. Web Mining:**
- Clickstream analysis
- Page recommendation
- User behavior patterns

**3. Healthcare:**
- Symptom-disease associations
- Drug interactions
- Treatment effectiveness

**4. Telecommunications:**
- Calling patterns
- Service bundles
- Churn prediction

### Đánh Giá Clustering

Làm thế nào đánh giá quality của clustering khi không có ground truth?

**Internal Metrics (Không Cần Ground Truth):**

**1. Silhouette Coefficient:**
$$s = \frac{b - a}{\max(a,b)}$$

- Range: [-1, 1]
- 1: Perfect
- 0: Overlapping clusters
- -1: Wrong assignment

**2. Davies-Bouldin Index:**
$$DB = \frac{1}{K}\sum_{i=1}^{K}\max_{j \neq i}\left(\frac{\sigma_i + \sigma_j}{d(c_i, c_j)}\right)$$

- Lower is better
- Ratio of within-cluster to between-cluster distances

**3. Calinski-Harabasz Index (Variance Ratio Criterion):**
$$CH = \frac{SS_B/(K-1)}{SS_W/(N-K)}$$

- Higher is better
- Ratio of between-cluster to within-cluster variance

**4. Within-Cluster Sum of Squares (WCSS):**
- Used trong elbow method
- Lower is better
- Decreases với more clusters

**External Metrics (Có Ground Truth):**

**1. Adjusted Rand Index (ARI):**
- Measure agreement between two clusterings
- Adjusted for chance
- Range: [-1, 1], 1 = perfect match

**2. Normalized Mutual Information (NMI):**
- Information theoretic measure
- Range: [0, 1], 1 = perfect match
- Không bị ảnh hưởng bởi số clusters

**3. Fowlkes-Mallows Index:**
- Geometric mean của precision và recall
- Range: [0, 1]

**4. Purity:**
$$Purity = \frac{1}{N}\sum_{k=1}^{K}\max_j|C_k \cap T_j|$$

- Simple, intuitive
- Increases với more clusters (biased)

**Chọn Metrics:**
- **No ground truth:** Silhouette, Davies-Bouldin
- **Have ground truth:** ARI, NMI
- **Exploratory:** Multiple metrics
- **Business context:** Domain-specific metrics

### Ứng Dụng Của Unsupervised Learning

**1. Customer Segmentation:**
- Nhóm customers theo behavior
- Targeted marketing
- Personalization
- Churn prediction

**2. Image Compression:**
- K-Means cho color quantization
- Reduce number of colors
- Smaller file size

**3. Anomaly Detection:**
- Fraud detection (credit cards, insurance)
- Network intrusion detection
- Manufacturing quality control
- Medical diagnosis (rare diseases)

**4. Recommender Systems:**
- Collaborative filtering
- User clustering
- Item clustering
- Matrix factorization (NMF, SVD)

**5. Topic Modeling:**
- Document clustering
- Automatic tagging
- Content organization
- Trend detection

**6. Gene Expression Analysis:**
- Group similar genes
- Identify cancer subtypes
- Drug discovery
- Understanding diseases

**7. Social Network Analysis:**
- Community detection
- Influencer identification
- Link prediction
- Recommendation

**8. Data Preprocessing:**
- Feature extraction (PCA, ICA)
- Noise reduction (autoencoders)
- Data compression
- Dimensionality reduction

**9. Market Basket Analysis:**
- Product recommendations
- Store layout
- Promotions
- Cross-selling

**10. Image Segmentation:**
- Medical imaging
- Object detection preparation
- Video processing
- Computer vision preprocessing

---

## Học Sâu (Deep Learning)

### Giới Thiệu về Học Sâu

Học sâu (Deep Learning) là một nhánh con của học máy sử dụng mạng nơ-ron nhân tạo với nhiều lớp ẩn để học các biểu diễn phân cấp của dữ liệu. Khác với các phương pháp học máy truyền thống, học sâu có khả năng tự động trích xuất đặc trưng từ dữ liệu thô mà không cần kỹ thuật đặc trưng thủ công.

**Đặc điểm chính:**
- **Học biểu diễn phân cấp:** Các lớp đầu học các đặc trưng cấp thấp (cạnh, góc), các lớp sau học đặc trưng cấp cao hơn (hình dạng, đối tượng)
- **Khả năng xử lý dữ liệu lớn:** Hiệu suất tăng theo lượng dữ liệu
- **End-to-end learning:** Học trực tiếp từ đầu vào thô đến đầu ra mong muốn
- **Tự động trích xuất đặc trưng:** Không cần thiết kế đặc trưng thủ công

**Ứng dụng đã cách mạng hóa:**
- Thị giác máy tính (nhận dạng ảnh, phát hiện đối tượng)
- Xử lý ngôn ngữ tự nhiên (dịch máy, chatbot, sinh văn bản)
- Nhận dạng giọng nói (trợ lý ảo, chuyển đổi giọng nói thành văn bản)
- Y tế (chẩn đoán hình ảnh, phát triển thuốc)
- Tự động hóa (xe tự lái, robot)

### Mạng Nơ-ron Nhân Tạo (Artificial Neural Networks - ANN)

Mạng nơ-ron nhân tạo được lấy cảm hứng từ cách thức hoạt động của não người, trong đó các nơ-ron sinh học truyền tín hiệu cho nhau thông qua các synapse.

### Perceptron - Đơn Vị Cơ Bản

Perceptron là đơn vị mạng nơ-ron đơn giản nhất, được phát minh bởi Frank Rosenblatt năm 1958.

**Công thức:**
$$y = \sigma(w^Tx + b)$$

Trong đó:
- $x = [x_1, x_2, ..., x_n]^T$: Vector đầu vào (các đặc trưng)
- $w = [w_1, w_2, ..., w_n]^T$: Vector trọng số (weights)
- $b$: Hệ số điều chỉnh (bias) - cho phép dịch chuyển hàm quyết định
- $\sigma$: Hàm kích hoạt (activation function)
- $y$: Đầu ra dự đoán

**Cách hoạt động:**
1. Nhận đầu vào từ các đặc trưng
2. Tính tổng có trọng số: $z = w^Tx + b = \sum_{i=1}^{n}w_i x_i + b$
3. Áp dụng hàm kích hoạt để tạo đầu ra

**Hạn chế quan trọng:** 
- Chỉ có thể học các mẫu phân tách tuyến tính (linearly separable)
- Không thể giải quyết bài toán XOR
- Không thể mô hình hóa các quan hệ phi tuyến phức tạp

**Ví dụ:** Một perceptron có thể phân loại điểm nằm phía trên hay dưới một đường thẳng, nhưng không thể phân loại các điểm trong bài toán XOR (cần đường cong để phân tách).

### Perceptron Đa Lớp (Multi-Layer Perceptron - MLP)

MLP khắc phục hạn chế của perceptron đơn bằng cách xếp chồng nhiều lớp, cho phép học các hàm phi tuyến phức tạp.

**Kiến trúc:**

**1. Lớp đầu vào (Input Layer):**
- Nhận dữ liệu thô
- Số nơ-ron = số đặc trưng đầu vào
- Không có phép biến đổi, chỉ truyền dữ liệu

**2. Lớp ẩn (Hidden Layers):**
- Thực hiện các phép biến đổi phi tuyến
- Số lượng có thể từ 1 đến hàng trăm lớp
- Mỗi lớp học biểu diễn trừu tượng hơn
- Số nơ-ron trong mỗi lớp là hyperparameter

**3. Lớp đầu ra (Output Layer):**
- Tạo dự đoán cuối cùng
- Số nơ-ron phụ thuộc vào bài toán:
  - Hồi quy: 1 nơ-ron
  - Phân loại nhị phân: 1 nơ-ron (với sigmoid) hoặc 2 (với softmax)
  - Phân loại đa lớp: K nơ-ron (K = số lớp)

**Lan truyền xuôi (Forward Propagation):**

Quá trình tính toán từ đầu vào đến đầu ra qua các lớp:

Với lớp $l$:
$$z^{[l]} = W^{[l]}a^{[l-1]} + b^{[l]}$$
$$a^{[l]} = \sigma(z^{[l]})$$

Trong đó:
- $W^{[l]}$: Ma trận trọng số của lớp $l$ (kích thước $n^{[l]} \times n^{[l-1]}$)
- $b^{[l]}$: Vector bias của lớp $l$ (kích thước $n^{[l]} \times 1$)
- $a^{[l-1]}$: Activation của lớp trước (đầu vào cho lớp $l$)
- $z^{[l]}$: Pre-activation (trước khi áp dụng hàm kích hoạt)
- $a^{[l]}$: Activation (sau khi áp dụng hàm kích hoạt)
- $\sigma$: Hàm kích hoạt

**Ví dụ minh họa:**
- Lớp 1: 3 nơ-ron, nhận input 784 chiều (ảnh 28×28) → $W^{[1]}$: 3×784
- Lớp 2: 2 nơ-ron, nhận từ lớp 1 → $W^{[2]}$: 2×3
- Lớp output: 10 nơ-ron (phân loại 10 chữ số) → $W^{[3]}$: 10×2

### Hàm Kích Hoạt (Activation Functions)

Hàm kích hoạt thêm tính phi tuyến vào mạng, cho phép học các quan hệ phức tạp. Không có hàm kích hoạt, mạng nhiều lớp chỉ tương đương một phép biến đổi tuyến tính.

**1. Sigmoid:**
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

**Đặc điểm:**
- Đầu ra: khoảng (0, 1)
- Hình dạng chữ S, trơn và khả vi
- Có thể hiểu như xác suất

**Ưu điểm:**
- Đầu ra bị chặn, dễ diễn giải
- Phù hợp cho lớp output trong phân loại nhị phân

**Nhược điểm:**
- **Vanishing gradient:** Gradient gần như bằng 0 khi $|z|$ lớn
- Output không tập trung quanh 0 (not zero-centered)
- Tính toán hàm exp tốn kém
- Ít được dùng trong lớp ẩn của mạng sâu

**2. Tanh (Hyperbolic Tangent):**
$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} = \frac{2}{1+e^{-2z}} - 1$$

**Đặc điểm:**
- Đầu ra: khoảng (-1, 1)
- Là phiên bản dịch chuyển và co giãn của sigmoid

**Ưu điểm:**
- Zero-centered (đầu ra tập trung quanh 0)
- Gradient mạnh hơn sigmoid
- Thường hoạt động tốt hơn sigmoid trong lớp ẩn

**Nhược điểm:**
- Vẫn bị vanishing gradient
- Tính toán hàm exp tốn kém

**3. ReLU (Rectified Linear Unit):**
$$ReLU(z) = \max(0, z) = \begin{cases} z & \text{nếu } z > 0 \\ 0 & \text{nếu } z \leq 0 \end{cases}$$

**Đặc điểm:**
- Cực kỳ đơn giản và hiệu quả
- Là hàm kích hoạt phổ biến nhất cho lớp ẩn

**Ưu điểm:**
- **Tính toán nhanh:** Chỉ cần so sánh với 0
- **Không bị vanishing gradient** khi $z > 0$
- **Sparsity:** Một số nơ-ron có activation = 0, tạo biểu diễn thưa
- **Tăng tốc hội tụ:** Nhanh hơn sigmoid/tanh 6 lần

**Nhược điểm:**
- **Dying ReLU problem:** Nếu $z < 0$ trong quá trình training, gradient = 0, nơ-ron "chết" và không bao giờ được cập nhật
- Output không zero-centered
- Unbounded output (có thể dẫn đến giá trị quá lớn)

**4. Leaky ReLU:**
$$LeakyReLU(z) = \max(\alpha z, z) = \begin{cases} z & \text{nếu } z > 0 \\ \alpha z & \text{nếu } z \leq 0 \end{cases}$$

Với $\alpha$ thường là 0.01 hoặc 0.02

**Ưu điểm:**
- Khắc phục dying ReLU: vẫn có gradient nhỏ khi $z < 0$
- Giữ được ưu điểm tính toán nhanh của ReLU

**Biến thể:**
- **Parametric ReLU (PReLU):** $\alpha$ là tham số học được
- **Randomized Rleaky ReLU (RReLU):** $\alpha$ được chọn ngẫu nhiên trong training

**5. ELU (Exponential Linear Unit):**
$$ELU(z) = \begin{cases} z & \text{nếu } z > 0 \\ \alpha(e^z - 1) & \text{nếu } z \leq 0 \end{cases}$$

Thường $\alpha = 1$

**Đặc điểm:**
- Trơn ở mọi điểm (khả vi liên tục)
- Mean activation gần 0 → zero-centered

**Ưu điểm:**
- Không có dying ReLU problem
- Output âm giúp push mean activation về 0
- Thường cho kết quả tốt hơn ReLU và Leaky ReLU

**Nhược điểm:**
- Tính toán chậm hơn (do hàm exp)

**6. GELU (Gaussian Error Linear Unit):**
$$GELU(z) = z \cdot \Phi(z)$$
Trong đó $\Phi(z)$ là hàm phân phối tích lũy chuẩn

**Đặc điểm:**
- Được sử dụng trong BERT và các transformer hiện đại
- Trơn hơn ReLU
- Xấp xỉ có thể tính nhanh: $0.5z(1 + \tanh[\sqrt{2/\pi}(z + 0.044715z^3)])$

**7. Swish:**
$$Swish(z) = z \cdot \sigma(z) = \frac{z}{1 + e^{-z}}$$

**Đặc điểm:**
- Được Google phát triển qua neural architecture search
- Trơn, non-monotonic
- Thường cho hiệu suất tốt nhưng tính toán chậm hơn ReLU

**8. Softmax (Dành cho Lớp Output):**
$$softmax(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K}e^{z_j}}$$

**Đặc điểm:**
- Chuyển đổi vector số thực thành phân phối xác suất
- Tổng các đầu ra = 1
- Mỗi đầu ra trong khoảng (0, 1)

**Sử dụng:**
- Lớp output cho bài toán phân loại đa lớp (multi-class classification)
- Với K lớp, có K đầu ra, mỗi đầu ra là xác suất thuộc lớp tương ứng

**Lưu ý về numerical stability:**
Để tránh overflow, thực tế tính:
$$softmax(z_i) = \frac{e^{z_i - \max(z)}}{\sum_{j}e^{z_j - \max(z)}}$$

### Hàm Mất Mát (Loss Functions)

Hàm mất mát đo lường sự khác biệt giữa dự đoán và giá trị thực tế, là thước đo để tối ưu hóa mạng.

**1. Sai Số Bình Phương Trung Bình (Mean Squared Error - MSE):**
$$L = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

**Đặc điểm:**
- **Sử dụng:** Bài toán hồi quy (regression)
- Phạt nặng các lỗi lớn do bình phương
- Luôn non-negative, = 0 khi dự đoán hoàn hảo

**Ưu điểm:**
- Khả vi, dễ tối ưu
- Có ý nghĩa thống kê rõ ràng

**Nhược điểm:**
- Nhạy cảm với outliers
- Không phù hợp với phân loại

**Biến thể:**
- **RMSE (Root Mean Squared Error):** $\sqrt{MSE}$ - có cùng đơn vị với dữ liệu
- **MAE (Mean Absolute Error):** $\frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$ - ít nhạy với outliers

**2. Binary Cross-Entropy (Phân Loại Nhị Phân):**
$$L = -\frac{1}{n}\sum_{i=1}^{n}[y_i\log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]$$

**Đặc điểm:**
- **Sử dụng:** Phân loại nhị phân (2 lớp)
- $y_i \in \{0, 1\}$: nhãn thực tế
- $\hat{y}_i \in (0, 1)$: xác suất dự đoán (output của sigmoid)

**Cách hoạt động:**
- Nếu $y_i = 1$: loss = $-\log(\hat{y}_i)$ → minimize khi $\hat{y}_i \to 1$
- Nếu $y_i = 0$: loss = $-\log(1-\hat{y}_i)$ → minimize khi $\hat{y}_i \to 0$

**Ưu điểm:**
- Phù hợp với sigmoid activation
- Gradient tốt, không bị vanishing
- Có ý nghĩa xác suất

**Lưu ý:** 
- Cần thêm epsilon nhỏ để tránh log(0): $\log(\hat{y}_i + \epsilon)$
- Còn gọi là log loss

**3. Categorical Cross-Entropy (Phân Loại Đa Lớp):**
$$L = -\sum_{i=1}^{n}\sum_{c=1}^{C}y_{i,c}\log(\hat{y}_{i,c})$$

**Đặc điểm:**
- **Sử dụng:** Phân loại đa lớp (nhiều hơn 2 lớp)
- $y_{i,c}$: nhãn thực tế dạng one-hot encoding (chỉ 1 phần tử = 1, còn lại = 0)
- $\hat{y}_{i,c}$: xác suất dự đoán cho lớp $c$ (output của softmax)
- $C$: số lớp

**Ví dụ:** Với 3 lớp, $y = [0, 1, 0]$ (lớp 2), $\hat{y} = [0.1, 0.7, 0.2]$
$$L = -(0 \cdot \log(0.1) + 1 \cdot \log(0.7) + 0 \cdot \log(0.2)) = -\log(0.7) \approx 0.357$$

**Biến thể:**
- **Sparse Categorical Cross-Entropy:** Nhãn là integer (0, 1, 2,...) thay vì one-hot, tiết kiệm bộ nhớ

**4. Huber Loss (Hồi Quy Bền Vững):**
$$L_{\delta}(y, \hat{y}) = \begin{cases} \frac{1}{2}(y - \hat{y})^2 & \text{nếu } |y - \hat{y}| \leq \delta \\ \delta(|y - \hat{y}| - \frac{1}{2}\delta) & \text{ngược lại} \end{cases}$$

**Đặc điểm:**
- Kết hợp MSE và MAE
- Ít nhạy cảm với outliers hơn MSE
- $\delta$ là hyperparameter kiểm soát điểm chuyển đổi

**Sử dụng:**
- Hồi quy khi có outliers
- Reinforcement learning (ví dụ: DQN)

### Lan Truyền Ngược (Backpropagation)

Backpropagation là thuật toán cốt lõi để huấn luyện mạng nơ-ron sâu, cho phép tính gradient một cách hiệu quả thông qua quy tắc chuỗi (chain rule).

**Ý tưởng cơ bản:**
- Tính toán gradient của loss function theo tất cả các tham số (weights và biases)
- Lan truyền gradient từ output về input qua các lớp
- Sử dụng quy tắc chuỗi để phân rã gradient phức tạp thành các phần đơn giản

**Quy tắc chuỗi (Chain Rule):**
$$\frac{\partial L}{\partial w^{[l]}} = \frac{\partial L}{\partial a^{[l]}} \cdot \frac{\partial a^{[l]}}{\partial z^{[l]}} \cdot \frac{\partial z^{[l]}}{\partial w^{[l]}}$$

Trong đó:
- $\frac{\partial L}{\partial a^{[l]}}$: Gradient của loss theo activation
- $\frac{\partial a^{[l]}}{\partial z^{[l]}}$: Đạo hàm của hàm kích hoạt
- $\frac{\partial z^{[l]}}{\partial w^{[l]}}$: Gradient của pre-activation theo weights

**Các bước chi tiết:**

**1. Forward Pass (Lan truyền xuôi):**
- Tính toán output của mỗi lớp từ input đến output
- Lưu trữ tất cả các giá trị $z^{[l]}$ và $a^{[l]}$ (cần cho backward pass)

**2. Tính Loss:**
- So sánh prediction với ground truth
- Tính giá trị loss: $L = Loss(y, \hat{y})$

**3. Backward Pass (Lan truyền ngược):**
- Bắt đầu từ lớp output, tính gradient của loss theo output
- Với mỗi lớp từ L về 1:
  - Tính $\frac{\partial L}{\partial z^{[l]}} = \frac{\partial L}{\partial a^{[l]}} \odot \sigma'(z^{[l]})$ (element-wise product)
  - Tính $\frac{\partial L}{\partial W^{[l]}} = \frac{\partial L}{\partial z^{[l]}} \cdot (a^{[l-1]})^T$
  - Tính $\frac{\partial L}{\partial b^{[l]}} = \frac{\partial L}{\partial z^{[l]}}$
  - Lan truyền về lớp trước: $\frac{\partial L}{\partial a^{[l-1]}} = (W^{[l]})^T \cdot \frac{\partial L}{\partial z^{[l]}}$

**4. Cập nhật Weights:**
- Sử dụng gradient descent hoặc các optimizer khác
- $W^{[l]} := W^{[l]} - \alpha \frac{\partial L}{\partial W^{[l]}}$
- $b^{[l]} := b^{[l]} - \alpha \frac{\partial L}{\partial b^{[l]}}$

**Ví dụ minh họa:**
Mạng 2 lớp: Input → Hidden → Output
- Forward: $a^{[1]} = \sigma(W^{[1]}x + b^{[1]})$, $\hat{y} = \sigma(W^{[2]}a^{[1]} + b^{[2]})$
- Loss: $L = (y - \hat{y})^2$
- Backward:
  - $\frac{\partial L}{\partial \hat{y}} = -2(y - \hat{y})$
  - $\frac{\partial L}{\partial W^{[2]}} = \frac{\partial L}{\partial \hat{y}} \cdot \sigma'(z^{[2]}) \cdot a^{[1]}$
  - Lan truyền về hidden layer tương tự

**Computational Graph:**
Backpropagation có thể được hiểu thông qua đồ thị tính toán (computational graph), trong đó:
- Mỗi node là một operation
- Edges mang giá trị và gradients
- Forward pass tính giá trị, backward pass tính gradients

**Vấn đề Vanishing/Exploding Gradients:**
- **Vanishing:** Gradient giảm dần khi lan truyền về các lớp đầu → các lớp đầu học chậm
  - Nguyên nhân: Hàm kích hoạt có đạo hàm nhỏ (sigmoid, tanh)
  - Giải pháp: ReLU, batch normalization, residual connections
- **Exploding:** Gradient tăng dần → weights cập nhật quá mạnh, không ổn định
  - Giải pháp: Gradient clipping, proper weight initialization

**Lưu ý về hiệu suất:**
- Độ phức tạp tính toán của backpropagation tương đương forward pass
- Matrix operations có thể vectorize → tính toán hiệu quả trên GPU
- Cần lưu trữ activations từ forward pass → tốn memory

### Thuật Toán Tối Ưu (Optimization Algorithms)

Các thuật toán tối ưu quyết định cách cập nhật weights để minimize loss function.

**1. Gradient Descent (Hạ Gradient):**
$$w := w - \alpha\frac{\partial L}{\partial w}$$

**Đặc điểm:**
- $\alpha$ (learning rate): Hyperparameter quan trọng nhất
- Cập nhật dựa trên toàn bộ training set (batch gradient descent)

**Ưu điểm:**
- Đơn giản, dễ hiểu
- Hội tụ ổn định với learning rate phù hợp
- Đảm bảo tìm được local minimum với hàm convex

**Nhược điểm:**
- Chậm với dữ liệu lớn (phải xử lý toàn bộ dataset mỗi iteration)
- Có thể bị kẹt ở local minima hoặc saddle points
- Learning rate cố định không phù hợp mọi giai đoạn training

**2. Stochastic Gradient Descent (SGD):**
$$w := w - \alpha\frac{\partial L_i}{\partial w}$$

**Đặc điểm:**
- Cập nhật sau **mỗi** mẫu dữ liệu (sample)
- Gradient ước lượng từ 1 sample → noisy nhưng nhanh

**Ưu điểm:**
- Rất nhanh, có thể train trên dữ liệu lớn
- Noise giúp thoát khỏi local minima
- Có thể train online (dữ liệu đến liên tục)

**Nhược điểm:**
- Quá trình hội tụ không ổn định, dao động mạnh
- Có thể không hội tụ chính xác đến minimum
- Khó song song hóa (sequential updates)

**3. Mini-batch Gradient Descent:**
$$w := w - \alpha\frac{1}{m}\sum_{i=1}^{m}\frac{\partial L_i}{\partial w}$$

**Đặc điểm:**
- Cập nhật sau một **batch nhỏ** (thường 32, 64, 128, 256)
- Kết hợp ưu điểm của batch GD và SGD
- **Là phương pháp được sử dụng phổ biến nhất trong thực tế**

**Ưu điểm:**
- Tốc độ nhanh, ổn định hơn SGD
- Có thể vectorize, tận dụng GPU hiệu quả
- Gradient ổn định hơn SGD nhưng vẫn có noise tốt
- Batch size là hyperparameter điều chỉnh được

**Lựa chọn batch size:**
- Nhỏ (32-64): Gradient noisy hơn, regularization effect, cần ít memory
- Lớn (256-512): Gradient stable, train nhanh hơn, cần nhiều memory
- Trade-off giữa tốc độ và chất lượng hội tụ

**4. Momentum:**
$$v_t = \beta v_{t-1} + (1-\beta)\nabla L$$
$$w := w - \alpha v_t$$

**Ý tưởng:**
- Tích lũy velocity (vận tốc) từ các gradient trước
- Giống như quả bóng lăn xuống dốc, tích lũy động lượng
- $\beta$ (thường 0.9): Hệ số ma sát, quyết định giữ lại bao nhiêu từ gradient cũ

**Ưu điểm:**
- **Tăng tốc hội tụ** trong các hướng nhất quán
- **Giảm dao động** trong các hướng gradient thay đổi nhiều
- Giúp vượt qua local minima nhỏ
- Đặc biệt hiệu quả với ravines (thung lũng hẹp trong loss surface)

**Nhược điểm:**
- Thêm một hyperparameter ($\beta$)
- Có thể overshoot minimum nếu momentum quá lớn

**Biến thể:**
- **Nesterov Accelerated Gradient (NAG):** Nhìn trước vị trí tiếp theo trước khi tính gradient
$$v_t = \beta v_{t-1} + (1-\beta)\nabla L(w - \beta v_{t-1})$$

**5. RMSprop (Root Mean Square Propagation):**
$$s_t = \beta s_{t-1} + (1-\beta)(\nabla L)^2$$
$$w := w - \alpha\frac{\nabla L}{\sqrt{s_t + \epsilon}}$$

**Ý tưởng:**
- Điều chỉnh learning rate cho mỗi tham số riêng biệt
- Chia gradient cho căn bậc hai của trung bình bình phương gradient (root mean square)
- $\beta$ (thường 0.9), $\epsilon$ (thường $10^{-8}$) để tránh chia cho 0

**Ưu điểm:**
- **Adaptive learning rates:** Tham số có gradient lớn → learning rate nhỏ, và ngược lại
- Hoạt động tốt với dữ liệu non-stationary
- Giảm dao động trong các chiều có gradient lớn
- Phù hợp cho RNN (giải quyết vanishing/exploding gradients)

**Cách hoạt động:**
- Nếu gradient liên tục lớn ở một chiều → $s_t$ lớn → chia cho số lớn → giảm update
- Nếu gradient nhỏ → $s_t$ nhỏ → learning rate hiệu quả tăng

**6. Adam (Adaptive Moment Estimation):**

**Thuật toán phổ biến nhất hiện nay**, kết hợp ưu điểm của Momentum và RMSprop.

$$m_t = \beta_1 m_{t-1} + (1-\beta_1)\nabla L \quad \text{(moment bậc 1 - trung bình)}$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2)(\nabla L)^2 \quad \text{(moment bậc 2 - variance)}$$

**Bias correction** (quan trọng ở đầu training):
$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}$$
$$\hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$

**Update rule:**
$$w := w - \alpha\frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

**Hyperparameters mặc định:**
- $\alpha = 0.001$ (learning rate)
- $\beta_1 = 0.9$ (decay rate cho moment bậc 1)
- $\beta_2 = 0.999$ (decay rate cho moment bậc 2)
- $\epsilon = 10^{-8}$

**Ưu điểm:**
- **Adaptive learning rates cho từng tham số**
- Kết hợp momentum (tăng tốc) và adaptive rates (ổn định)
- Hoạt động tốt với sparse gradients
- Ít nhạy cảm với hyperparameters
- **Lựa chọn mặc định tốt cho hầu hết bài toán**

**Nhược điểm:**
- Đôi khi generalize kém hơn SGD + Momentum
- Cần nhiều memory hơn (lưu $m_t$ và $v_t$)

**Biến thể:**
- **AdamW:** Thêm weight decay đúng cách (decoupled weight decay)
- **Nadam:** Adam + Nesterov momentum
- **RAdam:** Rectified Adam, sửa warm-up problem
- **AdaBelief:** Dựa vào "belief" về gradient thay vì gradient value

**7. So sánh các Optimizer:**

| Optimizer | Tốc độ | Ổn định | Memory | Phù hợp |
|-----------|--------|---------|---------|---------|
| SGD | Chậm | Thấp | Thấp | Simple tasks |
| SGD + Momentum | Trung bình | Trung bình | Thấp | CV tasks |
| RMSprop | Nhanh | Cao | Trung bình | RNNs |
| Adam | Nhanh | Cao | Cao | Mặc định (most tasks) |
| AdamW | Nhanh | Rất cao | Cao | Transformers, modern architectures |

**Lời khuyên thực tế:**
- **Bắt đầu với Adam:** Thường cho kết quả tốt ngay
- **Thử SGD + Momentum:** Nếu muốn generalization tốt hơn (có thể cần tune learning rate kỹ)
- **AdamW cho transformers:** Standard cho BERT, GPT, và các mô hình lớn
- **RMSprop cho RNN:** Nếu làm việc với recurrent networks

### Kỹ Thuật Điều Chuẩn (Regularization Techniques)

Regularization giúp giảm overfitting - hiện tượng mô hình học quá khớp với training data nhưng kém trên dữ liệu mới.

**1. L1/L2 Regularization:**

Thêm penalty term vào loss function để hạn chế độ lớn của weights.

**L2 Regularization (Weight Decay):**
$$L_{total} = L_{original} + \lambda\sum_{i}w_i^2$$

**Đặc điểm:**
- Penalty tỷ lệ với bình phương weights
- $\lambda$: Hệ số regularization (hyperparameter)
- Weights decay về 0 nhưng hiếm khi bằng chính xác 0

**Cách hoạt động:**
- Weights lớn bị phạt nặng → mô hình prefer weights nhỏ hơn
- Giảm độ phức tạp mô hình → generalize tốt hơn
- Còn gọi là Ridge Regression trong linear models

**L1 Regularization (Lasso):**
$$L_{total} = L_{original} + \lambda\sum_{i}|w_i|$$

**Đặc điểm:**
- Penalty tỷ lệ với giá trị tuyệt đối weights
- Có thể làm một số weights = 0 chính xác → **Feature selection**
- Tạo sparse models (nhiều weights = 0)

**So sánh L1 vs L2:**
| | L1 | L2 |
|---|---|---|
| Sparsity | Có (nhiều weights = 0) | Không |
| Feature selection | Có | Không |
| Gradient | Không trơn tại 0 | Trơn mọi nơi |
| Sử dụng | Nhiều features, cần sparse | Default choice |

**2. Dropout:**

Kỹ thuật cực kỳ hiệu quả được giới thiệu bởi Hinton et al. (2012).

**Cơ chế:**
- Trong mỗi iteration training, **ngẫu nhiên "tắt" (drop)** một số nơ-ron
- Mỗi nơ-ron có xác suất $p$ bị drop (thường $p = 0.2 - 0.5$)
- Nơ-ron bị drop không tham gia forward và backward pass
- Tại test time, sử dụng tất cả nơ-ron nhưng scale output với $(1-p)$

**Tại sao hiệu quả:**
- **Ngăn co-adaptation:** Nơ-ron không thể phụ thuộc quá nhiều vào nơ-ron cụ thể khác
- **Ensemble effect:** Mỗi iteration training một mạng con khác nhau → giống train nhiều mô hình
- **Noise injection:** Thêm noise vào training → mô hình robust hơn

**Cách sử dụng:**
- Áp dụng cho fully connected layers (không dùng cho convolutional layers)
- Hidden layers: dropout rate 0.5
- Input layer: dropout rate thấp hơn (0.2) nếu dùng
- **Không** sử dụng dropout trong test/inference

**Inverted Dropout:**
```python
# Training
mask = (np.random.rand(*shape) > dropout_rate) / (1 - dropout_rate)
output = input * mask

# Testing: không cần scale
output = input
```

**Biến thể:**
- **DropConnect:** Drop connections thay vì neurons
- **Spatial Dropout:** Drop entire feature maps trong CNN
- **Variational Dropout:** Dropout mask giống nhau qua time steps trong RNN

**3. Early Stopping:**

Dừng training khi validation loss bắt đầu tăng.

**Cách thực hiện:**
1. Chia data thành train/validation/test
2. Theo dõi validation loss sau mỗi epoch
3. Lưu model có validation loss tốt nhất
4. Dừng nếu validation loss không giảm sau $n$ epochs (patience)

**Ưu điểm:**
- Đơn giản, hiệu quả
- Tự động tìm số epoch tối ưu
- Không cần thêm hyperparameter phức tạp

**Lưu ý:**
- Cần validation set riêng (không dùng test set!)
- Patience thường 10-20 epochs
- Có thể kết hợp với learning rate scheduling

**4. Data Augmentation:**

Tăng cường dữ liệu training bằng cách tạo biến thể từ dữ liệu gốc.

**Cho ảnh (Computer Vision):**
- **Geometric transformations:**
  - Rotation (xoay): ±15-30 độ
  - Flip (lật): Horizontal, vertical
  - Crop (cắt): Random crop, center crop
  - Zoom: Scale in/out
  - Translation (dịch chuyển)
  - Shearing (nghiêng)
  
- **Color transformations:**
  - Brightness adjustment (độ sáng)
  - Contrast adjustment (độ tương phản)
  - Saturation adjustment (độ bão hòa)
  - Hue adjustment (sắc màu)
  - RGB channel shifts
  
- **Noise injection:**
  - Gaussian noise
  - Salt and pepper noise
  - Blur (làm mờ)
  
- **Advanced techniques:**
  - **Mixup:** Trộn hai ảnh: $x = \lambda x_1 + (1-\lambda)x_2$
  - **CutMix:** Cắt và dán vùng từ ảnh khác
  - **CutOut:** Che ngẫu nhiên một vùng của ảnh
  - **AutoAugment:** Tự động học policy augmentation tốt nhất

**Cho văn bản (NLP):**
- Synonym replacement (thay từ đồng nghĩa)
- Random insertion/deletion
- Back-translation (dịch qua lại)
- Paraphrasing

**Cho âm thanh:**
- Time stretching
- Pitch shifting
- Adding noise
- Time masking, frequency masking

**Lưu ý:**
- Augmentation phải giữ nguyên nhãn
- Cần domain knowledge (ví dụ: không flip chữ số)
- On-the-fly augmentation trong training (không pre-generate)

**5. Batch Normalization:**

Kỹ thuật chuẩn hóa activation của mỗi layer, được giới thiệu bởi Ioffe & Szegedy (2015).

**Công thức:**

Với một mini-batch:
$$\mu_B = \frac{1}{m}\sum_{i=1}^{m}x_i \quad \text{(mean của batch)}$$
$$\sigma_B^2 = \frac{1}{m}\sum_{i=1}^{m}(x_i - \mu_B)^2 \quad \text{(variance của batch)}$$

**Normalize:**
$$\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$

**Scale and shift** (learnable parameters):
$$y_i = \gamma\hat{x}_i + \beta$$

**Tại sao hiệu quả:**
- **Giảm Internal Covariate Shift:** Phân phối input của mỗi layer ổn định hơn
- **Cho phép learning rate cao hơn:** Training nhanh hơn 5-10 lần
- **Regularization effect:** Thêm noise từ batch statistics
- **Giảm nhạy cảm với weight initialization**

**Vị trí đặt:**
- Thường đặt **sau** linear/conv layer, **trước** activation function
- Có thể đặt sau activation (ít phổ biến hơn)

**Ưu điểm:**
- Tăng tốc training đáng kể
- Cho phép sử dụng activation functions có vanishing gradient (sigmoid, tanh)
- Giảm overfitting (có thể giảm dropout)
- Mô hình ít nhạy cảm với hyperparameters

**Nhược điểm:**
- **Phụ thuộc batch size:** Không hoạt động tốt với batch nhỏ
- Khác nhau giữa training và inference (cần lưu running statistics)
- Không phù hợp với RNNs
- Thêm computational cost

**Inference time:**
Sử dụng moving average của mean và variance từ training:
$$\mu_{test} = E[\mu_B], \quad \sigma_{test}^2 = E[\sigma_B^2]$$

**6. Layer Normalization:**

Thay thế cho Batch Normalization, chuẩn hóa theo features thay vì batch.

**Công thức:**
Với một sample, normalize across features:
$$\mu = \frac{1}{H}\sum_{i=1}^{H}x_i$$
$$\sigma^2 = \frac{1}{H}\sum_{i=1}^{H}(x_i - \mu)^2$$
$$\hat{x}_i = \frac{x_i - \mu}{\sqrt{\sigma^2 + \epsilon}}$$
$$y_i = \gamma\hat{x}_i + \beta$$

**Ưu điểm so với Batch Norm:**
- **Không phụ thuộc batch size** → hoạt động với batch size = 1
- **Giống nhau giữa training và inference** → không cần lưu running statistics
- **Phù hợp với RNNs** và sequence models
- Hoạt động tốt với Transformers

**Khi nào dùng:**
- RNNs, LSTMs, GRUs
- Transformers (BERT, GPT)
- Batch size nhỏ
- Online learning

**7. Weight Decay:**

Thêm penalty cho magnitude của weights trong update rule.

**Trong optimizer:**
$$w := w - \alpha(\frac{\partial L}{\partial w} + \lambda w)$$

**Khác với L2 Regularization:**
- L2 reg: Thêm vào loss function
- Weight decay: Thêm trực tiếp vào update rule
- Với SGD: Tương đương nhau
- Với Adam/AdamW: **Khác nhau!** AdamW implement weight decay đúng cách

**8. Stochastic Depth:**

Ngẫu nhiên skip một số layers trong training (dùng cho ResNets).

**9. Label Smoothing:**

Thay vì hard labels (0 hoặc 1), dùng soft labels.

**Ví dụ:** 
- Hard: [0, 1, 0, 0]
- Soft (ε=0.1): [0.025, 0.925, 0.025, 0.025]

**Công thức:**
$$y_{smooth} = (1-\epsilon)y + \frac{\epsilon}{K}$$

**Ưu điểm:**
- Ngăn mô hình quá tự tin (overconfident)
- Improve generalization
- Thường dùng trong image classification

**10. Gradient Clipping:**

Giới hạn magnitude của gradients, đặc biệt quan trọng cho RNNs.

**Clip by value:**
$$g = \max(\min(g, threshold), -threshold)$$

**Clip by norm:**
$$g = \frac{threshold \cdot g}{||g||} \text{ if } ||g|| > threshold$$

**Sử dụng:**
- RNNs, LSTMs (giải quyết exploding gradients)
- Transformers với sequence dài
- Threshold thường: 1.0 hoặc 5.0

### Mạng Nơ-ron Tích Chập (Convolutional Neural Networks - CNN)

CNN là kiến trúc mạng nơ-ron chuyên biệt cho xử lý dữ liệu dạng lưới (grid-like), đặc biệt là ảnh. Được lấy cảm hứng từ vỏ não thị giác (visual cortex) của động vật.

**Đặc điểm chính:**
- **Locally connected:** Mỗi nơ-ron chỉ kết nối với vùng local của input
- **Parameter sharing:** Cùng một filter được áp dụng trên toàn bộ input
- **Translation invariance:** Phát hiện đặc trưng ở bất kỳ vị trí nào
- **Hierarchical feature learning:** Lớp đầu học low-level features, lớp sau học high-level features

**Các Thành Phần Chính:**

**1. Lớp Tích Chập (Convolutional Layer):**

Áp dụng filters (kernels) trượt trên input để trích xuất features.

**Công thức:**
$$Output[i,j] = \sum_{m=0}^{k-1}\sum_{n=0}^{k-1}Input[i+m,j+n] \times Kernel[m,n] + bias$$

Hoặc dạng tổng quát với nhiều channels:
$$Output[i,j,d] = \sum_{c=0}^{C-1}\sum_{m=0}^{k-1}\sum_{n=0}^{k-1}Input[i+m,j+n,c] \times Kernel[m,n,c,d] + bias[d]$$

**Khái niệm quan trọng:**

**Filter/Kernel:**
- Ma trận nhỏ (thường 3×3, 5×5, 7×7)
- Chứa weights học được
- Mỗi filter phát hiện một đặc trưng cụ thể:
  - Lớp đầu: Edges (cạnh), corners (góc), colors
  - Lớp giữa: Textures (kết cấu), patterns (mẫu)
  - Lớp sâu: Parts of objects (phần của vật thể), objects

**Depth (Number of Filters):**
- Số lượng filters trong một lớp
- Tạo ra feature maps tương ứng
- Thường tăng dần qua các lớp: 32 → 64 → 128 → 256

**Stride:**
- Bước nhảy khi trượt filter
- Stride = 1: Di chuyển từng pixel
- Stride = 2: Di chuyển 2 pixels, giảm kích thước output
- Stride lớn: Giảm spatial dimensions, tăng receptive field

**Padding:**
- Thêm pixels (thường 0) xung quanh input
- **VALID (No padding):** Output size giảm
- **SAME (Zero padding):** Output size = Input size (khi stride=1)

**Tính Output Size:**
$$Output\_size = \frac{Input\_size - Kernel\_size + 2 \times Padding}{Stride} + 1$$

**Ví dụ:**
- Input: 32×32×3 (ảnh RGB)
- 64 filters 3×3, stride=1, padding=1
- Output: 32×32×64

**Số parameters:**
- Mỗi filter 3×3×3: 27 weights + 1 bias = 28 params
- 64 filters: 28 × 64 = 1,792 params
- **Ít hơn nhiều so với fully connected!**

**Ưu điểm của Convolution:**
- **Parameter sharing:** Giảm số lượng parameters cần học
- **Sparse connectivity:** Mỗi output chỉ phụ thuộc vào vùng local
- **Equivariance to translation:** Nếu input dịch chuyển, output cũng dịch chuyển tương ứng

**2. Lớp Pooling:**

Giảm spatial dimensions, giữ lại thông tin quan trọng.

**Max Pooling:**
- Lấy giá trị maximum trong mỗi region (thường 2×2)
- Phổ biến nhất
- Giữ lại features nổi bật nhất
- Invariant to small translations

**Công thức:**
$$Output[i,j] = \max_{m,n} Input[2i+m, 2j+n]$$

**Ví dụ Max Pooling 2×2:**
```
Input 4×4:        Output 2×2:
1  3  2  4        3  4
5  6  7  8   →    6  8
2  1  4  3
0  9  5  2
```

**Average Pooling:**
- Lấy trung bình trong mỗi region
- Ít phổ biến hơn Max Pooling
- Smoother, giữ được nhiều thông tin hơn

**Global Average Pooling:**
- Average trên toàn bộ feature map → 1 số
- Thay thế fully connected layers
- Giảm overfitting, ít parameters

**Hyperparameters:**
- Pool size: Thường 2×2 hoặc 3×3
- Stride: Thường = pool size
- Padding: Hiếm khi dùng

**Tác dụng:**
- **Downsampling:** Giảm spatial dimensions → giảm computation
- **Increase receptive field:** Mỗi nơ-ron "nhìn" được vùng rộng hơn
- **Translation invariance:** Ít nhạy cảm với vị trí chính xác
- **Regularization effect:** Giảm overfitting

**3. Lớp Fully Connected (Dense):**

Lớp truyền thống, mỗi nơ-ron kết nối với tất cả nơ-ron lớp trước.

**Vị trí:**
- Thường ở cuối mạng CNN
- Sau khi flatten feature maps thành vector

**Tác dụng:**
- Kết hợp tất cả features để ra quyết định cuối cùng
- Classification head

**Nhược điểm:**
- **Nhiều parameters:** Có thể chiếm 90% tổng số parameters
- Dễ overfit
- Xu hướng thay thế bằng Global Average Pooling + 1 FC nhỏ

**Kiến Trúc Điển Hình:**

**Pattern chung:**
```
Input → [Conv → ReLU → Pool] × N → [FC] × M → Output
```

**Ví dụ cụ thể:**
```
Input (224×224×3)
↓
Conv 64 filters 3×3, ReLU (224×224×64)
↓
MaxPool 2×2 (112×112×64)
↓
Conv 128 filters 3×3, ReLU (112×112×128)
↓
MaxPool 2×2 (56×56×128)
↓
Conv 256 filters 3×3, ReLU (56×56×256)
↓
MaxPool 2×2 (28×28×256)
↓
Flatten (200,704 dimensions)
↓
FC 1024, ReLU
↓
Dropout 0.5
↓
FC 10 (num_classes)
↓
Softmax
```

**Các Kiến Trúc CNN Kinh Điển:**

**LeNet-5 (1998 - Yann LeCun):**
- Một trong những CNN đầu tiên
- Phân loại chữ số viết tay (MNIST)
- Kiến trúc: Conv → Pool → Conv → Pool → FC → FC
- Chỉ ~60K parameters

**AlexNet (2012 - Krizhevsky, Sutskever, Hinton):**
- **Breakthrough moment** trong Deep Learning
- Thắng ImageNet 2012 với top-5 error 15.3% (giảm 10% so với runner-up)
- 8 layers, ~60M parameters

**Đóng góp quan trọng:**
- Sử dụng **ReLU** thay vì tanh/sigmoid
- **Dropout** regularization
- **Data augmentation** mạnh
- **GPU training** (2 GPUs)
- Local Response Normalization (LRN)

**VGGNet (2014 - Visual Geometry Group, Oxford):**
- Rất sâu: VGG-16 (16 layers), VGG-19 (19 layers)
- **Đơn giản và đồng nhất:** Chỉ dùng conv 3×3, pool 2×2
- ~138M parameters (rất lớn!)

**Kiến trúc VGG-16:**
```
Input (224×224×3)
↓
[Conv 3×3, 64] × 2 → Pool
↓
[Conv 3×3, 128] × 2 → Pool
↓
[Conv 3×3, 256] × 3 → Pool
↓
[Conv 3×3, 512] × 3 → Pool
↓
[Conv 3×3, 512] × 3 → Pool
↓
FC 4096 → FC 4096 → FC 1000
```

**Insight:**
- Nhiều conv 3×3 stacked = receptive field lớn hơn nhưng ít params hơn
- 2 conv 3×3 = receptive field 5×5
- 3 conv 3×3 = receptive field 7×7

**GoogLeNet/Inception (2014 - Google):**
- Thắng ImageNet 2014
- 22 layers nhưng chỉ 7M parameters (ít hơn AlexNet!)
- **Inception module:** Ý tưởng chính

**Inception Module:**
- Áp dụng **đồng thời** nhiều kích thước filter (1×1, 3×3, 5×5) và pooling
- Concatenate outputs
- Network tự học combination nào tốt

```
Input
├─ 1×1 conv
├─ 1×1 conv → 3×3 conv
├─ 1×1 conv → 5×5 conv
└─ 3×3 pool → 1×1 conv
↓ (Concatenate)
Output
```

**1×1 Convolutions:**
- Dimensionality reduction
- Thêm non-linearity
- "Network in Network"

**ResNet (2015 - Microsoft Research):**
- **Cách mạng trong deep learning**
- Rất sâu: ResNet-50, ResNet-101, ResNet-152 (thậm chí 1000+ layers)
- Thắng ImageNet 2015: Top-5 error 3.6% (better than human!)

**Vấn đề với mạng rất sâu:**
- **Degradation problem:** Mạng sâu hơn nhưng accuracy giảm (không phải overfitting!)
- Vanishing gradients

**Giải pháp: Skip Connections (Residual Connections):**
$$H(x) = F(x) + x$$

**Residual Block:**
```
x ─────────────────────→ +
  ↓                      ↑
  Conv 3×3, ReLU         │
  ↓                      │
  Conv 3×3               │
  ↓─────────────────────┘
  (Add)
  ↓
  ReLU
```

**Tại sao hiệu quả:**
- **Identity mapping:** Nếu thêm layers không giúp ích, học $F(x) = 0$ → $H(x) = x$
- **Gradient flow:** Gradients có thể flow trực tiếp qua shortcut
- Dễ optimize hơn

**Bottleneck Design (ResNet-50+):**
```
1×1 conv (reduce dim)
↓
3×3 conv
↓
1×1 conv (restore dim)
```
Giảm computational cost

**DenseNet (2017):**
- Kết nối mọi layer với tất cả layers sau nó
- Reuse features hiệu quả hơn ResNet

**EfficientNet (2019 - Google):**
- **Compound scaling:** Scale đồng thời depth, width, và resolution
- Balancing method
- State-of-the-art accuracy với ít parameters và FLOPS hơn

**MobileNet:**
- Thiết kế cho mobile devices và embedded systems
- **Depthwise Separable Convolutions:**
  - Depthwise conv: Áp dụng filter riêng cho mỗi channel
  - Pointwise conv: 1×1 conv để combine channels
  - Giảm parameters và computation 8-9 lần

**SqueezeNet:**
- AlexNet-level accuracy với 50× ít parameters hơn
- Fire modules: Squeeze (1×1 convs) + Expand (1×1 và 3×3 convs)

**Applications of CNNs:**

**Image Classification:**
- Phân loại ảnh vào các categories
- ImageNet, CIFAR, etc.

**Object Detection:**
- Phát hiện và localize objects trong ảnh
- **R-CNN family:** R-CNN, Fast R-CNN, Faster R-CNN
- **YOLO (You Only Look Once):** Real-time detection
- **SSD (Single Shot Detector)**

**Semantic Segmentation:**
- Phân loại mỗi pixel
- **FCN (Fully Convolutional Networks)**
- **U-Net:** Architecture for biomedical images
- **DeepLab:** Atrous convolution

**Instance Segmentation:**
- Segment mỗi object instance riêng biệt
- **Mask R-CNN**

**Face Recognition:**
- FaceNet, DeepFace

**Style Transfer:**
- Chuyển style từ ảnh này sang ảnh khác

**Medical Image Analysis:**
- X-ray, MRI, CT scan analysis
- Disease detection

### Mạng Nơ-ron Hồi Tiếp (Recurrent Neural Networks - RNN)

RNN được thiết kế đặc biệt cho dữ liệu tuần tự (sequential data) như văn bản, chuỗi thời gian, âm thanh, video.

**Đặc điểm:**
- **Kết nối recurrent:** Output ở bước $t$ phụ thuộc vào input hiện tại và các bước trước đó
- **Chia sẻ parameters** qua các time steps
- **Hidden state** lưu trữ thông tin từ quá khứ

**Kiến trúc Cơ Bản:**

$$h_t = \tanh(W_{hh}h_{t-1} + W_{xh}x_t + b_h)$$
$$y_t = W_{hy}h_t + b_y$$

Trong đó:
- $x_t$: Input tại time step $t$
- $h_t$: Hidden state tại time step $t$ (bộ nhớ của mạng)
- $h_{t-1}$: Hidden state từ time step trước
- $y_t$: Output tại time step $t$
- $W_{hh}, W_{xh}, W_{hy}$: Weight matrices (được chia sẻ qua tất cả time steps)

**Cách hoạt động:**
1. Nhận input $x_t$ và hidden state $h_{t-1}$ từ bước trước
2. Kết hợp chúng qua linear transformation
3. Áp dụng activation (tanh)
4. Tạo output $y_t$ và hidden state mới $h_t$
5. $h_t$ được truyền đến time step tiếp theo

**Các Dạng RNN:**

**1. One-to-One:**
- Input: 1 vector
- Output: 1 vector
- Giống feedforward network (không phải RNN thực sự)

**2. One-to-Many:**
- Input: 1 vector
- Output: Sequence of vectors
- **Ứng dụng:** Image captioning (ảnh → mô tả văn bản)

**3. Many-to-One:**
- Input: Sequence of vectors
- Output: 1 vector
- **Ứng dụng:** Sentiment analysis (câu → cảm xúc), video classification

**4. Many-to-Many (synced):**
- Input và output có cùng độ dài, aligned
- **Ứng dụng:** Video classification per frame, POS tagging

**5. Many-to-Many (seq2seq):**
- Input và output có độ dài khác nhau
- **Ứng dụng:** Machine translation, speech recognition, text summarization

**Backpropagation Through Time (BPTT):**
- Mở rộng backpropagation cho sequences
- "Unfold" RNN qua time → feed forward network lớn
- Tính gradients và backprop qua tất cả time steps
- Computational cost cao cho sequences dài

**Vấn Đề Nghiêm Trọng:**

**1. Vanishing Gradients:**
- Gradients giảm mũ khi backprop qua nhiều time steps
- Thông tin từ xa trong quá khứ bị "quên"
- Khó học long-term dependencies
- Nguyên nhân: Nhân nhiều lần với $W_{hh}$ và đạo hàm của tanh (< 1)

**2. Exploding Gradients:**
- Gradients tăng mũ
- Weights update quá lớn, training không ổn định
- Giải pháp: **Gradient clipping**

**Long Short-Term Memory (LSTM):**

LSTM giải quyết vanishing gradient bằng **gating mechanisms** để kiểm soát luồng thông tin. Được phát minh bởi Hochreiter & Schmidhuber (1997).

**Ý tưởng chính:**
- **Cell state** $C_t$: "Conveyor belt" chạy suốt chuỗi, ít thay đổi
- **Gates:** Các cơ chế điều khiển thông tin vào/ra cell state

**Các Gates:**

**1. Forget Gate $f_t$:**
$$f_t = \sigma(W_f[h_{t-1}, x_t] + b_f)$$
- Quyết định **quên** bao nhiêu thông tin từ cell state cũ
- Output: Vector trong [0,1]
- 0 = quên hoàn toàn, 1 = giữ hoàn toàn

**2. Input Gate $i_t$:**
$$i_t = \sigma(W_i[h_{t-1}, x_t] + b_i)$$
- Quyết định thông tin mới nào sẽ được **lưu trữ**
- Kết hợp với candidate values $\tilde{C}_t$

**Candidate Values $\tilde{C}_t$:**
$$\tilde{C}_t = \tanh(W_C[h_{t-1}, x_t] + b_C)$$
- Giá trị mới tiềm năng để thêm vào cell state

**3. Output Gate $o_t$:**
$$o_t = \sigma(W_o[h_{t-1}, x_t] + b_o)$$
- Quyết định output nào từ cell state

**Cell State Update:**
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
- $\odot$: Element-wise multiplication
- **Quên** phần cũ (nhân với $f_t$) + **Thêm** phần mới (nhân $i_t$ với $\tilde{C}_t$)

**Hidden State Update:**
$$h_t = o_t \odot \tanh(C_t)$$

**Tại sao LSTM hiệu quả:**
- **Cell state** cho phép gradient flow dễ dàng qua nhiều time steps
- Gates học được khi nào giữ/quên thông tin
- Có thể học dependencies rất dài (hundreds of time steps)

**Biến thể LSTM:**
- **Peephole connections:** Gates nhìn được cell state
- **Coupled forget and input gates:** $i_t = 1 - f_t$

**Gated Recurrent Unit (GRU):**

Phiên bản đơn giản hóa của LSTM, được giới thiệu bởi Cho et al. (2014).

**Sự khác biệt:**
- **Chỉ 2 gates** thay vì 3 (combine forget và input gate)
- **Không có cell state** riêng biệt
- **Ít parameters hơn** → train nhanh hơn
- Hiệu suất tương đương LSTM trong nhiều tasks

**Gates:**

**Reset Gate $r_t$:**
$$r_t = \sigma(W_r[h_{t-1}, x_t] + b_r)$$
- Quyết định bao nhiêu thông tin từ quá khứ cần **reset**

**Update Gate $z_t$:**
$$z_t = \sigma(W_z[h_{t-1}, x_t] + b_z)$$
- Quyết định bao nhiêu thông tin từ quá khứ cần **giữ lại**
- Giống combine forget + input gate trong LSTM

**Candidate Hidden State:**
$$\tilde{h}_t = \tanh(W[r_t \odot h_{t-1}, x_t] + b)$$
- Reset gate kiểm soát bao nhiêu past hidden state được dùng

**Hidden State Update:**
$$h_t = (1-z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$
- **Interpolation** giữa past hidden state và candidate

**LSTM vs GRU:**

| | LSTM | GRU |
|---|---|---|
| Parameters | Nhiều hơn | Ít hơn ~25% |
| Training speed | Chậm hơn | Nhanh hơn |
| Performance | Tốt hơn với data lớn | Tương đương với data nhỏ |
| Memory | Cell state + hidden | Chỉ hidden |
| Popularity | Phổ biến hơn | Ngày càng được ưa chuộng |

**Lời khuyên:**
- **Bắt đầu với GRU:** Nhanh hơn, đơn giản hơn
- **Thử LSTM** nếu GRU không đủ tốt hoặc có nhiều data
- **Test cả hai** để so sánh

**Bidirectional RNN (BiRNN):**

Xử lý sequence theo **cả hai hướng** (forward và backward).

**Cấu trúc:**
- **Forward RNN:** Xử lý từ trái sang phải ($\overrightarrow{h}_t$)
- **Backward RNN:** Xử lý từ phải sang trái ($\overleftarrow{h}_t$)
- **Kết hợp:** $h_t = [\overrightarrow{h}_t; \overleftarrow{h}_t]$ (concatenate)

**Ưu điểm:**
- Có thông tin từ **cả quá khứ và tương lai**
- Hiệu suất tốt hơn đáng kể trong nhiều tasks

**Nhược điểm:**
- **Không real-time:** Cần toàn bộ sequence trước khi xử lý
- **Gấp đôi parameters và computation**

**Ứng dụng:**
- NLP tasks (POS tagging, NER, sentiment analysis)
- Speech recognition
- Protein structure prediction

**Sequence-to-Sequence (Seq2Seq):**

Kiến trúc cho tasks với input và output sequences có độ dài khác nhau.

**Cấu trúc:**
- **Encoder:** RNN/LSTM/GRU xử lý input sequence → context vector
- **Decoder:** RNN/LSTM/GRU generate output sequence từ context vector

**Ứng dụng:**
- Machine translation
- Text summarization
- Question answering
- Chatbots

**Vấn đề:**
- **Bottleneck:** Context vector cố định phải chứa toàn bộ thông tin
- Khó với sequences dài

**Giải pháp: Attention Mechanism** (dẫn đến Transformers)

### Transformers

Kiến trúc cách mạng sử dụng cơ chế self-attention, được giới thiệu trong paper "Attention is All You Need" (Vaswani et al., 2017).

**Bối cảnh:**
- RNN/LSTM xử lý tuần tự → chậm, khó song song hóa
- Khó học dependencies rất dài
- Transformers giải quyết bằng cách loại bỏ recurrence, chỉ dùng attention

**Self-Attention (Scaled Dot-Product Attention):**

$$Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$$

Trong đó:
- $Q$ (Queries): "Tôi đang tìm gì?" - ma trận queries $(n \times d_k)$
- $K$ (Keys): "Tôi có thông tin gì?" - ma trận keys $(m \times d_k)$
- $V$ (Values): "Thông tin chi tiết là gì?" - ma trận values $(m \times d_v)$
- $d_k$: Dimension của keys (dùng để scale)
- $n$: Số lượng queries (thường = độ dài sequence)
- $m$: Số lượng keys/values

**Cách hoạt động từng bước:**

1. **Tính Attention Scores:**
   $$scores = \frac{QK^T}{\sqrt{d_k}}$$
   - Nhân $Q$ với $K^T$ để tính similarity
   - Chia cho $\sqrt{d_k}$ để scale (tránh softmax saturation)

2. **Áp dụng Softmax:**
   $$attention\_weights = softmax(scores)$$
   - Chuyển scores thành phân phối xác suất
   - Mỗi hàng tổng = 1

3. **Weighted Sum của Values:**
   $$output = attention\_weights \cdot V$$
   - Kết hợp values theo trọng số attention

**Ví dụ minh họa:**
Câu: "The cat sat on the mat"
- Khi xử lý "sat", attention có thể chú ý nhiều đến "cat" (subject) và "mat" (location)
- Attention weights cao cho những từ liên quan, thấp cho những từ không liên quan

**Multi-Head Attention:**

Thay vì một attention mechanism, dùng nhiều "heads" song song.

$$MultiHead(Q,K,V) = Concat(head_1, ..., head_h)W^O$$

Với mỗi head:
$$head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)$$

**Tại sao hiệu quả:**
- **Mỗi head học khía cạnh khác nhau:**
  - Head 1: Quan hệ syntactic (chủ-vị)
  - Head 2: Semantic similarity
  - Head 3: Coreference resolution (đại từ chỉ ai/gì)
- **Tăng model capacity** mà không tăng quá nhiều computation
- Thường dùng $h = 8$ hoặc $16$ heads

**Hyperparameters:**
- $h$: Số heads (thường 8, 12, 16)
- $d_{model}$: Model dimension (512, 768, 1024)
- $d_k = d_v = d_{model}/h$: Dimension mỗi head

**Positional Encoding:**

Transformer không có recurrence → không biết thứ tự từ!

**Giải pháp:** Thêm thông tin vị trí vào embeddings

$$PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})$$
$$PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})$$

Trong đó:
- $pos$: Vị trí của từ trong sequence (0, 1, 2, ...)
- $i$: Dimension index
- $d_{model}$: Model dimension

**Tại sao dùng sin/cos:**
- **Unique encoding** cho mỗi vị trí
- **Relative positions:** Model có thể học "từ A cách từ B bao xa"
- **Extrapolation:** Có thể xử lý sequences dài hơn training

**Kiến Trúc Transformer Đầy Đủ:**

**Encoder:**

Mỗi encoder layer gồm 2 sub-layers:

1. **Multi-Head Self-Attention:**
   - Input attend to tất cả positions trong input
   - Captures relationships giữa các từ

2. **Position-wise Feed-Forward Network:**
   $$FFN(x) = \max(0, xW_1 + b_1)W_2 + b_2$$
   - 2 linear transformations với ReLU
   - Áp dụng độc lập cho mỗi position
   - Thường: $d_{model} = 512 \to 2048 \to 512$

**Mỗi sub-layer có:**
- **Residual connection:** $output = LayerNorm(x + Sublayer(x))$
- **Layer Normalization**

**Stacking:** Thường stack 6 encoder layers (có thể 12, 24 với models lớn)

**Decoder:**

Mỗi decoder layer gồm 3 sub-layers:

1. **Masked Multi-Head Self-Attention:**
   - Tương tự encoder nhưng có **mask**
   - Không được nhìn vào future tokens (autoregressive)
   - Position $i$ chỉ attend to positions $\leq i$

2. **Encoder-Decoder Attention:**
   - **Queries:** Từ decoder
   - **Keys & Values:** Từ encoder output
   - Decoder "attend" to relevant parts của input

3. **Position-wise Feed-Forward Network:**
   - Giống encoder

**Residual connections và Layer Norm** sau mỗi sub-layer.

**Training:**
- **Teacher forcing:** Sử dụng ground truth output làm input cho decoder
- **Masking:** Mask future positions trong decoder self-attention

**Inference:**
- **Autoregressive:** Generate từng token, feed vào input cho token tiếp theo
- Chậm hơn training (sequential generation)

**Ưu Điểm của Transformers:**

1. **Parallelization:**
   - Không như RNN (sequential), có thể xử lý toàn bộ sequence song song
   - Training nhanh hơn nhiều lần trên GPU/TPU

2. **Long-range Dependencies:**
   - Mỗi position có thể trực tiếp attend to bất kỳ position nào
   - Không bị vanishing gradient qua nhiều steps

3. **Flexible Attention:**
   - Học được relationships phức tạp
   - Interpretable (có thể visualize attention weights)

4. **State-of-the-art Performance:**
   - Vượt trội trong hầu hết NLP tasks
   - Mở rộng sang Computer Vision, Speech, Multi-modal

**Nhược Điểm:**

1. **Computational Cost:**
   - Self-attention có độ phức tạp $O(n^2 \cdot d)$ với $n$ = sequence length
   - Expensive với sequences rất dài

2. **Memory:**
   - Cần lưu attention scores → $O(n^2)$ memory
   - Giới hạn maximum sequence length

3. **Need Lots of Data:**
   - Parameters nhiều → cần data lớn để train tốt

**Các Mô Hình Transformer Nổi Tiếng:**

**1. BERT (Bidirectional Encoder Representations from Transformers):**
- **Kiến trúc:** Chỉ dùng Encoder
- **Training:** Masked Language Modeling (MLM) + Next Sentence Prediction
- **Bidirectional:** Nhìn context cả 2 chiều
- **Sử dụng:** Feature extraction, fine-tuning cho downstream tasks
- **Variants:** RoBERTa, ALBERT, DistilBERT

**2. GPT (Generative Pre-trained Transformer):**
- **Kiến trúc:** Chỉ dùng Decoder
- **Training:** Autoregressive language modeling (predict next token)
- **Unidirectional:** Chỉ nhìn left context
- **Sử dụng:** Text generation, few-shot learning
- **Versions:** GPT-2, GPT-3, GPT-4 (ngày càng lớn hơn)

**3. T5 (Text-to-Text Transfer Transformer):**
- **Ý tưởng:** Mọi task đều là text-to-text
- **Ví dụ:** "translate English to German: Hello" → "Hallo"
- **Unified framework** cho mọi NLP tasks

**4. Vision Transformer (ViT):**
- **Áp dụng Transformer cho images**
- Chia ảnh thành patches, treat như sequence
- State-of-the-art trong image classification với data đủ lớn

**5. CLIP (Contrastive Language-Image Pre-training):**
- **Multi-modal:** Kết nối vision và language
- Zero-shot image classification
- Image-text matching

**6. Whisper (OpenAI):**
- **Speech recognition** với Transformer
- Robust, multilingual

**Efficient Transformers:**

Để giải quyết vấn đề $O(n^2)$ complexity:
- **Longformer:** Attention patterns hiệu quả hơn
- **Reformer:** Locality-sensitive hashing
- **Linformer:** Linear complexity attention
- **Performer:** Fast attention via random features

### Autoencoders

Autoencoders là mạng nơ-ron học không giám sát (unsupervised) được thiết kế để học biểu diễn (representation) hiệu quả của dữ liệu.

**Ý tưởng cơ bản:**
- Học cách **nén** (compress) input thành representation nhỏ gọn
- Sau đó **giải nén** (reconstruct) lại input từ representation đó
- Nếu reconstruction tốt → representation đã capture được thông tin quan trọng

**Kiến Trúc:**

**1. Encoder (Bộ mã hóa):**
$$z = f_{\theta}(x)$$
- Input $x$ (high-dimensional) → Latent representation $z$ (low-dimensional)
- Thường là feedforward network
- "Nén" thông tin, loại bỏ redundancy

**2. Latent Space (Code):**
- Bottleneck layer
- Representation learned $z$
- Thường có dimension nhỏ hơn nhiều so với input
- Là nơi "gói gọn" thông tin quan trọng

**3. Decoder (Bộ giải mã):**
$$\hat{x} = g_{\phi}(z)$$
- Latent code $z$ → Reconstructed output $\hat{x}$
- Mirror architecture của encoder
- "Giải nén" thông tin

**Loss Function - Reconstruction Error:**
$$L = ||x - \hat{x}||^2 = \sum_{i}(x_i - \hat{x}_i)^2$$

**Mục tiêu:** Minimize sự khác biệt giữa input và reconstruction

**Ví dụ:**
- Input: Ảnh 784 dimensions (28×28)
- Encoder: 784 → 128 → 32
- Latent: 32 dimensions
- Decoder: 32 → 128 → 784
- Output: Ảnh reconstructed 784 dimensions

**Các Loại Autoencoders:**

**1. Vanilla Autoencoder:**
- Autoencoder cơ bản
- Simple feedforward networks
- Loss: MSE reconstruction error

**Ứng dụng:**
- Dimensionality reduction (thay thế PCA)
- Feature learning
- Data compression

**2. Sparse Autoencoder:**

Thêm sparsity constraint vào latent representation.

$$L = ||x - \hat{x}||^2 + \lambda \sum_{j}|z_j|$$

**Mục tiêu:**
- Khuyến khích nhiều neurons trong latent layer = 0 hoặc gần 0
- Chỉ một số neurons active (sparse activation)

**Lợi ích:**
- **Disentangled representations:** Mỗi neuron học một feature riêng biệt
- Tránh encoder chỉ copy input
- Better feature learning

**Thực hiện:**
- L1 regularization trên activations
- KL divergence penalty

**3. Denoising Autoencoder (DAE):**

Train mạng reconstruct **clean input** từ **corrupted input**.

**Quá trình:**
1. Input sạch $x$
2. Thêm noise: $\tilde{x} = x + noise$ (Gaussian noise, masking, salt-and-pepper)
3. Encoder: $z = f(\tilde{x})$
4. Decoder: $\hat{x} = g(z)$
5. Loss: $||x - \hat{x}||^2$ (so sánh với original, không phải corrupted!)

**Tại sao hiệu quả:**
- **Học robust features:** Không bị mislead bởi noise
- **Force learning meaningful structure** trong data
- Better generalization

**Ứng dụng:**
- Image denoising
- Inpainting (fill missing regions)
- Robust feature extraction

**4. Variational Autoencoder (VAE):**

**Khác biệt lớn:** Thay vì deterministic, VAE là **probabilistic/generative model**.

**Ý tưởng:**
- Latent code $z$ không phải vector cố định, mà là một **distribution** (thường Gaussian)
- Có thể **generate new samples** bằng cách sample từ latent space

**Kiến trúc:**

**Encoder (Recognition/Inference Network):**
- Output: Mean $\mu$ và variance $\sigma^2$ của distribution
- $q_{\phi}(z|x) = \mathcal{N}(z; \mu(x), \sigma^2(x))$

**Reparameterization Trick:**
$$z = \mu + \sigma \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$
- Cho phép backpropagation qua sampling operation

**Decoder (Generative Network):**
- $p_{\theta}(x|z)$: Probability của x given z
- Generate $\hat{x}$ từ sampled $z$

**Loss Function:**
$$L = L_{reconstruction} + \beta \cdot KL(q_{\phi}(z|x) || p(z))$$

Trong đó:
- **Reconstruction Loss:** $\mathbb{E}_{z \sim q}[\log p_{\theta}(x|z)]$ - Đảm bảo reconstruction tốt
- **KL Divergence:** $KL(q_{\phi}(z|x) || p(z))$ - Regularization, đảm bảo latent distribution gần prior $p(z) = \mathcal{N}(0, I)$
- $\beta$: Hyperparameter kiểm soát trade-off (β-VAE)

**Tại sao KL divergence:**
- Force latent space có cấu trúc tốt (continuous, smooth)
- Cho phép generate by sampling $z \sim \mathcal{N}(0, I)$
- Regularization effect

**Ưu điểm VAE:**
- **Generative:** Có thể tạo dữ liệu mới
- **Smooth latent space:** Interpolation giữa samples có ý nghĩa
- **Probabilistic framework:** Principled, có foundation lý thuyết

**Nhược điểm:**
- Reconstructions thường blurry (do Gaussian assumption)
- Phức tạp hơn vanilla autoencoder

**Ứng dụng:**
- Image generation
- Data augmentation
- Anomaly detection (outliers có reconstruction error cao)
- Semi-supervised learning

**5. Contractive Autoencoder:**

Thêm penalty trên **derivative của latent representation** theo input.

$$L = ||x - \hat{x}||^2 + \lambda ||\frac{\partial f}{\partial x}||_F^2$$

**Mục tiêu:**
- Latent representation **robust to small changes** trong input
- Locally "contract" space

**Lợi ích:**
- Learn representations insensitive to small perturbations
- Regularization effect

**6. Convolutional Autoencoder:**

Sử dụng convolutional và pooling layers thay vì fully connected.

**Encoder:**
```
Conv → Pool → Conv → Pool → ...
```

**Decoder:**
```
ConvTranspose (Upsampling) → ConvTranspose → ...
```

**Ưu điểm:**
- **Ít parameters hơn** với images
- **Preserve spatial structure**
- Hiệu quả hơn với image data

**Ứng dụng:**
- Image compression
- Image denoising
- Super-resolution

**Ứng Dụng Thực Tế của Autoencoders:**

**1. Dimensionality Reduction:**
- Alternative to PCA
- Non-linear transformations
- Visualization trong 2D/3D (t-SNE trên latent space)

**2. Anomaly Detection:**
- Train trên normal data
- Anomalies có reconstruction error cao
- Applications: Fraud detection, defect detection, network intrusion

**3. Denoising:**
- Remove noise từ images, audio, signals
- Medical imaging
- Old photo restoration

**4. Feature Learning:**
- Pre-training cho supervised tasks
- Transfer learning
- Extract meaningful representations

**5. Generative Modeling (VAE):**
- Generate new faces, artwork
- Data augmentation
- Creative applications

**6. Image Compression:**
- Learn compression schemes tốt hơn traditional methods
- JPEG alternative

**7. Information Retrieval:**
- Semantic hashing
- Similar image search (search trong latent space)

**So sánh các loại Autoencoders:**

| Type | Goal | Output | Use Case |
|------|------|--------|----------|
| Vanilla | Dim reduction | Deterministic | Compression, features |
| Sparse | Interpretability | Sparse code | Feature learning |
| Denoising | Robustness | Denoised | Denoising, robust features |
| VAE | Generation | Probabilistic | Generation, sampling |
| Contractive | Stability | Robust code | Robust representations |

### Mạng Đối Sinh (Generative Adversarial Networks - GANs)

GANs là framework cho generative models được phát minh bởi Ian Goodfellow et al. (2014). Ý tưởng: Hai mạng nơ-ron "cạnh tranh" với nhau để cải thiện.

**Ẩn dụ:** 
- Generator giống như **tên làm tiền giả**
- Discriminator giống như **cảnh sát phát hiện tiền giả**
- Qua thời gian, cả hai đều giỏi hơn → tiền giả ngày càng thật

**Các Thành Phần:**

**1. Generator (Bộ Sinh):** $G(z) \to fake\_data$

**Input:**
- Random noise vector $z \sim p_z(z)$ (thường Gaussian hoặc Uniform)
- Dimension thường 100-1000

**Output:**
- Synthetic data (fake) $G(z)$
- Cùng kích thước với real data
- Ví dụ: Ảnh 64×64×3

**Mục tiêu:**
- **Generate realistic samples** không phân biệt được với real data
- "Lừa" Discriminator tin là real

**Kiến trúc:**
- Thường là deconvolutional network (transpose convolutions)
- Batch normalization, ReLU/LeakyReLU
- Tanh activation ở output (để output trong [-1, 1])

**2. Discriminator (Bộ Phân Biệt):** $D(x) \to [0,1]$

**Input:**
- Data sample $x$ (có thể real hoặc fake)

**Output:**
- Scalar trong [0, 1]: Xác suất sample là **real**
- Gần 1 = tin là real, gần 0 = tin là fake

**Mục tiêu:**
- **Phân biệt chính xác** real vs fake
- Maximize classification accuracy

**Kiến trúc:**
- Thường là CNN (convolutional network)
- Leaky ReLU, Dropout
- Sigmoid activation ở output

**Training - Minimax Game:**

Đây là một **two-player game** với objective function:

$$\min_G \max_D V(D,G) = \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1-D(G(z)))]$$

**Giải thích:**

**Discriminator muốn maximize:**
- $\mathbb{E}_{x \sim p_{data}}[\log D(x)]$: Maximize log probability của real data
- $\mathbb{E}_{z \sim p_z}[\log(1-D(G(z)))]$: Maximize log probability reject fake data

**Generator muốn minimize:**
- $\mathbb{E}_{z \sim p_z}[\log(1-D(G(z)))]$: Minimize log probability fake bị reject
- Tương đương: Maximize $\mathbb{E}_{z}[\log D(G(z))]$ (non-saturating loss trong thực tế)

**Thuật Toán Training:**

**Alternating Updates** (training xen kẽ):

**Mỗi iteration:**

1. **Train Discriminator (k steps, thường k=1):**
   - Sample mini-batch real data $\{x^{(1)}, ..., x^{(m)}\}$
   - Sample mini-batch noise $\{z^{(1)}, ..., z^{(m)}\}$
   - Generate fake data: $\tilde{x}^{(i)} = G(z^{(i)})$
   - Update D by **ascending** gradient:
   $$\nabla_{\theta_D} \frac{1}{m}\sum_{i=1}^{m}[\log D(x^{(i)}) + \log(1-D(G(z^{(i)})))]$$

2. **Train Generator (1 step):**
   - Sample mini-batch noise $\{z^{(1)}, ..., z^{(m)}\}$
   - Update G by **descending** gradient:
   $$\nabla_{\theta_G} \frac{1}{m}\sum_{i=1}^{m}\log(1-D(G(z^{(i)})))$$
   - Hoặc non-saturating: Ascending $\nabla_{\theta_G} \frac{1}{m}\sum_{i=1}^{m}\log D(G(z^{(i)}))$

**Lý do train D nhiều hơn G:**
- D cần đủ accurate để provide good gradient cho G
- Nếu D quá yếu, G không học được gì

**Thách Thức trong Training GANs:**

**1. Mode Collapse:**
- **Vấn đề:** Generator chỉ sinh một vài modes (variations) của data
- Ví dụ: Generate faces nhưng chỉ 5-10 khuôn mặt khác nhau, không đa dạng
- **Nguyên nhân:** G tìm được cách "lừa" D với một số samples → bỏ qua diversity

**Giải pháp:**
- Minibatch discrimination
- Feature matching
- Unrolled GAN

**2. Training Instability:**
- Loss oscillates, không converge
- D quá mạnh → gradient vanishing cho G
- G quá mạnh → D không học được gì
- **Cân bằng khó đạt được**

**Giải pháp:**
- Careful hyperparameter tuning
- Learning rate schedules
- Different architectures (DCGAN guidelines)

**3. Vanishing Gradients:**
- Nếu D perfect (D(G(z)) ≈ 0), gradient cho G ≈ 0
- G không learn được

**Giải pháp:**
- Non-saturating loss: Maximize $\log D(G(z))$ thay vì minimize $\log(1-D(G(z)))$
- Wasserstein loss (WGAN)

**4. Difficulty in Convergence:**
- Không rõ khi nào stop training
- Loss không phản ánh chất lượng samples

**Giải pháp:**
- Inception Score (IS)
- Fréchet Inception Distance (FID)
- Manual inspection

**Các Biến Thể GAN Quan Trọng:**

**1. DCGAN (Deep Convolutional GAN, 2015):**

**Architectural guidelines** giúp stable training:

**Generator:**
- Replace pooling với **strided convolutions** (transpose conv)
- **Batch Normalization** trong cả G và D (không dùng ở output layer của G và input layer của D)
- Remove fully connected hidden layers
- **ReLU** activation trong G, **Tanh** ở output
  
**Discriminator:**
- **Strided convolutions** thay vì pooling
- **Batch Normalization**
- **LeakyReLU** activation

**Impact:** Chuẩn hóa architecture, foundation cho nhiều GANs sau này

**2. Conditional GAN (cGAN, 2014):**

**Ý tưởng:** Condition generation trên additional information (labels, text, etc.)

**Modification:**
- Generator: $G(z, y)$ - Input noise + condition
- Discriminator: $D(x, y)$ - Input data + condition

**Loss:**
$$\min_G \max_D V(D,G) = \mathbb{E}_{x,y}[\log D(x,y)] + \mathbb{E}_{z,y}[\log(1-D(G(z,y),y))]$$

**Ứng dụng:**
- Text-to-image: "a red car" → generate ảnh xe đỏ
- Class-conditional generation: Chọn class → generate sample thuộc class đó
- Image-to-image translation với conditions

**3. Wasserstein GAN (WGAN, 2017):**

**Vấn đề với original GAN:** JS divergence không cung cấp gradient tốt khi distributions không overlap.

**Giải pháp:** Sử dụng **Wasserstein distance** (Earth Mover's Distance)

**New Objective:**
$$\min_G \max_{D \in \mathcal{D}} \mathbb{E}_{x \sim p_{data}}[D(x)] - \mathbb{E}_{z \sim p_z}[D(G(z))]$$

**Khác biệt:**
- D không output probability nữa, mà output **score** (không bound)
- D gọi là "critic" thay vì discriminator
- Remove sigmoid ở output của D

**1-Lipschitz Constraint:**
- D phải thỏa mãn Lipschitz constraint
- **Weight clipping** (WGAN): Clip weights trong [-c, c]
- **Gradient penalty** (WGAN-GP, better): Penalize gradient norm khác 1

**Ưu điểm:**
- **Stable training:** Ít mode collapse, ít training instability
- **Meaningful loss:** Loss correlate với sample quality → biết khi nào stop
- Có thể train D nhiều iterations mà không lo gradient vanishing

**4. StyleGAN (2018-2019):**

**Breakthrough** trong image generation quality, developed by NVIDIA.

**Key Ideas:**

**Style-based Generator:**
- Mapping network: $z \to w$ (intermediate latent space)
- Synthesis network: Dùng $w$ để control "style" ở mỗi scale
- Adaptive Instance Normalization (AdaIN)

**Progressive Growing:**
- Train từ low resolution (4×4) gradually tăng lên high resolution (1024×1024)
- Stable và faster

**Style Mixing:**
- Có thể mix styles từ nhiều sources
- Coarse styles (pose, shape) từ image A
- Fine styles (colors, micro-structures) từ image B

**Stochastic Variation:**
- Thêm noise per-pixel cho details (hair, pores)

**Kết quả:**
- **Photorealistic faces** ở 1024×1024
- Controllable generation
- Smooth interpolation trong latent space

**StyleGAN2, StyleGAN3:** Improvements về artifacts và motion

**5. CycleGAN (2017):**

**Vấn đề:** Image-to-image translation thường cần paired data (input-output pairs) → expensive

**Giải pháp:** **Unpaired image-to-image translation**

**Ý tưởng:**
- Học mapping giữa 2 domains $X$ và $Y$ **không cần paired examples**
- Ví dụ: Horses ↔ Zebras, Photos ↔ Paintings

**Architecture:**
- **2 Generators:** $G: X \to Y$ và $F: Y \to X$
- **2 Discriminators:** $D_X$ và $D_Y$

**Cycle Consistency Loss:**
$$L_{cyc} = \mathbb{E}_{x}[||F(G(x)) - x||_1] + \mathbb{E}_{y}[||G(F(y)) - y||_1]$$

- Forward cycle: $x \to G(x) \to F(G(x)) \approx x$
- Backward cycle: $y \to F(y) \to G(F(y)) \approx y$
- Đảm bảo mappings consistent

**Total Loss:**
$$L = L_{GAN}(G, D_Y) + L_{GAN}(F, D_X) + \lambda L_{cyc}$$

**Ứng dụng:**
- Style transfer
- Season transfer (summer ↔ winter)
- Object transfiguration (horse ↔ zebra)
- Photo enhancement

**Các biến thể khác:**
- **Pix2Pix:** Paired image-to-image translation (conditional GAN)
- **ProGAN:** Progressive growing
- **BigGAN:** Very large-scale GANs
- **StyleGAN-NADA:** Text-driven manipulation

**Ứng Dụng Thực Tế của GANs:**

**1. Image Generation:**
- Generate realistic faces (ThisPersonDoesNotExist.com)
- Artwork generation
- Synthetic training data

**2. Image-to-Image Translation:**
- Photo ↔ Sketch
- Day ↔ Night
- Semantic labels ↔ Photo

**3. Super-Resolution:**
- Upscale images với high quality (SRGAN, ESRGAN)

**4. Data Augmentation:**
- Generate synthetic training samples
- Balance imbalanced datasets

**5. Image Editing:**
- Change attributes (age, hair color, expression)
- Inpainting (fill missing regions)
- Remove objects

**6. Medical Imaging:**
- Generate synthetic medical images
- Image enhancement
- Cross-modality translation (MRI ↔ CT)

**7. Video Generation:**
- Generate realistic videos
- Frame interpolation
- Video prediction

**8. Text-to-Image:**
- DALL-E, Stable Diffusion (diffusion models giờ phổ biến hơn GANs)

**9. 3D Generation:**
- Generate 3D models from 2D images

**10. Art và Creative Applications:**
- Style transfer
- Face morphing
- Deepfakes (ethical concerns!)

**Đánh Giá GANs:**

**Metrics:**
- **Inception Score (IS):** Đo quality và diversity
- **Fréchet Inception Distance (FID):** So sánh distribution của real vs generated
- **Precision và Recall:** Quality vs Diversity trade-off
- **Human evaluation:** Manual assessment (gold standard)

### Học Chuyển Giao (Transfer Learning)

Transfer Learning là kỹ thuật tận dụng kiến thức đã học từ một task để giải quyết task khác, đặc biệt hữu ích khi dữ liệu hạn chế.

**Động lực:**
- Training deep networks từ đầu cần **rất nhiều data và computation**
- Pre-trained models đã học được **general features** trên large datasets
- Low-level features (edges, textures) thường **transferable** giữa các tasks
- Tiết kiệm thời gian và tài nguyên

**Khi nào sử dụng:**
- ✅ Data mới **ít** (hundreds đến thousands samples)
- ✅ Task mới **tương tự** task đã train
- ✅ Không đủ computational resources
- ❌ Data mới rất khác biệt với pre-trained data
- ❌ Có rất nhiều data và resources (có thể train from scratch)

**Các Phương Pháp:**

**1. Feature Extraction (Trích Xuất Đặc Trưng):**

**Cách làm:**
- **Freeze toàn bộ pre-trained layers** (set requires_grad = False)
- **Remove output layer** của pre-trained model
- **Add new output layers** cho task mới
- **Train chỉ new layers**

**Ví dụ với CNN:**
```
Pre-trained ResNet-50 (ImageNet):
Input → Conv layers (frozen) → ... → FC (frozen) → 1000 classes

Modified for new task (10 classes):
Input → Conv layers (frozen) → ... → [Remove old FC] → New FC → 10 classes
```

**Khi nào dùng:**
- Dataset mới **rất nhỏ** (< 1000 samples)
- New task **tương tự** original task
- Limited computational resources

**Ưu điểm:**
- **Rất nhanh** (chỉ train vài layers)
- **Ít parameters** → ít overfitting
- Không cần GPU mạnh

**Nhược điểm:**
- Ít flexible hơn
- Performance có thể không tối ưu nếu tasks khác nhau nhiều

**2. Fine-tuning (Tinh Chỉnh):**

**Cách làm:**
1. Load pre-trained model
2. **Replace output layer** cho task mới
3. **Unfreeze một số layers** (thường top layers)
4. Train với **learning rate nhỏ** (0.0001 - 0.00001)

**Strategies:**

**a) Fine-tune toàn bộ network:**
- Unfreeze tất cả layers
- Train với learning rate rất nhỏ
- Cần nhiều data hơn

**b) Fine-tune top layers:**
- **Freeze early layers** (low-level features)
- **Unfreeze later layers** (high-level, task-specific features)
- Phổ biến nhất

**c) Progressive unfreezing:**
- Ban đầu freeze tất cả, train new layers
- Dần dần unfreeze từ top xuống bottom layers
- Train từng nhóm layers

**Khi nào dùng:**
- Dataset mới **medium-sized** (1K - 100K samples)
- Task **hơi khác** original task
- Có computational resources

**Ưu điểm:**
- **Better performance** hơn feature extraction
- Adapt được features cho task cụ thể
- Balance giữa from-scratch và feature extraction

**Nhược điểm:**
- Chậm hơn feature extraction
- Risk overfitting với data ít
- Cần tune learning rate cẩn thận

**Learning Rate Strategy:**
- **Discriminative learning rates:** Layers khác nhau có LR khác nhau
  - Early layers: LR rất nhỏ (0.00001)
  - Middle layers: LR nhỏ (0.0001)
  - New layers: LR lớn hơn (0.001)
- Tránh phá hủy learned features ở early layers

**3. Domain Adaptation:**

Khi source và target domains khác nhau (distribution shift).

**Techniques:**
- **Adversarial domain adaptation:** Align feature distributions
- **Self-training:** Pseudo-labeling on target domain
- **Multi-task learning:** Train source và target tasks jointly

**Best Practices cho Transfer Learning:**

**1. Lựa chọn Pre-trained Model:**

**Computer Vision:**
- **General purpose:** ResNet-50, EfficientNet-B0 (balance accuracy/speed)
- **High accuracy:** ResNet-152, EfficientNet-B7, Vision Transformer
- **Mobile/Edge:** MobileNet, EfficientNet-Lite
- **Object detection:** Models pre-trained trên COCO
- **Medical imaging:** Models pre-trained trên medical datasets

**NLP:**
- **General text:** BERT, RoBERTa
- **Generation:** GPT-2, GPT-3
- **Multilingual:** XLM-RoBERTa, mBERT
- **Domain-specific:** BioBERT (medical), FinBERT (finance)

**2. Data Similarity:**

| Source vs Target | Strategy |
|------------------|----------|
| Very similar | Feature extraction, minimal fine-tuning |
| Somewhat similar | Fine-tune top layers |
| Quite different | Fine-tune more layers hoặc train from scratch |
| Very different | Train from scratch (transfer learning ít hiệu quả) |

**3. Dataset Size:**

| Dataset Size | Strategy |
|--------------|----------|
| Very small (< 1K) | Feature extraction only |
| Small (1K - 10K) | Feature extraction hoặc fine-tune top layer |
| Medium (10K - 100K) | Fine-tune several top layers |
| Large (> 100K) | Fine-tune nhiều layers hoặc entire network |
| Very large (> 1M) | Consider training from scratch |

**4. Technical Tips:**

**Data Preprocessing:**
- Sử dụng **same preprocessing** như pre-trained model
- Ví dụ: ImageNet models expect ImageNet normalization

**Batch Normalization:**
- **Freeze BN layers** khi fine-tune
- Hoặc set BN to eval mode
- Tránh update statistics với batch nhỏ

**Regularization:**
- Thêm Dropout nếu cần
- Data augmentation quan trọng với data ít
- Early stopping trên validation set

**Learning Rate:**
- Bắt đầu nhỏ (1e-4 hoặc nhỏ hơn)
- Learning rate scheduling (reduce on plateau)
- Warmup cho transformers

**Gradual Unfreezing:**
```python
# Epoch 1-5: Train only new layers
# Epoch 6-10: Unfreeze top layer
# Epoch 11-15: Unfreeze more layers
```

**Lợi Ích của Transfer Learning:**

1. **Faster Training:**
   - Converge nhanh hơn nhiều (hours thay vì days)
   - Pre-trained weights là starting point tốt

2. **Better Performance với Limited Data:**
   - Crucial khi data ít
   - Có thể đạt good results với hundreds samples

3. **Improved Generalization:**
   - Pre-trained features robust
   - Regularization effect

4. **Lower Computational Cost:**
   - Ít epochs cần thiết
   - Có thể dùng CPU/GPU nhỏ hơn

5. **Democratization of Deep Learning:**
   - Không cần massive datasets
   - Không cần expensive infrastructure

**Các Pre-trained Models Phổ Biến:**

**Computer Vision (ImageNet):**
- **ResNet family:** ResNet-18, 50, 101, 152
- **VGG:** VGG-16, VGG-19
- **Inception:** InceptionV3, InceptionResNetV2
- **EfficientNet:** B0 đến B7
- **MobileNet:** V1, V2, V3
- **DenseNet:** DenseNet-121, 169, 201
- **Vision Transformers:** ViT, Swin Transformer

**NLP:**
- **BERT variants:** BERT, RoBERTa, ALBERT, DistilBERT
- **GPT family:** GPT-2, GPT-3, GPT-4
- **T5:** Text-to-Text Transfer Transformer
- **XLNet, ELECTRA, DeBERTa**

**Multi-modal:**
- **CLIP:** Vision-Language
- **DALL-E:** Text-to-Image
- **Flamingo, BLIP**

**Speech:**
- **Wav2Vec 2.0**
- **HuBERT**
- **Whisper**

**Ví Dụ Thực Tế:**

**Medical Image Classification:**
- Pre-trained: ResNet-50 trên ImageNet (1.4M images)
- Fine-tune: Medical X-ray dataset (5K images)
- Result: 95% accuracy vs 78% training from scratch

**Sentiment Analysis:**
- Pre-trained: BERT trên Wikipedia + Books (3.3B words)
- Fine-tune: Movie reviews (25K samples)
- Result: 94% accuracy trong 3 epochs

**Challenges và Limitations:**

1. **Negative Transfer:**
   - Pre-trained model có thể hurt performance nếu quá khác biệt
   - Solution: Evaluate carefully, có thể train from scratch tốt hơn

2. **Computational Cost (Fine-tuning):**
   - Vẫn cần significant compute
   - Solution: Feature extraction hoặc parameter-efficient fine-tuning

3. **Bias Transfer:**
   - Pre-trained model có thể mang theo biases
   - Solution: Careful evaluation, debiasing techniques

4. **License và Ethical Issues:**
   - Một số models có restrictions
   - Privacy concerns với pre-training data

### Các Phương Pháp Hay Nhất cho Học Sâu (Deep Learning Best Practices)

**1. Chuẩn Bị Dữ Liệu:**

**Quantity:**
- Deep learning cần **nhiều data** (thousands đến millions)
- Rule of thumb: 5-10× số parameters (tối thiểu)
- Nếu ít: Consider transfer learning, data augmentation

**Quality:**
- **Clean data > big data:** Garbage in, garbage out
- Remove duplicates, corrupted samples
- Consistent labeling
- Handle missing values

**Balanced Classes:**
- Imbalanced data → model bias về majority class
- **Solutions:**
  - Oversampling minority class (SMOTE)
  - Undersampling majority class
  - Class weights trong loss function
  - Focal loss cho extreme imbalance

**Train/Validation/Test Split:**
- Typical: 70/15/15 hoặc 80/10/10
- Với data lớn: 98/1/1 ok
- **Stratified split** giữ tỷ lệ classes
- **Never touch test set** cho đến cuối!

**Data Augmentation:**
- Essential với data ít
- On-the-fly augmentation trong training
- Domain-specific augmentations

**Normalization:**
- **Images:** Normalize pixel values [0,1] hoặc standardize
- **Features:** StandardScaler, MinMaxScaler
- **Per-channel normalization** cho images (ImageNet stats)

**2. Thiết Kế Kiến Trúc:**

**Start Simple:**
- Begin với simple baseline model
- Gradually add complexity nếu cần
- Simpler models train nhanh, debug dễ

**Use Proven Architectures:**
- Không reinvent the wheel
- **Vision:** ResNet, EfficientNet
- **NLP:** Transformers (BERT, GPT)
- **Time series:** LSTM, Temporal CNNs

**Consider Constraints:**
- **Latency requirements:** MobileNet, pruning, quantization
- **Memory limitations:** Smaller models, gradient checkpointing
- **Interpretability needs:** Simpler models, attention mechanisms

**Modular Design:**
- Separate components (encoder, decoder, heads)
- Easy to modify và experiment

**3. Điều Chỉnh Hyperparameters:**

**Most Important Hyperparameters:**

**Learning Rate (QUAN TRỌNG NHẤT!):**
- Start với default của optimizer (Adam: 0.001)
- Learning rate too high → divergence, loss explode
- Learning rate too low → very slow convergence
- **Learning rate finder:** Plot loss vs LR, chọn trước điểm tăng đột ngột
- **Learning rate schedules:**
  - Step decay: Giảm mỗi N epochs
  - Exponential decay: Giảm dần liên tục
  - Cosine annealing: Smooth decrease
  - ReduceLROnPlateau: Giảm khi validation loss plateau

**Batch Size:**
- **Larger batches (128-512):**
  - Pros: Faster training (parallelization), stable gradients
  - Cons: Cần nhiều memory, có thể generalize kém hơn
- **Smaller batches (32-64):**
  - Pros: Regularization effect, better generalization, ít memory
  - Cons: Noisy gradients, train chậm hơn
- **Rule of thumb:** Bắt đầu 32-64, tăng nếu có memory

**Number of Epochs:**
- Start với nhiều epochs, dùng early stopping
- Monitor validation loss

**Network Architecture:**
- Number of layers: Start shallow, thêm depth nếu underfitting
- Number of neurons: Enough capacity nhưng không quá
- Dropout rate: 0.2-0.5

**Regularization Strength:**
- Weight decay (L2): 1e-4 hoặc 1e-5
- Dropout: 0.5 for FC, 0.2-0.3 for others

**Hyperparameter Tuning Strategies:**
- **Manual tuning:** Hiểu behavior, instructive
- **Grid search:** Exhaustive nhưng expensive
- **Random search:** Often better than grid
- **Bayesian optimization:** Intelligent search (Optuna, Hyperopt)
- **Learning rate first!** Tune LR trước, sau đó others

**4. Tips Trong Training:**

**Monitor Metrics:**
- **Training loss:** Phải giảm
- **Validation loss:** Quan trọng nhất, measure generalization
- **Train/val gap:** Lớn → overfitting
- **Accuracy, F1, etc.:** Task-specific metrics

**Visualization:**
- Plot loss curves (train vs validation)
- Learning rate vs loss
- Gradient norms
- Activation distributions
- Attention weights (interpretability)

**Learning Rate Scheduling:**
- Essential cho converge tốt
- Warmup (increase gradually) cho transformers
- Decay về cuối training

**Gradient Clipping:**
- **Critical for RNNs** (prevent exploding gradients)
- Useful cho transformers
- Typical value: 1.0 hoặc 5.0

**Checkpoint Best Models:**
- Save model với best validation metric
- Checkpoint mỗi N epochs hoặc khi improve
- Resume training nếu crash

**Early Stopping:**
- Stop nếu val loss không improve sau N epochs (patience=10-20)
- Saves time, prevents overfitting

**Mixed Precision Training:**
- FP16 thay vì FP32
- **2×** faster, ít memory hơn
- Nvidia GPUs (Tensor Cores)

**5. Debugging Deep Learning Models:**

**Start Small:**
- **Overfit một batch nhỏ:** Nếu không overfit được → bug trong model/training
- Nếu overfit được → model có capacity, issue là generalization

**Check Data:**
- Visualize samples: Correct labels? Reasonable augmentation?
- Check data pipeline: No bugs?
- Shuffle properly?

**Check Gradients:**
- Vanishing gradients: Gradients → 0, không học được
  - Solutions: Change activation (ReLU), batch norm, residual connections
- Exploding gradients: Gradients → ∞
  - Solutions: Gradient clipping, lower learning rate
- Use gradient visualization tools

**Sanity Checks:**
- Disable regularization (dropout, weight decay): Should overfit
- Train trên random labels: Should fit (báo model có capacity)
- Check loss: Không phải NaN, không explode

**Common Issues:**

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Loss is NaN | Learning rate too high, numerical instability | Lower LR, gradient clipping, check data |
| Loss không giảm | Learning rate too low, bad initialization | Increase LR, check data/labels |
| Train loss giảm, val loss không giảm | Overfitting | Regularization, data augmentation, smaller model |
| Both losses cao | Underfitting | Bigger model, more layers, train longer |
| Loss oscillates | Batch size too small, LR too high | Increase batch size, lower LR |

**Use Tools:**
- **TensorBoard:** Visualize metrics, graphs, histograms
- **Weights & Biases (wandb):** Experiment tracking
- **Neptune.ai, MLflow:** Experiment management

**6. Hardware và Infrastructure:**

**GPUs Essential:**
- Deep learning cần GPU (10-100× faster than CPU)
- **Consumer GPUs:** RTX 3080, 3090, 4090
- **Data center GPUs:** A100, H100 (very expensive)
- **Cloud options:** AWS, GCP, Azure, vast.ai

**TPUs:**
- Google's Tensor Processing Units
- Faster than GPUs cho certain workloads (transformers)
- Access qua Google Colab, GCP

**Multi-GPU Training:**
- **Data parallelism:** Split batch across GPUs
- **Model parallelism:** Split model across GPUs (very large models)
- **Distributed training:** Multiple machines

**Memory Management:**
- **Gradient accumulation:** Simulate large batch với small memory
- **Gradient checkpointing:** Trade compute for memory
- **Mixed precision:** FP16 uses less memory

**Cloud vs Local:**
- **Local:** Full control, no hourly costs, data privacy
- **Cloud:** Scalable, no upfront cost, powerful hardware
- **Colab/Kaggle:** Free GPUs, good for learning/prototyping

### Frameworks cho Học Sâu (Deep Learning Frameworks)

**1. TensorFlow / Keras:**

**TensorFlow:**
- Developed by Google
- **Industry standard** cho production
- Khó hơn PyTorch (historically)
- TensorFlow 2.0+: Eager execution, easier to use

**Keras:**
- High-level API trên TensorFlow
- Very user-friendly
- **Best cho beginners**
- Sequential và Functional APIs

**Ưu điểm:**
- **Production-ready:** TensorFlow Serving, TFLite (mobile), TF.js (web)
- **Ecosystem rộng:** TensorBoard, TFX (pipeline), TF Hub (models)
- **Strong industry adoption**
- **Deployment tools** mature

**Nhược điểm:**
- Khó debug hơn PyTorch
- Less Pythonic
- Community nhỏ hơn trong research

**Khi nào dùng:**
- Production systems
- Mobile/edge deployment
- Large-scale systems
- Nếu công ty dùng TensorFlow

**2. PyTorch:**

- Developed by Meta (Facebook)
- **Research favorite** (majority của papers)
- **Pythonic và intuitive**
- Dynamic computation graphs

**Ưu điểm:**
- **Easier to learn và debug**
- **Dynamic graphs:** Flexibility, conditional logic dễ
- **Strong research community**
- Excellent documentation
- **TorchServe** cho deployment
- **PyTorch Lightning:** High-level wrapper

**Nhược điểm:**
- Deployment chưa mature bằng TensorFlow (improving rapidly)
- Ít tools cho production
- Mobile deployment limited hơn (TorchScript, PyTorch Mobile improving)

**Khi nào dùng:**
- Research và prototyping
- Learning deep learning
- Custom architectures
- Academic projects
- Nếu cần flexibility

**3. JAX:**

- Developed by Google Research
- **High-performance** numerical computing
- **Functional programming** approach
- **Automatic differentiation** (autograd)

**Đặc điểm:**
- Composable transformations: `grad`, `jit`, `vmap`, `pmap`
- **NumPy-like API**
- Excellent cho custom algorithms
- Fast (XLA compilation)

**Ưu điểm:**
- **Fastest training** (với XLA)
- Clean functional code
- Great cho research
- **Flax, Haiku:** Neural network libraries trên JAX

**Nhược điểm:**
- Steep learning curve (functional programming)
- Ecosystem nhỏ hơn
- Less mature
- Ít pre-trained models

**Khi nào dùng:**
- High-performance computing
- Custom algorithms
- Research (nếu comfortable với functional programming)
- Scientific computing

**4. Các Frameworks Khác:**

**MXNet:**
- Developed by Apache
- Used by AWS
- Flexible, efficient
- Gluon API (high-level)
- Declining popularity

**Caffe:**
- One of earliest frameworks
- Good cho CNNs
- C++ based
- **Largely obsolete** now

**Theano:**
- Pioneer trong deep learning
- **Discontinued** (2017)
- Legacy influence

**So Sánh:**

| Feature | TensorFlow/Keras | PyTorch | JAX |
|---------|-----------------|---------|-----|
| Ease of learning | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Production | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Research | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Performance | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Community | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Deployment | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Debugging | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

**Recommendation:**
- **Learning:** PyTorch hoặc Keras
- **Production:** TensorFlow/Keras
- **Research:** PyTorch
- **High-performance computing:** JAX
- Ultimately: **Pick one và master it!** Concepts transfer dễ dàng

### Ứng Dụng của Học Sâu (Applications of Deep Learning)

**Computer Vision (Thị Giác Máy Tính):**

**1. Image Classification:**
- Phân loại ảnh vào categories
- **Applications:** Medical diagnosis, quality control, content moderation
- **Architectures:** ResNet, EfficientNet, ViT
- **Datasets:** ImageNet, CIFAR, Places

**2. Object Detection:**
- Phát hiện và localize objects trong ảnh
- **Applications:** Autonomous vehicles, surveillance, retail analytics
- **Methods:**
  - **Two-stage:** R-CNN, Fast R-CNN, Faster R-CNN (accurate, chậm)
  - **One-stage:** YOLO, SSD, RetinaNet (fast, real-time)
- **Advanced:** EfficientDet, DETR (transformer-based)

**3. Semantic Segmentation:**
- Phân loại mỗi pixel (pixel-wise classification)
- **Applications:** Medical imaging, autonomous driving, satellite imagery
- **Architectures:** FCN, U-Net, DeepLab, SegFormer

**4. Instance Segmentation:**
- Segment mỗi object instance riêng biệt
- **Applications:** Cell counting, object manipulation, scene understanding
- **Methods:** Mask R-CNN, YOLACT

**5. Face Recognition:**
- Identify/verify người từ faces
- **Applications:** Security, authentication, photo organization
- **Methods:** FaceNet, DeepFace, ArcFace

**6. Medical Image Analysis:**
- **X-ray, CT, MRI analysis:** Disease detection, tumor segmentation
- **Pathology:** Cancer cell detection
- **Retinal imaging:** Diabetic retinopathy
- **Impact:** Earlier detection, assist doctors, reduce workload

**7. Image Generation:**
- GANs, Diffusion models
- Art, design, data augmentation

**8. Pose Estimation:**
- Detect human pose (joints, keypoints)
- **Applications:** Sports analytics, AR, human-computer interaction

**Natural Language Processing:**

**1. Machine Translation:**
- Translate text giữa languages
- **Methods:** Seq2Seq, Transformer, mT5
- **Applications:** Google Translate, multilingual communication
- **Challenges:** Idioms, context, rare languages

**2. Text Generation:**
- Generate coherent text
- **Models:** GPT-2, GPT-3, GPT-4
- **Applications:**
  - Content creation, storytelling
  - Code generation (Copilot, CodeGen)
  - Dialogue systems (ChatGPT)

**3. Sentiment Analysis:**
- Classify sentiment (positive, negative, neutral)
- **Applications:** Brand monitoring, customer feedback, market research
- **Methods:** BERT, RoBERTa fine-tuned

**4. Question Answering:**
- Answer questions từ context
- **Types:**
  - Extractive (select span từ text)
  - Abstractive (generate answer)
- **Applications:** Customer support, information retrieval
- **Models:** BERT (SQuAD), T5, GPT-3

**5. Named Entity Recognition (NER):**
- Identify entities (person, location, organization, date)
- **Applications:** Information extraction, knowledge graphs
- **Methods:** BiLSTM-CRF, BERT-based

**6. Text Summarization:**
- Create concise summary từ long text
- **Types:** Extractive (select sentences), Abstractive (generate summary)
- **Applications:** News, research papers, documents
- **Models:** BART, T5, Pegasus

**7. Text Classification:**
- Categorize documents
- **Applications:** Spam detection, topic classification, intent detection

**Speech (Âm Thanh):**

**1. Speech Recognition (ASR):**
- Convert speech to text
- **Applications:** Virtual assistants (Siri, Alexa), transcription, accessibility
- **Models:** DeepSpeech, Wav2Vec 2.0, Whisper
- **Challenges:** Accents, background noise, multiple speakers

**2. Text-to-Speech (TTS):**
- Generate natural-sounding speech từ text
- **Applications:** Audiobooks, assistants, accessibility
- **Models:** Tacotron, FastSpeech, VITS
- **Features:** Multi-speaker, emotion control

**3. Voice Cloning:**
- Replicate specific person's voice
- **Applications:** Personalization, dubbing
- **Ethical concerns:** Deepfakes, misuse

**4. Speaker Recognition:**
- Identify speaker từ voice
- **Applications:** Security, forensics

**5. Speech Enhancement:**
- Denoise speech, separate speakers
- **Applications:** Teleconferencing, hearing aids

**Reinforcement Learning:**

**1. Game Playing:**
- **AlphaGo:** Beat world champion in Go
- **AlphaZero:** Master chess, shogi, Go từ scratch
- **OpenAI Five:** Dota 2
- **AlphaStar:** StarCraft II
- **Applications:** Strategy, decision-making

**2. Robotics:**
- **Manipulation:** Grasp, assemble objects
- **Navigation:** Autonomous navigation
- **Locomotion:** Walking, running (Boston Dynamics)
- **Applications:** Manufacturing, warehouse, service robots

**3. Autonomous Vehicles:**
- Self-driving cars
- **Companies:** Tesla, Waymo, Cruise
- **Challenges:** Safety, edge cases, regulations

**4. Resource Management:**
- **Data center cooling:** Google giảm 40% energy
- **Traffic light control**
- **Portfolio management**

**Các Ứng Dụng Khác:**

**1. Drug Discovery:**
- **Molecule generation:** Design new drugs
- **Property prediction:** Toxicity, efficacy
- **Protein folding:** AlphaFold (revolutionized biology)
- **Applications:** Faster drug development, personalized medicine

**2. Recommendation Systems:**
- Suggest products, movies, content
- **Applications:** Netflix, YouTube, Amazon, Spotify
- **Methods:** Collaborative filtering + deep learning, two-tower models
- **Impact:** User engagement, revenue

**3. Time Series Forecasting:**
- **Stock prediction** (với caveats)
- **Weather forecasting**
- **Energy demand**
- **Sales forecasting**
- **Methods:** LSTM, Temporal CNNs, Transformers

**4. Anomaly Detection:**
- Detect unusual patterns
- **Applications:**
  - **Fraud detection:** Credit cards, transactions
  - **Network intrusion detection**
  - **Manufacturing defects**
  - **Health monitoring:** ECG, vital signs
- **Methods:** Autoencoders, one-class classifiers

**5. Generative Design:**
- **Architecture:** Building design
- **Engineering:** Optimize structures
- **Fashion:** Design clothes

**6. Agriculture:**
- **Crop monitoring:** Satellite imagery analysis
- **Disease detection:** Plant diseases
- **Yield prediction**
- **Automated farming:** Tractors, drones

**7. Climate Science:**
- **Climate modeling**
- **Extreme weather prediction**
- **Carbon sequestration**

**8. Art và Creativity:**
- **Music generation:** MuseNet, Jukebox
- **Art creation:** DALL-E, Midjourney, Stable Diffusion
- **Video generation**
- **Style transfer**

**9. Cybersecurity:**
- **Malware detection**
- **Phishing detection**
- **Vulnerability discovery**
- **Automated penetration testing**

**10. Education:**
- **Personalized learning**
- **Automated grading**
- **Intelligent tutoring systems**
- **Content recommendation**

### Hướng Phát Triển Tương Lai (Future Directions)

**1. Efficient Deep Learning:**

Giảm computational cost và memory footprint.

**Model Compression:**
- **Pruning:** Remove unnecessary weights/neurons (structured/unstructured)
- **Quantization:** FP32 → INT8/INT4, giảm size 4-8×
- **Knowledge Distillation:** Student model học từ teacher model
- **Low-rank factorization:** Decompose weight matrices

**Neural Architecture Search (NAS):**
- **Automated model design**
- Search optimal architectures
- **Applications:** Mobile, edge devices
- **Examples:** EfficientNet, MnasNet

**Efficient Architectures:**
- **MobileNets, EfficientNets**
- **TinyML:** Deep learning trên microcontrollers
- **Edge AI:** On-device inference

**2. Few-shot và Zero-shot Learning:**

Learn from very few examples (hoặc không examples).

**Few-shot Learning:**
- Learn từ 1-5 examples per class
- **Methods:** Meta-learning (MAML), prototypical networks, matching networks
- **Applications:** Rare diseases, low-resource languages

**Zero-shot Learning:**
- Classify classes chưa thấy trong training
- **Methods:** Attribute-based, semantic embeddings, CLIP
- **Applications:** Open-world recognition

**Prompt Engineering:**
- Large language models (GPT-3) với clever prompts
- In-context learning

**3. Explainable AI (XAI):**

Make deep learning interpretable và transparent.

**Techniques:**
- **Attention visualization:** Xem model chú ý vào đâu
- **Saliency maps:** Highlight important regions (Grad-CAM, LIME, SHAP)
- **Feature importance**
- **Concept activation vectors**

**Importance:**
- **Trust:** Especially critical domains (medical, legal, finance)
- **Debugging:** Understand failures
- **Regulatory compliance:** EU AI Act
- **Fairness:** Detect biases

**4. Multimodal Learning:**

Kết hợp nhiều modalities (vision, language, audio, etc.).

**Applications:**
- **Vision-Language:** CLIP, DALL-E, Flamingo
  - Image captioning, VQA, text-to-image
- **Audio-Visual:** Lip reading, audiovisual speech recognition
- **Video Understanding:** Action recognition với audio + visual

**Benefits:**
- **Richer representations**
- **Cross-modal transfer**
- **More robust**

**5. Self-supervised Learning:**

Learn powerful representations **without labels**.

**Methods:**
- **Contrastive learning:** SimCLR, MoCo (vision)
- **Masked prediction:** BERT (language), MAE (vision)
- **Rotation prediction, jigsaw puzzles** (vision)

**Benefits:**
- **Leverage unlabeled data** (infinite on internet)
- **Better representations** than supervised trong một số cases
- **Foundation models:** GPT, CLIP trained với self-supervision

**6. Federated Learning:**

Train models **across distributed data** without centralizing.

**Process:**
1. Send model to devices
2. Train locally trên device data
3. Send updates (not data) to server
4. Aggregate updates
5. Repeat

**Benefits:**
- **Privacy-preserving:** Data never leaves devices
- **Scalability:** Leverage edge devices
- **Applications:** Mobile keyboards, health data

**Challenges:**
- Communication efficiency
- Heterogeneous devices/data
- Security (Byzantine attacks)

**7. Continual/Lifelong Learning:**

Learn continuously từ stream of data **without forgetting**.

**Challenge - Catastrophic Forgetting:**
- Training trên new tasks → forget old tasks

**Solutions:**
- **Regularization:** EWC (Elastic Weight Consolidation)
- **Replay:** Store/generate examples từ old tasks
- **Dynamic architectures:** Add capacity cho new tasks

**Applications:**
- **Robotics:** Learn new skills over time
- **Personalization:** Adapt to user over time

**8. Large Language Models (LLMs):**

Scaling up ngày càng lớn (billions to trillions parameters).

**Trends:**
- **Emergent abilities:** New capabilities với scale (reasoning, few-shot)
- **In-context learning:** Learn từ examples trong prompt
- **Instruction following:** ChatGPT, GPT-4

**Future:**
- **Multimodal LLMs:** GPT-4V (vision), Gemini
- **Agents:** LLMs sử dụng tools, plan, act
- **Efficiency:** Smaller models với comparable performance (Mistral, Phi)

**9. Diffusion Models:**

Alternative to GANs cho generation, hiện đang dominate.

**Methods:**
- **DDPM, Score-based models**
- **Stable Diffusion, DALL-E 2, Imagen**

**Advantages over GANs:**
- Stable training
- Higher quality
- Better mode coverage

**Applications:**
- **Text-to-image:** Revolutionary impact trên art/design
- **Image editing**
- **Video generation**
- **3D generation**

**10. AI Safety và Ethics:**

Ensuring AI beneficial và safe.

**Concerns:**
- **Bias và fairness:** Models reflect data biases
- **Robustness:** Adversarial attacks
- **Privacy:** Training data leakage
- **Misuse:** Deepfakes, misinformation
- **Alignment:** Ensure AI goals align với human values
- **Existential risk:** AGI safety

**Research Areas:**
- **Adversarial robustness**
- **Fairness metrics và debiasing**
- **Privacy-preserving ML**
- **AI alignment**
- **Red teaming**

**11. Neuromorphic Computing:**

Hardware inspired by brain.

**Advantages:**
- **Energy efficient**
- **Parallel processing**
- **Event-driven**

**Examples:**
- Intel Loihi
- IBM TrueNorth
- Memristor-based computing

**12. Quantum Machine Learning:**

Leverage quantum computers cho ML.

**Potential:**
- Exponential speedup cho certain tasks
- Quantum neural networks
- Quantum data encoding

**Status:** Very early stage, mostly research

**Kết Luận:**

Deep learning đang rapidly evolving. Future directions focus on:
- **Efficiency:** Less resources
- **Data efficiency:** Learn from less
- **Interpretability:** Understand decisions
- **Generalization:** Broader applicability
- **Safety và ethics:** Responsible AI
- **Human-AI collaboration:** Augment human capabilities

Exciting time trong AI/ML! 🚀

