# cards

API endpoints for cards.

## Endpoints


### [List project cards](list-project-cards.md)

`GET` `{{baseUrl}}/projects/columns/:column_id/cards?archived_state=not_archived&per_page=30&page=1`

...


### [Create a project card](create-a-project-card.md)

`POST` `{{baseUrl}}/projects/columns/:column_id/cards`

**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull ...

