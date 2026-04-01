# Update the authenticated user

**Note:** If your email is set to private and you send an `email` parameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API.

```http
PATCH {{baseUrl}}/user
```





## Request Body

=== "JSON"

    ```json
    {
        "name": "<string>",
        "email": "<string>",
        "blog": "<string>",
        "twitter_username": "<string>",
        "company": "<string>",
        "location": "<string>",
        "hireable": "<boolean>",
        "bio": "<string>"
    }
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "login": "octocat",
     "id": 1,
     "node_id": "MDQ6VXNlcjE=",
     "avatar_url": "https://github.com/images/error/octocat_happy.gif",
     "gravatar_id": "",
     "url": "https://api.github.com/users/octocat",
     "html_url": "https://github.com/octocat",
     "followers_url": "https://api.github.com/users/octocat/followers",
     "following_url": "https://api.github.com/users/octocat/following{/other_user}",
     "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
     "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
     "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
     "organizations_url": "https://api.github.com/users/octocat/orgs",
     "repos_url": "https://api.github.com/users/octocat/repos",
     "events_url": "https://api.github.com/users/octocat/events{/privacy}",
     "received_events_url": "https://api.github.com/users/octocat/received_events",
     "type": "User",
     "site_admin": false,
     "name": "monalisa octocat",
     "company": "GitHub",
     "blog": "https://github.com/blog",
     "location": "San Francisco",
     "email": "octocat@github.com",
     "hireable": false,
     "bio": "There once was...",
     "twitter_username": "monatheoctocat",
     "public_repos": 2,
     "public_gists": 1,
     "followers": 20,
     "following": 0,
     "created_at": "2008-01-14T04:33:35Z",
     "updated_at": "2008-01-14T04:33:35Z",
     "private_gists": 81,
     "total_private_repos": 100,
     "owned_private_repos": 100,
     "disk_usage": 10000,
     "collaborators": 8,
     "two_factor_authentication": true,
     "plan": {
      "name": "Medium",
      "space": 400,
      "private_repos": 20,
      "collaborators": 0
     }
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


=== "401 Unauthorized"

    Requires Authentication

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


=== "422 Unprocessable Entity (WebDAV) (RFC 4918)"

    Validation Failed

    ```json
    {
     "message": "culpa mollit",
     "documentation_url": "ipsum ut",
     "errors": [
      {
       "code": "consequat enim et velit",
       "resource": "anim ullamco",
       "field": "voluptate officia amet",
       "message": "exercitation sed dolore est",
       "index": 18359415,
       "value": "ullamco ut velit nulla eiusmod"
      },
      {
       "code": "occaecat eiusmod Duis",
       "resource": "esse ad Excepteur mollit",
       "field": "minim ipsum nisi exercitation non",
       "message": "proident reprehenderit",
       "index": -23326731,
       "value": "adipisicing cupidatat culpa in"
      }
     ]
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


=== "403 Forbidden"

    Forbidden

    ```json
    {
     "message": "incididunt labore",
     "documentation_url": "non"
    }
    ```


