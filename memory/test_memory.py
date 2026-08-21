import unittest

from prototype import MemoryStore


class MemoryStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.memory = MemoryStore()

    def test_remember_and_recent(self) -> None:
        self.memory.remember("Перше повідомлення")
        self.memory.remember("Друге повідомлення")
        recent = self.memory.recent()
        self.assertEqual([item.text for item in recent], ["Перше повідомлення", "Друге повідомлення"])

    def test_recent_limit(self) -> None:
        for index in range(5):
            self.memory.remember(f"Повідомлення {index}")
        recent = self.memory.recent(2)
        self.assertEqual([item.text for item in recent], ["Повідомлення 3", "Повідомлення 4"])

    def test_clear(self) -> None:
        self.memory.remember("Тест")
        self.memory.clear()
        self.assertEqual(self.memory.recent(), [])


if __name__ == "__main__":
    unittest.main()
