`GET    /api/v1/MappingItem/{id}` => retrieving MappingItem by ID, may responses with 404
`PATCH  /api/v1/MappingItem/{id}` => updating mappingItem, request-body contains updated object, path-id refers to the item, response with 200, 401 or 422
`PUT    /api/v1/MappingItem/{id}` => create or update mappingItem, request-body contains updated object, path-id refers to the item, responses with either 201, 401 or 422
`DELETE /api/v1/MappingItem/{id}` => delete mappingItem, responses wither with 200, 401 or 404

`GET /api/v1/MappingItem/search` => URL-Param searchText
`GET /api/v1/MappingItem/search/{hub}` => URL-Param searchText
`GET /api/v1/MappingItem/categories/{category}`

`GET /api/v1/MappingItem/updateAll`

