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