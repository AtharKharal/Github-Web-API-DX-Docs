# Create a registration token for an organization

**Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.


Returns a token that you can pass to the `config` script. The token expires after one hour. You must authenticate
using an access token with the `admin:org` scope to use this endpoint.

#### Example using registration token

Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.

```
./config.sh --url https://github.com/octo-org --token TOKEN
```

```http
POST {{baseUrl}}/orgs/:org/actions/runners/registration-token
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `org` | `string` | `Path` | `Yes` | (Required)  |



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


