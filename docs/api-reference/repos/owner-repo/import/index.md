# import

API endpoints for import.

## Endpoints


### [authors](authors/index.md)

`` ``




### [Get an import status](get-an-import-status.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/import`

View the progress of an import.

**Import status**

This section includes details about the possible...


### [Start an import](start-an-import.md)

`PUT` `{{baseUrl}}/repos/:owner/:repo/import`

Start a source import to a GitHub repository using GitHub Importer....


### [Update an import](update-an-import.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/import`

An import can be updated with credentials or a project choice by passing in the appropriate paramete...


### [Cancel an import](cancel-an-import.md)

`DELETE` `{{baseUrl}}/repos/:owner/:repo/import`

Stop an import for a repository....


### [Get large files](get-large-files.md)

`GET` `{{baseUrl}}/repos/:owner/:repo/import/large_files`

List files larger than 100MB found during the import...


### [Update Git LFS preference](update-git-lfs-preference.md)

`PATCH` `{{baseUrl}}/repos/:owner/:repo/import/lfs`

You can import repositories from Subversion, Mercurial, and TFS that include files larger than 100MB...

