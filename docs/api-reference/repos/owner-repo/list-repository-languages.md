# List repository languages

Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language.

```http
GET {{baseUrl}}/repos/:owner/:repo/languages
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "C": 78769,
     "Python": 7769
    }
    ```


