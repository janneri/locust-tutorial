import credentials

class Api:
    def __init__(self, client):
        self.client = client

    def add_book(self, library_guid, book_isbn, book_title):
        self.client.post("/books", auth=credentials.LIBRARIAN_AUTH, json={
            "library_guid": library_guid,
            "isbn": book_isbn,
            "title": book_title,
            "author": "Some Author"
        })
        return book_isbn

    def search_all(self):
        self.client.get("/books", auth=credentials.ONLINE_LIB_USER_AUTH)

    def search_by_title(self, title):
        self.client.get("/books?title=" + title, auth=credentials.ONLINE_LIB_USER_AUTH, name="/books?title=:title")

    def delete_book(self, book_isbn):
        # The name parameter groups the calls with different ISBNs to a single line in the report.
        self.client.delete("/books/" + book_isbn, auth=credentials.LIBRARIAN_AUTH, name="/books/:isbn")


