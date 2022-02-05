from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UploadFile(db.Model):
    __tablename__ = 'upload_file'
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(32))
    filename = db.Column(db.String(48))
    uploader_id = db.Column(db.Integer)
    tag = db.Column(db.String(1024))
    upload_time = db.Column(db.DateTime)

    def __init__(self, file_path, filename, uploader_id, tag, upload_time):
        self.file_path = self.__path_for_db(file_path)
        self.filename = filename
        self.uploader_id = uploader_id
        self.tag = tag
        self.upload_time = upload_time

    def __path_for_db(self, old_file_path):
        import os
        fpath = str(old_file_path)+os.path.sep
        if "\\" in fpath:
            fpath = fpath.replace("\\", "/")
        fpath = fpath.replace("static/", "")
        return fpath
