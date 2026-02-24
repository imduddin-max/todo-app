# API Notes

## HTTP Methods

### GET
- Used to **read/fetch** data from the server
- Does not change anything on the server
- Example: GET /todos → gives you all todos
- Example: GET /todos/1 → gives you one specific todo

### POST
- Used to **create** new data on the server
- You send data in the request body
- Example: POST /todos with a JSON body → creates a new todo
- Returns 201 Created on success

### PUT
- Used to **update/replace** existing data
- You send the full updated object in the body
- Example: PUT /todos/1 → replaces todo with id 1
- Returns 200 OK on success

### DELETE
- Used to **delete** data from the server
- Example: DELETE /todos/1 → deletes todo with id 1
- Returns 200 OK on success

## Status Codes I Saw
- **200 OK** → Request succeeded
- **201 Created** → New resource was created
- **404 Not Found** → The URL doesn't exist
- **500 Internal Server Error** → Something broke on the server

## What I Learned
- APIs return data in JSON format
- The URL path determines WHAT you're accessing (/todos vs /todos/1)
- The HTTP method determines WHAT ACTION you're performing (read, create, update, delete)
- These 4 methods together are called CRUD: Create, Read, Update, Delete
