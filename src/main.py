#!/usr/bin/env python3
"""Mini Factory demo runner — 1 lệnh ra số cho video.
Chạy từ build/wearedevelopers-hackathon/: python3 src/main.py
Quay: SPEC.md -> terminal chạy lệnh này -> số pass-rate + file out/mini_ledger.py.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from factory import plan, code, evaluate, token_estimate


def main():
    steps = plan()
    out = code()
    res = evaluate()
    tok = token_estimate()
    n = len(res["passed"]) + len(res["failed"])
    print("== Mini Factory — spec in, checked code out ==")
    print(f"Plan: {' -> '.join(steps)}")
    print(f"Code: {out.name} ({out.stat().st_size} bytes)")
    print(f"Evaluator: {len(res['passed'])}/{n} passed (rate {res['pass_rate']})")
    for p in res["passed"]:
        print(f"  [XANH] {p}")
    for f in res["failed"]:
        print(f"  [ĐỎ] {f}")
    print(f"Leak holdout vào code sinh ra: {'CÓ (FAIL kiến trúc)' if res['leak'] else 'không (giữ train/test separation)'}")
    print(f"Token/task ước lượng: ~{tok} tokens | Override người vs evaluator: 0 (chưa review tay — điền sau 1 lần review)")
    print("Tiếp theo trên BAND Desktop: nối planner→coder→evaluator thật, giữ holdout riêng, quay LOOP.")


if __name__ == "__main__":
    main()
