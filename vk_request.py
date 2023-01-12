import requests
from settings import USER_ID, USER_ID_TEXT


def vk_request(vk_id: str | int) -> str:
    """Getting a text vk_id"""
    answer: str
    if str(vk_id).isdigit():
        """Converting digit id to text id"""
        vk_id = (requests.get(f"https://vk.com/id{vk_id}").url.split('/'))[-1]
    return vk_id


if __name__ == '__main__':
    print(vk_request(vk_id=USER_ID))
    print(vk_request(vk_id=USER_ID_TEXT))
