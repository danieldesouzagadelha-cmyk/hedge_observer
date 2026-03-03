import websocket
import json

price_data = {
    "price": None
}

def on_message(ws, message):
    data = json.loads(message)
    price_data["price"] = float(data["c"])

def start_socket():
    socket = "wss://stream.binance.com:9443/ws/btcusdt@ticker"
    ws = websocket.WebSocketApp(socket, on_message=on_message)
    ws.run_forever()
