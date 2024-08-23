import asana

client = asana.Client.access_token('ACCESS_TOKEN')

result = client.tasks.create_task(
    {'workspace': 'WORKSPACE_GID', 'name': 'Sample task', 'assignee': 'me'})

print(result)