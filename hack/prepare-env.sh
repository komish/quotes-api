#!/usr/bin/env bash

# helper to set up your environment 
# variables for development

export DB_HOST='127.0.0.1'
export DB_USER='root'
export DB_NAME='quotesdb'
echo -n "DB_PASSWORD: "; read -s DB_PASS; echo
echo -n "ADMIN_TOKEN: " ;read -s ADMIN_TOKEN; echo
export DB_PASS ADMIN_TOKEN
