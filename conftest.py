pytest_plugins = [
	"ecommerce_api.tests.selenium",
]

def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )