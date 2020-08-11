cat words1.txt | while read a; do echo "bucket $a"; python3 fileScraper.py $a >> all_files ; done 
