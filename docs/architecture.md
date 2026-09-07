# Architecture

Offline: authored documents → LangChain loaders → metadata → recursive chunks → embeddings → persisted Chroma.

Online: question + history → query rewrite → persisted Chroma → similarity retrieval → relevance gate → grounded prompt → structured response → citations.

The index is built separately and never re-embedded per query.