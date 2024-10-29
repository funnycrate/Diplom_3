from selenium import webdriver

class BrowserFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name.lower() == "chrome":
            return webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")

 