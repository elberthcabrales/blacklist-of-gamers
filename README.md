# blacklist-of-gamers
## run docker-compose up --build
### then You can then access to endpoints by visiting http://localhost:5000 in your web browser.

### Endpoints
#### POST /api/v1/blacklist
##### Request
```json
{
    "steamId": "76561198000000000"
}
```
##### Response
```json
{
    "steamId": "76561198000000000",
    "blacklisted": true
}
```
#### POST /api/v1/blacklist/check
##### Request
```json
{
    "steamId": "76561198000000000"
}
```
##### Response
```json
{
    "steamId": "76561198000000000",
    "blacklisted": true
}
```

### swagger docs http://127.0.0.1:5000/apidocs/