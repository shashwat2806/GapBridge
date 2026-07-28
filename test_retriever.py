from rag.retriever import retrieve_context

results = retrieve_context("no incident response procedure documented")
for i, chunk in enumerate(results, 1):
    print(f"--- Chunk {i} ---")
    print(chunk[:200])
    print()