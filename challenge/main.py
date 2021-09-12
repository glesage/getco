from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', status_code=status.HTTP_200_OK)
def health(db: Session = Depends(get_db)):
    db.query(models.Challenge).count()
    return 'Ok'


@app.get('/challenges', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    challenges = db.query(models.Challenge).all()
    return challenges


@app.get('/challenges/{id}', status_code=status.HTTP_200_OK)
def findById(id: int, db: Session = Depends(get_db)):
    challenge = db.query(models.Challenge).filter(models.Challenge.id == id).first()
    if not challenge:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not find blog with ID {id}')
    return challenge


@app.post('/challenges', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Challenge, db: Session = Depends(get_db)):
    new_challenge = models.Challenge(
        title=request.title,
        description=request.description
    )
    db.add(new_challenge)
    db.commit()
    db.refresh(new_challenge)
    return new_challenge


@app.put('/challenges/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Challenge, db: Session = Depends(get_db)):
    challenges = db.query(models.Challenge).filter(models.Challenge.id == id)
    if not challenges.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not update blog with ID {id}')
    challenges.update(request.dict())
    db.commit()
    db.refresh(challenges.first())
    return challenges.first()


@app.delete('/challenges/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteById(id: int, db: Session = Depends(get_db)):
    affected_rows = db.query(models.Challenge).filter(models.Challenge.id == id).delete(synchronize_session=False)
    if not affected_rows:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Could not delete blog with ID {id}')
    else:
        db.commit()
