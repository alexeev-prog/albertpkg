from albertpkg.entities.package import Package, GitRepository
from rich import print

package = Package(
    "albertpkg-base",
    "0.1.0",
    "alexeev-prog",
    GitRepository(
        "https://github.com/alexeev-prog/albertpkg",
        "16ba01e19248fe7d4976d3a673a4059c079ce328",
        "main",
    ),
    description="Base package for AlbertPKG",
)


def main() -> None:
    print(package)
