# SPEC — mini_todo (versioned, coder chỉ đọc file này + AGENTS.md)

## Goal
Sinh module `mini_todo` quản lý việc cần làm trong bộ nhớ, đủ để demo factory end-to-end.

## Interfaces (bắt buộc, tên hàm + chữ ký)
- `add(title: str) -> dict` — thêm việc, trả `{id:int, title:str, done:bool}`. Title rỗng phải raise ValueError.
- `list_all() -> list[dict]` — trả tất cả theo thứ tự thêm.
- `done(todo_id: int) -> dict` — đánh dấu xong, id sai raise KeyError.
- `clear() -> None` — dùng để reset giữa các test evaluator.

## Constraints
- Stdlib only, không mạng, không file ngoài bộ nhớ.
- Id tăng dần từ 1, không tái dùng id đã xóa (ở đây không có xóa).
- Không đọc `holdout.json` trong code sinh ra (evaluator kiểm tra bằng grep).

## Non-goals
- Không persistence, không auth, không UI web. Chỉ module + hàm đúng spec.
