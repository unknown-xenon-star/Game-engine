# Suggestions for `TODO_TUI.py`, `TODO_CLI.py`, and Related Files

## Scope Reviewed
- `TODO_TUI.py`
- `TODO_CLI.py`
- `task_manager.py`
- `json_handler.py`
- `new_json.py`
- `README.MD`
- `requirements.txt`

## Highest-Value Improvements (Prioritized)

1. **Unify data access behind one storage API (critical)**
- `TODO_TUI.py` writes directly to `tasks.txt` (`TODO_TUI.py:98-100`, `TODO_TUI.py:123-125`) while CLI uses `task_manager.py`.
- This creates duplicated logic and future drift.
- Upgrade: make both CLI and TUI call only `task_manager.py` methods (`add_task`, `remove_task`, `save_tasks`), and never open files directly from UI code.

2. **Fix broken JSON integration path (critical)**
- `task_manager.py` calls `json_handler.JsonManager(FILE_NAME).load_Json()` and `.save_Json()` (`task_manager.py:57`, `task_manager.py:65`), but `json_handler.py` defines `Load_Json` and `Save_Json` (`json_handler.py:109`, `json_handler.py:116`).
- Also, `FILE_NAME` is `tasks.txt`, but JSON manager expects a JSON file.
- Upgrade: standardize method names (`load_json`, `save_json`), and use a real JSON path like `todo.json`.

3. **Repair incorrect `Task` construction in JSON layer (critical)**
- In `json_handler.py`, when passing a dict, `self.task = list(args[0])` (`json_handler.py:19-20`) stores only keys, not task data.
- Upgrade: replace with `self.task = dict(args[0])` and validate required keys.

4. **Fix `JsonData` argument handling bug (high)**
- `isinstance(args, (list, tuple))` in `JsonData.__init__` (`json_handler.py:61`) checks the tuple-of-args, not the first argument.
- Upgrade: use `isinstance(args[0], (list, tuple))`.

5. **Make file writes safe and deterministic (high)**
- Current writes overwrite directly (`task_manager.py:28`, `TODO_TUI.py:98`, `TODO_TUI.py:123`) without atomic strategy.
- Upgrade: write to temp file and `os.replace()`; this avoids partial corruption on interruption.

6. **Fix TUI input lifecycle issues (high)**
- Pressing add/delete repeatedly can mount multiple `Input` widgets.
- `Esc` only cancels `task_input` (`TODO_TUI.py:130-134`), not `delete_input`.
- Upgrade: maintain one active input widget, support Esc cancel for both modes, and clear stale references after removal.

7. **Add input validation parity between CLI and TUI (medium)**
- CLI adds empty tasks (`TODO_CLI.py:26-27`) while TUI blocks empty tasks (`TODO_TUI.py:114-117`).
- Upgrade: shared validator in `task_manager.py` for non-empty/trimmed text.

8. **Improve naming consistency and Python style (medium)**
- Mixed case conventions: `Load_Json`, `Save_Json`, `To_Dict`, `load_Json`.
- Upgrade: switch to snake_case everywhere (`load_json`, `save_json`, `to_dict`) and keep one convention.

9. **Resolve encoding and dependency hygiene issues (medium)**
- `requirements.txt` appears UTF-16/encoded with null bytes (visible garbling), which can break tooling.
- Upgrade: save as UTF-8 and keep only runtime dependencies needed by this project.

10. **Align README with real project state (medium)**
- `README.MD` describes an `engine/`, `tasks/`, `cli/`, `utils/` layout not present in current repository.
- Upgrade: document current files and exact run commands for CLI/TUI.

## Feature Upgrades Worth Implementing Next

1. **Task model expansion**
- Add fields: `id`, `title`, `done`, `created_at`, optional `due_date`, optional `priority`.
- Benefit: enables sorting, filtering, completion tracking.

2. **TUI productivity features**
- Keybindings: mark done, edit task, move task up/down, clear completed.
- Add a focused input/status bar instead of mounting ad-hoc inputs.

3. **CLI command mode**
- Move from menu loop to command-style usage:
- `python TODO_CLI.py add "buy milk"`
- `python TODO_CLI.py list --done/--pending`
- `python TODO_CLI.py done 3`
- Benefit: scriptability and automation.

4. **Storage migration path**
- Migrate from `tasks.txt` to `todo.json` while preserving existing data.
- On first run: import text tasks, assign IDs, persist JSON.

5. **Testing baseline**
- Add tests for `task_manager` and JSON manager:
- load/save roundtrip
- add/remove bounds
- invalid input
- empty/corrupt file handling

## Suggested Implementation Order

1. Standardize storage API and method names.
2. Fix JSON object/model bugs.
3. Refactor TUI and CLI to use shared task-manager API only.
4. Add atomic writes + validation.
5. Add tests.
6. Add new features (done/due/priority/filter/sort).

## Quick Wins (Can Be Done Immediately)

1. Fix typo and UX text issues:
- `"Please Enter a Valis Number."` -> `"Please enter a valid number."` (`TODO_CLI.py:38`)
- `"task's Found"` -> `"tasks found"` (`TODO_TUI.py:27`)

2. Remove unused imports:
- `save_tasks` in `TODO_CLI.py` is imported but unused.

3. Use `task_manager.save_tasks()` in TUI instead of direct `open("tasks.txt", "w")`.

4. Handle both `task_input` and `delete_input` in Esc key handler.

5. Normalize naming to snake_case in new code, even before full refactor.
