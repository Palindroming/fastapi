from fastapi import APIRouter

router  = APIRouter()

@router.get('/hello')
def say_hello():
    return{"message:" "hello"}


@router.get('/goodbye')
def say_goodbye():
    return{"message": "goodbye"}