from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired, Length
from flask_login import login_required
from flask import Blueprint, render_template, request, redirect, url_for
from service.ServUploadFile import ServUploadFile
from flask_login import current_user

upload_file_bp = Blueprint('upload_file_bp', __name__,
                           template_folder='templates', static_folder='static')


class UploadForm(Form):
    tag_input = StringField('tag_input', validators=[
        InputRequired(), Length(min=1, max=1024)])


@upload_file_bp.route('/upload_file', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'GET':
        return render_template('upload_file.html')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload_file.html', upload_info_hint="No file part!")
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return render_template('upload_file.html', upload_info_hint="No selected file!")
        form = UploadForm(request.form)
        ufservice = ServUploadFile(
            file=file, uploader_id=current_user.id, tag=form.tag_input.data)
        if not ufservice.is_allowed_upload():
            return render_template('upload_file.html', upload_info_hint="not allowed file type!")
        if file:
            ufservice.upload()
        return render_template('upload_file.html', upload_info_hint="upload successfully!")
        # return redirect(url_for('index_bp.index'))
    return
