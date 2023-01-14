import requests
import argparse
from settings import USER_ID, USER_ID_TEXT


class Tools:

    @staticmethod
    def del_digital_id(values):
        """Return the list of ids without digital ids."""
        list_id = []
        for value in values:
            if not value[:1] == "id" and not value[2:].isdigit():
                list_id.append(value)
        return list_id

    @staticmethod
    def parameters():
        parsers = argparse.ArgumentParser(description="Choice the parameters")
        parsers.add_argument('-id', default=USER_ID)
        parsers.add_argument('-f', default="all")
        return [parsers.parse_args().id, parsers.parse_args().f]

    @staticmethod
    def vk_request(vk_id: str | int) -> str:
        """Getting a text vk_id"""
        answer: str
        if str(vk_id).isdigit():
            """Converting digit id to text id"""
            vk_id = (requests.get(f"https://vk.com/id{vk_id}").url.split('/'))[-1]
        return vk_id


if __name__ == '__main__':
    tools = Tools()
    print(tools.vk_request(vk_id=USER_ID))
    print(tools.vk_request(vk_id=USER_ID_TEXT))
