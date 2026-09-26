"""Smoke test — CI chạy, NTD tin được. Giữ xanh luôn."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent if (Path(__file__).resolve().parent.name == "src") else Path(__file__).resolve().parent
SRC_MAIN = Path(__file__).resolve().parent / "main.py"


def test_no_stub_template():
    txt = SRC_MAIN.read_text(encoding="utf-8") if SRC_MAIN.exists() else ""
    assert "TODO: gắn sponsor API" not in txt, "src/main.py còn stub template"
    assert "[MVP] nhận:" not in txt, "src/main.py còn stub return — thay bằng logic thật"


def test_entrypoint_runs():
    # main có build(): test trực tiếp; factory/bob không có build(): chạy subprocess
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from main import build as _build
        out = _build("smoke input")
        assert isinstance(out, str) and len(out) > 0
        return
    except ImportError:
        pass  # factory pattern (plan/code/evaluate) — chạy main thay vì build()
    p = subprocess.run([sys.executable, str(SRC_MAIN,)], capture_output=True,
                       text=True, timeout=30)
    assert p.returncode == 0, f"src/main.py chạy lỗi: {(p.stderr or p.stdout)[:300]}"
