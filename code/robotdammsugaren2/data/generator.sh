#!/usr/bin/env bash

PPATH=$(realpath ..)
REQUIRE_SAMPLE_REUSE=0
. ../../../testdata_tools/gen.sh

#use_solution bmswapping.py python2 # ../jury_sol.cpp
use_solution nils.cpp

compile gen.py


samplegroup
limits t=0
sample_manual 1

testcase() {
	NAME=$(printf "%02d" $1)
	group group$NAME 10
	limits t=$1
	tc "case$NAME" "${@:2}" tc=$1
}

testcase 1 gen R=10 C=10 N=10 B=10
testcase 2 gen R=100 C=100 N=250 B=500
testcase 3 gen R=100 C=100 N=250 B=2000
testcase 4 gen R=100 C=100 N=2000 B=2000
testcase 5 gen R=500 C=500 N=500 B=10000
testcase 6 gen R=500 C=500 N=500 B=50000
testcase 7 gen R=500 C=500 N=500 B=10000 mode=half
testcase 8 gen R=2000 C=2000 N=2000 B=100000
testcase 9 gen R=2000 C=2000 N=2000 B=800000
testcase 10 gen R=2000 C=2000 N=2000 B=300000 mode=half

# Clamp final scores to 100
echo 'grading: custom' >> testdata.yaml
echo 'grading: default' >> secret/testdata.yaml
echo 'grading: default' >> sample/testdata.yaml
