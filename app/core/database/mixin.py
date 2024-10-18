from datetime import datetime

from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TrackTimeMixin:

    def __init__(self):
        self.deleted_at = None

    created_at = Column(DateTime, default=func.now())

    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    delete_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()