#!/bin/bash

sed_cmd="sed"

os="$(uname -s)"

if [[ "$os" == "Darwin" ]]; then
	if ! command -v gsed > /dev/null 2>&1; then
    brew install gnu-sed
	fi
	sed_cmd="gsed"
fi

mvn eclipse:clean
mvn eclipse:eclipse

# remove path from .classpath
$sed_cmd -i '/src\/main\/java\/generated/d' ./.classpath
