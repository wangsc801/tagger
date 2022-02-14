from database import Base
from sqlalchemy import Column, Integer, String, DateTime


class UploadFile(Base):
    __tablename__ = 'upload_file'
    id = Column(Integer, primary_key=True)
    file_path = Column(String(32))
    filename = Column(String(48))
    uploader_id = Column(Integer)
    tag = Column(String(1024))
    upload_time = Column(DateTime)

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
