# Get interaction restrictions for an organization

Shows which group of GitHub users can interact with this organization and when the restriction expires. If there are no restrictions, you will see an empty response.

```http
GET {{baseUrl}}/orgs/:org/interaction-limits
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


=== "200 OK"

    response

    ```json
    {
     "limit": "collaborators_only",
     "origin": "organization",
     "expires_at": "2018-08-17T04:18:39Z"
    }
    ```


