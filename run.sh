if [[ -z $1 ]]
then 
    echo "run aoc2023"
    docker build --rm -t aoc2023 -f images/aoc2023/Dockerfile .
    docker run aoc2023
else
    echo "run aoc2022"
    docker build --rm -t aoc2022 -f images/aoc2022/Dockerfile .
    docker run aoc2022
fi
