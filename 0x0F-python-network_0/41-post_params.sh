#!/bin/bash
# using curl to send a basic email
curl -X POST -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
