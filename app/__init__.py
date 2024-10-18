from app.core.database.mixin import Base
from app.models import User
from app.core.database.session import engine

Base.metadata.create_all(bind=engine)