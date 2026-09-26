# CONCEPT chốt — Dark Factory (spec → checked code, đo được)

**Tên:** Mini Factory — 1 spec văn bản ra 1 module todo chạy được, evaluator chấm holdout coder không được đọc.
**Elevator (10s):** Viết spec 1 trang, factory tự plan-code-tự chấm, ra code merge được kèm số pass-rate.

## Vì sao thắng (4/4)
- [x] Core loop 24h: `python3 src/main.py` đã chạy end-to-end tối nay (planner→coder→evaluator, 5 holdout).
- [x] Niche: solo/team nhỏ cần ship CRUD/tool mà không đọc diff — factory làm + tự chấm.
- [x] ≤3 màn hình: spec → terminal chạy factory → báo số + code sinh ra.
- [x] Sponsor load-bearing: gỡ BAND/evaluator ra là còn code không ai chấm — demo chết. Triển khai thật trên BAND Desktop ở bước tiếp (giữ kiến trúc tách evaluator).

## Số phải báo (evaluator in ra)
- Pass-rate holdout (n=5), override-rate người vs evaluator, token/task ước lượng.
- 1 run end-to-end trên camera: spec → plan → code → self-check → merge.

## Không làm
- Không UI app màu mè (judge chấm LOOP, không chấm UI).
- Coder không được import/read `holdout.json` (train/test separation — check bằng grep trong submit).
