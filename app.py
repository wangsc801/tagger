from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import toml
from route.index import index_bp
from route.login import login_bp
from route.upload_file import upload_file_bp
from route.gallary import gallary_bp

app = Flask(__name__)

'''
(python code)
app.config['ENV']='development'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_COMMIT_TEARDOWN']=True
app.config['SECRET_KEY']="python -c 'import os; print(os.urandom(16))'"

(toml file)
ENV = "development"
SQLALCHEMY_DATABASE_URI = "mysql://username:password@localhost/db_name"
SQLALCHEMY_TRACK_MODIFICATIONS = true
SQLALCHEMY_COMMIT_TEARDOWN = true
SECRET_KEY = "python -c 'import os; print(os.urandom(16))'"
'''
app.config.from_file('config.toml', load=toml.load)

db = SQLAlchemy(app)

app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(upload_file_bp)
app.register_blueprint(gallary_bp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_bp.login'


@login_manager.user_loader
def load_user(user_id):
    from model.User import User
    return User.query.get(user_id)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
