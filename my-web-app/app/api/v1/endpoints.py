from fastapi import APIRouter

router = APIRouter()

@router.get("/tech-stack")
async def get_tech_stack():
    # Logic to fetch and return tech stack data
    return {"message": "Tech stack data will be returned here."}

@router.get("/portfolio")
async def get_portfolio():
    # Logic to fetch and return portfolio data
    return {"message": "Portfolio data will be returned here."}