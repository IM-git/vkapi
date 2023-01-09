from settings import VK_TOKEN, USER_ID
import requests
import pprint
import vk_api

# method = 'wall.get'
# token = VK_TOKEN
# version = 5.131
# session = vk_api.VkApi(token=token)
# url = f"https://api.vk.com/method/{method}?owner_id={USER_ID}&access_token={token}&v={version}"


class ImVkApi:
    """
    There are gathered main methods for work with vk API methods.
    """

    def __init__(self, user_id: str | int = USER_ID):
        self.session = vk_api.VkApi(token=VK_TOKEN)
        self.user_id = str(user_id)

    def get_wall_entries(self) -> list:
        """Get list posts from user wall"""
        return self.session.method("wall.get", {"owner_id": self.user_id})

    def get_online_friends_list(self) -> list:
        """Get a list of friends online from user."""
        return self.session.method("friends.getOnline",
                                   {"user_id": self.user_id})

    def get_friends_list(self) -> list:
        """Get a list of all friends from user."""
        list_friends = self.session.method("friends.get", {
            "user_id": self.user_id,
            "fields": "nickname"})
        items = list_friends["items"]
        data_friends = []
        for item in items:
            full_name = item["first_name"] + " " + item["last_name"]
            data_friends.append({"fullname": full_name,
                                 "id": item["id"]})
        return data_friends


if __name__ == '__main__':
    imvkapi = ImVkApi()
    # r = requests.get(url=url)
    # print(r.status_code)
    # pprint.pprint(r.json())
    # pprint.pprint(get_wall_entries())
    # pprint.pprint(imvkapi.get_online_friends_list())
    pprint.pprint(imvkapi.get_friends_list())
