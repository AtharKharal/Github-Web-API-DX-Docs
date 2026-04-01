# Create a remove token for a repository

Returns a token that you can pass to remove a self-hosted runner from a repository. The token expires after one hour.
You must authenticate using an access token with the `repo` scope to use this endpoint.

#### Example using remove token
 
To remove your self-hosted runner from a repository, replace TOKEN with the remove token provided by this endpoint.

```
./config.sh remove --token TOKEN
```

```http
POST {{baseUrl}}/repos/:owner/:repo/actions/runners/remove-token
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


=== "201 Created"

    response

    ```json
    {
     "token": "AABF3JGZDX3P5PMEXLND6TS6FCWO6",
     "expires_at": "2020-01-29T12:13:35.123-08:00"
    }
    ```


