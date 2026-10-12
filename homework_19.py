import requests

BASE_URL = "http://127.0.0.1:8080"

# POST - загрузка изображения
with open("test.png", "rb") as image_file:
    files = {
        "image": image_file
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

print("UPLOAD:")
print(response.status_code)
print(response.json())

# имя файла
filename = "test.png"

# GET - получение ссылки
response = requests.get(
    f"{BASE_URL}/image/{filename}",
    headers={"Content-Type": "text"}
)

print("\nGET:")
print(response.status_code)
print(response.json())

# DELETE - удаление файла
response = requests.delete(
    f"{BASE_URL}/delete/{filename}"
)

print("\nDELETE:")
print(response.status_code)
print(response.json())