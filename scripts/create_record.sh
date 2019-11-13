#!/usr/bin/env bash

curl -k --header "Content-Type: application/json" \
--request POST \
--data '{"title":"Some title", "contributors": [{"name": "Doe, John"}]}' \
https://127.0.0.1:5000/api/records/?prettyprint=1

curl -k --header "Content-Type: application/json" \
--request PUT \
--data '{"title":"Some title", "contributors": [{"name": "Doe, John"}]}' \
https://127.0.0.1:5000/api/records/$pid?prettyprint=1