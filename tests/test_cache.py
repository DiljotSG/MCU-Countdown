import time
import unittest

from src.services.cache import Cache, CacheEntry


class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache()
        self.cache.clear()  # Ensure clean state

    def tearDown(self):
        self.cache.clear()

    def test_cache_set_and_get(self):
        self.cache.set("test_key", "test_value", ttl=60)
        result = self.cache.get("test_key")
        self.assertEqual(result, "test_value")

    def test_cache_get_nonexistent(self):
        result = self.cache.get("nonexistent_key")
        self.assertIsNone(result)

    def test_cache_expiration(self):
        self.cache.set("expire_test", "value", ttl=1)

        # Value should exist immediately
        result = self.cache.get("expire_test")
        self.assertEqual(result, "value")

        # Wait for expiration
        time.sleep(1.1)

        # Value should be None after expiration
        result = self.cache.get("expire_test")
        self.assertIsNone(result)

    def test_cache_delete(self):
        self.cache.set("delete_test", "value", ttl=60)
        self.assertEqual(self.cache.get("delete_test"), "value")

        self.cache.delete("delete_test")
        self.assertIsNone(self.cache.get("delete_test"))

    def test_cache_clear(self):
        self.cache.set("key1", "value1", ttl=60)
        self.cache.set("key2", "value2", ttl=60)

        self.assertEqual(self.cache.get("key1"), "value1")
        self.assertEqual(self.cache.get("key2"), "value2")

        self.cache.clear()

        self.assertIsNone(self.cache.get("key1"))
        self.assertIsNone(self.cache.get("key2"))

    def test_cache_cleanup(self):
        self.cache.set("active", "value1", ttl=60)
        self.cache.set("expired", "value2", ttl=1)

        time.sleep(1.1)

        # Before cleanup, expired entry still in cache dict
        self.cache.cleanup()

        # After cleanup, expired should be removed but active remains
        self.assertEqual(self.cache.get("active"), "value1")
        self.assertIsNone(self.cache.get("expired"))

    def test_cache_overwrite(self):
        self.cache.set("key", "value1", ttl=60)
        self.assertEqual(self.cache.get("key"), "value1")

        self.cache.set("key", "value2", ttl=60)
        self.assertEqual(self.cache.get("key"), "value2")

    def test_cache_entry_is_expired(self):
        entry = CacheEntry("test", ttl=1)
        self.assertFalse(entry.is_expired())

        time.sleep(1.1)
        self.assertTrue(entry.is_expired())

    def test_cache_complex_objects(self):
        test_dict = {"key": "value", "nested": {"a": 1, "b": 2}}
        test_list = [1, 2, 3, "four", {"five": 5}]

        self.cache.set("dict", test_dict, ttl=60)
        self.cache.set("list", test_list, ttl=60)

        self.assertEqual(self.cache.get("dict"), test_dict)
        self.assertEqual(self.cache.get("list"), test_list)


if __name__ == "__main__":
    unittest.main()
