docker build --rm -t testing:local -f src/test/Dockerfile .
docker run testing:local