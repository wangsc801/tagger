from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from model.UploadFile import UploadFile
from database import db_session
import datetime


class ServUploadFile:
    def __init__(self, file: FileStorage = None, uploader_id: int = None, tag: str = None):
        self.upload_file = UploadFile(file=file, uploader_id=uploader_id, tag=tag)
        self.upload_file.set_filename()
        self.upload_file.set_filetype()
        
    def upload(self):
        file_suffix = self.upload_file.filename.rsplit('.', 1)[1].lower()
        filename = self.upload_file.uuid_without_seperator() + '.' + file_suffix
        secured_filename = secure_filename(filename)
        self.upload_file.filename=secured_filename
        self.upload_file.set_filepath()
        self.upload_file.upload_time = datetime.datetime.now()
        self.upload_file.file.save(self.upload_file.file_sys_path.joinpath(self.upload_file.filename))
        db_session.add(self.upload_file)
        db_session.commit()

    def get_by_id(self,id):
        return UploadFile.query.filter_by(id=id).first()

    def get_by_uploader_id(self):
        return UploadFile.query.filter_by(uploader_id=self.upload_file.uploader_id).all()

    def get_by_tag(self, tag: str):
        return db_session.execute(
            f"SELECT * FROM upload_file WHERE uploader_id={self.upload_file.uploader_id} AND LOCATE(\"{tag}\",tag)>0;")
