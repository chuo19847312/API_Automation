import pytest
from helpers.RequestHelper import RequestHelper

@pytest.fixture(scope="session", name="newTask")
def createTask():
    new_task = RequestHelper().create_task(endpoint = 'https://todo.pixegami.io/')
    return new_task

@pytest.fixture(name="taskID")
def get_task_id(newTask):
    task_id = newTask['task']['task_id']
    return task_id

@pytest.fixture(name="userID")
def get_user_id(newTask):
    user_id = newTask['task']['user_id']
    return user_id