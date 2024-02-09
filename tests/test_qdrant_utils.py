from esg_toolkit.src import QdrantExecutor


os.environ["QDRANT_URI"] = "0.0.0.0:6333"
qdrant_executor = QdrantExecutor()
