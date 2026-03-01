"""
Database Initialization Script for DAP
Executes init_db.sql to create all required tables and seed data
"""
import psycopg2
from psycopg2 import sql
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def init_database():
    """Initialize the DAP database with schema and seed data"""
    
    # Get connection from DATABASE_URL
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("ERROR: DATABASE_URL not found in .env")
        return False
    
    # Read the SQL initialization script
    sql_file_path = Path(__file__).parent / 'init_db.sql'
    
    if not sql_file_path.exists():
        print(f"ERROR: SQL file not found at {sql_file_path}")
        return False
    
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    
    try:
        # Connect to PostgreSQL
        print(f"Connecting to PostgreSQL at {db_url.split('@')[-1]}...")
        conn = psycopg2.connect(db_url)
        conn.autocommit = True
        cursor = conn.cursor()
        
        print("Executing database initialization script...")
        
        # Execute the SQL script
        cursor.execute(sql_script)
        
        print("Database initialized successfully!")
        print("\nDatabase Summary:")
        
        # Verify tables were created
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        
        tables = cursor.fetchall()
        print(f"   Created {len(tables)} tables:")
        for table in tables:
            print(f"   - {table[0]}")
        
        # Check site configuration
        cursor.execute("SELECT site_id, domain, name FROM sites;")
        sites = cursor.fetchall()
        print(f"\nRegistered Sites:")
        for site in sites:
            print(f"   - {site[2]} ({site[1]}) [ID: {site[0]}]")
        
        # Close connection
        cursor.close()
        conn.close()
        
        print("\nDatabase is ready for use!")
        return True
        
    except psycopg2.OperationalError as e:
        print(f"Connection Error: {e}")
        print("\nTroubleshooting:")
        print("   1. Ensure PostgreSQL is running")
        print("   2. Verify database 'dap_banking_demo' exists")
        print("   3. Check username/password in .env file")
        return False
        
    except psycopg2.Error as e:
        print(f"Database Error: {e}")
        return False
        
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("DAP Database Initialization")
    print("=" * 60)
    init_database()
