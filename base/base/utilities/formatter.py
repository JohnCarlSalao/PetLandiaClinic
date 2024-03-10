from rest_framework import serializers
import datetime 

class CustomDateFormatField(serializers.DateField):
    def to_internal_value(self, value):
        if value == "":
            return None  # Return None for empty strings
        try:
            # Parse the input date in 'YYYY/MM/DD' format
            date_obj = datetime.datetime.strptime(value, '%Y/%m/%d').date()
            return date_obj
        except ValueError:
            raise serializers.ValidationError("Invalid date format. Please use 'YYYY/MM/DD'.")