# Weather API

## Requirements
- docker with docker-compose
- make utility
- curl

===============================================================================

### Building the containers
```sh
make build
make up
# or
make all # builds, bring containers up, runs tests
```

===============================================================================


## Run rests
```
make tests
```

===============================================================================



## Explore the Weather API
```sh
curl -XGET 'http://localhost:8000/_status'                         # check an application status
curl -XGET 'http://localhost:8000/api/v1/temperature?date=Y-m-d'   # get temperatures accoring to provided date
```
