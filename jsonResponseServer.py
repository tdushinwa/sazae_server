#!/usr/bin/python
# encoding: utf-8

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib


# 詳細データの読み込み
with open('family.json', mode='r', encoding='utf-8') as f:
    json_string = json.load(f)
print(json.dumps(json_string, indent=2))
post_data = json_string['list']


class JsonResponseHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # POSTされたデータの内容確認
        content_len = int(self.headers.get('content-length'))
        post_content = self.rfile.read(content_len).decode('UTF-8')
        result = urllib.parse.parse_qs(post_content)

        # レスポンス用jsonを作る
        length = len(result['id'])
        data = []
        for i in range(length):
            d = post_data[int(result['id'][i]) - 1]
            data.append({"id": d['id'], "name": d['name']})
            # if i != 0:
            #     data += ','
            # data += '{'
            # data += '"id": {0}, "name": {1}'.format(
            #     str(d['id']),
            #     d['name'].encode('utf-8').decode('utf-8'))
            # data += '}'
        # data += ']}'

        # レスポンスの設定
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # レスポンスを送る
        responseData = json.dumps(data)
        self.wfile.write(responseData.encode('UTF-8'))

server = HTTPServer(('', 80), JsonResponseHandler)
server.serve_forever()
