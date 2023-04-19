from server import app


class TestLoginLogout:
    
    client = app.test_client()

    def test_login(self):
        
        """This method tests whether sending a GET request
        to the root URL / returns an HTTP status code of 200."""
        
        result = self.client.get("/")
        assert result.status_code == 200

    def test_logout(self):
        
        """This method tests if sending a GET request to the /logout URL returns an HTTP status code of 302,
        which indicates that the request was redirected to another page"""
        
        result = self.client.get("/logout")
        assert result.status_code == 302