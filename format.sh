black src

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Black exited with error code $retVal"
fi
exit $retVal
