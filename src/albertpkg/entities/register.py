from abc import ABC, abstractmethod
from albertpkg.entities.package import Package


class RegisterManager(ABC):
    @abstractmethod
    def add(self, package: Package):
        pass

    @abstractmethod
    def get(self, package: Package):
        pass

    @abstractmethod
    def remove(self, package: Package):
        pass

    @abstractmethod
    def update(self, package: Package):
        pass
