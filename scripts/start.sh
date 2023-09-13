#!/bin/bash

ping_until_available() {
    echo "Preparing to ping ${1}"
    until ping -c 1 $1; do
        echo "Waiting for service ${1}..."
        sleep 3
    done
}

startapp() {
    case $1 in
        "API")
            ping_until_available $2 > /dev/null
            uvicorn main_api.main:app --reload --host 0.0.0.0 --port 8000
            ;;
        *)
            exit
            ;;
    esac
}


startapp $@