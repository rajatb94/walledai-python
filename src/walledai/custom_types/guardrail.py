from typing import List
from typing_extensions import TypedDict, NotRequired

class SafetyItem(TypedDict):
    safety: str
    isSafe: bool
    score: int

class GreetingItem(TypedDict):
    greeting_type: str
    isPresent: bool

class Data(TypedDict):
    safety: NotRequired[List[SafetyItem]]  # Optional field
    compliance: NotRequired[List]  # Optional field, empty list
    pii: NotRequired[List]  # Optional field, empty list
    greetings: NotRequired[List[GreetingItem]]  # Optional field

class GuardRailResponse(TypedDict):
    success:bool
    data: NotRequired[Data]
    error:NotRequired[Exception]