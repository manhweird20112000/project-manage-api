from app.models import User
from app.core.database.database import engine, Base

Base.metadata.create_all(bind=engine)