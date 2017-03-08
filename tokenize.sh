echo "Tokenize with vnTokenizer"
docker cp input.txt b211:/vnTokenizer/vnTokenizer/input.txt
docker exec b21 /bin/bash -c "cd /vnTokenizer/vnTokenizer/ && ./vnTokenizer.sh -i input.txt -o output.txt"
docker cp b211:/vnTokenizer/vnTokenizer/output.txt output.txt
