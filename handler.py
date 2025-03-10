import json

def handle(data):
    try:
        # Проверяем, является ли data строкой (JSON) или уже словарем
        if isinstance(data, str):
            try:
                params = json.loads(data)  # Парсим JSON-строку
            except json.JSONDecodeError:
                return json.dumps({"error": "Invalid JSON format in input data"})
        elif isinstance(data, dict):
            params = data  # Данные уже являются словарем
        else:
            return json.dumps({"error": "Input data must be a JSON string or dictionary"})

        # Проверяем, что params является словарем
        if not isinstance(params, dict):
            return json.dumps({"error": "Input data is not a dictionary"})

        # Извлекаем search_status
        search_status = params.get("search_status", "")

        # Извлекаем массивы dial_statuses и call_statuses
        dial_statuses = params.get("dial_statuses", [])
        call_statuses = params.get("call_statuses", [])

        # Проверяем, что dial_statuses и call_statuses являются списками
        if not isinstance(dial_statuses, list) or not isinstance(call_statuses, list):
            return json.dumps({"error": "'dial_statuses' and 'call_statuses' must be lists"})

        # Функция для поиска элемента в массиве
        def find_element(array, status):
            return next((item for item in array if str(item.get("status")) == str(status)), None)

        # Ищем элемент в dial_statuses
        result = find_element(dial_statuses, search_status)
        if result:
            return json.dumps({"found": result})

        # Если не найдено в dial_statuses, ищем в call_statuses
        result = find_element(call_statuses, search_status)
        if result:
            return json.dumps({"found": result})

        # Если элемент не найден ни в одном массиве
        return json.dumps({"error": "Element not found"})

    except Exception as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return json.dumps({"error": str(e)})
