import threading
from collections import OrderedDict
from typing import Any, Optional


class CacheBusyException(Exception):
    """Raised when the cache is locked and cannot be acquired."""
    pass


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache.

        Args:
            capacity (int): Maximum number of items to hold in the cache.
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        self.lock = threading.Lock()
        self.size = 0

    def get(self, key: Any, block: bool = True, timeout: Optional[float] = None) -> Optional[Any]:
        """
        Retrieve a value from the cache.

        Args:
            key: The key to look up.
            block (bool): Whether to block waiting for the lock.
            timeout (float or None): Max time to wait for the lock.

        Returns:
            The cached value if found, or None if not found.

        Raises:
            CacheBusyException: If the lock could not be acquired in time.
        """
        acquired = self.lock.acquire(blocking=block, timeout=timeout)

        if not block or timeout is not None:
            if not acquired:
                raise CacheBusyException("Cache is currently busy. Try again later.")

        try:
            if key not in self.cache:
                return None
            self.cache.move_to_end(key)
            return self.cache[key]
        finally:
            self.lock.release()

    def put(self, key: Any, value: Any, block: bool = True, timeout: Optional[float] = None) -> bool:
        """
        Add or update a value in the cache.

        Args:
            key: The key to store.
            value: The value to store.
            block (bool): Whether to block waiting for the lock.
            timeout (float or None): Max time to wait for the lock.

        Returns:
            True if the value was stored successfully.

        Raises:
            CacheBusyException: If the lock could not be acquired in time.
        """
        acquired = self.lock.acquire(blocking=block, timeout=timeout)

        if not block or timeout is not None:
            if not acquired:
                raise CacheBusyException("Cache is currently busy. Try again later.")

        try:
            already_present = key in self.cache
            existing_value = self.cache.get(key)

            if already_present and existing_value == value:
                # No need to update value, but ensure MRU
                self.cache.move_to_end(key)
                return True

            self.cache[key] = value
            self.cache.move_to_end(key)

            if not already_present:
                self.size += 1

            if self.size > self.capacity:
                evicted_key, _ = self.cache.popitem(last=False)
                self.size -= 1
                print(f" -- Cache evicted key: {evicted_key}")

            return True
        finally:
            self.lock.release()

    def clear(self, block: bool = True, timeout: Optional[float] = None) -> None:
        """
        Clear all entries from the cache.

        Args:
            block (bool): Whether to block waiting for the lock.
            timeout (float or None): Max time to wait for the lock.

        Raises:
            CacheBusyException: If the lock could not be acquired in time.
        """
        acquired = self.lock.acquire(blocking=block, timeout=timeout)

        if not block or timeout is not None:
            if not acquired:
                raise CacheBusyException("Cache is currently busy. Try again later.")

        try:
            self.cache.clear()
            self.size = 0
        finally:
            self.lock.release()

    def __contains__(self, key: Any) -> bool:
        with self.lock:
            return key in self.cache

    def __len__(self) -> int:
        with self.lock:
            return self.size

    def __repr__(self) -> str:
        return f"LRUCache(capacity={self.capacity}, current_size={self.size})"
