from locust import HttpUser, task, between


class LocustTestServer(HttpUser):

    wait_time = between(1, 5)

    def on_start(self):
        self.client.get("/", name="Index")

    @task
    def get_summary(self):
        self.client.post("/showSummary", data={'email': "john@simplylift.co"},  name="Show_Summary")
  
    @task
    def get_booking(self):
        self.client.get("/book/FallClassic/Simply_Lift", name="book")

    @task
    def post_booking(self):
        self.client.post("/purchasePlaces", data={"places": 0, "club": "Simply_Lift", "competition": "FallClassic"}, name="purchase_places")

    @task
    def get_board(self):
        self.client.get("/points", name="points")
