# import pydantic
from pydantic import BaseModel
from typing import List

class Change(BaseModel):
	FILE_PATH: str
	LINE_POSITION: int
	COMMENT_BODY: str

	def __str__(self):
		return str(self)

	def __repr__(self):
		return f"```suggestion{self}```"
	
class Answer(BaseModel):
	changes: List[Change]

	def __str__(self):
		return str(self)
	