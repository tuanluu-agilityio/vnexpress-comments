import json
import requests
import sys

def site_content(idx, url):
    jData = get_data_from_api(url)
    data = jData['data']
    items = data['items']

    with open('list_comments_{}.txt'.format(idx), 'w') as file:
        file.write('Total: {}'.format(int(data['total'])))
        file.write('\nTotal Items: {}\n'.format(int(data['totalitem'])))

        write_comment_file(items, file)

def get_data_from_api(url):
    myResponse = requests.get(url)
    jData = json.loads(myResponse.content)

    return jData

def write_comment_file(data, f):
    for item in data:
        time = item['time'].encode('utf-8').strip()
        full_name = item['full_name'].encode('utf-8').strip()
        content = item['content'].encode('utf-8').strip()

        f.write('\n\n {} ({})'.format(full_name, time))
        f.write('\n\t {}'.format(content))

        replys = item['replys']
        if hasattr(item, 'replys') and len(replys) > 0:
            replys_items = replys['items']
            write_comment_file(replys_items, f)

def read_url_file():
    with open('url.txt', 'r') as file:
        for idx, url in enumerate(file):
            site_content(idx, url)

if __name__ == "__main__":
    read_url_file()
