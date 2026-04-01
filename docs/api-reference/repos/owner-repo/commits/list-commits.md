# List commits

**Signature verification object**

The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:

These are the possible values for `reason` in the `verification` object:

| Value                    | Description                                                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `expired_key`            | The key that made the signature is expired.                                                                                       |
| `not_signing_key`        | The "signing" flag is not among the usage flags in the GPG key that made the signature.                                           |
| `gpgverify_error`        | There was an error communicating with the signature verification service.                                                         |
| `gpgverify_unavailable`  | The signature verification service is currently unavailable.                                                                      |
| `unsigned`               | The object does not include a signature.                                                                                          |
| `unknown_signature_type` | A non-PGP signature was found in the commit.                                                                                      |
| `no_user`                | No user was associated with the `committer` email address in the commit.                                                          |
| `unverified_email`       | The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. |
| `bad_email`              | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature.             |
| `unknown_key`            | The key that made the signature has not been registered with any user's account.                                                  |
| `malformed_signature`    | There was an error parsing the signature.                                                                                         |
| `invalid`                | The signature could not be cryptographically verified using the key whose key-id was found in the signature.                      |
| `valid`                  | None of the above errors applied, so the signature is considered to be verified.                                                  |

```http
GET {{baseUrl}}/repos/:owner/:repo/commits?sha=<string>&path=<string>&author=<string>&since=<string>&until=<string>&per_page=30&page=1
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `sha` | `string` | `Query` | `No` | SHA or branch to start listing commits from. Default: the repository’s default branch (usually `master`). |

| `path` | `string` | `Query` | `No` | Only commits containing this file path will be returned. |

| `author` | `string` | `Query` | `No` | GitHub login or email address by which to filter by commit author. |

| `since` | `string` | `Query` | `No` | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. |

| `until` | `string` | `Query` | `No` | Only commits before this date will be returned. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. |

| `per_page` | `string` | `Query` | `No` | Results per page (max 100) |

| `page` | `string` | `Query` | `No` | Page number of the results to fetch. |



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
      "id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "tree_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "message": "Fix all the bugs",
      "timestamp": "2016-10-10T00:00:00Z",
      "author": {
       "name": "Monalisa Octocat",
       "email": "mona@github.com"
      },
      "committer": {
       "name": "Monalisa Octocat",
       "email": "mona@github.com"
      }
     },
     {
      "id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "tree_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "message": "Fix all the bugs",
      "timestamp": "2016-10-10T00:00:00Z",
      "author": {
       "name": "Monalisa Octocat",
       "email": "mona@github.com"
      },
      "committer": {
       "name": "Monalisa Octocat",
       "email": "mona@github.com"
      }
     }
    ]
    ```


=== "409 Conflict"

    Conflict

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "400 Bad Request"

    Bad Request

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "500 Internal Server Error"

    Internal Error

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "404 Not Found"

    Resource Not Found

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


