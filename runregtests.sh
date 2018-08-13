#!/bin/bash

SEWPY_TOOL=sewpysolver.py

checkresult(){
    local status=$?
    if [ $status -ne 0 ]; then
        echo -e "FAILED. Last command failed. Exiting..."
        exit $status
    fi
}

# run all regression tests
echo -e "Running test case 1"
${SEWPY_TOOL} ref/case1/bateman.i b1.out

echo -e "Running test case 2"
${SEWPY_TOOL} ref/case2/bateman.i b2.out

# compare the outputs
echo -e "Comparing test case 1 output"
diff ref/case1/bateman.out b1.out
checkresult

echo -e "Comparing test case 2 output"
diff ref/case2/bateman.out b2.out
checkresult
