import rclpy
from rclpy.node import Node
from person_msgs.srv import Query   #変更: 作ったQuery型を使う

rclpy.init()
node = Node("listener")


def main():
    client = node.create_client(Query, 'query')   #変更: 依頼する側（クライアント）を作成
    while not client.wait_for_service(timeout_sec=1.0):   #変更: talkerが立ち上がるまで待つ
        node.get_logger().info('待機中')

    req = Query.Request()             #変更: 依頼（リクエスト）を作る
    req.name = "鈴木太郎"              #変更: 依頼に名前を入れる
    future = client.call_async(req)   #変更: 依頼を送る（返事は待たずに次へ進む）

    while rclpy.ok():
        rclpy.spin_once(node)   #通信の処理を1回だけ行う
        if future.done():       #返事が届いていたら
            try:
                response = future.result()   #返事を取り出す
            except:
                node.get_logger().info('呼び出し失敗')
            else:   #exceptにならなかったとき（成功したとき）
                node.get_logger().info("age: {}".format(response.age))   #年齢を表示

            break   #whileを出る

    node.destroy_node()   #ノードの後始末
    rclpy.shutdown()      #通信の後始末
