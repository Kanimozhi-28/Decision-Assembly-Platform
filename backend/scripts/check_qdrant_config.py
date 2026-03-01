from qdrant_client import QdrantClient

client = QdrantClient(url="http://10.100.20.76:6333")
collection_name = "dap_products"

    output = f"""
Collection: {collection_name}
Points count: {info.points_count}
Status: {info.status}
Params: {info.config.params}
HNSW Config: {info.config.hnsw_config}
Optimizer Config: {info.config.optimizer_config}
Wal Config: {info.config.wal_config}
Payload Schema: {info.payload_schema}
"""
    with open("qdrant_config_log.txt", "w") as f:
        f.write(output)
    print(output)
    
except Exception as e:
    with open("qdrant_config_log.txt", "w") as f:
        f.write(f"Error: {e}")
    print(f"Error: {e}")
