import asyncio

from message_utils import Message, generate_message_client


def generate_messages() -> list[Message]:
    return [Message("Message 1"), Message("Message 2")]


async def send_messages() -> None:
    message_client = generate_message_client()
    messages = generate_messages()
    await asyncio.gather(*[message_client.send(message) for message in messages])


def main() -> None:
    asyncio.run(send_messages())


if __name__ == "__main__":
    main()
