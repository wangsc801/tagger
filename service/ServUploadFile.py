from pathlib import Path
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from model.UploadFile import UploadFile
from datetime import datetime
from util.UtilUploadFile import UtilUploadFile, uuid_without_seperator
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ServUploadFile:
    def __init__(self, file: FileStorage = None, uploader_id: int = None, tag: str = None):
        self.file = file
        self.uploader_id = uploader_id
        self.tag = tag

    def is_allowed_upload(self) -> bool:
        return UtilUploadFile(self.file).allowed_file()

    def upload(self) -> Path:
        util = UtilUploadFile(self.file)
        upload_path = util.generate_path()
        filename = uuid_without_seperator() + Path(self.file.filename).suffix
        secured_filename = secure_filename(filename)
        self.file.save(upload_path.joinpath(secured_filename))

        uf = UploadFile(upload_path, secured_filename,
                        self.uploader_id, self.tag, datetime.now())
        db.session.add(uf)
        db.session.commit()
        return upload_path

    def get_by_uploader_id(self):
        return UploadFile.query.filter_by(uploader_id=self.uploader_id).all()

    def get_by_tag(self, tag: str):
        return db.session.execute(
            f"SELECT * FROM upload_file WHERE uploader_id={self.uploader_id} AND LOCATE(\"{tag}\",tag)>0;")
