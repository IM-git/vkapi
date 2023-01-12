from settings import VK_TOKEN, USER_ID
import pprint
import vk_api
import argparse
from vk_request import vk_request


# Added for running im_vkapi with parameter to command prompt
# Example: py .\im_vkapi.py -id 12345678 -f online
def parameters():
    parsers = argparse.ArgumentParser(description="Choice the parameters")
    parsers.add_argument('-id', default=USER_ID)
    parsers.add_argument('-f', default="all")
    return [parsers.parse_args().id, parsers.parse_args().f]


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
    parameters_id = parameters()[0]
    parameters_f = parameters()[1]

    imvkapi = ImVkApi(user_id=parameters_id)

    # pprint.pprint(imvkapi.get_wall_entries())
    # pprint.pprint(imvkapi.get_online_friends_list())
    # pprint.pprint(imvkapi.get_friends_list())
    got_list = []
    if parameters_f.lower() == "all":
        # pprint.pprint(imvkapi.get_id_list_friends())
        got_list = imvkapi.get_id_list_friends()
    elif parameters_f.lower() == "online":
        # pprint.pprint(imvkapi.get_online_friends_list())
        got_list = imvkapi.get_online_friends_list()

    for _ in got_list:
        print(vk_request(_))

