import os
from sqlalchemy import (
        MetaData, Table, Text,
        Column, DateTime, Integer
)
from datetime import datetime

metadata = MetaData()

def create_tables(engine, metadata):
    try:
        metadata.create_all(engine)
        return True, None
    except Exception as e:
        return False, e

quotes = Table('quotes', metadata,
Column('id', Integer(), primary_key=True),
Column('created_at', DateTime(), 
        default=datetime.now, 
        nullable=False),
Column('msg', Text(65535), nullable=False),
Column('source', Text(65535), nullable=False),
Column('source_material', Text(65535)),
Column('contributor', Text(65535)),
Column('contribution_method', Text(65535)),
Column('uses', Integer(), nullable=False))