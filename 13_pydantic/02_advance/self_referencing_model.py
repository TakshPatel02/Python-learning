from typing import List , Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List["Comment"]] = None # self-referencing model , replies can contain list of comments , if no replies then it can be None

Comment.model_rebuild() # to handle self-referencing models we need to call model_rebuild method after the class definition

comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(
            id=2,
            content="First reply"
        )
    ]
)
print(comment)
# we can further nest comments in replies