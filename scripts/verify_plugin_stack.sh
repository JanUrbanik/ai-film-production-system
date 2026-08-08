#!/usr/bin/env bash
# verify_plugin_stack.sh — health-check Grok marketplace integration for this factory
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PATH="${HOME}/.grok/bin:${HOME}/.local/bin:${PATH}"

PASS=0
FAIL=0
WARN=0

pass() { echo "PASS  $*"; PASS=$((PASS+1)); }
fail() { echo "FAIL  $*"; FAIL=$((FAIL+1)); }
warn() { echo "WARN  $*"; WARN=$((WARN+1)); }

echo "=== AI Film Production System — plugin stack verify ==="
echo "root: $ROOT"
echo

# 1) Repo integration files
for f in \
  "02_Tools/plugins/GROK_MARKETPLACE_INTEGRATION.md" \
  "02_Tools/plugins/INSTALLED_STACK.snapshot.json" \
  "05_Workflows/PLUGIN_AUGMENTED_RESEARCH.md" \
  "06_Skills/ops/PLUGIN_STACK.md" \
  ".grok/config.toml" \
  ".grok/rules.md"
do
  if [[ -f "$f" ]]; then pass "repo file $f"; else fail "missing $f"; fi
done

# 2) config declares stack
if grep -q 'superpowers' .grok/config.toml && grep -q 'tavily' .grok/config.toml; then
  pass ".grok/config.toml declares plugin stack"
else
  fail ".grok/config.toml missing plugin stack entries"
fi

# 3) grok CLI
if command -v grok >/dev/null 2>&1; then
  pass "grok CLI: $(grok --version 2>/dev/null | head -1)"
else
  fail "grok CLI not on PATH"
  echo "SUMMARY pass=$PASS fail=$FAIL warn=$WARN"
  exit 1
fi

# 4) plugins installed
PLIST="$(grok plugin list 2>&1 || true)"
for p in superpowers firecrawl tavily chrome-devtools; do
  if echo "$PLIST" | grep -qi "$p"; then pass "plugin installed: $p"; else fail "plugin missing: $p"; fi
done

# 5) mcp doctor
DOC="$(grok mcp doctor 2>&1 || true)"
echo "$DOC"
if echo "$DOC" | grep -q '0 failing'; then
  pass "mcp doctor: 0 failing"
else
  # parse failing count if present
  if echo "$DOC" | grep -Eq 'failing'; then
    fail "mcp doctor reports failures — re-auth MCP (tavily/firecrawl) or check chrome-devtools"
  else
    warn "could not parse mcp doctor failing count"
  fi
fi

for p in tavily firecrawl chrome-devtools; do
  if echo "$DOC" | grep -A2 "$p" | grep -q 'handshake OK'; then
    pass "mcp healthy: $p"
  else
    # chrome may appear as chrome-devtools
    if echo "$DOC" | grep -qi "handshake OK" && echo "$DOC" | grep -qi "$p"; then
      pass "mcp present: $p"
    else
      fail "mcp not healthy: $p"
    fi
  fi
done

echo
echo "SUMMARY pass=$PASS fail=$FAIL warn=$WARN"
if [[ "$FAIL" -gt 0 ]]; then
  exit 1
fi
exit 0
