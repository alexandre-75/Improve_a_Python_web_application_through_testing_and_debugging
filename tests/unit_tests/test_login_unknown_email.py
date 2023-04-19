import server
from server import app


class TestLogin:

    client = app.test_client()

    def test_valid_email(self):

        """This method tests whether sending a valid email address
        to the /showSummary endpoint returns an HTTP status code of 200,
        indicating that the request was successfully processed."""

        result = self.client.post("/showSummary", data={"email": server.clubs[0]["email"]})
        assert result.status_code == 200

    def test_invalid_email(self):
        
        """This method tests whether sending an invalid email address
        to the /showSummary endpoint returns an HTTP status code of 403,
        indicating that the request was forbidden or denied."""
        
        result = self.client.post("/showSummary", data=dict(email="test_invalid_email"))
        assert result.status_code == 403

    def test_empty_email(self):
        
        """This method tests whether sending an empty string as an email address
        to the /showSummary endpoint returns an HTTP status code of 403,
        indicating that the request was forbidden or denied"""
        
        result = self.client.post("/showSummary", data={"email":" "})
        assert result.status_code == 403