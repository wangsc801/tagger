from flask import Blueprint, render_template, url_for
from flask_login import login_required

index_bp = Blueprint('index_bp', __name__, template_folder='templates')


@index_bp.route('/')
def index():
    return render_template('index.html')
