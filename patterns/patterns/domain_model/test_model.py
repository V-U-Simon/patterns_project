from .model import *

if __name__ == "__main__":
    mike = User(name='Mike')
    john = User(name='John')
    snow = User(name='Show')
    sara = User(name='Sara')

    project = Project(name='Site Developing', owner=mike)

    # userhood creating Role object
    project.add_role('Director', 1)
    project.add_role('Developer',)
    project.add_role('DevOps', 1)
    project.add_role('Designer', 2)

    # roles
    roles: list[Role] = project.roles
    role: Role = project.get_role

    # without role
    project.invite(mike, john)
    project.application(snow)  # send to project admins

    # with role
    project.role(sara, role)
    project.role(sara, None)
    project.role(sara)

    # membership
    users: list[Membership] = project.memberships

    member: Membership = project.get_member(sara)

    is_member(project, user)

    #
    project = projects.find(name='Site Developing')
