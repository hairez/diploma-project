#!/usr/bin/env bash

PPATH=$(realpath ..)

REQUIRE_SAMPLE_REUSE=0
. ../../testdata_tools/gen.sh

use_solution randomPath.py

compile gen.py

group g1 10
tc random_small gen n=10

group g2 10
tc random_medium gen n=1000

group g3 10
tc random_big gen n=1000000

group g4 10
tc smalln1 gen n=1000


group g5 40
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
