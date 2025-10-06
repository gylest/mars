import unittest
import src.scrape_selenium as scrape_selenium

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = scrape_selenium.create_driver()

    def test_search_in_python_org(self):
        search_value="pycon"
        result = scrape_selenium.search_pythonorg( self.driver, search_value)
        title, page_source = result

        self.assertIn("Python", title)
        self.assertNotIn("No results found.", page_source)

    def tearDown(self):
        scrape_selenium.close_driver(self.driver)

#
# If this run as startup file, the if statement is true and the main() is called.
# This will run all tests within class and print report at the end.
#
if __name__ == "__main__":
    unittest.main()
