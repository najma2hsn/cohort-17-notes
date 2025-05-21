Create a Chat Application that allows two users to send messages to each other. The producer should send messages with the user's name and the message content, and the consumer should display them in a human-readable format.

The program should run in an infinite loop, allowing the user to send messages until they choose to exit.


A producer that sends dictionaries with multiple keys/values instead of basic strings. It should:

- Include a name key with the sender's name
- Include a message key with the message content
- Include a timestamp key with the current time

On the Consumer side it should:

- Display the message in a human-readable format
- Ignore any messages that don't fit the expected format
