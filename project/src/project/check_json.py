# import pydantic
from pydantic import BaseModel
# from typing import List, Dict, Any

class Answer(BaseModel):
	FILE_PATH: str
	LINE_POSITION: int
	COMMENT_BODY: str

	def __str__(self):
		return str(self)

	def __repr__(self):
		return f"```suggestion{self}```"