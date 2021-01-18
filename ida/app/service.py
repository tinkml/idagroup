from typing import Optional, List

from django.db.models import Prefetch

from .models import Image, ResizedImage


class ServiceImage:

    @staticmethod
    def create(data: dict) -> Image:
        return Image.objects.create(**data)

    @staticmethod
    def get_by_name(name: str) -> Optional[Image]:
        return Image.objects.filter(name=name).first()

    @staticmethod
    def get_all_images() -> List[Image]:
        return Image.objects.all()


class ServiceResizedImage:

    @staticmethod
    def create(data: dict) -> ResizedImage:
        return ResizedImage.objects.create(**data)

    @staticmethod
    def get_by_name(name: str) -> Optional[ResizedImage]:
        return ResizedImage.objects.filter(name=name).get()

    @staticmethod
    def get_all_images() -> List[ResizedImage]:
        return ResizedImage.objects.all()

