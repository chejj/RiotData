#!/bin/bash

conda activate riot

python_scripts=("../summoners/br1.py" "../summoners/eun1.py" "../summoners/euw1.py" "../summoners/jp1.py" "../summoners/kr.py" "../summoners/la1.py" "../summoners/la2.py" "../summoners/na1.py" "../summoners/oc1.py" "../summoners/ph2.py" "../summoners/ru.py" "../summoners/sg2.py" "../summoners/th2.py" "../summoners/tr1.py" "../summoners/tw2.py" "../summoners/vn2.py")

for script in "${python_scripts[@]}"
do
	nice -n -10 python3 "$script" >> "script.log" 2>&1 &
done

sleep 5

pgrep -f python3 | xargs -I {} renice -n -10 -p {}
