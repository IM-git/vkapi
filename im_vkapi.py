from settings import VK_TOKEN, USER_ID
import vk_api
from tools import Tools


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

    def get_friends_list_with_fullname(self) -> list:
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

    def get_id_list_friends(self) -> list:
        """Get a list of all friends from user."""
        list_friends = self.session.method("friends.get", {
            "user_id": self.user_id,
            "fields": "nickname"})
        items = list_friends["items"]
        data_friends = []
        for item in items:
            data_friends.append(item["id"])
        return data_friends


if __name__ == '__main__':
    tools = Tools()
    parameters_id = tools.parameters()[0]
    parameters_f = tools.parameters()[1]
    imvkapi = ImVkApi(user_id=parameters_id)
    got_list = []
    # Check the selected parameter "friends"
    if parameters_f.lower() == "all":
        got_list = imvkapi.get_id_list_friends()
    elif parameters_f.lower() == "online":
        got_list = imvkapi.get_online_friends_list()
    # Parsing the list of ids and deleting digital ids
    vk_ids = []
    for _ in got_list:
        vk_ids.append(tools.vk_request(_))

    print(tools.del_digital_id(vk_ids))

