from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

DATA_PATH = Path(__file__).resolve().parent.parent / "DB" / "activities.json"


def _ensure_data_file() -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_PATH.exists():
        sample = [
            {"id": 1, "duration": 30, "type": "Running", "count_per_week": 3},
            {"id": 2, "duration": 45, "type": "Cycling", "count_per_week": 2},
            {"id": 3, "duration": 20, "type": "Push-ups", "count_per_week": 4},
            {"id": 4, "duration": 60, "type": "Yoga", "count_per_week": 1},
        ]
        DATA_PATH.write_text(json.dumps(sample, indent=2), encoding="utf-8")


def _load() -> List[Dict[str, Any]]:
    _ensure_data_file()
    try:
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save(items: List[Dict[str, Any]]) -> None:
    DATA_PATH.write_text(json.dumps(items, indent=2), encoding="utf-8")


def get_all() -> List[Dict[str, Any]]:
    return _load()


def get_by_id(item_id: int) -> Optional[Dict[str, Any]]:
    for it in _load():
        if int(it.get("id")) == int(item_id):
            return it
    return None


def add_activity(data: Dict[str, Any]) -> Dict[str, Any]:
    items = _load()
    next_id = (max((it.get("id") or 0) for it in items) + 1) if items else 1
    item = {
        "id": int(next_id),
        "duration": int(data.get("duration", 0)),
        "type": str(data.get("type", "")),
        "count_per_week": int(data.get("count_per_week", 0)),
    }
    items.append(item)
    _save(items)
    return item


def update_activity(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    items = _load()
    for i, it in enumerate(items):
        if int(it.get("id")) == int(item_id):
            it["duration"] = int(data.get("duration", it.get("duration", 0)))
            it["type"] = str(data.get("type", it.get("type", "")))
            it["count_per_week"] = int(data.get("count_per_week", it.get("count_per_week", 0)))
            items[i] = it
            _save(items)
            return it
    return None


def delete_activity(item_id: int) -> bool:
    items = _load()
    new = [it for it in items if int(it.get("id")) != int(item_id)]
    if len(new) == len(items):
        return False
    _save(new)
    return True
