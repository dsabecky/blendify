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
    
class PlaylistHistory:
    def __init__(self, path: str = "playlist_history.json") -> None:
        self.path = Path(path)
        self._db: dict[str, str] = {"recent": "", "history": {}}
        self.load()

    def load(self) -> None:
        try:
            with self.path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                # Validate structure
                if isinstance(data, dict):
                    self._db = data
                else:
                    self._db = {"recent": "", "history": {}}
                    self.save()
        except (FileNotFoundError, json.JSONDecodeError):
            self._db = {"recent": "", "history": {}}
            self.save()

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            self._db["history"] = dict(list(self._db["history"].items())[-5:])
            json.dump(self._db, f, ensure_ascii=False, indent=4)

    def add(self, playlist_id: str, playlist_name: str) -> None:
        if playlist_id not in self._db["history"]:
            self._db["history"][playlist_id] = playlist_name
            self.save()

    def remove(self, playlist_id: str) -> bool:
        if playlist_id in self._db["history"]:
            del self._db["history"][playlist_id]
            self.save()
            return True
        return False
    
    def update_recent(self, playlist_id: str) -> None:
        self._db["recent"] = playlist_id
        self.save()
    
    def update_history(self, playlist_id: str, playlist_name: str) -> None:
        if playlist_id in self._db["history"]:
            self._db["history"][playlist_id] = playlist_name
            self.save()

    def __contains__(self, playlist_id: str) -> bool:
        return playlist_id in self._db["history"]

    def get(self, key: str, default: str | None = None) -> str | None:
        return self._db.get(key, default)

    def last_five(self) -> dict[str, str]:
        return dict(list(self._db["history"].items())[-5:])

    def clear(self) -> None:
        self._db = {"recent": "", "history": {}}
        self.save()
    
class RequestHistory:
    def __init__(self, path: str = "request_history.json") -> None:
        self.path = Path(path)
        self._db: dict[str, list[str]] = {"requests": []}
        self.load()

    def load(self) -> None:
        try:
            with self.path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                # Validate structure
                if isinstance(data, dict) and "requests" in data and isinstance(data["requests"], list):
                    self._db = data
                else:
                    self._db = {"requests": []}
                    self.save()
        except (FileNotFoundError, json.JSONDecodeError):
            self._db = {"requests": []}
            self.save()

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self._db, f, ensure_ascii=False, indent=4)

    def add(self, request: str) -> None:
        if request not in self._db["requests"]:
            self._db["requests"].append(request)
            self.save()

    def remove(self, request: str) -> bool:
        if request in self._db["requests"]:
            self._db["requests"].remove(request)
            self.save()
            return True
        return False

    def __contains__(self, request: str) -> bool:
        return request in self._db["requests"]

    def get_all(self) -> list[str]:
        return list(self._db["requests"])

    def clear(self) -> None:
        self._db["requests"] = []
        self.save()
    
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