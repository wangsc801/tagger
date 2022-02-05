from werkzeug.datastructures import FileStorage
from pathlib import Path
import uuid
import time
import datetime


class UtilUploadFile:
    def __init__(self, file: FileStorage):
        self.filename = file.filename
        self.file_ext = file.filename.rsplit('.', 1)[1].lower()
        self.file_type = False
        self.EXTENSIONS = {'video': ['mp4', 'avi'],
                           'image': ['png', 'jpg', 'jpeg', 'gif']}

    def allowed_file(self):
        if '.' in self.filename:
            for file_type, exts in self.EXTENSIONS.items():
                if self.file_ext in exts:
                    self.file_type = file_type
                    return True
        return False

    def generate_path(self) -> Path:
        if self.allowed_file():
            print("\n\n---------- the type \n--------\n------")
            today = datetime.datetime.today()
            path = Path(".").joinpath('static','upload', self.file_type,
                                      str(today.year), str(today.month))
            print(f"\n\n-- -- \npath:{path}")
            upload_path = Path(path)
            print(f"\n\n-- -- \npath:{upload_path}")
            if not upload_path.exists():
                print(f"\n\n-- -- \npath:{upload_path.exists()}")
                # parents=True makes mkdir() effort like mkdir -p
                upload_path.mkdir(parents=True)
            return upload_path
        return


def uuid_without_seperator() -> str:
    original_uuid = uuid.uuid3(uuid.NAMESPACE_OID, str(time.time()))
    return "".join(str(original_uuid).split("-"))
