import asyncio
import unittest
from solution import get_matrix, parse_matrix, spiral_traversal


class TestMatrix(unittest.TestCase):

    def test_spiral(self):  # обход по спирали
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [1, 4, 7, 8, 9, 6, 3, 2, 5]
        self.assertEqual(spiral_traversal(matrix), expected)

    def test_single(self):  # матрица из одного числа
        self.assertEqual(spiral_traversal([[5]]), [5])

    def test_invalid(self):  # неверная матрица
        with self.assertRaises(ValueError):
            parse_matrix("| 1 | 2 |\n| 3 |")

    def test_loading(self):  # загрузка матрицы с сайта
        url = (
            "https://raw.githubusercontent.com/"
            "avito-tech/python-trainee-assignment/main/matrix.txt"
        )
        expected = [
            10, 50, 90, 130, 140, 150, 160, 120,
            80, 40, 30, 20, 60, 100, 110, 70
        ]
        self.assertEqual(asyncio.run(get_matrix(url)), expected)


if __name__ == "__main__":
    unittest.main()
