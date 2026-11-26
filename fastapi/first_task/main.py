from fastapi import FastAPI, Response

books = [
    {
        "id": 1,
        "title": "Classical Physics",
        "author": "Issac Newton",
        "publisher": "Pearson",
        "year": 1875
    },
    
    {
        "id": 2,
        "title": "Modern Physics",
        "author": "Albert Einstein",
        "publisher": "Cambridge University Press",
        "year": 1920
    },
    
    {
        "id": 3,
        "title": "Quantum Mechanics",
        "author": "Niels Bohr",
        "publisher": "Oxford University Press",
        "year": 1925
    }
]

app = FastAPI(title="Book Directory API")

@app.get("/")
def index():
    return {"message": "Welcome to Book API"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/books")
def get_books():
    return {"books": books}

@app.get("/book/{title}")
def get_book_by_title(title: str, response: Response):
    filtered_books =  [book for book in books if book["title"].lower() == title.lower()]
    if not filtered_books:
        # Then, filtered books is falsy
        # it does not contains any book
        response.status_code = 404
        return {"error": f"No books found with title {title}"}
    # If this point is reached, it means filtered_books is truthy
    return filtered_books

