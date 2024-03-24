from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session

from app.routes.deps import get_db_session
from app.schemas.category import Category, CategoryOutput
from app.use_cases.category import CategoryUseCases

router = APIRouter(prefix="/category", tags=["Category"])


@router.post("/add")
def add_category(category: Category, db_session: Session = Depends(get_db_session)):
    uc = CategoryUseCases(db_session=db_session)
    uc.add_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)
