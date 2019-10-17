
```sh
## encode the entire disc data to mp3
lame -q 0 --vbr-old -V 4 -r image.img image.mp3

## split mp3
mp3splt -c image.cue -o track%n2 -d mp3 -O 0.0 -n  image.mp3 | tee mp3splt.sh

## get gracenote data
gn_query.py image.cue | tee gn_data.json

## confirm gn_data.json
less gn_data.json

## entag
gn_entagger.py -i 1 data.json
```