cat input.txt | python map.py > map_output.txt

cat map_output.txt | python reduce.py > reduce_output.txt
