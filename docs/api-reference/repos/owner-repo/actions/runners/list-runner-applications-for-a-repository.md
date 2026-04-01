# List runner applications for a repository

Lists binaries for the runner application that you can download and run. You must authenticate using an access token with the `repo` scope to use this endpoint.

```http
GET {{baseUrl}}/repos/:owner/:repo/actions/runners/downloads
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
      "os": "osx",
      "architecture": "x64",
      "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-osx-x64-2.164.0.tar.gz",
      "filename": "actions-runner-osx-x64-2.164.0.tar.gz"
     },
     {
      "os": "linux",
      "architecture": "x64",
      "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-x64-2.164.0.tar.gz",
      "filename": "actions-runner-linux-x64-2.164.0.tar.gz"
     },
     {
      "os": "linux",
      "architecture": "arm",
      "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-arm-2.164.0.tar.gz",
      "filename": "actions-runner-linux-arm-2.164.0.tar.gz"
     },
     {
      "os": "win",
      "architecture": "x64",
      "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-win-x64-2.164.0.zip",
      "filename": "actions-runner-win-x64-2.164.0.zip"
     },
     {
      "os": "linux",
      "architecture": "arm64",
      "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-arm64-2.164.0.tar.gz",
      "filename": "actions-runner-linux-arm64-2.164.0.tar.gz"
     }
    ]
    ```


