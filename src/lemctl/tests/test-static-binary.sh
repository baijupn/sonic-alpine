#!/bin/bash
set -euo pipefail

binary=${1:?Usage: test-static-binary.sh /path/to/lemctl}
headers=$(readelf --program-headers "$binary")
dynamic=$(readelf --dynamic "$binary")
if grep -q 'INTERP' <<<"$headers" || grep -q '(NEEDED)' <<<"$dynamic"; then
    echo "Expected a static lemctl without an ELF interpreter or shared-library dependencies: $binary" >&2
    exit 1
fi
