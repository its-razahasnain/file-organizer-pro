from pathlib import Path


class Scanner:
    def __init__(self, directory_path):
        self.directory_path = Path(directory_path)

    def scan_directory(self) -> list[dict]:
        """
        Scan the directory and return metadata for all visible files.

        Returns:
            list[dict]: Information about each file.

        Raises:
            FileNotFoundError
            NotADirectoryError
            PermissionError
        """
        files = []
        if not self.directory_path.exists():
            raise FileNotFoundError(f"The path {self.directory_path} doesn't exists!")
        if not self.directory_path.is_dir():
            raise NotADirectoryError(
                f"The path '{self.directory_path}' is a file, not a directory."
            )
        try:
            items = self.directory_path.iterdir()
        except PermissionError:
            raise PermissionError(
                f"Read permission denied for directory: {self.directory_path}"
            )
        for item in items:
            if item.name.startswith("."):
                continue
            try:
                if item.is_file():
                    size = item.stat().st_size
                    files.append(
                        {
                            "name": item.name,
                            "extension": item.suffix,
                            "size": size,
                            "path": item,
                        }
                    )
            except PermissionError:
                continue
        return files
