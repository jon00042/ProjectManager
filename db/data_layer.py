from db.base import DbManager
from db.entities import Project, Task

db = DbManager()

# PROJECT FUNCTIONS

def get_project(project_id):
    return db.open().query(Project).filter(Project.id == project_id).one()

def get_all_projects():
    return db.open().query(Project).all()

def create_project(name):
    project = Project()
    project.name = name
    return db.save(project)

def update_project(project_id, name):
    project = get_project(project_id)
    project.name = name
    return db.update(project)

def delete_project(project_id):
    return db.delete(get_project(project_id))


# TASK FUNCTIONS

def create_task(project_id, description):
    task = Task()
    task.description = description
    task.project_id = project_id
    return db.save(task)

def get_task(task_id):
    return db.open().query(Task).filter(Task.id == task_id).one()

def get_all_tasks(project_id):
    return db.open().query(Task).filter(Task.project_id == project_id).all()

def update_task(task_id, description):
    task = get_task(task_id)
    task.description = description
    return db.update(task)

def delete_task(task_id):
    return db.delete(get_task(task_id))
