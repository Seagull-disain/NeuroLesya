import tempfile
import unittest
from pathlib import Path

from .persistent import PersistentMemoryStore


class PersistentMemoryStoreTests(unittest.TestCase):
    def test_memory_survives_recreation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "memory.json"

            first = PersistentMemoryStore(path)
            first.remember("Володимир любить українську мову", kind="preference", tags=["language"])

            second = PersistentMemoryStore(path)
            self.assertEqual(len(second.items), 1)
            self.assertEqual(second.items[0].text, "Володимир любить українську мову")
            self.assertEqual(second.items[0].kind, "preference")
            self.assertEqual(second.items[0].tags, ["language"])

    def test_clear_persists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "memory.json"
            store = PersistentMemoryStore(path)
            store.remember("temporary")
            store.clear()

            restored = PersistentMemoryStore(path)
            self.assertEqual(restored.items, [])


if __name__ == "__main__":
    unittest.main()
