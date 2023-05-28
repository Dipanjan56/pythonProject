def get_author_record_endpoint():
    return '/api/v1/Authors'


def create_author_record_endpoint():
    return '/api/v1/Authors'


def get_author_record_by_id_endpoint(id):
    return f'/api/v1/Authors/{id}'


def get_book_record_by_id_endpoint(book_id):
    return f'/api/v1/Authors/authors/books/{book_id}'


def update_author_record_endpoint(id):
    return f'/api/v1/Authors/{id}'


def delete_author_record_endpoint(id):
    return f'/api/v1/Authors/{id}'
