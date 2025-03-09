import json

def handle(data):
    try:
        # Преобразуем входные данные из JSON в Python-объекты
        params = json.loads(data)
        array = params.get("data", [])
        search_name = params.get("search_name", "")

        # Ищем элемент с name == search_name
        result = next((item for item in array if item.get("name") == search_name), None)

        # Если элемент найден, возвращаем его в формате JSON
        if result:
            return json.dumps({"found": result})
        else:
            return json.dumps({"error": "Element not found"})

    except Exception as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return json.dumps({"error": str(e)})
