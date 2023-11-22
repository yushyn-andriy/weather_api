# Weather API

## Requirements
- linux machine
- python3.11 
- make utility
- curl
- Open Weather API Key 

===============================================================================

### Run 
```sh
# API key from  https://openweathermap.org/api
export WEATHER_OPEN_API_KEY='YOUR API KEY'

make up_local
```

===============================================================================



## Explore the Weather API
```sh
# check an application status
curl -XGET 'http://localhost:5000/api/v1/_status'
# get temperatures accoring to provided date
curl -XGET -H "x-token:$(python3 -c 'print("-"*32)')" 'http://localhost:5000/api/v1/weather?day=2023-11-22'
```
