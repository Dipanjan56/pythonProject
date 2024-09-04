from abc import ABC, abstractmethod

class WebDriver(ABC):

    """This means we must implement this method behavior in child classes as the implementation can be different for different classes"""
    @abstractmethod
    def click(self):
        pass


class ChromeDriver(WebDriver):

    def capturingScreenshot(self):
        print("Capturing screenshot")

    def click(self):
        print("Clicking in Chrome")


class FirefoxDriver(WebDriver):

    def capturingScreenshot(self):
        print("Capturing screenshot")


    def click(self):
        print("Clicking in Firefox")



obj = ChromeDriver()
obj.capturingScreenshot()
obj.click()

obj1 = FirefoxDriver()
obj1.click()