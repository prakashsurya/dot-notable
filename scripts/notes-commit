#!/bin/bash -ex

TOP=$(git rev-parse --show-toplevel 2>/dev/null)

if [[ -z "$TOP" ]]; then
	echo "Must be run inside the git repsitory."
	exit 1
fi

if [[ $EUID -eq 0 ]]; then
	echo "This script must not be run as root." 1>&2
	exit 1
fi

git commit --allow-empty-message -m ''
