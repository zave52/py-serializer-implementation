import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    content = JSONRenderer().render(serializer.data)
    return content


def deserialize_car_object(json: bytes) -> Car:
    content = io.BytesIO(json)
    data = JSONParser().parse(content)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car.objects.create(**serializer.data)
    return serializer.errors
