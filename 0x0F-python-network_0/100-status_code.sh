#!/bin/bash
# writes the status code and "outputs" to stdout and /dev/null
curl -sLw "%{http_code}" -o /dev/null "$1"
