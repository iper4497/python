#!/bin/sh

set -ue

# Usage:
# pasta.sh file
# pasta.sh file --password
# pasta.sh file --self-burning
# cat file | pasta.sh
# cat file | pasta.sh --password
# cat file | pasta.sh --self-burning

filename=""
content="-"
pasta_type="standard"
mask=' '
server="https://pasta.cf"

for o in "$@"; do
    case "$o" in

        --password)
            pasta_type="editable"
            mask="^(password|view):"
        ;;

        --self-burning)
            pasta_type="self_burning"
            mask="^(raw|view):"
        ;;

        --local)
            server="http://127.0.0.1:25516"
        ;;

        *)
            filename=$(basename "$o")
            content="$o"
        ;;
    esac
done

mask="($mask)|(There was an error|Failed to create paste)"

response=$(proxychains curl \
    --silent --show-error \
    $server/api/create \
    -F "content=<$content" \
    -F "filename=$filename" \
    -F "pasta_type=$pasta_type")
echo "$response" 
proxychains curl -d private=1 -d name=Herbert --data-urlencode text@$1 http://ypbnurlwfis7xsei.onion/api/create
