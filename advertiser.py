from base_model import BaseAdvertising


# This class represents an advertiser.
# It inherits from the BaseAdvertising class (likely for functionalities like id management).
# This class keeps track of advertiser specific information and statistics.
class Advertiser(BaseAdvertising):
    # Keeps track of total clicks across all Advertiser instances (static variable)
    _total_clicks: int = 0

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    @staticmethod
    def help() -> str:
        id_description = "id: The unique identifier for the advertising object."
        name_description = "name: The advertiser name"
        views_description = "views: The number of clicks for this advertising object."
        clicks_description = "clicks: The number of views for this advertising object."
        return f'{id_description} \n {name_description} \n {views_description} \n {clicks_description}'

    # Static method to retrieve total clicks across all advertisers
    @staticmethod
    def get_total_clicks() -> int:
        return Advertiser._total_clicks

    # Increments clicks for the advertiser and the total clicks
    def inc_clicks(self) -> None:
        super().inc_clicks()
        Advertiser._total_clicks += 1

    def describe_me(self) -> str:
        return 'This class represents an advertiser.'
