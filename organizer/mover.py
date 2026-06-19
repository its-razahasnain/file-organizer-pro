from pathlib import Path
import shutil
from models.file_info import FileInfo

FILE_TYPES = {
            "Application": [
                ".exe",
                ".msi",
                ".app",
                ".dmg",
                ".apk",
                ".ipa",
                ".deb",
                ".rpm",
                ".bat",
                ".sh",
                ".crx",
                ".xpi",
                ".vsix",
                "ui_extension",
                "app_service",
                "web_pixel",
                "theme_extension",
            ],
            "PDF": [".pdf"],
            "Audio": [
                ".mp3",
                ".wav",
                ".aac",
                ".flac",
                ".ogg",
                ".m4a",
                ".wma",
                ".alac",
                ".aiff",
                ".opus",
            ],
            "Video": [
                ".mp4",
                ".mkv",
                ".avi",
                ".mov",
                ".wmv",
                ".flv",
                ".webm",
                ".m4v",
                ".mpeg",
                ".3gp",
            ],
            "Archives": [
                ".zip",
                ".rar",
                ".7z",
                ".tar",
                ".gz",
                ".bz2",
                ".xz",
                ".zipx",
                ".iso",
                ".tgz",
            ],
            "Images": [
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".bmp",
                ".webp",
                ".svg",
                ".tiff",
                ".ico",
                ".heic",
            ],
            "Python": [".py"],
            "Documents": [
                ".docx",
                ".doc",
                ".txt",
                ".rtf",
                ".odt",
                ".pages",
                ".xlsx",
                ".pptx",
                ".csv",
            ],
        }


class FileMover:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.file_types = FILE_TYPES

    def organize(self, file_info: list[FileInfo]) -> None:
        for info in file_info:
            category = self.get_category(info)
            self.create_folder(category=category)
            destination = Path(self.directory_path) / category
            self.move_file(source=info, destination=destination)

    def get_category(self, info: FileInfo) -> str:
        for category, extensions in self.file_types.items():
            if info.extension.lower() in extensions:
                return category
        return "Others"

    def create_folder(self, category: str) -> None:
        folder_path = Path(self.directory_path) / category
        folder_path.mkdir(parents=True, exist_ok=True)

    def move_file(self, source: FileInfo, destination: Path) -> None:
        file_destination = destination / source.name
        if file_destination.exists():
            return
        shutil.move(source.path, file_destination)
