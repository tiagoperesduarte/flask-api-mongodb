from mongoengine import DoesNotExist

from models.task import Task


class TaskService:
    def get_tasks(self):
        return Task.objects

    def get_task_by_id(self, id):
        try:
            return Task.objects.get(id=id)
        except DoesNotExist as err:
            return None

    def save_task(self, task):
        return task.save()

    def delete_task_by_id(self, id):
        Task.objects.get(id=id).delete()
