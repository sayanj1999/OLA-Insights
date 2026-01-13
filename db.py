from sqlalchemy import create_engine

def get_engine():
    engine = create_engine(
        "postgresql://postgres:post#@localhost:5432/ola_insights_db"
    )
    return engine
