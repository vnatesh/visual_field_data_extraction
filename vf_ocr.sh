#!/bin/bash

for i in *.PNG; do tesseract $i $i; done;

rm *.PNG
