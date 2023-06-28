@dataclass
class Role:

    def __init__(self, name: str) -> None:
        self.name = name


# self.role = role

# может ли пользователь быть одновременно на нескольких ролях?
# - думаю это излишне

# роль по умлочанию для создателя проекта — owner
# роль по умлочанию для вступающих в проект — member

# self.owners: set[User] = {owner}

# role: Role,

# role: str = f'\trole: {self.role.name}'