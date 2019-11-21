## Test case application written in Python/Flask

Using Celery for background job and redis as message broker.

## Docker instructions

Build all services with
```shell
docker-compose build
```

Then run
```shell
docker-compose up
```

## API instructions

#### POST: 0.0.0.0:5001/submit
* url - absolute path to file
* email - your address (optional)

```shell
curl -X POST -d http://0.0.0.0:5001/submit?email=azovsky777@gmail.com&url=https://i.imgur.com/dnBnvxc.jpg"

{
    "id": "327ebcc3-deb4-41d9-bccc-8e9f36803eb9"
}
```
Returns unique id of current task
#### GET: 0.0.0.0:5001/check
* id - the one you got from previous response

```shell
curl -X GET http://0.0.0.0:5001/check?id=327ebcc3-deb4-41d9-bccc-8e9f36803eb9

{
    "md5": "f8d3f074da63a27f6d8d74cb82065c7a",
    "status": "SUCCESS",
    "url": "https://i.imgur.com/dnBnvxc.jpg"
}
```

Returns MD5 hash status and url in case of success and only status otherwise 


