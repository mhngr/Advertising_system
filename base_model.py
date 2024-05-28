# This class defines a base advertising object
class BaseAdvertising:
    def __init__(self, id: int = None):
        """
        Initializes a BaseAdvertising object.

        Args:
            id (int, optional): The unique identifier for the advertising object. Defaults to None.
        """
        self._id: int = id
        self._clicks: int = 0
        self._views: int = 0

    def get_clicks(self) -> int:
        """
        Returns the number of clicks for this advertising object.
        """
        return self._clicks

    def get_views(self) -> int:
        """
        Returns the number of views for this advertising object.
        """
        return self._views

    def inc_clicks(self) -> None:
        """
        Increments the click count for this advertising object.
        """
        self._clicks += 1

    def inc_views(self) -> None:
        """
        Increments the view count for this advertising object.
        """
        self._views += 1

    def describe_me(self) -> str:
        return 'This class defines a base advertising object'
