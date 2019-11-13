#!/usr/bin/env bash

pid=$1
file=$2

curl -k -H "Content-Type: application/octet-stream" \
-X PUT \
--data-binary @$file https://127.0.0.1:5000/api/records/$pid/files/$(basename $file)