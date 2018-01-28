#!/bin/bash
PY_FILES=`find . -name 'tests' -prune -o -name '*.py' -print`

lint_file() {
  printf "###### Linting $1 ######\n"
  pylint $1
  return_code=$?
  if [ $return_code != 0 ]; then
    exit $return_code
  fi
  printf "\n"
}

for file in $PY_FILES; do
  lint_file $file
done
