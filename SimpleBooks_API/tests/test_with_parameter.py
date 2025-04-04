import pytest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestDebug():

    @pytest.mark.debugparam
    @pytest.mark.parametrize("book_type", [11, "comedy", True])
    def test_get_list_of_books_filter_by_invalid_type(self, book_type):
        response = SimpleBooksRequests.get_list_of_books(type=book_type)
        expected_error_message = "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."
        assert response.status_code == 400, "Unexpected status code"
        assert response.json()["error"] == expected_error_message, "Unexpected error message"
