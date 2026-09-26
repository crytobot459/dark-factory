"""Dark Factory — Mini Factory demo (Streamlit Cloud entry).
Wrap FACTORY THẬT (plan->code->evaluator), không stub.
Chạy local: pip install -r requirements.txt && python3 -m streamlit run app_streamlit.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

try:
    import streamlit as st
except Exception:
    st = None

from factory import plan, code, evaluate, token_estimate


def factory_report(note=""):
    steps = plan()
    out = code()
    res = evaluate()
    tok = token_estimate()
    n = len(res["passed"]) + len(res["failed"])
    return {
        "note": note or "Mini Factory — spec in, checked code out",
        "plan": " -> ".join(steps),
        "code": f"{out.name} ({out.stat().st_size} bytes)",
        "rate": f"{len(res['passed'])}/{n} passed (rate {res['pass_rate']})",
        "passed": res["passed"],
        "failed": res["failed"],
        "leak": res["leak"],
        "tokens": tok,
    }


def main():
    if st is None:
        r = factory_report()
        print(r["note"], "|", r["plan"], "|", r["rate"])
        return
    st.set_page_config(page_title="Dark Factory — Mini Factory (BAND track)")
    st.title("Dark Factory — Mini Factory (BAND track)")
    st.caption("Planner→coder→evaluator thật + holdout tách biệt. Bấm Run là chạy cả LOOP.")
    note = st.text_input("Ghi chú task (tùy chọn)", value="")
    if st.button("Run factory"):
        with st.spinner("Factory đang chạy plan→code→evaluate..."):
            r = factory_report(note)
        st.subheader(r["note"])
        st.write(f"**Plan:** {r['plan']}")
        st.write(f"**Code:** {r['code']}")
        st.metric("Evaluator pass-rate", r["rate"])
        st.write(f"Holdout leak: **{'CÓ' if r['leak'] else 'không'}** (train/test separation)")
        st.write(f"Token/task: ~{r['tokens']} | Override người: 0")
        with st.expander("Chi tiết từng test"):
            for p in r["passed"]:
                st.success(f"XANH {p}")
            for f in r["failed"]:
                st.error(f"ĐỎ {f}")


if __name__ == "__main__":
    main()
