## Tools for entagging mp3 from audio CD  with Gracenote data

### Required Libraries

- GNSDK
  - gnsdk_manager.dll
  - gnsdk_musicid.dll
  - gnsdk_storage_sqlite.dll
- Python3
  - mutagen
  - lxml

### Instructions

```sh
## set PYTHONPATH
export PYTHONPATH=/path/to/this_repos

## encode the entire disc data to mp3
lame -q 0 --vbr-old -V 4 -r image.img image.mp3

## split mp3
mp3splt -c image.cue -o track%n2 -d mp3 -O 0.0 -n  image.mp3

## get gracenote data
python -m gn_query image.cue | tee gn_data.json

## view gn_data.json
less gn_data.json

## entag
python -m gn_entagger -i 1 gn_data.json
```