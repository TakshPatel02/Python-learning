from pydantic  import BaseModel , computed_field , Field

class Product(BaseModel):
    price : float
    quantity : int

    @computed_field # computed_field decorator is used to define a computed property in pydantic model
    @property # property decorator makes field accessible like an attribute
    def total_price(self) -> float:
        return self.price * self.quantity
    
class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(... , ge= 1) # nights must be at least 1
    price_per_night : float 

    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.price_per_night
    
booking = Booking(
    user_id= 123,
    room_id= 202,
    nights= 3,
    price_per_night= 180.0
)
print(booking) # user_id=123 room_id=202 nights=3 price_per_night=180.0 total_cost=540.0
print(booking.model_dump())