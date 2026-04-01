# Get all codes of conduct



```http
GET {{baseUrl}}/codes_of_conduct
```





## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    [
     {
      "key": "citizen_code_of_conduct",
      "name": "Citizen Code of Conduct",
      "url": "https://api.github.com/codes_of_conduct/citizen_code_of_conduct",
      "html_url": "http://citizencodeofconduct.org/"
     },
     {
      "key": "contributor_covenant",
      "name": "Contributor Covenant",
      "url": "https://api.github.com/codes_of_conduct/contributor_covenant",
      "html_url": "https://www.contributor-covenant.org/version/2/0/code_of_conduct/"
     }
    ]
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "415 Unsupported Media Type"

    Preview Header Missing

    ```json
    {
     "message": "enim velit officia",
     "documentation_url": "et proident"
    }
    ```


