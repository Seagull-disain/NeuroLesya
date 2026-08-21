import unittest

from main import NeuroLesyaCore


class NeuroLesyaCoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.core = NeuroLesyaCore()

    def test_empty_request(self) -> None:
        self.assertIn("Потрібно отримати запит", self.core.handle(""))

    def test_question(self) -> None:
        self.assertIn("Отримано запит", self.core.handle("Що таке НейроЛеся?"))

    def test_general_message(self) -> None:
        self.assertIn("Отримано повідомлення", self.core.handle("Привіт"))


if __name__ == "__main__":
    unittest.main()
