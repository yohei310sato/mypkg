import rclpy
from rclpy.node import Node
from person_msgs.srv import Query   #変更: 作ったQuery型を使う

rclpy.init()
node = Node("talker")


def cb(request, response):          #変更: 依頼が来るたびに呼ばれる
    if request.name == "佐藤耀平":   #変更: 依頼（request）のnameを見る
        response.age = 41           #変更: 返事（response）のageに年齢を入れる
    else:
        response.age = 255          #変更: 知らない人なら255
    return response                 #変更: 返事を返す


def main():
    srv = node.create_service(Query, "query", cb)   #変更: サービスを作成（型、名前、関数）
    rclpy.spin(node)
