class User:

    def __init__(self, name: str):
        self.name = name


class Project:

    def __init__(self, name: str, owner: User) -> None:
        self.name = name
        self.owner = owner


class Membership:

    def __init__(self, user: User, project: Project) -> None:
        self.user = user
        self.project = project

    def __str__(self) -> str:
        return f'{self.user.name} is a member of {self.project.name}'
