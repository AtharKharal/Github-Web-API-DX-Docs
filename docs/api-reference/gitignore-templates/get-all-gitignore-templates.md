# Get all gitignore templates

List all templates available to pass as an option when [creating a repository](https://developer.github.com/v3/repos/#create-a-repository-for-the-authenticated-user).

```http
GET {{baseUrl}}/gitignore/templates
```





## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "200 OK"

    response

    ```json
    [
     "Actionscript",
     "Android",
     "AppceleratorTitanium",
     "Autotools",
     "Bancha",
     "C",
     "C++"
    ]
    ```


