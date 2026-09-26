# WeAreDevelopers x BAND present: Dark Factory (hackathon edition)

![demo](https://img.shields.io/badge/demo-live-brightgreen) ![ci](https://img.shields.io/badge/ci-pytest-blue) ![license](https://img.shields.io/badge/license-MIT-green)

Event: https://lablab.ai/ai-hackathons/wearedevelopers-hackathon | Stack: band | Demo: (chưa deploy — xem DEPLOY_HF.md) | Video: (chưa quay — điền YouTube unlisted sau)

> 1 dòng: app làm gì + cho ai + đo được gì (điền sau khi chốt CONCEPT).

## Demo

- Live: (chưa deploy — xem DEPLOY_HF.md) (judge/NTD mở là dùng được, không setup)
- Video 2 phút: (chưa quay — điền YouTube unlisted sau)

## Chạy (5 phút, không hỏi thêm)

```bash
python3 src/main.py "input thử của bạn"
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python3 -m pytest src/ -q
```

## Architecture

```
input -> src/main.py:build() [sponsor band load-bearing] -> output
                                          |-> app.py (Gradio HF Spaces)
                                          |-> src/test_smoke.py (pytest)
```

- `src/main.py` — core tái dùng (mang sang job/freelance được, không lẫn code thi)
- `app.py` — demo entry (Gradio), wrap `build()`
- `SPEC.md` (nếu có) — interfaces versioned cho agent khác build tiếp

## Results (pocketful track, chạy lại được bằng `python3 src/main.py`)

- Before: code ví viết tay ~2h + review diff thủ công -> After: factory spec→checked code ~1 phút + evaluator tự chấm
- Evaluator: 5/5 passed (rate 1.0) | Token/task: ~609 | Override: 0 (chưa review tay)
- Invariants chứng minh: conservation (deposit 100+50=150), transfer giữ tổng, double-spend raise, âm raise, balance mới = 0

## Cần key gì (nếu có)

- Liệt kê key sponsor ở đây + link lấy key free.
- Không commit key thật. Dùng biến môi trường (xem `.gitignore`).

## Cấu trúc (root đẩy GitHub, docs thi vào docs/lablab/)

- `src/main.py` — MVP entrypoint
- `src/test_smoke.py` — smoke test (CI chạy)
- `app.py`, `requirements.txt`, `Dockerfile` — deploy HF Spaces
- `docs/lablab/` — BRIEF/CONCEPT/JUDGE_REPORT/DEMO_SCRIPT/PITCH_SCRIPT/DECK (nộp giải, không nhiễu NTD)
- `DEMO_SCRIPT.md` — kịch bản quay 2 phút (bản thi, sẽ move vào docs/lablab khi export)
