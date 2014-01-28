#!/bin/bash
echo "bash:"
for a in 1 2 3; do
	for b in a b c; do
		echo -e "\t$a $b"
	done
done