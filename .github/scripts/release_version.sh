#!/usr/bin/env bash
# Print the version a release run publishes, and write it to pyproject.toml for the build.
# Run from the CIM-Graph checkout: release_version.sh develop|main
#
# pyproject.toml holds the next release target X.Y.Z. The published version is derived from
# what is already released (PyPI and the v* git tags) and is never committed, so nothing
# pushes to the protected branches:
#
#   develop  the next free alpha of the target: 0.6.0a1 released -> 0.6.0a2
#   main     the target itself: 0.6.0
#
# Once the target is released, both branches move on to the next patch (0.6.1a1, 0.6.1).
# Bump the target in a PR for a minor or major release.
set -euo pipefail

branch=$1
if [[ $branch != develop && $branch != main ]]; then
    echo "::error::Releases run from develop or main, not $branch" >&2
    exit 1
fi

target=$(uv version --short)
if [[ ! $target =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "::error::pyproject.toml version must be the next release target X.Y.Z, got $target" >&2
    exit 1
fi

# Tags cover a release this workflow made moments ago that PyPI's JSON API does not show yet
pypi=$(curl --silent --fail https://pypi.org/pypi/cim-graph/json | jq -r '.releases | keys[]')
released=$(printf '%s\n' "$pypi"; git tag --list 'v*' | sed 's/^v//')

while grep --quiet --line-regexp --fixed-strings "$target" <<< "$released"; do
    target=$(uv version --bump patch --frozen --short)
done

if [[ $branch == main ]]; then
    version=$target
else
    last_alpha=$(grep --extended-regexp "^${target//./\\.}a[0-9]+$" <<< "$released" \
                 | sed 's/.*a//' | sort --numeric-sort | tail -1 || true)
    version="${target}a$(( ${last_alpha:-0} + 1 ))"
fi

uv version "$version" --frozen > /dev/null
echo "$version"
