import importlib
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent))

modules_to_test = [
    "app.config",
    "app.db.database",
    "app.services.embeddings",
    "app.services.qdrant_store",
    "app.services.dag",
    "app.services.assemble",
    "app.routers.auth",
    "app.routers.rationale",
    "app.routers.crawl",
    "app.routers.search",
    "app.routers.admin",
    "app.routers.assemble",
    "app.routers.behavior",
    "app.main"
]

def test_imports():
    for mod_name in modules_to_test:
        print(f"Testing import: {mod_name}...", end=" ", flush=True)
        try:
            importlib.import_module(mod_name)
            print("SUCCESS")
        except Exception as e:
            print(f"FAILED: {e}")

if __name__ == "__main__":
    test_imports()
