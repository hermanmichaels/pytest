from unittest.mock import AsyncMock, Mock, call, patch

import pytest as pytest
from message_sending import send_messages
from message_utils import Message


class MessageMatcher(str):
    def __eq__(self, other: object):
        if not isinstance(other, Message):
            return NotImplemented
        return self in other.body


@pytest.fixture
def message_client_mock():
    message_client_mock = Mock()
    message_client_mock_send = AsyncMock()
    message_client_mock.send = message_client_mock_send
    return message_client_mock


@pytest.mark.asyncio
@patch("message_sending.generate_message_client")
async def test_send_messages(generate_message_client: Mock, message_client_mock: Mock):
    generate_message_client.return_value = message_client_mock

    await send_messages()

    message_client_mock.send.assert_has_calls(
        [call(Message("Message 1")), call(MessageMatcher("2"))]
    )
