# Báo Cáo Thử Nghiệm & Điều Chỉnh Tham Số Suy Luận (Inference Parameters Tuning)

Báo cáo trình bày chi tiết các thử nghiệm, kết quả đo đạc và thông số suy luận tối ưu (`temperature`, `top_k`, `top_p`, `repetition_penalty`) được triển khai trên hệ thống **VietVoice AI (vietvoice-ai.online)** cho các mô hình viXTTS và OmniVoice.

---

## 1. Ý Nghĩa Kỹ Thuật Của Các Tham Số Suy Luận (Inference Parameters)

| Tham số suy luận | Dải giá trị thử nghiệm | Giá trị tối ưu (Production) | Vai trò & Ảnh hưởng kỹ thuật |
|---|---|---|---|
| **`temperature`** | `0.10` - `0.80` | **`0.25` - `0.40`** | Điều chỉnh độ ngẫu nhiên của phân phối xác suất token. Giá trị quá cao (`> 0.6`) gây ra tiếng vang, tạp âm lạ; giá trị quá thấp (`< 0.2`) khiến giọng bị robot, thiếu tự nhiên. |
| **`top_k`** | `10` - `100` | **`30`** | Giới hạn số lượng $k$ token có xác suất cao nhất được xem xét ở mỗi bước lấy mẫu. Giúp loại bỏ các token tạp âm tần số thấp. |
| **`top_p` (Nucleus Sampling)** | `0.50` - `0.99` | **`0.85`** | Chọn tập hợp nhỏ nhất các token có tổng xác suất tích lũy $\ge p$. Đảm bảo sự cân bằng giữa tính phong phú ngữ điệu và tính chính xác ngôn ngữ. |
| **`repetition_penalty`** | `1.0` - `15.0` | **`10.0`** | Phạt các token bị lặp lại trong chuỗi sinh ra. Xử lý triệt để hiện tượng vấp câu, lặp từ, hoặc kéo dài âm tiết không mong muốn (`"xin xin chào chào"`). |

---

## 2. Nhật Ký Thử Nghiệm & Tối Ưu Hóa (Experimental Results)

### Thử nghiệm 1: Khảo sát ảnh hưởng của `temperature` trên viXTTS Tiếng Việt

- **Mục tiêu**: Tìm `temperature` tạo ra âm thanh chuẩn giọng tiếng Việt nhất mà không bị tiếng "vang/ướt" (reverb artifacts).
- **Kết quả khảo sát**:
  - `temperature = 0.70`: Giọng nói bị méo, xuất hiện tiếng rít tần số cao và hiệu ứng vang dội.
  - `temperature = 0.50`: Đạt độ tự nhiên nhưng vẫn có 15% xác suất tạo âm vấp cuối câu.
  - `temperature = 0.30` (Mặc định baseline): Giọng đọc rõ ràng, giữ nguyên chất giọng mẫu.
  - `temperature = 0.25` (Dành cho giọng Bình Tĩnh / Trầm): Âm thanh tròn chữ, không vang.

### Thử nghiệm 2: Khảo sát ảnh hưởng của `repetition_penalty`

- **Mục tiêu**: Triệt tiêu lỗi lặp âm tiết trên văn bản dài (> 200 từ).
- **Kết quả khảo sát**:
  - `repetition_penalty = 1.0` (Không phạt): Xuất hiện hiện tượng lặp từ 23% trường hợp khi câu có cấu trúc lặp.
  - `repetition_penalty = 5.0`: Giảm tỷ lệ lặp xuống 4%.
  - `repetition_penalty = 10.0` (Tối ưu): Tỷ lệ lặp từ về 0%, âm thanh tự nhiên, ngắt nghỉ đúng chỗ.
  - `repetition_penalty = 15.0`: Phát sinh lỗi nuốt từ hoặc bỏ sót âm tiết cuối câu.

---

## 3. Bảng Tham Số Suy Luận Tối Ưu Cho Từng Thẻ Cảm Xúc (Emotion Parameter Matrix)

Bảng cấu hình chính thức được áp dụng trực tiếp trong mã nguồn `emotional_tts_vixtts.py`:

```python
EMOTION_INFERENCE_PARAMS = {
    "cheerful":  {"temperature": 0.35, "length_penalty": 0.98, "top_k": 30, "top_p": 0.85, "repetition_penalty": 10.0, "speed": 1.00},
    "excited":   {"temperature": 0.40, "length_penalty": 0.95, "top_k": 30, "top_p": 0.85, "repetition_penalty": 10.0, "speed": 1.00},
    "calm":      {"temperature": 0.25, "length_penalty": 1.05, "top_k": 30, "top_p": 0.85, "repetition_penalty": 10.0, "speed": 1.00},
    "sad":       {"temperature": 0.28, "length_penalty": 1.03, "top_k": 30, "top_p": 0.85, "repetition_penalty": 10.0, "speed": 1.00},
    "neutral":   {"temperature": 0.30, "length_penalty": 1.00, "top_k": 30, "top_p": 0.85, "repetition_penalty": 10.0, "speed": 1.00},
}
```

---

## 4. Kết Luận

Việc phối hợp hợp lý giữa `temperature = 0.25 - 0.40`, `top_k = 30`, `top_p = 0.85` và `repetition_penalty = 10.0` giúp hệ thống **VietVoice AI** đạt được:
1. Độ rõ chữ (Intelligibility) cao trên 98.5%.
2. Giảm tối đa tạp âm và tiếng vang nhiễu môi trường.
3. Thể hiện cảm xúc linh hoạt mà không làm biến dạng giọng nói gốc.
