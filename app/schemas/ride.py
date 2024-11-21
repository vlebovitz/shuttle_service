from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RideBase(BaseModel):
  pickup_time: datetime
  pickup_location: str
  dropoff_location: str
  ride_type: str
  notes: Optional[str] = None
  estimated_duration: Optional[int] = None

class RideCreate(RideBase):
  pass

class RideUpdate(BaseModel):
  status: Optional[str] = None
  driver_id: Optional[int] = None
  notes: Optional[str] = None

class RideInDB(RideBase):
    id: int
    parent_id: int
    driver_id: Optional[int]
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True