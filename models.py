from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True)
    linkedin_url = Column(Text)
    linkedin_id = Column(Text)
    status = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


class ExtractedData(Base):
    __tablename__ = "extracted_data"

    id = Column(Integer, primary_key=True)

    source_id = Column(Integer)

    linkedin_id = Column(Text)

    raw_response = Column(JSON)

    # headline = Column(Text)

    # about = Column(Text)

    # skills = Column(JSON)

    status = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

class Destination(Base):
    __tablename__ = "destination"

    id = Column(Integer, primary_key=True)

    linkedin_id = Column(Text, unique=True)

    first_name = Column(Text)
    last_name = Column(Text)

    headline = Column(Text)
    about = Column(Text)

    skills = Column(Text)

    certifications = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )