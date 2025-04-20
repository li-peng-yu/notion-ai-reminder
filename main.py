from utils.notion_reader import fetch_tasks
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    print("Fetching tasks from Notion...")
    tasks = fetch_tasks()
    for task in tasks:
        print(f"{task['name']} (Status: {task['status']})")
