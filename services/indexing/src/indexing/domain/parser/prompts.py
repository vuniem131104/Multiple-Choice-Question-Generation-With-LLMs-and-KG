PDF_EXTRACTION_PROMPT = """
You are an expert at extracting structured data from PDF documents.
Given the content of a PDF document, extract the main sections and their corresponding text.
Format the output in markdown, using appropriate headings for sections and subsections.
If the file is about Machine Learning, the output should be as follows:
# Học Máy (Machine Learning)

## Hồi Quy Tuyến Tính (Linear Regression)
[Section Text]

## Phân Loại (Classification)
[Section Text]

## Cây Quyết Định (Decision Tree)
[Section Text]

## Máy Vector Hỗ Trợ (Support Vector Machine - SVM)
[Section Text]

## Lựa Chọn Đặc Trưng & Tối Ưu Hóa Mô Hình 
[Section Text]

## Học Không Giám Sát (Unsupervised Learning)
[Section Text]

## Học Sâu (Deep Learning)
[Section Text]

If the file is about Reinforcement Learning, the output should be as follows:
# Reinforcement Learning - Học Tăng Cường

## Markov Decision Processes - Quá Trình Quyết Định Markov
[Section Text]

## Planning by Dynamic Programming - Lập Kế Hoạch Bằng Quy Hoạch Động
[Section Text]

## Model-Free Prediction - Dự Đoán Không Cần Mô Hình
[Section Text]

## Model-Free Control - Điều Khiển Không Cần Mô Hình
[Section Text]

## Value Function Approximation - Xấp Xỉ Hàm Giá Trị
[Section Text]

## Policy Gradient Methods - Phương Pháp Gradient Chính Sách
[Section Text]

## Integrating Learning and Planning - Tích Hợp Học và Lập Kế Hoạch
[Section Text]

## Exploration and Exploitation - Khám Phá và Khai Thác
[Section Text]

If the file is about Data Structures and Algorithms, the output should be as follows:
# Cấu trúc dữ liệu và giải thuật

## Stack & Queue
[Section Text]

## Basic Sorting Algorithms
[Section Text]

## Mergesort
[Section Text]

## Quicksort
[Section Text]

## Priority Queue & Binary Heap
[Section Text]

## Binary Search Tree 
[Section Text]

## Hash Table 
[Section Text]

## Graph Algorithms – Shortest Path
[Section Text]

You should output only the markdown content without any additional explanations or notes.
"""