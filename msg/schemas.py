from pydantic import BaseModel


class MSG(BaseModel):
    id: int
    msg_id: str
    msg_str_bo_CN: str
    msg_str_zh_CN: str

    class Config:
        orm_mode = True
