# Create a registration token for a repository

Returns a token that you can pass to the `config` script. The token expires after one hour. You must authenticate
using an access token with the `repo` scope to use this endpoint.

#### Example using registration token
 
Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.

```
./config.sh --url https://github.com/octo-org/octo-repo-artifacts --token TOKEN
```

```http
POST {{baseUrl}}/repos/:owner/:repo/actions/runners/registration-token
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
     "token": "LLBF3JGZDX3P5PMEXLND6TS6FCWO6",
     "expires_at": "2020-01-22T12:13:35.123-08:00"
    }
    ```


