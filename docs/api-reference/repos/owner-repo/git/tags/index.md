# tags

API endpoints for tags.

## Endpoints


### [Create a tag object](create-a-tag-object.md)

`POST` `{{baseUrl}}/repos/:owner/:repo/git/tags`

Note that creating a tag object does not create the reference that makes a tag in Git. If you want t...


### [Get a tag](get-a-tag.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/git/tags/:tag_sha`

**Signature verification object**

The response will include a `verification` object that describes ...

