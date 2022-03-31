class BasePage():
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
