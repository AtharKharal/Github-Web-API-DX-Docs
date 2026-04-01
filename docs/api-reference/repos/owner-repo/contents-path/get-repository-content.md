# Get repository content

Gets the contents of a file or directory in a repository. Specify the file path or directory in `:path`. If you omit
`:path`, you will receive the contents of all files in the repository.

Files and symlinks support [a custom media type](https://developer.github.com/v3/repos/contents/#custom-media-types) for
retrieving the raw content or rendered HTML (when supported). All content types support [a custom media
type](https://developer.github.com/v3/repos/contents/#custom-media-types) to ensure the content is returned in a consistent
object format.

**Note**:
*   To get a repository's contents recursively, you can [recursively get the tree](https://developer.github.com/v3/git/trees/).
*   This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the [Git Trees
API](https://developer.github.com/v3/git/trees/#get-a-tree).
*   This API supports files up to 1 megabyte in size.

#### If the content is a directory
The response will be an array of objects, one object for each item in the directory.
When listing the contents of a directory, submodules have their "type" specified as "file". Logically, the value
_should_ be "submodule". This behavior exists in API v3 [for backwards compatibility purposes](https://git.io/v1YCW).
In the next major version of the API, the type will be returned as "submodule".

#### If the content is a symlink 
If the requested `:path` points to a symlink, and the symlink's target is a normal file in the repository, then the
API responds with the content of the file (in the format shown in the example. Otherwise, the API responds with an object 
describing the symlink itself.

#### If the content is a submodule
The `submodule_git_url` identifies the location of the submodule repository, and the `sha` identifies a specific
commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out
the submodule at that specific commit.

If the submodule repository is not hosted on github.com, the Git URLs (`git_url` and `_links["git"]`) and the
github.com URLs (`html_url` and `_links["html"]`) will have null values.

```http
GET {{baseUrl}}/repos/:owner/:repo/contents/:path?ref=<string>
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `owner` | `string` | `Path` | `Yes` | (Required)  |

| `repo` | `string` | `Path` | `Yes` | (Required)  |

| `path` | `string` | `Path` | `Yes` | (Required) path+ parameter |

| `ref` | `string` | `Query` | `No` | The name of the commit/branch/tag. Default: the repository’s default branch (usually `master`) |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "type": "file",
     "encoding": "base64",
     "size": 5362,
     "name": "README.md",
     "path": "README.md",
     "content": "encoded content ...",
     "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
     "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
     "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
     "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
     "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
     "_links": {
      "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
      "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
      "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
     }
    }
    ```


=== "302 Found"

    Found

    ```json
    
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


