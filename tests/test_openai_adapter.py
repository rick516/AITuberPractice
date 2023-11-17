from src.openai_adapter import OpenAIAdapter
from unittest.mock import patch, MagicMock
from src.openai_adapter import main

class TestOpenAIAdapter:
    def setup_method(self, method):
        self.adapter = OpenAIAdapter()

    def test_create_message(self):
        role = "system"
        message = "Hello, World!"
        result = self.adapter._create_message(role, message)
        assert result == {"role": role, "content": message}

    def test_create_message_invalid_role(self):
        role = "invalid_role"
        message = "Hello, World!"
        try:
            result = self.adapter._create_message(role, message)
        except ValueError:
            assert True
        else:
            assert False, "ValueError was not raised"

    def test_create_chat(self):
        question = "こんにちは、世界！"
        with patch('openai.ChatCompletion.create') as mock_create:
            mock_create.return_value = MagicMock(choices=[MagicMock(message=MagicMock(role="assistant", content="こんにちは、世界！"))])
            result = self.adapter._create_chat(question)
            assert result == "こんにちは、世界！"

    def test_create_chat_no_question(self):
        question = ""
        with patch('openai.ChatCompletion.create') as mock_create:
            try:
                self.adapter._create_chat(question)
            except ValueError:
                assert True
            else:
                assert False, "ValueError was not raised"
                
		# OpenAIのAPIを呼び出す処理はテストしない 
    # def test_main(self):
    #     with patch('builtins.input', return_value="こんにちは、世界！"), \
    #         patch('builtins.print') as mock_print:
    #         main()
    #         mock_print.assert_called_once()
