# NucliaDB

# The [Makefile](./Makefile)

The Makefile holds all relevant commands that we have in this application. Below are described all possible ones:

- **run-dev** [L15]
    
    This command will run in "dev-mode". We can understand as "dev-mode" the direct acess to the terminal and possibility of include breakpoints across the code and yet iteract with them within the terminal where this command were called.

- **run** [L19]

    This command will run in "prod-mode". We can understand as "prod-mode" the isolated run of the app. In other words, It will run inside container in an isolated environment, with no direct acess to the app, diferently from the previous command.

- **run-test** [L23]

    This command will run some test cases for the endpoints. It will, basically, build a container for the app and another one for nuclia database and run the tests.


# The [App](./main_api/main.py)

The main API consists in two main routers, one for healthcheck of nuclia db - a simple endpoint that will ping the service and return 200 If It's ok. Considering that the only need is to validate the inner call, It Is a `HEAD` method, so no body will be returned.

The other route, called `api_kb`, will be responsible for `CREATE`, `READ` and `DELETE` a given knowledge box.


## Nuclia Dependencies


The `NucliaEndpoints` module defines constants for configuring Nuclia API endpoints.

- `ROOT`: The hostname or IP address of the Nuclia server.
- `PORT`: The port number for Nuclia API.
- `PROTOCOL`: The protocol (HTTP/HTTPS) used for communication.

### NucliaCreated Model

The `NucliaCreated` model represents the response when a new Knowledge Box (KB) is created.

- `slug` (`str`): The unique identifier (slug) for the created KB.

### NucliaGetOrCreate Model

The `NucliaGetOrCreate` model is used for creating or retrieving a Knowledge Box (KB).

- `slug` (`str`): The unique identifier (slug) for the KB.
- `model` (`Optional[SentenceTransformer]`): An optional SentenceTransformer model for encoding text data.

#### Methods:

- `get_or_create_by_slug()`: Asynchronously creates or retrieves a Knowledge Box based on the provided slug and returns it. The method constructs the Nuclia API URL using the configured `NucliaEndpoints` and `slug`.

- `upload_to_knowledge_box(dataset: List[dict])`: Asynchronously uploads data from a dataset to the Knowledge Box. The method iterates over items in the dataset, extracts prompts, and uploads them to the KB along with encoded vectors generated by the SentenceTransformer model.

### NucliaDelete Model

The `NucliaDelete` model is used for deleting a Knowledge Box.

- `slug` (`str`): The unique identifier (slug) for the KB to be deleted.

#### Method:

- `delete_by_slug()`: Asynchronously deletes a Knowledge Box based on the provided slug and returns it. The method constructs the Nuclia API URL using the configured `NucliaEndpoints` and `slug`.

### NucliaSearch Model

The `NucliaSearch` model is used for searching within a Knowledge Box.

- `term` (`str`): The search term.

#### Method:

- `search(query: ndarray, knowledgebox: KnowledgeBox)`: Asynchronously performs a search within the specified Knowledge Box based on a query vector, vectorset, and minimum score threshold. It returns a `SearchResult` object containing the search results.

This code defines models and methods for interacting with the Nuclia API, including creating, retrieving, uploading data to, and searching within Knowledge Boxes. It utilizes the `nucliadb_sdk` library and the SentenceTransformer for natural language understanding tasks.

# Examples

CREATE
```
curl --location 'http://localhost:8000/v1/knowledge-box/create' \
--header 'Content-Type: application/json' \
--data '{"slug": "nuclinha_test"}'
```

GET
```
curl --location 'http://localhost:8000/v1/knowledge-box/search?term=programming&slug=nuclinha_test'
```

DELETE
```
curl --location --request DELETE 'http://localhost:8000/v1/knowledge-box/delete' \
--header 'Content-Type: application/json' \
--data '{"slug": "nuclinha_test"}'
```
