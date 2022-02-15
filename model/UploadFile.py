from werkzeug.datastructures import FileStorage
from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from pathlib import Path
import datetime
import uuid
import time


class UploadFile(Base):
    __tablename__ = 'upload_file'
    id = Column(Integer, primary_key=True)
    filepath = Column(String(32))
    filename = Column(String(48))
    filetype = Column(String(16))
    uploader_id = Column(Integer)
    tag = Column(String(1024))
    upload_time = Column(DateTime)

    EXTENSIONS = {'video': ['mp4', 'avi'],
                  'image': ['png', 'jpg', 'jpeg', 'gif']}

    def __init__(self, file: FileStorage = None, id: int = None, uploader_id: int = None,
                 tag: str = None, upload_time: datetime = None, filetype: str = None):
        self.id = id
        self.file = file
        self.uploader_id = uploader_id
        self.tag = tag
        self.upload_time = upload_time
        self.filetype = filetype

    def set_filename(self):
        if not self.file is None:
            self.filename = self.file.filename

    def set_filetype(self):
        if not self.file is None:
            for k_type, v_exts in self.EXTENSIONS.items():
                if self.filename.rsplit('.', 1)[1].lower() in v_exts:
                    self.filetype = k_type

    def set_filepath(self):
        if not self.filetype is None:
            today = datetime.datetime.today()
            path = Path(".").joinpath('static', 'upload', self.filetype,
                                      str(today.year), str(today.month))
            upload_path = Path(path)
            if not upload_path.exists():
                # parents=True makes mkdir() effort like mkdir -p
                upload_path.mkdir(parents=True)
            self.file_sys_path = Path(path)
            import os
            fpath = str(upload_path)+os.path.sep
            if "\\" in fpath:
                fpath = fpath.replace("\\", "/")
            fpath = fpath.replace("static/", "")
            self.filepath=fpath

    def uuid_without_seperator(self):
        original_uuid = uuid.uuid3(uuid.NAMESPACE_OID, str(time.time()))
        return "".join(str(original_uuid).split("-"))
