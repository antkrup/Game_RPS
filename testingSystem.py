import unittest
from server import RockPaperScissorsGame  

class TestRockPaperScissorsGame(unittest.TestCase):
    
    def setUp(self):
        """Цей метод запускається перед кожним тестом."""
        self.game = RockPaperScissorsGame()

    def test_determine_winner_tie(self):
        """Тест на випадок, коли хід гравця і сервера однакові."""
        result = self.game.determine_winner('rock', 'rock')
        self.assertEqual(result, "It's a tie!")

    def test_determine_winner_player_wins(self):
        """Тест на перемогу гравця."""
        result = self.game.determine_winner('rock', 'scissors')
        self.assertEqual(result, "You win!")
        
        result = self.game.determine_winner('scissors', 'paper')
        self.assertEqual(result, "You win!")
        
        result = self.game.determine_winner('paper', 'rock')
        self.assertEqual(result, "You win!")

    def test_determine_winner_server_wins(self):
        """Тест на перемогу сервера."""
        result = self.game.determine_winner('rock', 'paper')
        self.assertEqual(result, "You lose!")
        
        result = self.game.determine_winner('scissors', 'rock')
        self.assertEqual(result, "You lose!")
        
        result = self.game.determine_winner('paper', 'scissors')
        self.assertEqual(result, "You lose!")

    def test_generate_server_move(self):
        """Тест на перевірку генерації серверного ходу."""
        server_move = self.game.generate_server_move()
        self.assertIn(server_move, ['rock', 'paper', 'scissors'])

    def test_play(self):
        """Тест на повний ігровий процес."""
        result = self.game.play('rock')
        self.assertIn(result, ["It's a tie!", "You win!", "You lose!"])

    def test_generate_response_xml(self):
        """Тест на генерацію XML-відповіді."""
        self.game.play('rock')
        xml_response = self.game.generate_response_xml()
        self.assertIn(b'<response>', xml_response)
        self.assertIn(b'<player_move>rock</player_move>', xml_response)

if __name__ == '__main__':
    unittest.main()
