conn = new Mongo("mongo");
db = conn.getDB("dogs_db");
db.racas.createIndex( { raca: "text", porte: "text" } );