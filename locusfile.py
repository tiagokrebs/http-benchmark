from locust import HttpLocust, TaskSet, task, between
import json


class UserBehavior(TaskSet):
    # @task(1)
    # def create_post(self):
    #     headers = {'content-type': 'application/json', 'Accept-Encoding': 'gzip'}
    #     self.client.post("/posts", data=json.dumps({
    #         "title": "foo",
    #         "body": "bar",
    #         "userId": 1
    #     }),
    #                      headers=headers,
    #                      name="Create a new post")

    wait_time = between(3, 25)

    @task(2)
    def create_get(self):
        self.client.get(url="/juarez-assets/magazine/menu/x60/default/target.html", name="Create a new get")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior