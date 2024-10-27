from datetime import datetime

from app import Admin
from app.core.repositories import ICrudRepository


class AdminCrudRepository(ICrudRepository):
    def __init__(self, session):
        self.session = session

    def store(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)

    def get_by_id(self, entity_id: int) -> Admin:
        return self.session.query().filter_by(id=entity_id, delete_at=None).first()

    def find_by_one(self, **kwargs) -> Admin:
        return self.session.query(Admin).filter_by(**kwargs, delete_at=None).first()

    def update(self, entity: Admin):
        self.session.commit()

    def soft_delete(self, entity_id: int):
        user = self.get_by_id(entity_id)
        if user:
            user.delete_at = datetime.now()
            self.update(user)
        else:
            raise Exception('Not Found.')


