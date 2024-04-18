import requests
import uuid


class RequestHelper:

    def create_payload(self):
        user_id = uuid.uuid4().hex
        payload = {
        "content": "test content",
        "user_id": user_id,
        "is_done": False,
        }
        return payload

    def get_task(self, endpoint: str, task_id: str):
        return requests.get(endpoint + f"/get-task/{task_id}")

    def delete_task(self, endpoint: str, task_id: str):
        return requests.delete(endpoint + f"/delete-task/{task_id}")
    
    def list_task(self, endpoint: str, user_id: str):
        return requests.get(endpoint + f"/list-tasks/{user_id}")
    
    def create_task(self, endpoint: str):
        payload = self.create_payload()
        response = requests.put(endpoint + "/create-task", json=payload)
        return response.json()
