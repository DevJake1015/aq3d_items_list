#!/bin/sh
exec > ./../data/items_tmp.txt
node ./script.js
cp ./../data/items_tmp.txt ./../data/items_bu.txt