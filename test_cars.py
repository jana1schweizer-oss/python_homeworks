import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_search.log", mode="w"),
        logging.StreamHandler()
    ],
    force=True
)
@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    response = session.post(
        "http://127.0.0.1:8080/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    access_token = response.json()["access_token"]

    session.headers.update(
        {"Authorization": f"Bearer {access_token}"}
    )

    return session


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 2),
        ("price", 10),
        ("year", 1),
        ("engine_volume", 4)
    ]
)
class TestCarsSearch:

    def test_search_cars(self, auth_session, sort_by, limit):
        url = "http://127.0.0.1:8080/cars"
        params = {"sort_by": sort_by, "limit": limit}

        # Логуємо початок запиту
        logging.info(f"Запуск тесту пошуку автомобілів з параметрами: sort_by={sort_by}, limit={limit}")

        # Виконуємо GET-запит за допомогою сесії, яка вже має токен
        response = auth_session.get(url, params=params)

        # Логуємо результат відповіді від сервера
        logging.info(f"Отримано відповідь. Статус код: {response.status_code}")

        # Перевіряємо, що запис пройшов успішно (статус 200)
        assert response.status_code == 200, f"Очікувався статус 200, але отримано {response.status_code}"

        # Отримуємо JSON-дані
        cars_list = response.json()
        logging.info(f"Кількість знайдених автомобілів у відповіді: {len(cars_list)}")

        # Перевіряємо, чи кількість елементів не перевищує ліміт
        assert len(cars_list) <= limit, f"Очікувався ліміт {limit}, але сервер повернув {len(cars_list)} елементів"

