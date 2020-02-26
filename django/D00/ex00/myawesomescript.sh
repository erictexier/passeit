#!/bin/sh

curl "$1" 2>&-  | grep '=' | cut -d '"' -f2  | cut -d '"' -f1 
