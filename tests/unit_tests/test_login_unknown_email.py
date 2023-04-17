import server
from server import app


class TestLogin:

    client = app.test_client()

    def test_valid_email(self):
        result = self.client.post("/showSummary", data={"email": server.clubs[0]["email"]})
        assert result.status_code == 200

    def test_invalid_email(self):
        result = self.client.post("/showSummary", data=dict(email="test_invalid_email"))
        assert result.status_code == 403

    def test_empty_email(self):
        result = self.client.post("/showSummary", data={"email":" "})
        assert result.status_code == 403