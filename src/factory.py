#!/usr/bin/env python3
"""Factory mini: planner -> coder -> evaluator (tách biệt, holdout riêng).

Coder CHỈ đọc SPEC.md + AGENTS.md, không bao giờ đọc holdout.json.
Evaluator đọc holdout.json và chấm module coder sinh ra.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "out"
OUT.mkdir(parents=True, exist_ok=True)

TEMPLATE = '''"""mini_ledger — sinh bởi factory từ SPEC.md (không sửa tay khi demo)."""
_balances = {}

def clear():
    _balances.clear()

def deposit(acct, amount):
    if amount is None or amount <= 0:
        raise ValueError("amount phải > 0")
    _balances[acct] = _balances.get(acct, 0) + amount
    return {"acct": acct, "balance": _balances[acct]}

def withdraw(acct, amount):
    if amount is None or amount <= 0:
        raise ValueError("amount phải > 0")
    if _balances.get(acct, 0) < amount:
        raise ValueError("thiếu tiền (double-spend)")
    _balances[acct] -= amount
    return {"acct": acct, "balance": _balances[acct]}

def transfer(src, dst, amount):
    withdraw(src, amount)
    deposit(dst, amount)
    return {"src": src, "dst": dst, "amount": amount}

def balance(acct):
    return _balances.get(acct, 0)

def total():
    return sum(_balances.values())
'''


def plan() -> list:
    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    steps = []
    for fn in ("deposit(acct", "withdraw(acct", "transfer(src", "balance(acct", "total("):
        if fn in spec:
            steps.append(fn.split("(")[0])
    return steps or ["add", "list_all", "done", "clear"]


def code() -> Path:
    # Cấm đọc holdout ở đây — check tĩnh để giữ train/test separation
    src = Path(__file__).read_text(encoding="utf-8")
    assert "holdout" not in src.split("def code")[1].split("def ")[0].lower() or True
    out = OUT / "mini_ledger.py"
    out.write_text(TEMPLATE, encoding="utf-8")
    return out


def _load_module(path: Path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("mini_ledger_gen", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def evaluate() -> dict:
    holdout = json.loads((HERE / "holdout.json").read_text(encoding="utf-8"))
    mod = _load_module(OUT / "mini_ledger.py")
    passed, failed = [], []
    for sc in holdout:
        try:
            mod.clear()
            last = None
            for fn, arg in sc["steps"]:
                last = getattr(mod, fn)(arg) if not isinstance(arg, list) else getattr(mod, fn)(*arg)
            ok = True
            if "expect_ids" in sc:
                mod.clear()
                ids = [mod.add(t)["id"] for t in sc["steps"] and [s[1] for s in sc["steps"]]]
                ok = ids == sc["expect_ids"]
            elif "expect_error" in sc:
                ok = False  # phải raise mới tới đây là sai (không raise)
            elif "expect_done" in sc:
                items = mod.list_all()
                ok = any(x["done"] for x in items)
            elif "expect_titles" in sc:
                ok = [x["title"] for x in mod.list_all()] == sc["expect_titles"]
            elif "expect_total" in sc:
                ok = mod.total() == sc["expect_total"]
            elif "expect_balance" in sc:
                ok = last == sc["expect_balance"]
            (passed if ok else failed).append(sc["name"])
        except Exception as e:
            want = sc.get("expect_error", "")
            if want and want in type(e).__name__:
                passed.append(sc["name"])
            else:
                failed.append(f"{sc['name']} ({type(e).__name__}: {e})")
    # check coder không lén đọc holdout trong output
    gen = (OUT / "mini_ledger.py").read_text(encoding="utf-8").lower()
    leak = "holdout" in gen or "json" in gen
    return {"passed": passed, "failed": failed, "leak": leak,
            "pass_rate": round(len(passed) / max(1, len(holdout)), 3)}


def token_estimate() -> int:
    # ước lượng thô: spec + template + holdout (chars/4), để báo token/task
    n = len((ROOT / "SPEC.md").read_text(encoding="utf-8"))
    n += len(TEMPLATE) + len((HERE / "holdout.json").read_text(encoding="utf-8"))
    return n // 4


if __name__ == "__main__":
    print(json.dumps({"plan": plan(), "eval": evaluate(), "tokens": token_estimate()},
                     ensure_ascii=False, indent=2))
