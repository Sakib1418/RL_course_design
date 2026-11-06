#!/usr/bin/env bash
# Build the site and publish _site/ to the gh-pages branch, which GitHub Pages serves at
#   https://sakib1418.github.io/RL_course_design/
# Usage (Git Bash):  bash course_site/publish.sh
set -euo pipefail
cd "$(dirname "$0")"
python build.py

REMOTE=$(git -C .. remote get-url origin)
NAME=$(git -C .. config user.name)
EMAIL=$(git -C .. config user.email)
STAGE=${PUBLISH_TMP:-$(mktemp -d)}/gh-pages-stage
rm -rf "$STAGE" && mkdir -p "$STAGE"
cp -r _site/. "$STAGE"/

cd "$STAGE"
git init -q -b gh-pages
git add -A
git -c user.name="$NAME" -c user.email="$EMAIL" commit -q -m "Publish course site $(date -u +%Y-%m-%dT%H:%MZ)"
git push -f "$REMOTE" gh-pages
echo "Published. Live in ~1 minute: https://sakib1418.github.io/RL_course_design/"
