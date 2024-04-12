## VKAPI
____
Getting the list with all/online friends to vk.\
How it works:

1. Need to create your own vk [access token](https://dev.vk.com/api/getting-started). Simple way to [create vk app and get token](https://badtry.net/vk-api-osnovy-poluchieniie-tokiena).
2. Create [.env](https://github.com/theskumar/python-dotenv) for safe storage data([habr article](https://habr.com/ru/post/472674/)).

Example:

    .env
        VK_TOKEN=your_own_token
        USER_ID=test_any_user_id
        USER_ID_TEXT=test_any_user_text_id
3. Run script: `py im_vkapi.py -id 12345678 -f online`

test test
123 4