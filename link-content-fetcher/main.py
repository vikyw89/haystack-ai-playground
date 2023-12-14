from haystack import Pipeline
from haystack.document_stores import InMemoryDocumentStore
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.converters import HTMLToDocument
from haystack.components.writers import DocumentWriter

document_store = InMemoryDocumentStore()
fetcher = LinkContentFetcher()
converter = HTMLToDocument()
writer = DocumentWriter(document_store = document_store)

indexing_pipeline = Pipeline()
indexing_pipeline.add_component(instance=fetcher, name="fetcher")
indexing_pipeline.add_component(instance=converter, name="converter")
indexing_pipeline.add_component(instance=writer, name="writer")

indexing_pipeline.connect("fetcher.streams", "converter.sources")
indexing_pipeline.connect("converter.documents", "writer.documents")

indexing_pipeline.run(data={"fetcher": {"urls": ["https://haystack.deepset.ai/blog/guide-to-using-zephyr-with-haystack2"]}})
print(indexing_pipeline.graph)
print(indexing_pipeline.draw("indexing_pipeline.png"))
print(indexing_pipeline.dumps())