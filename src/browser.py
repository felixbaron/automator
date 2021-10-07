"""Automate the browser with Selenium
"""

from selenium import webdriver
import pickle


class Browser:
    """Create Selenium browser object
    Usage:::
        from automator import Browser
        b = Browser()
        b.launch()
        b.run_script('/path/to/script')
    """

    def __init__(self):
        self.driver = None

    def save_browser_instance(self):
        """Persitantly save the driver with help of pickle"""
        # TODO: implement Pickle
        pass

    def launch(self):
        """Launch Chrome browser"""
        options = webdriver.ChromeOptions()
        options.add_extension("./Wizmage-Image-Hider.crx")
        self.driver = webdriver.Chrome(
            executable_path="./chromedriver", options=options
        )
