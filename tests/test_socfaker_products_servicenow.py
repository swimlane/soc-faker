def test_socfaker_products_servicenow_search(socfaker_fixture):
    assert socfaker_fixture.products.servicenow.search()
