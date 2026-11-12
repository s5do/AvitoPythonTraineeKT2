from typing import List  # для списков
import aiohttp  # HTTP запросы


async def get_matrix(url: str) -> List[int]:  # Получение матрицы по ссылке
    async with aiohttp.ClientSession() as session:  # Создаём сессию
        async with session.get(url) as response:  #  GEtзапрос
            response.raise_for_status()  # ошибки запроса
            text = await response.text()  # ответ сервера

    return spiral_traversal(parse_matrix(text))


def parse_matrix(text: str) -> List[List[int]]:
    matrix = []  # для матрицы

    for line in text.splitlines():
        line = line.strip()

        if not line.startswith("|"):
            continue  # лишние строки

        values = [
            int(value.strip())  # в целые числа
            for value in line.strip("|").split("|")
        ]
        matrix.append(values)

    n = len(matrix)  # кол-во строк

    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("Неверный размер матрицы")  # проверяем размер

    return matrix


def spiral_traversal(matrix: List[List[int]]) -> List[int]:
    result = []
    n = len(matrix)

    # границы матрицы
    top, bottom = 0, n - 1
    left, right = 0, n - 1

    while top <= bottom and left <= right:
        for row in range(top, bottom + 1):
            result.append(matrix[row][left])  # сверху вниз
        left += 1

        if left > right:
            break

        for col in range(left, right + 1):
            result.append(matrix[bottom][col])  # слева направо
        bottom -= 1

        if top > bottom:
            break

        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][right])  # снизу вверх
        right -= 1

        if left > right:
            break

        for col in range(right, left - 1, -1):
            result.append(matrix[top][col])  # справа налево
        top += 1

    return result
