from ..models import User
from sqlalchemy.orm import Session


def get_all(db: Session):
    return db.query(User).all()
