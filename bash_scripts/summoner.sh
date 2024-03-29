#!/bin/bash

python_scripts=("br1.py" "eun1.py" "euw1.py" "jp1.py" "kr.py" "la1.py" "la2.py" "na1.py" "oc1.py" "ph2.py" "ru.py" "sg2.py" "th2.py" "tr1.py" "tw2.py" "vn2.py")

for script in "${python_scripts[@]}"
do
	nice -n -10 python3 "$script" >> "script.log" 2>&1 &
done

sleep 5

pgrep -f python3 | xargs -I {} renice -n -10 -p {}
