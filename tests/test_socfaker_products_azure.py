def test_socfaker_products_azure_vm(socfaker_fixture):
    assert socfaker_fixture.products.azure.vm

def test_socfaker_products_azure_vm_details(socfaker_fixture):
    assert socfaker_fixture.products.azure.vm.details

def test_socfaker_products_azure_vm_metrics(socfaker_fixture):
    assert socfaker_fixture.products.azure.vm.metrics

#def test_socfaker_products_azure_vm_metrics_average(socfaker_fixture):
#    assert socfaker_fixture.products.azure.vm.metrics.average

#def test_socfaker_products_azure_vm_metrics_graphs(socfaker_fixture):
#    assert socfaker_fixture.products.azure.vm.metrics.graphs

def test_socfaker_products_azure_vm_topology(socfaker_fixture):
    assert socfaker_fixture.products.azure.vm.topology

#def test_socfaker_products_azure_vm_topology_graphic(socfaker_fixture):
 #   assert socfaker_fixture.products.azure.vm.topology_graphic()
