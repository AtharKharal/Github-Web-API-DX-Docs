# Create a remove token for an organization

**Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.


Returns a token that you can pass to the `config` script to remove a self-hosted runner from an organization. The
token expires after one hour. You must authenticate using an access token with the `admin:org` scope to use this
endpoint.

#### Example using remove token

To remove your self-hosted runner from an organization, replace `TOKEN` with the remove token provided by this
endpoint.

```
./config.sh remove --token TOKEN
```

```http
POST {{baseUrl}}/orgs/:org/actions/runners/remove-token
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
     "token": "AABF3JGZDX3P5PMEXLND6TS6FCWO6",
     "expires_at": "2020-01-29T12:13:35.123-08:00"
    }
    ```


