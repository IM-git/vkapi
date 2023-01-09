from settings import VK_TOKEN, USER_ID
import requests
import pprint
import vk_api

method = 'wall.get'
token = VK_TOKEN
version = 5.131
session = vk_api.VkApi(token=token)
url = f"https://api.vk.com/method/{method}?owner_id={USER_ID}&access_token={token}&v={version}"


def get_wall_entries():
    return session.method("wall.get", {"owner_id": USER_ID})


def online_friends():
    return session.method("friends.getOnline", {"user_id": USER_ID})


def get_friends_list():
    list_friends = session.method("friends.get", {"user_id": USER_ID, "fields": "nickname"})
    items = list_friends["items"]
    data_friends = []
    for item in items:
        full_name = item["first_name"] + " " + item["last_name"]
        data_friends.append({"fullname": full_name,
                             "id": item["id"]})
    return data_friends


if __name__ == '__main__':
    # r = requests.get(url=url)
    # print(r.status_code)
    # pprint.pprint(r.json())
    # pprint.pprint(get_wall_entries())
    # pprint.pprint(online_friends())
    pprint.pprint(get_friends_list())
