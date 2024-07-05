def individual_serial(todo) -> dict:
    return {
        'id': str(todo['_id']),
        'name': todo['name'],
        'description': todo['description'],
        'is_done': todo['is_done']
    }


def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]