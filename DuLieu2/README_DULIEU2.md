# Thư Mục `DuLieu2`: Lịch Sử Prompt & Kiến Trúc Tiến Hoá

Thư mục **`DuLieu2`** tổng hợp toàn bộ các báo cáo, tài liệu kỹ thuật, lịch sử prompt và bảng thực nghiệm tham số suy luận theo đúng yêu cầu đề bài.

---

## 📁 Cấu Trúc Thư Mục `DuLieu2`

```
DuLieu2/
├── 1_LichSu_Prompt_Logs/               # Nhật ký Prompt & Tiến hoá mẫu lệnh
│   ├── PROMPT_LOGS_EVOLUTION.md        # Báo cáo lịch sử prompt engineering qua 4 giai đoạn
│   └── prompt_templates.json           # Cấu trúc JSON lưu trữ mẫu prompt theo phiên bản
│
├── 2_KienTruc_TienHoa_Pipeline/        # Nhật ký các phiên bản pipeline qua từng giai đoạn
│   ├── PIPELINE_ARCHITECTURE_EVOLUTION.md  # Sơ đồ & phân tích tiến hóa kiến trúc hệ thống
│   └── pipeline_changelog.md           # Log lịch sử thay đổi phiên bản từ v1.0 đến v2.5
│
├── 3_NhatKy_ThamSo_SuyLuan/            # Thử nghiệm & điều chỉnh các tham số suy luận
│   ├── INFERENCE_PARAMETERS_EXPERIMENTS.md # Báo cáo chi tiết thử nghiệm: temperature, top_k, top_p, repetition_penalty
│   ├── inference_config_benchmarks.json    # Bảng tham số tối ưu cho từng cảm xúc (JSON)
│   └── test_inference_params.py        # Script Python kiểm tra & benchmark tham số
│
└── README_DULIEU2.md                   # Tài liệu tổng quan thư mục DuLieu2
```

---

## 📌 Tóm Tắt Tệp Yêu Cầu

1. **Prompt Logs**: Lưu giữ tại `1_LichSu_Prompt_Logs/PROMPT_LOGS_EVOLUTION.md`.
2. **Kiến Trúc Tiến Hóa Pipeline**: Lưu giữ tại `2_KienTruc_TienHoa_Pipeline/PIPELINE_ARCHITECTURE_EVOLUTION.md`.
3. **Tham Số Suy Luận (`temperature`, `top_k`, `top_p`, `repetition_penalty`)**: Lưu giữ chi tiết tại `3_NhatKy_ThamSo_SuyLuan/INFERENCE_PARAMETERS_EXPERIMENTS.md`.
