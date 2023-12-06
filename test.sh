year=2023
day=1

while getopts y:d: flag 
do
    case "${flag}" in
        y) year=${OPTARG};;
        d) day=${OPTARG};;
    esac
done

echo "Year: $year Day: $day"

cd src
cd $year
cd $day

pytest