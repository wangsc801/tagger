from tkinter.tix import Form
from flask import Blueprint, render_template, request
from flask_login import current_user
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired, Length, DataRequired

from service.ServUploadFile import ServUploadFile

gallary_bp = Blueprint('gallary_bp', __name__,
                       template_folder='templates', static_folder='static')


class GallaryForm(Form):
    search = StringField('search', validators=[
                         InputRequired(), Length(min=1, max=64), DataRequired()])


@gallary_bp.route('/gallary', methods=['GET', 'POST'])
def gallary():
    form = GallaryForm(request.form)
    upload_file_serv = ServUploadFile(uploader_id=current_user.id)
    files=[]
    if request.method == 'GET':
        get_files = upload_file_serv.get_by_uploader_id()
        for f in get_files:
            files.append(f)
    if form.validate():
        tag=form.search.data
        get_files=upload_file_serv.get_by_tag(tag)
        for f in get_files:
            files.append(f)
    return render_template('gallary.html', files=files, form=form)
