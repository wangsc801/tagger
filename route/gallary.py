from flask import Blueprint, render_template, session, url_for
from flask_login import current_user

from service.ServUploadFile import ServUploadFile

gallary_bp = Blueprint('gallary_bp', __name__,
                       template_folder='templates', static_folder='static')


@gallary_bp.route('/gallary')
def gallary():
    upload_file_serv = ServUploadFile(uploader_id=current_user.id)
    get_files = upload_file_serv.get_by_uploader_id()
    paths = []
    for f in get_files:
        paths.append(
            (url_for('static', filename=f.file_path+f.filename), f.tag))
    return render_template('gallary.html', paths=paths)
