import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def chrome_browser_instance(request):
	""" 
	provides a selenium web driver instance
	"""

	options = Options()
	options.headless = False
	browser = webdriver.chrome(chrome_options=options)
	yield browser
	browser.close()