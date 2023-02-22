# Kata Wemanity

## Mars Rover Kata

https://kata-log.rocks/mars-rover-kata

<img src="https://static.wikia.nocookie.net/lemondededisney/images/3/34/WallE_PS3_Visuel002.jpg/revision/latest?cb=20120305142525&path-prefix=fr"
     alt="Wall-e"
     style="float: left; margin-right: 300px; width: 300px;" />

## How to test

To start tests execute:

python manage.py test


## How to use

To use the api send a POST request to the `/move/` endpoint followed by the Rover id and put the sequence in the payload:

```
     SERVER_URL/move/<rover_id>

     The json Payload should be like this
     {
     "sequence": "lfffrbb"
     }
```