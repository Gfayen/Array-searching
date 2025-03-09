import json

def handle(data):
    try:
        # Первый этап: парсим внешний JSON
        params = json.loads(data)

        # Проверяем, что params является словарем
        if not isinstance(params, dict):
            return json.dumps({"error": "Input data is not a dictionary"})

        # Извлекаем search_status
        search_status = params.get("search_status", "")

        # Извлекаем data (которое может быть строкой)
        data_str = params.get("data", "")

        # Второй этап: парсим вложенный JSON внутри data
        try:
            data = json.loads(data_str)  # Преобразуем строку в объект
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid JSON format in 'data'"})

        # Извлекаем массивы dial_statuses и call_statuses
        dial_statuses = data.get("dial_statuses", [])
        call_statuses = data.get("call_statuses", [])

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
