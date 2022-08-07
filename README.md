# EurekaLabs API

## Usage:

### Register and get api key

#### Request
```
curl --location --request POST 'https://eurekalabs-api.herokuapp.com/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "username"
}'
```

#### Response
```
{
    "message": "User created successfully.",
    "api_key": "b0370cb1b8604186abcecb51ace2baa6"
}
```

### Get Stock data

#### Request
```
curl --location --request GET 'https://eurekalabs-api.herokuapp.com/stock?symbol=IBM&api_key=5bea8cc4ff934ed2b7b9a8ccbf7b5dd5'
```

#### Response
```
{
    "open price": "131.2500",
    "higher price": "132.6700",
    "lower price": "131.0700",
    "variation": 0.84
}
```

## Considerations:
- Initial data for sign up: username.
- Validations rules: unique username.
- Deployed in Heroku
- Github repo: https://github.com/ArnedisGobbo/eurekalabs.git
- API throttling: 10 calls per minute
- Logging files located in ./logs
