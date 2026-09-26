# Deploy Streamlit Cloud — Dark Factory (free, không thẻ)

Streamlit Community Cloud free thật: 1 app public, deploy từ GitHub repo.

## Bạn làm (10 phút)

1. Tạo repo GitHub mới (public), vd `dark-factory`: https://github.com/new
2. Push code export (tôi đưa lệnh ở dưới — chạy trong `/tmp/dark-factory`):
   ```bash
   git remote add origin https://github.com/<user>/dark-factory.git
   git branch -M main && git push -u origin main
   ```
3. Mở https://share.streamlit.io → **New app** → chọn repo/branch/`app_streamlit.py` → **Deploy**.
4. Chờ build → copy URL dạng `https://<app>.streamlit.app`.
5. Verify cửa sổ ẩn danh: bấm **Run factory** → ra **5/5 passed, Holdout leak: không**.

## Sau có URL

- Điền vào `config/events.yaml` → `wearedevelopers-hackathon.demo_url`, nhắn agent verify:
  `python3 agent/judge.py wearedevelopers-hackathon --live-check <url>`
  `python3 agent/submit.py wearedevelopers-hackathon --check --live-check <url>`
- Quay video mở URL thật (không quay localhost).

Ghi chú: `app.py` (Gradio/HF) giữ lại làm backup — HF đòi billing (402) nên demo chính là Streamlit.
