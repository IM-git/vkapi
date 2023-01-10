from settings import VK_TOKEN, USER_ID
import pprint
import vk_api
import argparse

# Added for running im_vkapi with parameter to command prompt
# Example: py .\im_vkapi.py -id 12345678
parsers = argparse.ArgumentParser(description="Choice the parameters")
parsers.add_argument('-id', default=USER_ID)
args = parsers.parse_args()


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
    imvkapi = ImVkApi(user_id=args.id)
    # imvkapi = ImVkApi()
    # pprint.pprint(get_wall_entries())
    # pprint.pprint(imvkapi.get_online_friends_list())
    pprint.pprint(imvkapi.get_friends_list())
