from .model import *


def list_projects():
    return projects.all()


def get_project(name: str):
    return projects.find(name=name)


def create_project(name: str):
    project = Project(name='Site Developing', owner=mike)
    return project


def remove_project(name: str):
    project = projects.find(name=name)
    project.delete()


def chage_project(project, **kwargs):
    project.update(**kwargs)


def list_my_projects(user: User):
    return user.projects


def create_membership(project: Project, role: Role, user: Optional[User] = None):
    membership = Membership(project=project, role=role, user=user)
    return membership