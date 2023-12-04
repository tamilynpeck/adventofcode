year=23

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -22|--22) year=22 ;;
        -23|--23) year=23 ;;
        -a|--all) year=0 ;;
        year) command="$1"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done


docker build --rm -t testing:local -f src/test/Dockerfile .

if [ $year == 0 ]; then
  echo "No year specified, running all tests"
  docker run testing:local
elif [ $year == 23 ]; then
  echo "Running tests for year 2023"
  docker run --entrypoint pytest testing:local  --cov-config test/.coveragerc --cov -p no:cacheprovider test/aoc2023
elif [ $year == 22 ]; then
  echo "Running tests for year 2022"
  docker run --entrypoint pytest testing:local  --cov-config test/.coveragerc --cov -p no:cacheprovider test/aoc2022
else
  echo "Running default"
  docker run testing:local
fi

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Tests exited with error code $retVal"
fi
exit $retVal
