from db.base import DbManager
from db.entities import Project, Task
import sqlalchemy

db = DbManager()

# PROJECT FUNCTIONS

def db_get_project(project_id):
    return db.open().query(Project).filter(Project.id == project_id).one()

def db_get_all_projects():
    return db.open().query(Project).all()

def db_create_project(name):
    project = Project()
    project.name = name
    try:
        return db.save(project)
    except sqlalchemy.exc.IntegrityError:
        print('*** db_create_project: \'{}\' already exists'.format(name))
    except Exception as e:
        print(type(e))

def db_update_project(project_id, name):
    project = db_get_project(project_id)
    project.name = name
    try:
        return db.update(project)
    except sqlalchemy.exc.IntegrityError:
        print('*** db_update_project: \'{}\' already exists'.format(name))
    except Exception as e:
        print(type(e))

def db_delete_project(project_id):
    return db.delete(db_get_project(project_id))

# TASK FUNCTIONS

def db_create_task(project_id, description):
    task = Task()
    task.description = description
    task.project_id = project_id
    return db.save(task)

def db_get_task(task_id):
    return db.open().query(Task).filter(Task.id == task_id).one()

def db_get_all_tasks(project_id):
    return db.open().query(Task).filter(Task.project_id == project_id).all()

def db_update_task(task_id, description):
    task = get_task(task_id)
    task.description = description
    return db.update(task)

def db_delete_task(task_id):
    return db.delete(get_task(task_id))
