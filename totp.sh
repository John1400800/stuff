#!/usr/bin/env bash
set -euo pipefail

# ---- usage ----
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 BASE32_SECRET" >&2
    exit 1
fi

SECRET="$1"

# ---- normalize & decode base32 secret ----
keyhex=$(
    printf '%s' "$SECRET" \
    | tr -d ' ' \
    | tr '[:lower:]' '[:upper:]' \
    | base32 -d \
    | od -An -v -t x1 \
    | tr -d ' \n'
)

# ---- time counter (30s period) ----
counterhex=$(printf '%016x' $(( $(date +%s) / 30 )))

# ---- HMAC-SHA1 ----
hmachex=$(
    printf '%b' "$(printf '%s' "$counterhex" | sed 's/../\\x&/g')" \
    | openssl dgst -sha1 -mac HMAC -macopt hexkey:"$keyhex" -binary \
    | od -An -v -t x1 \
    | tr -d ' \n'
)

# ---- dynamic truncation ----
offset=$(( 0x${hmachex: -2} & 0x0f ))
part=${hmachex:$((offset * 2)):8}

# ---- 6-digit TOTP ----
code=$(( (0x$part & 0x7fffffff) % 1000000 ))
printf '%06d\n' "$code"
