""" Defines the User repository """

from digital_twin_migration.models.efficiency_app import User
from core.repository import BaseRepository


class UserRepository(BaseRepository[User]):

    def get_by_name(self, name: str, join_: set[str] | None = None):
        query = self._query(join_)
        query = query.filter(User.name == name)

        if join_ is not None:
            return self._all_unique(query)

        return self._one_or_none(query)

    def get_by_uuid(self, uuid: str, join_: set[str] | None = None):
        query = self._query(join_)
        query = query.filter(User.id == uuid)

        if join_ is not None:
            return self._all_unique(query)

        return self._one_or_none(query)
