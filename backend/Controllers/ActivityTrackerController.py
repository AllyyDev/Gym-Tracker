from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from ..Services import ActivityTracker as service

router = APIRouter()


class ActivityIn(BaseModel):
	duration: int
	type: str
	count_per_week: int


class ActivityOut(ActivityIn):
	id: int


@router.get("/activities", response_model=List[ActivityOut])
def list_activities():
	return service.get_all()


@router.get("/activities/{activity_id}", response_model=ActivityOut)
def get_activity(activity_id: int):
	it = service.get_by_id(activity_id)
	if not it:
		raise HTTPException(status_code=404, detail="Activity not found")
	return it


@router.post("/activities", response_model=ActivityOut)
def create_activity(payload: ActivityIn):
	item = service.add_activity(payload.dict())
	return item


@router.put("/activities/{activity_id}", response_model=ActivityOut)
def update_activity(activity_id: int, payload: ActivityIn):
	it = service.update_activity(activity_id, payload.dict())
	if not it:
		raise HTTPException(status_code=404, detail="Activity not found")
	return it


@router.delete("/activities/{activity_id}")
def delete_activity(activity_id: int):
	ok = service.delete_activity(activity_id)
	if not ok:
		raise HTTPException(status_code=404, detail="Activity not found")
	return {"deleted": True}

