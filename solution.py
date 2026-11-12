from typing import List  # для списков
import aiohttp  # HTTP запросы


async def get_matrix(url: str) -> List[List[int]]:  # Получение матрицы по ссылке
    async with aiohttp.ClientSession() as session:  # Создаём сессию
        async with session.get(url) as response:  #  GEtзапрос
            response.raise_for_status()  # ошибки запроса
            text = await response.text()  # ответ сервера

    return parse_matrix(text)


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
