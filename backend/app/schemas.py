from pydantic import BaseModel


class QRCreate(BaseModel):
    title: str
    destination_url: str


class QRResponse(BaseModel):
    qr_id: str
    short_code: str
    title: str
    destination_url: str
    status: str

    class Config:
        from_attributes = True