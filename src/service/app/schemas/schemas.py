from pydantic import BaseModel


class RecognitionResponse(BaseModel):
    plate_number: str
    status: str = "success"

    class Config:
        schema_extra = {
            "example": {
                "plate_number": "А123БВ77",
                "status": "success"
            }
        }