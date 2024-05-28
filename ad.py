from base_model import BaseAdvertising
from advertiser import Advertiser


# This class represents an advertisement.
# It inherits from the BaseAdvertising class and adds additional attributes
# specific to ads, such as title, image URL, link, and advertiser.
class Ad(BaseAdvertising):
    def __init__(
            self, id: int, title: str, image_url: str, link: str, advertiser: Advertiser
    ):
        # Initialize base class attributes and store ad specific attributes
        super().__init__(id)
        self._title: str = title
        self._image_url: str = image_url
        self._link: str = link
        self._advertiser: Advertiser = advertiser

    def get_title(self) -> str:
        return self._title

    def set_title(self, title: str) -> None:
        self._title = title

    def get_link(self) -> str:
        return self._link

    def set_link(self, link: str) -> None:
        self._link = link

    def get_image_url(self) -> str:
        return self._image_url

    def set_image_url(self, url: str) -> None:
        self._image_url = url

    def set_advertiser(self, advertiser: Advertiser) -> None:
        self._advertiser = advertiser

    def describe_me(self) -> str:
        return "This class represents an advertisement."

    def inc_clicks(self) -> None:
        super().inc_clicks()
        self._advertiser.inc_clicks()

    def inc_views(self) -> None:
        super().inc_views()
        self._advertiser.inc_views()
