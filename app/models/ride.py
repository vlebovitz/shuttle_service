from sqlalchemy import Column, Integer, String,DateTime, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
import enum
from app.db.base_class import Base
from datetime import datetime, timezone

class RideStatus(str, enum.Enum):
  SCHEDULED = "scheduled"
  CONFIRMED = "confirmed"
  IN_PROGRESS = "in_progress"
  COMPLETED = "completed"
  CANCELLED = "cancelled"

#setup recurring scheduled ride to optimize pickups
class RideType(str, enum.Enum):
  ONE_TIME = "one_time"
  RECURRING = "recurring"

class Ride(Base):
  id = Column(Integer, primary_key=True, index=True)
    
  # Scheduling info
  pickup_time = Column(DateTime, nullable=False)
  pickup_location = Column(String, nullable=False)
  dropoff_location = Column(String, nullable=False)
  
  # Type and status
  ride_type = Column(String, nullable=False, default=RideType.ONE_TIME)
  status = Column(String, nullable=False, default=RideStatus.SCHEDULED)
  
  # Relations
  parent_id = Column(Integer, ForeignKey("user.id"), nullable=False)
  driver_id = Column(Integer, ForeignKey("user.id"), nullable=True)  # Nullable as driver might be assigned later
  
  # Optional fields
  notes = Column(String, nullable=True)
  estimated_duration = Column(Integer, nullable=True)  # in minutes
  
  # Tracking
  created_at = Column(DateTime, default=datetime.now(timezone.utc))
  updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
  
  # Relationships
  parent = relationship("User", foreign_keys=[parent_id], back_populates="parent_rides")
  driver = relationship("User", foreign_keys=[driver_id], back_populates="driver_rides")
