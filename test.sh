year=0
all=0

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --last) year=22 ;;
        -a|--all) all=1 ;;;
        year) command="$1"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

docker build --rm -t testing:local -f src/test/Dockerfile .

if [ $year=0 ]; then
  docker run testing:local
elif [ $year=0 ]; then
  docker run --entrypoint pytest testing:local  --cov-config test/.coveragerc --cov -p no:cacheprovider test/aoc2023
elif [ year=22 ]; then
  docker run --entrypoint pytest testing:local  --cov-config test/.coveragerc --cov -p no:cacheprovider test/aoc2022
else
  docker run testing:local
fi

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Tests exited with error code $retVal"
fi
exit $retVal
