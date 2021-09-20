from fastapi import APIRouter, Depends, status
from typing import List
from .. import schemas
from ..data import challenge
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/challenges',
    tags=['Challenges']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowChallenge])
def all(db: Session = Depends(get_db)):
    return challenge.read(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowChallenge)
def findById(id: int, db: Session = Depends(get_db)):
    return challenge.read(db, id)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Challenge, db: Session = Depends(get_db)):
    return challenge.create(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Challenge, db: Session = Depends(get_db)):
    challenge.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteById(id: int, db: Session = Depends(get_db)):
    challenge.destroy(id, db)
