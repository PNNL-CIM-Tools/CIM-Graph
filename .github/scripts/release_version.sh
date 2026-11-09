#!/usr/bin/env bash
# Set the version a release run publishes, in pyproject.toml and uv.lock, and print it.
# Run from the CIM-Graph checkout: release_version.sh develop|main
#
#   develop  the next pre-release: 0.6.0a1 -> 0.6.0a2 (and b1 -> b2, rc1 -> rc2). Once the
#            stable 0.6.0 is out, or from a stable version: 0.6.0 -> 0.6.1a1.
#   main     the stable version: 0.6.0a2 -> 0.6.0. Fails if that is already released.
#
# A version that is not released yet (no git tag, not on PyPI) is published as it is, so a
# version set by hand, e.g. 1.0.0rc1, goes out unchanged.
set -euo pipefail

branch=$1
prerelease='(a|b|rc)[0-9]+$'

released() {
    git rev-parse --quiet --verify "refs/tags/v$1" > /dev/null \
        || curl --silent --fail --output /dev/null "https://pypi.org/pypi/cim-graph/$1/json"
}

bump() {
    uv version --no-sync "$@" > /dev/null  # writes pyproject.toml and re-locks uv.lock
}

version=$(uv version --short)
case $branch in
    develop)
        if released "$version"; then
            if [[ $version =~ $prerelease ]] && ! released "$(uv version --short --bump stable --dry-run)"; then
                declare -A kinds=([a]=alpha [b]=beta [rc]=rc)
                bump --bump "${kinds[${BASH_REMATCH[1]}]}"
            else
                bump --bump patch --bump alpha
            fi
        fi
        ;;
    main)
        if [[ $version =~ $prerelease ]]; then
            bump --bump stable
        fi
        if released "$(uv version --short)"; then
            echo "::error::$(uv version --short) is already released: set the next version in pyproject.toml" >&2
            exit 1
        fi
        ;;
    *)
        echo "::error::Releases run from develop or main, not $branch" >&2
        exit 1
        ;;
esac
uv version --short
