def test_socfaker_products_qualysguard_scan(socfaker_fixture):
    assert socfaker_fixture.products.qualysguard.scan(count=1)
