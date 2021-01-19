import uvicorn
from app.app import app
from app.schema import OwidCovidData as SchemaOwidCovidData
from app.models import OwidCovidData as ModelOwidCovidData
from datetime import date

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/owidCovidData")
async def create_data(data: SchemaOwidCovidData):
    status = await ModelOwidCovidData.create(**data.dict())
    return status


@app.get("/owidCovidData", response_model=SchemaOwidCovidData)
async def get_data(iso_code: str, continent: str, location: str, date: date):
    data = await ModelOwidCovidData.get(iso_code=iso_code, continent=continent, location=location, date=date)
    return SchemaOwidCovidData(**data).dict()


@app.put("/owidCovidData")
async def update_data(inData: SchemaOwidCovidData):
    status = await ModelOwidCovidData.update(**inData.dict())
    return status


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
