from locust import HttpUser, between, task
import api
import testdata


class OnlineLibraryUser(HttpUser):
    wait_time = between(3, 10)
    # How many users of this type are spawned compared to other users.
    weight = 2

    def on_start(self):
        self.api = api.Api(self.client)

    @task
    def search_all(self):
        self.api.search_all()

    @task
    def search_with_filter(self):
        self.api.search_by_title("JavaScript")


class LibraryAdminUser(HttpUser):
    wait_time = between(3, 10)
    weight = 1

    def on_start(self):
        self.api = api.Api(self.client)
        self.my_books = []

    @task
    def add_books(self):
        self.my_books.append(
            self.api.add_book(testdata.get_random_existing_library_guid(),
                              testdata.get_next_isbn(),
                              testdata.get_random_book_title())
        )

    def on_stop(self):
        print("stopping")
        [self.api.delete_book(isbn) for isbn in self.my_books]

