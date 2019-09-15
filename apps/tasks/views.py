from flask import render_template, request, redirect, url_for

from app import db
from apps.tasks import bp

from apps.tasks.models import Todo


@bp.route('/', methods=['GET'])
def index():
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', tasks=tasks)


@bp.route("/create/", methods=['POST'])
def create():
    task_content = request.form['content']
    new_task = Todo(content=task_content)

    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks.index'))
    except Exception as ex:
        print(ex)
        return 'There was an issue adding your task'

@bp.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('tasks.index'))
    except:
        return 'There was a problem deleting that task'


@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect(url_for('tasks.index'))
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)
