from abc import abstractmethod


class ICrudRepository:
    @abstractmethod
    def store(self, entity):
        pass

    def get_by_id(self, entity_id):
        pass

    def update(self, entity):
        pass

    def delete(self, entity_id):
        pass



