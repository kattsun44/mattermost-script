import requests
import json
import setting

HEADERS = {'Authorization': 'Bearer {}'.format(
    setting.MATTERMOST_ACCESS_TOKEN)}

# https://api.mattermost.com/#operation/GetPostsForChannel
GET_POSTS_FOR_A_CHANNEL_PATH = '/channels/{}/posts'.format(setting.CHANNEL_ID)

r_get = requests.get(
    setting.URL + GET_POSTS_FOR_A_CHANNEL_PATH + '?PER_PAGE=1000', headers=HEADERS)
posts = r_get.json()

print(json.dumps(posts['posts'], ensure_ascii=False))
