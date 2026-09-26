# BAND_EVIDENCE — Dark Factory pocketful (room thật, agents thật)

Room: `4ec606f4-95fa-4c55-8480-02975cfbfd6b` — "Dark Factory wallet ledger"
Xem: https://app.band.ai (login) → chats → room trên.

## Participants (4)
- crytobot459 (User/human — owner, approve gate)
- crytobot459/factory-architect-df (planner)
- crytobot459/factory-coder-df (implementer)
- crytobot459/factory-tester-df (independent evaluator)

## LOOP đã chạy thật (26/9, fetch live từ API)
1. Human brief → cả 3 agents (msg `f2bcfe46`, recipients đủ 3).
2. Coder: "Task 1 DONE — out/mini_ledger.py implements all 6 SPEC signatures".
3. Tester độc lập: "5/5 passed, rate 1.0... will trigger re-test if coder updates".
4. Architect confirm tester. Tester ack + "Confirming wait for human approval".
5. Human APPROVE (msg `0a1eb8f0`): "5/5 holdout green, no leak. Ship it."
- 20+ messages trong room gồm text + tool_call/tool_result/task events
  (`band_send_message` + `band_send_event` — read-back được qua API).

## Vì sao load-bearing (gỡ BAND ra là chết)
- Không có room = không có handoff, không veto, không approve gate.
- Evaluator độc lập + holdout coder không đọc (train/test separation).
- Số đo: 5/5 holdout, ~609 tokens/task, override người 0.

## Secrets
UUID/key 3 agents nằm trong `band-agents/agent_config.yaml` (gitignore, KHÔNG commit).
