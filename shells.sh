#!/bin/bash
var1=newus
echo "$var1"
var2=test2
CICD=1
if [[$CICD -eq 1]]
then
    echo "CICD is working"
else
    echo "Build Not working"
fi