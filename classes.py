####################################################################
# Imports
####################################################################

import json
from pathlib import Path


####################################################################
# Classes
####################################################################

class PlaylistDB:
    def __init__(self, path: str = "playlist_db.json"):
        self.path = Path(path)
        self._db: dict[str, list[str]] = {}
        self.load()

    def load(self) -> None:
        try:
            with self.path.open("r", encoding="utf-8") as f:
                self._db = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self._db = {}
            self.save()

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self._db, f, ensure_ascii=False, indent=4)

    def add(self, playlist_name: str, songs: list[str]) -> None:
        self._db[playlist_name] = songs
        self.save()

    def remove(self, playlist_name: str) -> bool:
        if playlist_name in self._db:
            del self._db[playlist_name]
            self.save()
            return True
        return False

    def __getitem__(self, playlist_name: str) -> list[str]:
        return self._db[playlist_name]

    def __setitem__(self, playlist_name: str, value: list[str]) -> None:
        self._db[playlist_name] = value
        self.save()

    def __contains__(self, playlist_name: str) -> bool:
        return playlist_name in self._db

    def get(self, playlist_name: str, default=None) -> list[str]:
        return self._db.get(playlist_name, default)

    def all(self) -> dict[str, list[str]]:
        return self._db
    
class SongDB:
    def __init__(self, path: str = "song_db.json") -> None:
        self.path = Path(path)
        self._db: dict[str, str] = {}
        self.load()

    def load(self) -> None:
        try:
            with self.path.open("r", encoding="utf-8") as f:
                self._db = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self._db = {}
            self.save()

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self._db, f, ensure_ascii=False, indent=4)

    def add(self, title: str, uri: str) -> None:
        self._db[title] = uri
        self.save()

    def remove(self, title: str) -> bool:
        if title in self._db:
            del self._db[title]
            self.save()
            return True
        return False

    def __getitem__(self, title: str) -> str:
        return self._db[title]

    def __setitem__(self, title: str, uri: str) -> None:
        self._db[title] = uri
        self.save()

    def __contains__(self, title: str) -> bool:
        return title in self._db

    def get(self, title: str, default: str | None = None) -> str | None:
        return self._db.get(title, default)

    def all(self) -> dict[str, str]:
        return dict(self._db)