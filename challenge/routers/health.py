from fastapi import APIRouter, Depends, status
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Health'])


@router.get('/', status_code=status.HTTP_200_OK, tags=['Health'])
def health(db: Session = Depends(get_db)):
    db.query(models.Challenge).count()
    return 'Ok'
