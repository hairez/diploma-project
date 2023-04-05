#!/usr/bin/env bash

PPATH=$(realpath ..)

REQUIRE_SAMPLE_REUSE=0
. ../../testdata_tools/gen.sh

use_solution jonathan.cpp

compile gen.py

samplegroup
sample 1
sample 2

group g1 20
limits maxn=2
tc tinyn1 gen n=1
tc tinyn2 gen n=2
tc tinyn3 gen n=2
tc tinyn4 gen n=2

group g2 20
limits reversed=1
tc reversed1 gen reversed=1 n=1000 max_ai=1000
tc reversed2 gen reversed=1 n=10000 max_ai=1000
tc reversed3 gen reversed=1 max_ai=1000
tc reversed4 gen reversed=1

group g3 20
limits maxn=1000
tc smalln1 gen n=1000
tc smalln2 gen n=1000
tc smalln3 gen n=1000
tc smalln4 gen n=1000

group g4 40
include_group g1
include_group g2
include_group sample
tc full2 gen
tc full3 gen
tc full4 gen
tc full5 gen
tc full6 gen
tc full7 gen
tc full8 gen
tc full9 gen
tc full10 gen
tc full11 gen
tc full12 gen
