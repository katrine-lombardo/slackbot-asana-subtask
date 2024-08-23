import os
from dotenv import load_dotenv, find_dotenv
from typing import List
import asana


# Initialise environment
def initialize_environment() -> List[str]:
    load_dotenv(find_dotenv())
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    WORKSPACE_GID = os.getenv("WORKSPACE_GID")


client = asana.Client.access_token("ACCESS_TOKEN")

result = client.tasks.create_task(
    {"workspace": "WORKSPACE_GID", "name": "Sample task", "assignee": "me"}
)

print(result)
