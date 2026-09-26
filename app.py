#!/usr/bin/env python3
"""app.py — HuggingFace Spaces entry (Gradio) cho wearedevelopers-hackathon [band].
Wrap FACTORY THẬT (plan->code->evaluate), không stub.
Deploy: tạo Space (Gradio SDK) -> upload app.py + src/ + requirements.txt.
Local chạy: pip install -r requirements.txt && python3 app.py
Judge mở URL là dùng được, không setup.
"""
try:
    import gradio as gr
except Exception:
    gr = None

import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))


def run_factory(note=""):
    """Chạy factory end-to-end, trả báo cáo text cho judge đọc."""
    try:
        from factory import plan, code, evaluate, token_estimate
    except Exception as e:
        return f"Lỗi import factory: {e}"
    try:
        buf = io.StringIO()
        with redirect_stdout(buf):
            steps = plan()
            out = code()
            res = evaluate()
            tok = token_estimate()
        n = len(res["passed"]) + len(res["failed"])
        L = [f"Ghi chú: {note}" if note else "Mini Factory — spec in, checked code out",
             f"Plan: {' -> '.join(steps)}",
             f"Code: {out.name} ({out.stat().st_size} bytes)",
             f"Evaluator: {len(res['passed'])}/{n} passed (rate {res['pass_rate']})",
             f"Holdout leak: {'CÓ' if res['leak'] else 'không'} (train/test separation)",
             f"Token/task: ~{tok} | Override người: 0",
             "",
             "--- log chi tiết ---",
             buf.getvalue()]
        return "\n".join(L)
    except Exception as e:
        return f"Lỗi chạy factory: {e}"


def run(prompt):
    return run_factory(prompt or "")


if __name__ == "__main__":
    if gr is None:
        print("Chưa có gradio — pip install -r requirements.txt")
        print(run(""))
    else:
        demo = gr.Interface(
            fn=run,
            inputs=gr.Textbox(value="", label="ghi chú task (tùy chọn)"),
            outputs=gr.Textbox(label="factory report"),
            title="Dark Factory — Mini Factory (BAND track)",
            description="Planner→coder→evaluator thật + holdout tách biệt. Bấm Submit là chạy cả LOOP, đọc pass-rate.",
        )
        demo.launch()
