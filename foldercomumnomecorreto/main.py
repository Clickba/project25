from google.cloud import pubsub_v1
from google.cloud import storage
def main(event, context):
    publisher = pubsub_v1.PublisherClient()
    topic_path = "projectsgcp-6th-academy-364009topicstopic_demo_acasa"
    data_str = "Message aaaaaaaaaaaaaaaaaaaaaaa"
    # Data must be a bytestring
    data = data_str.encode(utf-8)
    # When you publish a message, the client returns a future.
    publisher.publish(topic_path, data)
