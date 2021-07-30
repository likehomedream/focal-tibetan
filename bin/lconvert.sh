#!/usr/bin/env bash

for qm in $(find ./ -type f -name '*.qm'); do
  lconvert $qm -o ${qm%.qm}.ts
done
