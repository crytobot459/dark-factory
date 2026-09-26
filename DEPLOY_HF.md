# Deploy HF Spaces — WeAreDevelopers x BAND present: Dark Factory (hackathon edition)

1. Tạo Space: https://huggingface.co/new-space -> SDK Gradio, Public.
2. Upload: `app.py`, `requirements.txt`, `Dockerfile`, `src/main.py`.
3. Chờ build -> copy public URL vào `config/events.yaml: demo_url:` + README.
4. Verify: stranger mở URL, nhập `solana,dev,agent` + min 300 -> ra shortlist.
5. Quay video mở URL thật (không quay localhost).

Check: `python3 agent/submit.py wearedevelopers-hackathon --check --live-check <hf-url>`
