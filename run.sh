year=${1:-$(date +%Y)}
day=${2:-$(date +%-d)}

echo "Year: $year Day: $day"

cd src
cd $year
cd $day

python program.py
