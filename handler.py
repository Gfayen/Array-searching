import json

def handle(data):
    try:
        # Преобразуем входные данные из JSON в Python-объекты
        try:
            params = json.loads(data)  # Преобразуем строку JSON в словарь
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid JSON format in input data"})

        # Проверяем, что params является словарем
        if not isinstance(params, dict):
            return json.dumps({"error": "Input data is not a dictionary"})

        # Извлекаем массивы dial_statuses и call_statuses
        dial_statuses = params.get("data", {}).get("dial_statuses", [])
        call_statuses = params.get("data", {}).get("call_statuses", [])

        # Проверяем, что dial_statuses и call_statuses являются списками
        if not isinstance(dial_statuses, list) or not isinstance(call_statuses, list):
            return json.dumps({"error": "'dial_statuses' and 'call_statuses' must be lists"})

        # Извлекаем значение для поиска
        search_name = params.get("search_name", "")

        # Функция для поиска элемента в массиве
        def find_element(array, name):
            return next((item for item in array if item.get("name") == name), None)

        # Ищем элемент в dial_statuses
        result = find_element(dial_statuses, search_name)
        if result:
            return json.dumps({"found": result})

        # Если не найдено в dial_statuses, ищем в call_statuses
        result = find_element(call_statuses, search_name)
        if result:
            return json.dumps({"found": result})

        # Если элемент не найден ни в одном массиве
        return json.dumps({"error": "Element not found"})

    except Exception as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return json.dumps({"error": str(e)})
