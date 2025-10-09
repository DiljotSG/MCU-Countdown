import time
from typing import Any, Optional


class CacheEntry:
    def __init__(self, value: Any, ttl: int):
        self.value = value
        self.expires_at = time.time() + ttl

    def is_expired(self) -> bool:
        return time.time() > self.expires_at


class Cache:
    def __init__(self):
        self._cache: dict = {}

    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None

        entry = self._cache[key]
        if entry.is_expired():
            del self._cache[key]
            return None

        return entry.value

    def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        self._cache[key] = CacheEntry(value, ttl)

    def delete(self, key: str) -> None:
        if key in self._cache:
            del self._cache[key]

    def clear(self) -> None:
        self._cache.clear()

    def cleanup(self) -> None:
        expired_keys = [key for key, entry in self._cache.items() if entry.is_expired()]
        for key in expired_keys:
            del self._cache[key]


_global_cache = Cache()


def get_cache() -> Cache:
    return _global_cache
