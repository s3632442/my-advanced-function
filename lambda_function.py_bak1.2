import json

def lambda_handler(event, context):
    # Example input event
    # {
    #     "id": "123456",
    #     "metrics": {
    #         "humans or animals": "animals",
    #         "natural or arteficial": "natural",
    #         "me or them": "them",
    #         "sustainability or now": "now"
    #     }
    # }

    # Extract metrics and ID from the input event
    metrics = event.get("metrics", {})
    item_id = event.get("id")

    # Sort the metrics by their matching numeric values in reverse order
    sorted_metrics = sorted(metrics.items(), key=lambda x: int(x[1]), reverse=False)

    # Create a JSON response with text values ordered by numeric values in reverse
    response = {
        "id": item_id,
        "ordered_categories": [
            {"category": category, "text_value": text_value} for category, text_value in sorted_metrics
        ]
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

