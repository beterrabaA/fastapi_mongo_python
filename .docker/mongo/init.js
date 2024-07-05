db = db.getSiblingDB('todo_db');

db.createCollection('tasks_collection');

db.sample_collection.insertMany([
 {
    name: 'helpdev',
    description: 'salada mista',
    is_done: false
  },
  {
    name: 'helpdev',
    description: 'quero quero',
    is_done: false
  },
  {
    name: 'helpdev',
    description: 'passagem de onibus',
    is_done: false
  }  
]);