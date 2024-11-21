from sqlalchemy import Boolean, Column, Integer, String
from app.db.base_class import Base
from app.models.ride import Ride
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__  = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  full_name = Column(String)
  hashed_password = Column(String)
  is_active = Column(Boolean, default=True)
  user_type = Column(String) #parent or driver type
  parent_rides = relationship("Ride", foreign_keys="[Ride.parent_id]", back_populates="parent")
  driver_rides = relationship("Ride", foreign_keys="[Ride.driver_id]", back_populates="driver")