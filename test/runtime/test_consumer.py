from ingestion.messaging.consumer import get_consumer

print("Initializing consumer...")

consumer = get_consumer()

print("Waiting for messages...")

message_found = False

for message in consumer:

    print("\nRECEIVED MESSAGE:")
    print(message.value)

    message_found = True
    break

if not message_found:
    print("No messages received.")

print("Consumer test completed.")