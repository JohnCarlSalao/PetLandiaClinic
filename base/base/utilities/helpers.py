from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_birthday(value):
    """
    Validate that the birthday is not in the future.
    """
    today = timezone.localdate()
    if value > today:
        raise ValidationError("Birthday cannot be in the future.")
    return value

def validate_past(value):
    today = timezone.localdate()
    if value > today:
        raise ValidationError("Date Can't be in the future")
    
def validate_future(value):
    today = timezone.localdate()
    if value < today:
        raise ValidationError("Date Can't be in the past")