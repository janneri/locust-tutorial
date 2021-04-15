const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Database
let books = [];

// Add a middleware to make it handle json
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


app.post('/books', (req, res) => {
    const book = req.body;
    console.log(book);
    books.push(book);

    res.send('Book is added to the database');
});

app.get('/books', (req, res) => {
    const title = req.query.title;
    if (title) {
        res.json(books.filter(b => b.title && b.title.includes(title)))
    }
    else {
        res.json(books);
    }
});

app.delete('/books/:isbn', (req, res) => {
    books = books.filter(b => b.isbn !== req.params.isbn);
    res.send('Book was deleted from the database');
});


app.listen(port, () => console.log(`App listening on port ${port}!`))