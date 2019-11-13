#!/usr/bin/env bash

pid=$1
title=$2

curl -k --header "Content-Type: application/json" \
--request PUT \
--data "{\"title\":\"Some title ($title)\", \"contributors\": [{\"name\": \"Doe, John\"}]}" \
https://127.0.0.1:5000/api/records/$pid?prettyprint=1