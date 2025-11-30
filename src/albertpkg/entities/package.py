from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
from datetime import datetime


class PackageStatus(Enum):
    INSTALLED = "installed"
    OUTDATED = "outdated"
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


@dataclass
class GitRepository:
    url: str
    commit_hash: str
    branch: str = "main"


@dataclass
class Package:
    name: str
    version: str
    author: str
    repository: GitRepository
    package_hash: str = None
    description: str = ""
    dependencies: list[str] = None
    installed_at: datetime = None
    status: PackageStatus = PackageStatus.AVAILABLE

    def __post_init__(self):
        if self.dependencies is None:
            object.__setattr__(self, "dependencies", [])

        if self.package_hash is None:
            object.__setattr__(
                self,
                "package_hash",
                sha256(
                    f"{self.author}_{self.name}_{self.repository.url}".encode("utf-8")
                ).hexdigest(),
            )
