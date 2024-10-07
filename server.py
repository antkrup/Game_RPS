import socket
import xml.etree.ElementTree as ET
import random

MOVES = ['rock', 'paper', 'scissors']

class RockPaperScissorsGame:
    def __init__(self):
        self.player_move = None
        self.server_move = None

    def determine_winner(self, player_move, server_move):
        if player_move == server_move:
            return "It's a tie!"
        elif (player_move == 'rock' and server_move == 'scissors') or \
             (player_move == 'scissors' and server_move == 'paper') or \
             (player_move == 'paper' and server_move == 'rock'):
            return "You win!"
        else:
            return "You lose!"
    
    def generate_server_move(self):
        return random.choice(MOVES)

    def play(self, player_move):
        self.player_move = player_move
        self.server_move = self.generate_server_move()
        return self.determine_winner(self.player_move, self.server_move)

    def generate_response_xml(self):
        response = ET.Element('response')
        ET.SubElement(response, 'player_move').text = self.player_move
        ET.SubElement(response, 'server_move').text = self.server_move
        result = self.determine_winner(self.player_move, self.server_move)
        ET.SubElement(response, 'result').text = result
        return ET.tostring(response)


class RockPaperScissorsServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server is listening on port {self.port}...")

    def start(self):
        while True:
            conn, addr = self.server_socket.accept()
            print(f"Connection from {addr} has been established!")
            data = conn.recv(1024).decode()
            print(f"Received from client: {data}")

            player_move = data.strip().lower()
            game = RockPaperScissorsGame()
            game.play(player_move)

            response_xml = game.generate_response_xml()
            conn.send(response_xml)
            conn.close()

    def stop(self):
        self.server_socket.close()


if __name__ == "__main__":
    server = RockPaperScissorsServer()
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
        print("Server has been stopped.")
