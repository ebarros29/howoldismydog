#! /bin/bash

mongoimport --host mongo --db dogs_db --collection racas --type json --file /mongo-seed/dogs_db.json --jsonArray

mongo mongo:27017/dogs_db /mongo-seed/create_index.js
