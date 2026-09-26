# AGENTS.md — context ổn định cho mọi agent vào repo

## Build
- `python3 src/main.py` — chạy factory end-to-end (plan→code→evaluate), in số.
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python3 -m pytest src/ -q` — chạy test (nếu có).

## Conventions
- Coder chỉ đọc `SPEC.md` + file này. Cấm đọc `src/holdout.json` (evaluator giữ riêng).
- Code sinh ra ghi vào `out/mini_ledger.py` (không ghi đè src/).
- Mọi số báo cáo (pass-rate, override, token) phải chạy lại được bằng 1 lệnh trên.

## Architecture
- `src/factory.py`: `plan()` đọc SPEC → steps; `code()` sinh module từ template theo SPEC; `evaluate()` import module sinh ra + chạy holdout.
- Train/test separation: `code()` không import holdout; `evaluate()` là agent tách biệt.
