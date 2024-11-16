from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select

# FastAPI app
app = FastAPI()

# Database connection setup
DATABASE_URL = "mysql+pymysql://root@localhost/test_db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
people = Table("people", metadata, autoload_with=engine)

# Request body schema
class EmailRequest(BaseModel):
    email: EmailStr

@app.get("/people")
async def get_person_by_email(request: EmailRequest):
    with engine.connect() as conn:
        # Use *people.c to select all columns
        query = select(*people.c).where(people.c.email == request.email)
        result = conn.execute(query).fetchone()

        if result is None:
            raise HTTPException(status_code=404, detail="Person not found")

        # Convert Row object to dictionary
        return dict(result._asdict())

@app.get("/emails")
async def get_all_emails():
    with engine.connect() as conn:
        # Query to select only the email column
        query = select(people.c.email)
        result = conn.execute(query).fetchall()

        # If no emails are found
        if not result:
            raise HTTPException(status_code=404, detail="No emails found")

        # Return the list of emails
        emails = [row[0] for row in result]  # Extract emails from the result set
        return {"emails": emails}
