# Lịch Sử Prompt & Tiến Hoá Mẫu Lệnh (Prompt Logs & Evolution)

Tài liệu ghi chép lại lịch sử phát triển, thử nghiệm và tối ưu hóa các Prompt (Prompt Engineering) cho hệ thống **VietVoice AI (vietvoice-ai.online)** từ giai đoạn khởi tạo đến hiện tại.

---

## 1. Tổng Quan Lịch Sử Prompt Qua Các Giai Đoạn

| Giai đoạn | Mục tiêu Prompt | Thay đổi chính | Kết quả |
|---|---|---|---|
| **Giai đoạn 1 (Baseline)** | Nhận diện thẻ cảm xúc đơn giản | Dùng regex cắt thẻ `(vui)`, `(buồn)` thô sơ | Bị sót thẻ nếu viết hoa/có dấu câu kèm theo |
| **Giai đoạn 2 (Normalization Prompt)** | Chuẩn hóa số, ngày tháng, ký tự đặc biệt | Bổ sung quy tắc Prompt chuẩn hóa chữ số tiếng Việt (`123` -> `một trăm hai mươi ba`) | Giảm 90% lỗi phát âm từ/số |
| **Giai đoạn 3 (Emotion Control Prompt)** | Điều khiển cảm xúc qua viXTTS & OmniVoice | Thiết kế prompt hướng dẫn cho OmniVoice (`instruct="Nói với giọng vui vẻ, hào hứng"`) và mapping thẻ tiếng Việt | Giọng nói truyền cảm, đúng ngữ cảnh |
| **Giai đoạn 4 (Multi-language Prompt)** | Dịch thuật tự động và đa ngôn ngữ | tích hợp Prompt dịch thuật tiếng Anh - Việt chuẩn ngữ cảnh giọng nói | Hỗ trợ 600+ ngôn ngữ với OmniVoice |

---

## 2. Nhật Ký Chi Tiết Prompt Qua Các Phiên Bản

### 2.1. Prompt Phân Tích Cảm Xúc (Emotion Parsing Prompt)

- **Version 1.0 (Regex Baseline)**:
  - Pattern: `\((vui|buồn|tức giận|bình tĩnh)\)`
  - Hạn chế: Không nhận dạng được các cụm từ mở rộng như `(hào hứng)`, `(trầm lắng)`, `(phấn khởi)`.

- **Version 2.0 (Bảng Mapping Cảm Xúc Tiếng Việt)**:
  - Thêm Alias mapping tự động trong `emotion_parser.py`:
    - `cheerful` / `vui`: `"cheerful"`, `"hào hứng"`, `"vui vẻ"`, `"phấn khởi"`
    - `sad` / `buồn`: `"sad"`, `"u uất"`, `"trầm lắng"`, `"xúc động"`
    - `calm` / `bình tĩnh`: `"calm"`, `"nhẹ nhàng"`, `"thư thái"`
    - `excited` / `phấn kích`: `"excited"`, `"sôi nổi"`, `"nhiệt huyết"`

- **Version 3.0 (OmniVoice Instruction Prompting)**:
  - Cấu trúc Prompt gửi đến OmniVoice Model:
    ```text
    instruct: "Speak in a cheerful, energetic Vietnamese voice with expressive emotion."
    text: "Chào mừng bạn đến với VietVoice AI!"
    ```

---

## 3. Mẫu Prompt Tiêu Chuẩn Hiện Tại (Production Prompt Templates)

### Prompt Dịch Thuật & Phân Tích Ý Định (Translation & Intent Prompt)
```json
{
  "system_prompt": "You are a professional Vietnamese voice actor assistant. Your task is to clean, normalize, and format the text for High-Quality Text-to-Speech synthesis.",
  "user_prompt_template": "Text to process: '{input_text}'. Emotion intent: '{emotion}'."
}
```
