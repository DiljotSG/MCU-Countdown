class ListNotFoundError(Exception):
    def __init__(self, list_id: int, message: str = None):
        self.list_id = list_id
        self.message = message or f"TMDB list {list_id} not found or returned no data"
        super().__init__(self.message)


class NoUpcomingProductionsError(Exception):
    def __init__(self, list_id: int = None, desired_date: str = None):
        self.list_id = list_id
        self.desired_date = desired_date
        self.message = f"No productions found after {desired_date}"
        if list_id:
            self.message += f" in list {list_id}"
        super().__init__(self.message)
