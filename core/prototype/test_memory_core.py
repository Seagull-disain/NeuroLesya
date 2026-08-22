import unittest

from memory_core import MemoryAwareNeuroLesyaCore


class MemoryAwareCoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.core = MemoryAwareNeuroLesyaCore()

    def test_first_message_is_saved(self) -> None:
        self.core.handle("Мене звати Володимир")
        self.assertEqual(self.core.recent_memory(), ["Мене звати Володимир"])

    def test_relevant_messages_are_loaded_before_new_request(self) -> None:
        self.core.handle("Ми працюємо над пам'яттю НейроЛесі")
        self.core.handle("Сьогодні говорили про погоду")
        self.core.handle("Пам'ять НейроЛесі має працювати з контекстом")
        self.assertEqual(
            self.core.last_memory_context,
            ["Пам'ять НейроЛесі має працювати з контекстом", "Ми працюємо над пам'яттю НейроЛесі"],
        )

    def test_unrelated_message_is_not_loaded(self) -> None:
        self.core.handle("Ми працюємо над пам'яттю НейроЛесі")
        self.core.handle("Сьогодні говорили про погоду")
        self.core.handle("Яка погода завтра?")
        self.assertEqual(self.core.last_memory_context, ["Сьогодні говорили про погоду"])

    def test_empty_message_is_not_saved(self) -> None:
        self.core.handle("   ")
        self.assertEqual(self.core.recent_memory(), [])


if __name__ == "__main__":
    unittest.main()
