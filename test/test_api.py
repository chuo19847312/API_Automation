from helpers.RequestHelper import RequestHelper

endpoint = 'https://todo.pixegami.io/'

def test_getTask(taskID):
    getTask = RequestHelper().get_task(endpoint=endpoint, task_id=taskID)
    assert getTask.status_code == 200

def test_deleteTask(taskID):
    delTask = RequestHelper().delete_task(endpoint=endpoint, task_id=taskID)
    assert delTask.status_code == 200
    DeletedTask = RequestHelper().get_task(endpoint=endpoint, task_id=taskID)
    assert DeletedTask.status_code == 404

def test_listTask(userID):
    listTask = RequestHelper().list_task(endpoint=endpoint, user_id=userID)
    assert listTask.status_code == 200