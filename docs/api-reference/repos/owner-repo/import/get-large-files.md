# Get large files

List files larger than 100MB found during the import

```http
GET {{baseUrl}}/repos/:owner/:repo/import/large_files
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
    [
     {
      "ref_name": "refs/heads/master",
      "path": "foo/bar/1",
      "oid": "d3d9446802a44259755d38e6d163e820",
      "size": 10485760
     },
     {
      "ref_name": "refs/heads/master",
      "path": "foo/bar/2",
      "oid": "6512bd43d9caa6e02c990b0a82652dca",
      "size": 11534336
     },
     {
      "ref_name": "refs/heads/master",
      "path": "foo/bar/3",
      "oid": "c20ad4d76fe97759aa27a0c99bff6710",
      "size": 12582912
     }
    ]
    ```


