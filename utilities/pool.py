from typing import Callable

from primitives.base import PrimitiveBase


class PrimitivePool:
    def __init__(self,
                 on_create: Callable,
                 on_get: Callable or None = None,
                 on_release: Callable or None = None):
        # on_create returns a PrimitiveBase
        self.__on_create = on_create
        self.__on_get = on_get
        self.__on_release = on_release
        self.__internal_buffer = []
        pass

    def get(self) -> PrimitiveBase:
        if len(self.__internal_buffer) == 0:
            new_object = self.__on_create()
            self.__internal_buffer.append(new_object)

        result = self.__internal_buffer.pop(0)
        if self.__on_get:
            self.__on_get(result)
        return result

    def release(self, instance):
        if self.__on_release:
            self.__on_release(instance)
        self.__internal_buffer.append(instance)
        pass
