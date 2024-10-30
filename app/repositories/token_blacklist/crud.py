

from app.core.repositories import ICrudRepository
from app.models import TokenBlackList


class TokenBlacklistCrudRepository(ICrudRepository):
    def __init__(self, session):
        self.session = session

    def store(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)

    def get_by_id(self, entity_id: int) -> TokenBlackList:
        return self.session.query().filter_by(id=entity_id, delete_at=None).first()

    def find_by_one(self, **kwargs) -> TokenBlackList:
        return self.session.query(TokenBlackList).filter_by(**kwargs).first()

    def update(self, entity: TokenBlackList):
        self.session.commit()

    def soft_delete(self, entity_id: int):
        user = self.get_by_id(entity_id)
        if user:
            self.delete(user)
        else:
            raise Exception('Not Found.')


