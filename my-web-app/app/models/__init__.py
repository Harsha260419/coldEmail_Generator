from pydantic import BaseModel

# Define your data models or schemas here
class TechStack(BaseModel):
    tech_stack: str
    portfolio_url: str

class JobPosting(BaseModel):
    job_title: str
    job_description: str
    job_location: str
    job_type: str
    skills_required: list[str]