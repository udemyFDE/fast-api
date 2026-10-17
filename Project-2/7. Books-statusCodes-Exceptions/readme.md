## Status Codes
* An HTTP status code is used to help the client (system or user submitting data to the server) to understand what happened on the server side application.
* Status codes are international standards on how a client or server should handle the result of a request.
* It allows everyone who sends a request to know if their submission was successful or not.

#### Some of the common status codes

* **1xx (100 series)** &rarr; information responses that a request is processing. So it might be giving information to the user that something is happening behind the scenes.
* **2xx (200 series)** &rarr; successful requests.
    | code | message |
    | --- | --- |
    | `200: ok` | Is a standard response for a successful request. Commonly used for successful `GET` requests when data is being returned back to the client. |
    | `201: creatd` | This means that the request has been successful and created a new resource. This is used a lot when a `POST` request creates a new entity for the application. |
    | `204: No Content` | means it was successful, but it did not create an entity, nor does the response return anything. It's commonly used for `PUT` requests where the application is not returning an entity, but it did change it behind the scenes on the server side application. |
    
* **3xx (300 series)** &rarr; read directions, which means further action must be complete.
* **4xx (400 series)** &rarr; client errors &rarr; error caused by the client.

    | code | message |
    | --- | --- |
    | `400: Bad Request` | Which means it cannot process the request due to client error. Commonly used for invalid request methods. |
    | `401: Unauthorized` | Which means a client does not have valid authentication for target resource. |
    | `404: Not Found` | which means a client requested resources can not be found. |
    | `422: Unprocessable Entity` | Which means there's some kind of semantic errors in the client request. |
* **5xx (500 series)** &rarr; server error &rarr; error occured on the server side of application.
    - `500: Internal Server Error` &rarr; This is a generic error message when an unexpected issue on the server happened. Something's like the python code broke in some weird spot or we might be getting a null response that we're just going to throw a 500 error. So the client knows that something happened on the server side, not on the client side.