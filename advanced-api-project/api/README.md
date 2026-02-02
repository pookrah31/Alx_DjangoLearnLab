ListView (BookListView)

Purpose: Get all books

Permissions: Anyone

URL: /api/books/

DetailView (BookDetailView)

Purpose: Get one book

Permissions: Anyone

URL: /api/books/<id>/

CreateView (BookCreateView)

Purpose: Add new book

Permissions: Authenticated only

URL: /api/books/create/

Validation: publication_year must not be in the future

UpdateView (BookUpdateView)

Purpose: Update book details

Permissions: Authenticated only

URL: /api/books/<id>/update/

DeleteView (BookDeleteView)

Purpose: Remove a book

Permissions: Authenticated only

URL: /api/books/<id>/delete/