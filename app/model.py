class ItemBackend:
    def __init__(self):
        self._items = {
            12: {"Name": "Sample Predefined Item"},
        }
        self._next_id = 1

    def add_item(self, item_data: dict):
        item_id = self._next_id
        self._items[item_id] = item_data
        self._next_id = item_id + 1
        return item_id

    def get_item(self, item_id: int):
        return self._items[item_id]

    def list_items(self):
        return self._items
