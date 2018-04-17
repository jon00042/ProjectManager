from flask import Flask, flash, session, request, redirect, render_template, url_for

from db.data_layer import db_create_project, db_get_all_projects, db_get_project, db_update_project, db_delete_project
from db.data_layer import db_create_task, db_get_all_tasks, db_get_task, db_update_task, db_delete_task

app = Flask(__name__)

@app.route('/')
def index():
    db_projects = db_get_all_projects()
    return render_template('index.html', projects=db_projects)

@app.route('/create_project', methods=['POST'])
def create_project():
    db_create_project(request.form['project_name'])
    return redirect(url_for('index'))

@app.route('/edit_project/<db_project_id>')
def edit_project(db_project_id):
    db_project = db_get_project(db_project_id)
    return render_template('edit_project.html', project=db_project)

@app.route('/delete_project/<db_project_id>')
def delete_project(db_project_id):
    db_delete_project(db_project_id)
    return redirect(url_for('index'))

@app.route('/update_project', methods=['POST'])
def update_project():
    db_update_project(request.form['db_project_id'], request.form['project_name'])
    return redirect(url_for('index'))

@app.route('/tasks/<db_project_id>')
def tasks(db_project_id):
    db_project = db_get_project(db_project_id)
    return render_template('tasks.html', project=db_project)

@app.route('/create_task', methods=['POST'])
def create_task():
    db_project = db_get_project(request.form['db_project_id'])
    db_create_task(db_project.id, request.form['task_name'])
    return redirect(url_for('tasks', db_project_id=db_project.id))

@app.route('/edit_task/<db_task_id>/<db_project_id>')
def edit_task(db_task_id, db_project_id):
    db_task = db_get_task(db_task_id)
    db_project = db_get_project(db_project_id)
    return render_template('edit_task.html', task=db_task, project=db_project)

@app.route('/delete_task/<db_task_id>/<db_project_id>')
def delete_task(db_task_id, db_project_id):
    db_delete_task(db_task_id)
    db_project = db_get_project(db_project_id)
    return render_template('tasks.html', project=db_project)

@app.route('/update_task/', methods=['POST'])
def update_task():
    db_update_task(request.form['db_task_id'], request.form['task_name'])
    db_project = db_get_project(request.form['db_project_id'])
    return render_template('tasks.html', project=db_project)

app.run(debug=True)

