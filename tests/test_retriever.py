from src.retrieval.retriever import Retriever


def test_retriever_initializes():
    retriever = Retriever()
    assert retriever is not None


def test_retrieval_returns_results():
    retriever = Retriever()
    results = retriever.retrieve(query="Who developed BERT?",top_k=3)
    assert len(results) > 0


def test_top_k_limit():
    retriever = Retriever()
    results = retriever.retrieve(query="Who developed BERT?",top_k=3)
    assert len(results) <= 3


def test_result_schema():
    retriever = Retriever()
    result = retriever.retrieve(query="Who developed BERT?",top_k=1)[0]
    assert hasattr(result,"document_title")
    assert hasattr(result,"text")
    assert hasattr(result,"score")