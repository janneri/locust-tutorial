from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    # How long a simulated user should wait between executing tasks
    wait_time = between(3, 10)

    # A User will call its on_start method when it starts running
    def on_start(self):
        self.client.post("/books", {
            "isbn": "9781593275846",
            "title": "Eloquent JavaScript, Second Edition",
            "author": "Marijn Haverbeke"
        })

    # When a load test is started, an instance of a User class will be created for each simulated user.
    # Each user will start running within their own green thread.
    # When these users run they pick tasks that they execute, sleep for awhile, and then pick a new task and so on.
    @task
    def search_all(self):
        self.client.get("/books")

    @task
    def search_with_filter(self):
        self.client.get("/books?title=JavaScript")
