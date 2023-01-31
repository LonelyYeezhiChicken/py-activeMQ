from time import sleep
import stomp


class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, message):
        print("收到消息：", message)


# 連接 ActiveMQ
conn = stomp.Connection10([("127.0.0.1", 1883)])
conn.connect()

# 訂閱消息
conn.subscribe("/queue/test", id=1, ack="auto")

# 註冊監聽器
# conn.set_listener("", MyListener())

# 推送消息
conn.send("/queue/test", "測試消息", headers={"transformation": "jms-map-json"})

# for i in range(1, 101):
#     print(i)
#     sleep(1)

# 斷開連接
conn.disconnect()
