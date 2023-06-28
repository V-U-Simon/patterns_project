from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class User:

    def __init__(self, id: int):
        self.id = id

    def __repr__(self) -> str:
        return f'<User: {self.id}>'


class Project:

    def __init__(self, name: str, owner: User) -> None:
        self.name: str = name
        self.memberships: set[Membership] = set()

    def include(self, user: User):
        self.memberships.add(user)

    def exclude(self, user: User):
        self.memberships.remove(user)

    def __repr__(self) -> str:
        return f'<Project: {self.name} / {self.owner.name}>'

    # def __str__(self) -> str:
    #     return f'{self.name} project'


class Membership:

    def __init__(self, project: Project, user: Optional[User] = None) -> None:
        self.project = project
        self.user = user

    def __repr__(self) -> str:
        return f'<Membership: {self.project.name} {self.user.name}>'

    # def __str__(self) -> str:
    #     return f'{self.user.name} is a member of {self.project.name}'
