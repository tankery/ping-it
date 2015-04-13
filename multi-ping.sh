#!/bin/bash

mkdir -p result

cat sites.txt | while read site; do
    if [ -z "$site" ]; then
        continue
    fi
    
    echo "Start ping $site"
    echo >> result/$site.txt
    echo >> result/$site.txt
    date >> result/$site.txt
    ping -c 10 $site >>result/$site.txt || echo "Ping $site has a error."
done

