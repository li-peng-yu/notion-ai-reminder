import os
from notion_client import Client

notion = Client(auth=os.getenv("NOTION_TOKEN"))

DATABASE_ID = os.getenv("DATABASE_ID")

def fetch_tasks():
    response = notion.databases.query(
        **{
            "database_id": DATABASE_ID,
            "filter": {
                "property": "Name",
                "rich_text": {
                    "is_not_empty": True
                }
            }
        }
    )

    results = []
    for page in response["results"]:
        properties = page["properties"]
        task = {
            "name": properties["Name"]["title"][0]["plain_text"] if properties["Name"]["title"] else "Untitled",
            "status": properties.get("Status", {}).get("select", {}).get("name", "No status")
        }
        results.append(task)

    return results
