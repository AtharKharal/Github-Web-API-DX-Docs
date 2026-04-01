# Add an email address for the authenticated user

This endpoint is accessible with the `user` scope.

```http
POST {{baseUrl}}/user/emails
```





## Request Body

=== "JSON"

    ```json
    {
        "emails": [
            "<string>",
            "<string>"
        ]
    }
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


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "culpa mollit",
     "documentation_url": "ipsum ut",
     "errors": [
      {
       "code": "consequat enim et velit",
       "resource": "anim ullamco",
       "field": "voluptate officia amet",
       "message": "exercitation sed dolore est",
       "index": 18359415,
       "value": "ullamco ut velit nulla eiusmod"
      },
      {
       "code": "occaecat eiusmod Duis",
       "resource": "esse ad Excepteur mollit",
       "field": "minim ipsum nisi exercitation non",
       "message": "proident reprehenderit",
       "index": -23326731,
       "value": "adipisicing cupidatat culpa in"
      }
     ]
    }
    ```


=== "201 Created"

    response

    ```json
    [
     {
      "email": "octocat@octocat.org",
      "primary": false,
      "verified": false,
      "visibility": "public"
     },
     {
      "email": "octocat@github.com",
      "primary": false,
      "verified": false,
      "visibility": null
     },
     {
      "email": "mona@github.com",
      "primary": false,
      "verified": false,
      "visibility": null
     }
    ]
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


