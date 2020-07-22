def test_socfaker_products_elastic_document_get(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.get(count=1)

def test_socfaker_products_elastic_document_fields_agent(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.agent

def test_socfaker_products_elastic_document_fields_base(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.base
   
def test_socfaker_products_elastic_document_fields_client(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.client

def test_socfaker_products_elastic_document_fields_container(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.container

def test_socfaker_products_elastic_document_fields_destination(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.destination

def test_socfaker_products_elastic_document_fields_dll(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.dll

def test_socfaker_products_elastic_document_fields_dns(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.dns

def test_socfaker_products_elastic_document_fields_event(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.event

def test_socfaker_products_elastic_document_fields_file(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.file

def test_socfaker_products_elastic_document_fields_host(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.host

def test_socfaker_products_elastic_document_fields_http(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.http

def test_socfaker_products_elastic_document_fields_network(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.network

def test_socfaker_products_elastic_document_fields_organization(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.organization

def test_socfaker_products_elastic_document_fields_package(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.package

def test_socfaker_products_elastic_document_fields_registry(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.registry

def test_socfaker_products_elastic_document_fields_server(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.server

def test_socfaker_products_elastic_document_fields_source(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.source

def test_socfaker_products_elastic_document_fields_cloud(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.cloud

def test_socfaker_products_elastic_document_fields_code_signature(socfaker_fixture):
   assert socfaker_fixture.products.elastic.document.fields.code_signature
