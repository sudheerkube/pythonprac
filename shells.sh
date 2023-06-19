#!/bin/bash

var1=newus
echo "$var1"
var2=test2
CICD=true
if [[ "$CICD" = true ]]
then
    echo "CICD is working"
else
    echo "Build Not working"
 fi