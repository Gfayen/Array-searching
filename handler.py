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

        # Извлекаем search_name
        search_name = params.get("search_name", "")
        print(f"Search name: {search_name}")  # Отладочный вывод

        # Извлекаем массивы dial_statuses и call_statuses
        dial_statuses = params.get("data", {}).get("dial_statuses", [])
        call_statuses = params.get("data", {}).get("call_statuses", [])

        # Проверяем, что dial_statuses и call_statuses являются списками
        if not isinstance(dial_statuses, list) or not isinstance(call_statuses, list):
            return json.dumps({"error": "'dial_statuses' and 'call_statuses' must be lists"})

        print(f"Dial statuses: {dial_statuses}")  # Отладочный вывод
        print(f"Call statuses: {call_statuses}")  # Отладочный вывод

        # Функция для поиска элемента в массиве
        def find_element(array, name):
            for item in array:
                item_name = item.get("name")
                print(f"Checking name: {item_name} against search_name: {name}")  # Отладочный вывод
                if str(item_name) == str(name):  # Преобразуем в строки для сравнения
                    return item
            return None

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
        # В случае ошибки возвращаем сообщение об ошибке
        return json.dumps({"error": str(e)})
