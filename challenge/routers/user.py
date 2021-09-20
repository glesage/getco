from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..hashing import Hash
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/users',
    tags=['Users'])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['Users'])
def createUser(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        firstName=request.firstName,
        lastName=request.lastName,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['Users'])
def showUser(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not find user with ID {id}')
    return user
