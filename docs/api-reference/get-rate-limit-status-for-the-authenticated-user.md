# Get rate limit status for the authenticated user

**Note:** Accessing this endpoint does not count against your REST API rate limit.

**Note:** The `rate` object is deprecated. If you're writing new API client code or updating existing code, you should use the `core` object instead of the `rate` object. The `core` object contains the same information that is present in the `rate` object.

```http
GET {{baseUrl}}/rate_limit
```





## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "200 OK"

    response

    ```json
    {
     "resources": {
      "core": {
       "limit": 5000,
       "remaining": 4999,
       "reset": 1372700873
      },
      "search": {
       "limit": 30,
       "remaining": 18,
       "reset": 1372697452
      },
      "graphql": {
       "limit": 5000,
       "remaining": 4993,
       "reset": 1372700389
      },
      "integration_manifest": {
       "limit": 5000,
       "remaining": 4999,
       "reset": 1551806725
      }
     },
     "rate": {
      "limit": 5000,
      "remaining": 4999,
      "reset": 1372700873
     }
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


