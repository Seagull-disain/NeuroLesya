import unittest

from memory_core import MemoryAwareNeuroLesyaCore


class MemoryAwareCoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.core = MemoryAwareNeuroLesyaCore()

    def test_first_message_is_saved(self) -> None:
        self.core.handle("Мене звати Володимир")
        self.assertEqual(self.core.recent_memory(), ["Мене звати Володимир"])

    def test_previous_messages_are_loaded_before_new_request(self) -> None:
        self.core.handle("Перше повідомлення")
        self.core.handle("Друге повідомлення")
        self.assertEqual(
            self.core.last_memory_context,
            ["Перше повідомлення"],
        )
        self.assertEqual(
            self.core.recent_memory(),
            ["Перше повідомлення", "Друге повідомлення"],
        )

    def test_empty_message_is_not_saved(self) -> None:
        self.core.handle("   ")
        self.assertEqual(self.core.recent_memory(), [])


if __name__ == "__main__":
    unittest.main()
