import pytest
import src.scrape_selenium as scrape_selenium

@pytest.fixture
def driver():
    driver = scrape_selenium.create_driver()
    yield driver
    scrape_selenium.close_driver(driver)

def test_search_in_python_org(driver):
    search_value="pycon"
    result = scrape_selenium.search_pythonorg( driver, search_value)
    title, page_source = result

    assert "Python" in title
    assert "No results found." not in page_source
