#!/bin/bash
# Sends a JSON POST request ($2) to a URL ($1)
curl -sH "Content-Type: application/json" -d @$2 $1
