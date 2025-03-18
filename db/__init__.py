from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///./nt_msg.decrypt.db")
session = Session(engine)
