#!/usr/bin/env sh
ROOT="$(pwd -P)"
printf "Building Distribution at: %s\n" "$ROOT"

DIST="$ROOT/temp"
PKG="$DIST/src/django_tasks_cloud"

PACKAGE_DIRS="base aws azure"
ROOT_FILES="pyproject.toml README.md LICENSE"

if [ -d "$DIST" ]; then
  rm -rf "$DIST"
fi

mkdir -p "$PKG"
touch "$PKG/__init__.py"

for name in $PACKAGE_DIRS; do
  src="$ROOT/$name"
  if [ -d "$src" ]; then
    cp -R "$src" "$PKG/$name"
  fi
done

for name in $ROOT_FILES; do
  src="$ROOT/$name"
  if [ -f "$src" ]; then
    cp -p "$src" "$DIST/$name"
  fi
done

mkdir -p "$DIST/tests"
uv build "$DIST"
