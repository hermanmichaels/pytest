from dataclasses import dataclass


@dataclass
class Message:
    body: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Message):
            return NotImplemented
        return self.body == other.body


class MessageClient:
    async def send(self, message: Message) -> None:
        print(f"Sending message: {message}")


def generate_message_client() -> MessageClient:
    return MessageClient()
