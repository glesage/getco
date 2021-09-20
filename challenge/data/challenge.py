from fastapi import status, HTTPException
from .. import schemas
from .. import models
from sqlalchemy.orm import Session


def create(request: schemas.Challenge, db: Session):
    new_challenge = models.Challenge(
        title=request.title,
        description=request.description,
        author_user_id=request.author_user_id
    )
    db.add(new_challenge)
    db.commit()
    db.refresh(new_challenge)
    return new_challenge


def read(db: Session, id=None):
    if not id:
        return db.query(models.Challenge).all()
    else:
        challenge = db.query(models.Challenge).filter(models.Challenge.id == id).first()
        if not challenge:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not find challenge with ID {id}')
        return challenge


def update(id: int, request: schemas.Challenge, db: Session):
    challenges = db.query(models.Challenge).filter(models.Challenge.id == id)
    if not challenges.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not update challenge with ID {id}')
    challenges.update(request.dict())
    db.commit()
    db.refresh(challenges.first())
    return challenges.first()


def destroy(id: int, db: Session):
    affected_rows = db.query(models.Challenge).filter(models.Challenge.id == id).delete(synchronize_session=False)
    if not affected_rows:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not delete challenge with ID {id}')
    else:
        db.commit()
