# Get a gitignore template

The API also allows fetching the source of a single template.
Use the raw [media type](https://developer.github.com/v3/media/) to get the raw contents.

```http
GET {{baseUrl}}/gitignore/templates/:name
```




## Parameters

| Name | Type | In | Required | Description |
| :--- | :--- | :--- | :--- | :--- |

| `name` | `string` | `Path` | `Yes` | (Required) name parameter |



## Request Body

=== "JSON"

    ```json
    
    ```


## Responses


=== "200 OK"

    response

    ```json
    {
     "name": "C",
     "source": "# Object files\n*.o\n\n# Libraries\n*.lib\n*.a\n\n# Shared objects (inc. Windows DLLs)\n*.dll\n*.so\n*.so.*\n*.dylib\n\n# Executables\n*.exe\n*.out\n*.app\n"
    }
    ```


=== "304 Not Modified"

    Not Modified

    ```json
    
    ```


