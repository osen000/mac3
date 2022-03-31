def test_first(driver):
    driver.get(driver.base_url)
    assert "Store" in driver.title
