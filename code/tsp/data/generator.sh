#!/usr/bin/env bash

PPATH=$(realpath ..)

REQUIRE_SAMPLE_REUSE=0

. ../../testdata_tools/gen.sh

use_solution 2-opt.py

compile gen.py

group g1 10
tc random_small gen n=10

group g2 10
tc random_medium gen n=1000

group g3 10
tc random_big gen n=10000

group g4 10
tc_manual ../data/manual_testdata/sweden.in

group g5 10
tc_manual ../data/manual_testdata/united_states.in


group g6 10
tc strictlyIncrease gen increase=1 n=10000

group g7 10
tc circle gen circle=1 n=10000

group g8 10
tc grid gen grid=1 n=10000

group g9 10
tc straight gen straight=1 n=10000

group g10 10
tc strictlyIncrease_small gen increase=1 n=100
