from pythonosc.udp_client import SimpleUDPClient

ip = "127.0.0.1"
port = 8000
client = SimpleUDPClient(ip, port)

client.send_message("/play_drum", 1)

print("OSC command sent to Ableton!")
