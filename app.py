def handler(event, context):
    print("hoge1")

    return {"statusCode": 200, "body": "update from codebuild"}
