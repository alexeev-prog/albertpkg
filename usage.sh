#!/usr/bin/env bash
set -e
set -u
set -o pipefail

# Register

## Add
albertpkg register add --file albertpkg.albman
albertpkg register add --name albertpkg --author alexeev-prog --url https://github.com/alexeev-prog/albertpkg

## Get
albertpkg register get --package_hash "826a876f6eba6bce3374308c340b73c36428509932b5f1955b4b50e66ebd0c39"
albertpkg register get alexeev-prog.albertpkg
albertpkg register get --file albertpkg.albman

## Remove
albertpkg register remove --package_hash "826a876f6eba6bce3374308c340b73c36428509932b5f1955b4b50e66ebd0c39"
albertpkg register remove alexeev-prog.albertpkg
albertpkg register remove --file albertpkg.albman

## Update
albertpkg register update --file albertpkg.albman
albertpkg register update alexeev-prog.albertpkg --author alexeev-prog --name albertpkg_core --url https://github.com/alexeev-prog/albertpkg


