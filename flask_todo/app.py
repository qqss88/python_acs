from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/qsun.ctr/workspace/python_acs/flask_todo/todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()

    return render_template('index.html',
                           incomplete=incomplete, complete=complete)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username


# app = Flask(__name__)
# ####### Database#######

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# db = SQLAlchemy(app)


# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(200))
#     complete = db.Column(db.Boolean)


# # db.create_all()
# ###### Route when nothing is specified in the url######
# @app.route('/')
# def index():
#     incomplete = Todo.query.filter_by(complete=False).all()
#     complete = Todo.query.filter_by(complete=True).all()

#     return render_template('index.html',
#                            incomplete=incomplete, complete=complete)


# ###### Adding items######
# @app.route('/add', methods=['POST'])
# def add():
#     todo = Todo(text=request.form['todoitem'], complete=False)
#     print(todo)
#     db.session.add(todo)
#     db.session.commit()
#     print('saved.')
#     return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
