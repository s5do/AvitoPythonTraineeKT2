from typing import List  # для списка чисел
import aiohttp  # HTTP запросы


async def get_matrix(url: str) -> List[int]:  # Получение матрицы по ссылке
    async with aiohttp.ClientSession() as session:  # Создаём сессию
        async with session.get(url) as response:  #  GEtзапрос
            response.raise_for_status()  # ошибки запроса
            text = await response.text()  # ответ сервера

    return []
