from dataclasses import dataclass
from typing import Optional


class User:

    def __init__(self, name: str):
        self.name = name
        self.invites: list[Project] = []

    def approve(self, invite):
        project = self.invites.pop(invite)
        project.include(self)
        
        


class Project:

    def __init__(self, name: str, owner: User) -> None:
        self.name: str = name
        self.owners: list[User] = [owner, ]
        self.memberships: list[Membership] = []


    def invite(self, role: 'Membership', user: User):
        user.invites.append(self)

    def include(user: User):
        pass

    def exclude(self, user: User):
        pass

    def __repr__(self) -> str:
        return f'<Project: {self.name} / {self.owner.name}>'

    def __str__(self) -> str:
        return f'{self.name} is a project of {self.owner.name}'


@dataclass
class Role:
    def __init__(self, name: str) -> None:
        self.name = name
        
    

class Membership:

    def __init__(self, project: Project, role: Role, user: Optional[User] = None) -> None:
        self.project = project
        self.role = role
        self.user = user

    def __repr__(self) -> str:
        membership: str = f'<Membership: {self.project.name}\n'
        role: str = f'\trole: {self.role.name}'
        user: str = f'\tuser: {self.user.name}>'
        return membership + role + user

    def __str__(self) -> str:
        return f'{self.user.name} is a member of {self.project.name}'

class Invite()