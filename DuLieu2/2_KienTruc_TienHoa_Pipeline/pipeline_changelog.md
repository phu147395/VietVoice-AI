# Nhật Ký Thay Đổi Cấu Trúc Pipeline (Pipeline Changelog)

## [v2.5.0] - 2026-09-15
### Added
- Tích hợp **OmniVoice Multi-lingual Engine** hỗ trợ 600+ ngôn ngữ qua `OmniVoiceDaemonClient`.
- Cơ chế quản lý bộ nhớ VRAM tự động (`_release_cuda_cache`), tự động giải phóng RAM/VRAM giữa các chunk.
- Tự động fallback từ GPU sang CPU khi phát hiện sự cố CUDA OOM (Out of Memory).

### Fixed
- Lỗi xung đột dependency giữa `transformers==4.44` (viXTTS) và `transformers>=5.3` (OmniVoice).
- Lỗi đứt đoạn âm thanh khi ghép nhiều chunk (sử dụng `_trim_wav_edges` và `_truncate_reverb_tail`).

## [v2.0.0] - 2026-06-20
### Added
- Module RVC Voice Conversion (`rvc_wrapper.py`, `rvc_trainer.py`).
- Emotion Control tự động dựa trên thẻ văn bản `parse_split_by_emotion`.

## [v1.5.0] - 2026-03-10
### Added
- Engine chuẩn hóa văn bản tiếng Việt nâng cao `VietnameseTTSNormalizer`.
- Xử lý biểu thức toán học `math_symbol_normalizer.py`.

## [v1.0.0] - 2026-01-05
### Added
- Phiên bản thử nghiệm viXTTS baseline đơn lẻ cho tiếng Việt.
