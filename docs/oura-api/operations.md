# API 路径与操作

以下 JSON 保留原始字段；`$ref` 指向组件文档中的定义。

## `/v2/sandbox/usercollection/daily_activity`

### GET — Sandbox - Multiple Daily Activity Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Daily Activity Documents",
  "operationId": "Sandbox___Multiple_daily_activity_Documents_v2_sandbox_usercollection_daily_activity_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailyActivity_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Daily Activity Documents V2 Sandbox Usercollection Daily Activity Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_activity?start_date=2021-11-01&end_date=2021-12-01&fields=day,score' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_activity' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,score' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_activity?start_date=2021-11-01&end_date=2021-12-01&fields=day,score', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_activity?start_date=2021-11-01&end_date=2021-12-01&fields=day,score\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_activity/{document_id}`

### GET — Sandbox - Single Daily Activity Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Daily Activity Document",
  "operationId": "Sandbox___Single_daily_activity_Document_v2_sandbox_usercollection_daily_activity__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailyActivity"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_activity/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_activity/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_activity/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_activity/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_cardiovascular_age`

### GET — Sandbox - Multiple Daily Cardiovascular Age Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Daily Cardiovascular Age Documents",
  "operationId": "Sandbox___Multiple_daily_cardiovascular_age_Documents_v2_sandbox_usercollection_daily_cardiovascular_age_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailyCardiovascularAge_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Daily Cardiovascular Age Documents V2 Sandbox Usercollection Daily Cardiovascular Age Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_cardiovascular_age?start_date=2021-11-01&end_date=2021-12-01&fields=day,pulse_wave_velocity' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_cardiovascular_age' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,pulse_wave_velocity' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_cardiovascular_age?start_date=2021-11-01&end_date=2021-12-01&fields=day,pulse_wave_velocity', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_cardiovascular_age?start_date=2021-11-01&end_date=2021-12-01&fields=day,pulse_wave_velocity\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_cardiovascular_age/{document_id}`

### GET — Sandbox - Single Daily Cardiovascular Age Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Daily Cardiovascular Age Document",
  "operationId": "Sandbox___Single_daily_cardiovascular_age_Document_v2_sandbox_usercollection_daily_cardiovascular_age__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailyCardiovascularAge"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_cardiovascular_age/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_cardiovascular_age/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_cardiovascular_age/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_cardiovascular_age/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_readiness`

### GET — Sandbox - Multiple Daily Readiness Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Daily Readiness Documents",
  "operationId": "Sandbox___Multiple_daily_readiness_Documents_v2_sandbox_usercollection_daily_readiness_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailyReadiness_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Daily Readiness Documents V2 Sandbox Usercollection Daily Readiness Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_readiness?start_date=2021-11-01&end_date=2021-12-01&fields=day,score' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_readiness' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,score' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_readiness?start_date=2021-11-01&end_date=2021-12-01&fields=day,score', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_readiness?start_date=2021-11-01&end_date=2021-12-01&fields=day,score\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_readiness/{document_id}`

### GET — Sandbox - Single Daily Readiness Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Daily Readiness Document",
  "operationId": "Sandbox___Single_daily_readiness_Document_v2_sandbox_usercollection_daily_readiness__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailyReadiness"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_readiness/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_readiness/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_readiness/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_readiness/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_resilience`

### GET — Sandbox - Multiple Daily Resilience Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Daily Resilience Documents",
  "operationId": "Sandbox___Multiple_daily_resilience_Documents_v2_sandbox_usercollection_daily_resilience_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_DailyResilienceModel_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Daily Resilience Documents V2 Sandbox Usercollection Daily Resilience Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_resilience?start_date=2021-11-01&end_date=2021-12-01' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_resilience' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_resilience?start_date=2021-11-01&end_date=2021-12-01', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_resilience?start_date=2021-11-01&end_date=2021-12-01\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_resilience/{document_id}`

### GET — Sandbox - Single Daily Resilience Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Daily Resilience Document",
  "operationId": "Sandbox___Single_daily_resilience_Document_v2_sandbox_usercollection_daily_resilience__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/DailyResilienceModel"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_resilience/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_resilience/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_resilience/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_resilience/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_sleep`

### GET — Sandbox - Multiple Daily Sleep Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Daily Sleep Documents",
  "operationId": "Sandbox___Multiple_daily_sleep_Documents_v2_sandbox_usercollection_daily_sleep_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailySleep_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Daily Sleep Documents V2 Sandbox Usercollection Daily Sleep Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01&fields=day,score' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_sleep' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,score' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01&fields=day,score', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01&fields=day,score\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_sleep/{document_id}`

### GET — Sandbox - Single Daily Sleep Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Daily Sleep Document",
  "operationId": "Sandbox___Single_daily_sleep_Document_v2_sandbox_usercollection_daily_sleep__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailySleep"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_sleep/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_sleep/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_sleep/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_sleep/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_spo2`

### GET — Sandbox - Multiple Daily Spo2 Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Daily Spo2 Documents",
  "operationId": "Sandbox___Multiple_daily_spo2_Documents_v2_sandbox_usercollection_daily_spo2_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailySpO2_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Daily Spo2 Documents V2 Sandbox Usercollection Daily Spo2 Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_spo2?start_date=2021-11-01&end_date=2021-12-01&fields=breathing_disturbance_index,day' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_spo2' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'breathing_disturbance_index,day' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_spo2?start_date=2021-11-01&end_date=2021-12-01&fields=breathing_disturbance_index,day', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_spo2?start_date=2021-11-01&end_date=2021-12-01&fields=breathing_disturbance_index,day\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_spo2/{document_id}`

### GET — Sandbox - Single Daily Spo2 Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Daily Spo2 Document",
  "operationId": "Sandbox___Single_daily_spo2_Document_v2_sandbox_usercollection_daily_spo2__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailySpO2"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_spo2/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_spo2/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_spo2/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_spo2/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_stress`

### GET — Sandbox - Multiple Daily Stress Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Daily Stress Documents",
  "operationId": "Sandbox___Multiple_daily_stress_Documents_v2_sandbox_usercollection_daily_stress_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailyStress_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Daily Stress Documents V2 Sandbox Usercollection Daily Stress Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_stress?start_date=2021-11-01&end_date=2021-12-01&fields=day,day_summary' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_stress' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,day_summary' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_stress?start_date=2021-11-01&end_date=2021-12-01&fields=day,day_summary', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_stress?start_date=2021-11-01&end_date=2021-12-01&fields=day,day_summary\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/daily_stress/{document_id}`

### GET — Sandbox - Single Daily Stress Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Daily Stress Document",
  "operationId": "Sandbox___Single_daily_stress_Document_v2_sandbox_usercollection_daily_stress__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailyStress"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/daily_stress/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/daily_stress/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/daily_stress/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/daily_stress/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/enhanced_tag`

### GET — Sandbox - Multiple Enhanced Tag Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Enhanced Tag Documents",
  "operationId": "Sandbox___Multiple_enhanced_tag_Documents_v2_sandbox_usercollection_enhanced_tag_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_EnhancedTagModel_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Enhanced Tag Documents V2 Sandbox Usercollection Enhanced Tag Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/enhanced_tag?start_date=2021-11-01&end_date=2021-12-01' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/enhanced_tag' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/enhanced_tag?start_date=2021-11-01&end_date=2021-12-01', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/enhanced_tag?start_date=2021-11-01&end_date=2021-12-01\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/enhanced_tag/{document_id}`

### GET — Sandbox - Single Enhanced Tag Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Enhanced Tag Document",
  "operationId": "Sandbox___Single_enhanced_tag_Document_v2_sandbox_usercollection_enhanced_tag__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/EnhancedTagModel"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/enhanced_tag/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/enhanced_tag/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/enhanced_tag/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/enhanced_tag/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/heartrate`

### GET — Sandbox - Multiple Heartrate Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Heartrate Documents",
  "operationId": "Sandbox___Multiple_heartrate_Documents_v2_sandbox_usercollection_heartrate_get",
  "parameters": [
    {
      "name": "start_datetime",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Datetime"
      }
    },
    {
      "name": "end_datetime",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Datetime"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/TimeSeriesResponse_PublicHeartRateRow_"
              },
              {
                "$ref": "#/components/schemas/TimeSeriesResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Heartrate Documents V2 Sandbox Usercollection Heartrate Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "# The '+' symbol in the timezone must be escaped to `%2B` if included. \ncurl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/heartrate?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,bpm' \\ \n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/heartrate' \nparams={ \n    'start_datetime': '2021-11-01T00:00:00-08:00', \n    'end_datetime': '2021-12-01T00:00:00-08:00',\n    'fields': 'timestamp,bpm' \n} \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/heartrate?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,bpm', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/heartrate?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,bpm\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/rest_mode_period`

### GET — Sandbox - Multiple Rest Mode Period Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Rest Mode Period Documents",
  "operationId": "Sandbox___Multiple_rest_mode_period_Documents_v2_sandbox_usercollection_rest_mode_period_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicRestModePeriod_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Rest Mode Period Documents V2 Sandbox Usercollection Rest Mode Period Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/rest_mode_period?start_date=2021-11-01&end_date=2021-12-01&fields=end_day,end_time' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/rest_mode_period' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'end_day,end_time' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/rest_mode_period?start_date=2021-11-01&end_date=2021-12-01&fields=end_day,end_time', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/rest_mode_period?start_date=2021-11-01&end_date=2021-12-01&fields=end_day,end_time\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/rest_mode_period/{document_id}`

### GET — Sandbox - Single Rest Mode Period Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Rest Mode Period Document",
  "operationId": "Sandbox___Single_rest_mode_period_Document_v2_sandbox_usercollection_rest_mode_period__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicRestModePeriod"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/rest_mode_period/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/rest_mode_period/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/rest_mode_period/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/rest_mode_period/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/ring_battery_level`

### GET — Sandbox - Multiple Ring Battery Level Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Ring Battery Level Documents",
  "operationId": "Sandbox___Multiple_ring_battery_level_Documents_v2_sandbox_usercollection_ring_battery_level_get",
  "parameters": [
    {
      "name": "start_datetime",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Datetime"
      }
    },
    {
      "name": "end_datetime",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Datetime"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/TimeSeriesResponse_PublicRingBatteryLevelRow_"
              },
              {
                "$ref": "#/components/schemas/TimeSeriesResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Ring Battery Level Documents V2 Sandbox Usercollection Ring Battery Level Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "# The '+' symbol in the timezone must be escaped to `%2B` if included. \ncurl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/ring_battery_level?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,timestamp_unix' \\ \n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/ring_battery_level' \nparams={ \n    'start_datetime': '2021-11-01T00:00:00-08:00', \n    'end_datetime': '2021-12-01T00:00:00-08:00',\n    'fields': 'timestamp,timestamp_unix' \n} \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/ring_battery_level?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,timestamp_unix', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/ring_battery_level?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,timestamp_unix\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/ring_configuration`

### GET — Sandbox - Multiple Ring Configuration Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Ring Configuration Documents",
  "operationId": "Sandbox___Multiple_ring_configuration_Documents_v2_sandbox_usercollection_ring_configuration_get",
  "parameters": [
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicRingConfiguration_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Ring Configuration Documents V2 Sandbox Usercollection Ring Configuration Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/ring_configuration?fields=color,design' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/ring_configuration' \nparams = {'fields': 'color,design'}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/ring_configuration?fields=color,design', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/ring_configuration?fields=color,design\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/ring_configuration/{document_id}`

### GET — Sandbox - Single Ring Configuration Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Ring Configuration Document",
  "operationId": "Sandbox___Single_ring_configuration_Document_v2_sandbox_usercollection_ring_configuration__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicRingConfiguration"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/ring_configuration/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/ring_configuration/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/ring_configuration/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/ring_configuration/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/session`

### GET — Sandbox - Multiple Session Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Session Documents",
  "operationId": "Sandbox___Multiple_session_Documents_v2_sandbox_usercollection_session_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicSession_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Session Documents V2 Sandbox Usercollection Session Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/session?start_date=2021-11-01&end_date=2021-12-01&fields=day,end_datetime' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/session' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,end_datetime' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/session?start_date=2021-11-01&end_date=2021-12-01&fields=day,end_datetime', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/session?start_date=2021-11-01&end_date=2021-12-01&fields=day,end_datetime\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/session/{document_id}`

### GET — Sandbox - Single Session Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Session Document",
  "operationId": "Sandbox___Single_session_Document_v2_sandbox_usercollection_session__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicSession"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/session/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/session/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/session/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/session/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/sleep`

### GET — Sandbox - Multiple Sleep Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Sleep Documents",
  "operationId": "Sandbox___Multiple_sleep_Documents_v2_sandbox_usercollection_sleep_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicModifiedSleepModel_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Sleep Documents V2 Sandbox Usercollection Sleep Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/sleep?start_date=2021-11-01&end_date=2021-12-01&fields=average_breath,average_heart_rate' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/sleep' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'average_breath,average_heart_rate' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/sleep?start_date=2021-11-01&end_date=2021-12-01&fields=average_breath,average_heart_rate', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/sleep?start_date=2021-11-01&end_date=2021-12-01&fields=average_breath,average_heart_rate\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/sleep/{document_id}`

### GET — Sandbox - Single Sleep Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Sleep Document",
  "operationId": "Sandbox___Single_sleep_Document_v2_sandbox_usercollection_sleep__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicModifiedSleepModel"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/sleep/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/sleep/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/sleep/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/sleep/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/sleep_time`

### GET — Sandbox - Multiple Sleep Time Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Sleep Time Documents",
  "operationId": "Sandbox___Multiple_sleep_time_Documents_v2_sandbox_usercollection_sleep_time_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicSleepTime_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Sleep Time Documents V2 Sandbox Usercollection Sleep Time Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/sleep_time?start_date=2021-11-01&end_date=2021-12-01&fields=day,optimal_bedtime' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/sleep_time' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,optimal_bedtime' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/sleep_time?start_date=2021-11-01&end_date=2021-12-01&fields=day,optimal_bedtime', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/sleep_time?start_date=2021-11-01&end_date=2021-12-01&fields=day,optimal_bedtime\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/sleep_time/{document_id}`

### GET — Sandbox - Single Sleep Time Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Sleep Time Document",
  "operationId": "Sandbox___Single_sleep_time_Document_v2_sandbox_usercollection_sleep_time__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicSleepTime"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/sleep_time/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/sleep_time/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/sleep_time/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/sleep_time/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/tag`

### GET — Sandbox - Multiple Tag Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Tag Documents",
  "operationId": "Sandbox___Multiple_tag_Documents_v2_sandbox_usercollection_tag_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_TagModel_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Tag Documents V2 Sandbox Usercollection Tag Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/tag?start_date=2021-11-01&end_date=2021-12-01' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/tag' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/tag?start_date=2021-11-01&end_date=2021-12-01', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/tag?start_date=2021-11-01&end_date=2021-12-01\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/tag/{document_id}`

### GET — Sandbox - Single Tag Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Tag Document",
  "operationId": "Sandbox___Single_tag_Document_v2_sandbox_usercollection_tag__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/TagModel"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/tag/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/tag/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/tag/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/tag/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/vO2_max`

### GET — Sandbox - Multiple Vo2 Max Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Vo2 Max Documents",
  "operationId": "Sandbox___Multiple_vO2_max_Documents_v2_sandbox_usercollection_vO2_max_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicVO2Max_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Vo2 Max Documents V2 Sandbox Usercollection Vo2 Max Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/vO2_max?start_date=2021-11-01&end_date=2021-12-01&fields=day,timestamp' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/vO2_max' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,timestamp' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/vO2_max?start_date=2021-11-01&end_date=2021-12-01&fields=day,timestamp', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/vO2_max?start_date=2021-11-01&end_date=2021-12-01&fields=day,timestamp\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/vO2_max/{document_id}`

### GET — Sandbox - Single Vo2 Max Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Vo2 Max Document",
  "operationId": "Sandbox___Single_vO2_max_Document_v2_sandbox_usercollection_vO2_max__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicVO2Max"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/vO2_max/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/vO2_max/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/vO2_max/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/vO2_max/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/workout`

### GET — Sandbox - Multiple Workout Documents

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Multiple Workout Documents",
  "operationId": "Sandbox___Multiple_workout_Documents_v2_sandbox_usercollection_workout_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicWorkout_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Sandbox   Multiple Workout Documents V2 Sandbox Usercollection Workout Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/workout?start_date=2021-11-01&end_date=2021-12-01&fields=activity,calories' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/workout' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'activity,calories' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/workout?start_date=2021-11-01&end_date=2021-12-01&fields=activity,calories', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/workout?start_date=2021-11-01&end_date=2021-12-01&fields=activity,calories\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/sandbox/usercollection/workout/{document_id}`

### GET — Sandbox - Single Workout Document

```json
{
  "tags": [
    "Sandbox Routes"
  ],
  "summary": "Sandbox - Single Workout Document",
  "operationId": "Sandbox___Single_workout_Document_v2_sandbox_usercollection_workout__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicWorkout"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/sandbox/usercollection/workout/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/sandbox/usercollection/workout/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/sandbox/usercollection/workout/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/sandbox/usercollection/workout/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_activity`

### GET — Multiple Daily Activity Documents

```json
{
  "tags": [
    "Daily Activity Routes"
  ],
  "summary": "Multiple Daily Activity Documents",
  "operationId": "Multiple_daily_activity_Documents_v2_usercollection_daily_activity_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailyActivity_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Daily Activity Documents V2 Usercollection Daily Activity Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_activity?start_date=2021-11-01&end_date=2021-12-01&fields=day,score' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_activity' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,score' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_activity?start_date=2021-11-01&end_date=2021-12-01&fields=day,score', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_activity?start_date=2021-11-01&end_date=2021-12-01&fields=day,score\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_activity/{document_id}`

### GET — Single Daily Activity Document

```json
{
  "tags": [
    "Daily Activity Routes"
  ],
  "summary": "Single Daily Activity Document",
  "operationId": "Single_daily_activity_Document_v2_usercollection_daily_activity__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailyActivity"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_activity/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_activity/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_activity/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_activity/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_cardiovascular_age`

### GET — Multiple Daily Cardiovascular Age Documents

```json
{
  "tags": [
    "Daily Cardiovascular Age Routes"
  ],
  "summary": "Multiple Daily Cardiovascular Age Documents",
  "operationId": "Multiple_daily_cardiovascular_age_Documents_v2_usercollection_daily_cardiovascular_age_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailyCardiovascularAge_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Daily Cardiovascular Age Documents V2 Usercollection Daily Cardiovascular Age Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_cardiovascular_age?start_date=2021-11-01&end_date=2021-12-01&fields=day,pulse_wave_velocity' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_cardiovascular_age' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,pulse_wave_velocity' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_cardiovascular_age?start_date=2021-11-01&end_date=2021-12-01&fields=day,pulse_wave_velocity', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_cardiovascular_age?start_date=2021-11-01&end_date=2021-12-01&fields=day,pulse_wave_velocity\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_cardiovascular_age/{document_id}`

### GET — Single Daily Cardiovascular Age Document

```json
{
  "tags": [
    "Daily Cardiovascular Age Routes"
  ],
  "summary": "Single Daily Cardiovascular Age Document",
  "operationId": "Single_daily_cardiovascular_age_Document_v2_usercollection_daily_cardiovascular_age__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailyCardiovascularAge"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_cardiovascular_age/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_cardiovascular_age/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_cardiovascular_age/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_cardiovascular_age/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_readiness`

### GET — Multiple Daily Readiness Documents

```json
{
  "tags": [
    "Daily Readiness Routes"
  ],
  "summary": "Multiple Daily Readiness Documents",
  "operationId": "Multiple_daily_readiness_Documents_v2_usercollection_daily_readiness_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailyReadiness_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Daily Readiness Documents V2 Usercollection Daily Readiness Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_readiness?start_date=2021-11-01&end_date=2021-12-01&fields=day,score' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_readiness' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,score' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_readiness?start_date=2021-11-01&end_date=2021-12-01&fields=day,score', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_readiness?start_date=2021-11-01&end_date=2021-12-01&fields=day,score\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_readiness/{document_id}`

### GET — Single Daily Readiness Document

```json
{
  "tags": [
    "Daily Readiness Routes"
  ],
  "summary": "Single Daily Readiness Document",
  "operationId": "Single_daily_readiness_Document_v2_usercollection_daily_readiness__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailyReadiness"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_readiness/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_readiness/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_readiness/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_readiness/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_resilience`

### GET — Multiple Daily Resilience Documents

```json
{
  "tags": [
    "Daily Resilience Routes"
  ],
  "summary": "Multiple Daily Resilience Documents",
  "operationId": "Multiple_daily_resilience_Documents_v2_usercollection_daily_resilience_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "N/A. This route does not support field selection yet, all fields will be returned.",
        "title": "Fields"
      },
      "description": "N/A. This route does not support field selection yet, all fields will be returned."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_DailyResilienceModel_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Daily Resilience Documents V2 Usercollection Daily Resilience Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_resilience?start_date=2021-11-01&end_date=2021-12-01' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_resilience' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_resilience?start_date=2021-11-01&end_date=2021-12-01', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_resilience?start_date=2021-11-01&end_date=2021-12-01\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_resilience/{document_id}`

### GET — Single Daily Resilience Document

```json
{
  "tags": [
    "Daily Resilience Routes"
  ],
  "summary": "Single Daily Resilience Document",
  "operationId": "Single_daily_resilience_Document_v2_usercollection_daily_resilience__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/DailyResilienceModel"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_resilience/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_resilience/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_resilience/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_resilience/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_sleep`

### GET — Multiple Daily Sleep Documents

```json
{
  "tags": [
    "Daily Sleep Routes"
  ],
  "summary": "Multiple Daily Sleep Documents",
  "operationId": "Multiple_daily_sleep_Documents_v2_usercollection_daily_sleep_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailySleep_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Daily Sleep Documents V2 Usercollection Daily Sleep Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01&fields=day,score' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_sleep' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,score' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01&fields=day,score', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01&fields=day,score\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_sleep/{document_id}`

### GET — Single Daily Sleep Document

```json
{
  "tags": [
    "Daily Sleep Routes"
  ],
  "summary": "Single Daily Sleep Document",
  "operationId": "Single_daily_sleep_Document_v2_usercollection_daily_sleep__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailySleep"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_sleep/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_sleep/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_sleep/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_sleep/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_spo2`

### GET — Multiple Daily Spo2 Documents

```json
{
  "tags": [
    "Daily Spo2 Routes"
  ],
  "summary": "Multiple Daily Spo2 Documents",
  "operationId": "Multiple_daily_spo2_Documents_v2_usercollection_daily_spo2_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailySpO2_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Daily Spo2 Documents V2 Usercollection Daily Spo2 Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_spo2?start_date=2021-11-01&end_date=2021-12-01&fields=breathing_disturbance_index,day' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_spo2' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'breathing_disturbance_index,day' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_spo2?start_date=2021-11-01&end_date=2021-12-01&fields=breathing_disturbance_index,day', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_spo2?start_date=2021-11-01&end_date=2021-12-01&fields=breathing_disturbance_index,day\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_spo2/{document_id}`

### GET — Single Daily Spo2 Document

```json
{
  "tags": [
    "Daily Spo2 Routes"
  ],
  "summary": "Single Daily Spo2 Document",
  "operationId": "Single_daily_spo2_Document_v2_usercollection_daily_spo2__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailySpO2"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_spo2/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_spo2/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_spo2/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_spo2/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_stress`

### GET — Multiple Daily Stress Documents

```json
{
  "tags": [
    "Daily Stress Routes"
  ],
  "summary": "Multiple Daily Stress Documents",
  "operationId": "Multiple_daily_stress_Documents_v2_usercollection_daily_stress_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicDailyStress_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Daily Stress Documents V2 Usercollection Daily Stress Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_stress?start_date=2021-11-01&end_date=2021-12-01&fields=day,day_summary' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_stress' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,day_summary' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_stress?start_date=2021-11-01&end_date=2021-12-01&fields=day,day_summary', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_stress?start_date=2021-11-01&end_date=2021-12-01&fields=day,day_summary\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/daily_stress/{document_id}`

### GET — Single Daily Stress Document

```json
{
  "tags": [
    "Daily Stress Routes"
  ],
  "summary": "Single Daily Stress Document",
  "operationId": "Single_daily_stress_Document_v2_usercollection_daily_stress__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicDailyStress"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/daily_stress/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/daily_stress/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/daily_stress/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/daily_stress/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/enhanced_tag`

### GET — Multiple Enhanced Tag Documents

```json
{
  "tags": [
    "Enhanced Tag Routes"
  ],
  "summary": "Multiple Enhanced Tag Documents",
  "operationId": "Multiple_enhanced_tag_Documents_v2_usercollection_enhanced_tag_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "N/A. This route does not support field selection yet, all fields will be returned.",
        "title": "Fields"
      },
      "description": "N/A. This route does not support field selection yet, all fields will be returned."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_EnhancedTagModel_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Enhanced Tag Documents V2 Usercollection Enhanced Tag Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/enhanced_tag?start_date=2021-11-01&end_date=2021-12-01' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/enhanced_tag' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/enhanced_tag?start_date=2021-11-01&end_date=2021-12-01', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/enhanced_tag?start_date=2021-11-01&end_date=2021-12-01\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/enhanced_tag/{document_id}`

### GET — Single Enhanced Tag Document

```json
{
  "tags": [
    "Enhanced Tag Routes"
  ],
  "summary": "Single Enhanced Tag Document",
  "operationId": "Single_enhanced_tag_Document_v2_usercollection_enhanced_tag__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/EnhancedTagModel"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/enhanced_tag/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/enhanced_tag/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/enhanced_tag/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/enhanced_tag/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/heartrate`

### GET — Multiple Heartrate Documents

```json
{
  "tags": [
    "Heart Rate Routes"
  ],
  "summary": "Multiple Heartrate Documents",
  "operationId": "Multiple_heartrate_Documents_v2_usercollection_heartrate_get",
  "parameters": [
    {
      "name": "start_datetime",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Datetime"
      }
    },
    {
      "name": "end_datetime",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Datetime"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "latest",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "boolean"
          },
          {
            "type": "null"
          }
        ],
        "description": "If True, returns most recent sample.",
        "title": "Latest"
      },
      "description": "If True, returns most recent sample."
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/TimeSeriesResponse_PublicHeartRateRow_"
              },
              {
                "$ref": "#/components/schemas/TimeSeriesResponseDict"
              }
            ],
            "title": "Response Multiple Heartrate Documents V2 Usercollection Heartrate Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "# The '+' symbol in the timezone must be escaped to `%2B` if included. \ncurl --location --request GET 'https://api.ouraring.com/v2/usercollection/heartrate?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,bpm' \\ \n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/heartrate' \nparams={ \n    'start_datetime': '2021-11-01T00:00:00-08:00', \n    'end_datetime': '2021-12-01T00:00:00-08:00',\n    'fields': 'timestamp,bpm' \n} \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/heartrate?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,bpm', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/heartrate?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,bpm\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/personal_info`

### GET — Single Personal Info Document

```json
{
  "tags": [
    "Personal Info Routes"
  ],
  "summary": "Single Personal Info Document",
  "operationId": "Single_Personal_Info_Document_v2_usercollection_personal_info_get",
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PersonalInfoResponse"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/personal_info' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/personal_info' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders,\n}; \nfetch('https://api.ouraring.com/v2/usercollection/personal_info', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/personal_info\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/rest_mode_period`

### GET — Multiple Rest Mode Period Documents

```json
{
  "tags": [
    "Rest Mode Period Routes"
  ],
  "summary": "Multiple Rest Mode Period Documents",
  "operationId": "Multiple_rest_mode_period_Documents_v2_usercollection_rest_mode_period_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicRestModePeriod_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Rest Mode Period Documents V2 Usercollection Rest Mode Period Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/rest_mode_period?start_date=2021-11-01&end_date=2021-12-01&fields=end_day,end_time' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/rest_mode_period' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'end_day,end_time' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/rest_mode_period?start_date=2021-11-01&end_date=2021-12-01&fields=end_day,end_time', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/rest_mode_period?start_date=2021-11-01&end_date=2021-12-01&fields=end_day,end_time\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/rest_mode_period/{document_id}`

### GET — Single Rest Mode Period Document

```json
{
  "tags": [
    "Rest Mode Period Routes"
  ],
  "summary": "Single Rest Mode Period Document",
  "operationId": "Single_rest_mode_period_Document_v2_usercollection_rest_mode_period__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicRestModePeriod"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/rest_mode_period/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/rest_mode_period/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/rest_mode_period/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/rest_mode_period/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/ring_battery_level`

### GET — Multiple Ring Battery Level Documents

```json
{
  "tags": [
    "Ring Battery Level Routes"
  ],
  "summary": "Multiple Ring Battery Level Documents",
  "operationId": "Multiple_ring_battery_level_Documents_v2_usercollection_ring_battery_level_get",
  "parameters": [
    {
      "name": "start_datetime",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Datetime"
      }
    },
    {
      "name": "end_datetime",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Datetime"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "latest",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "boolean"
          },
          {
            "type": "null"
          }
        ],
        "description": "If True, returns most recent sample.",
        "title": "Latest"
      },
      "description": "If True, returns most recent sample."
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/TimeSeriesResponse_PublicRingBatteryLevelRow_"
              },
              {
                "$ref": "#/components/schemas/TimeSeriesResponseDict"
              }
            ],
            "title": "Response Multiple Ring Battery Level Documents V2 Usercollection Ring Battery Level Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "# The '+' symbol in the timezone must be escaped to `%2B` if included. \ncurl --location --request GET 'https://api.ouraring.com/v2/usercollection/ring_battery_level?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,timestamp_unix' \\ \n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/ring_battery_level' \nparams={ \n    'start_datetime': '2021-11-01T00:00:00-08:00', \n    'end_datetime': '2021-12-01T00:00:00-08:00',\n    'fields': 'timestamp,timestamp_unix' \n} \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/ring_battery_level?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,timestamp_unix', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/ring_battery_level?start_datetime=2021-11-01T00:00:00-08:00&end_datetime=2021-12-01T00:00:00-08:00&fields=timestamp,timestamp_unix\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/ring_configuration`

### GET — Multiple Ring Configuration Documents

```json
{
  "tags": [
    "Ring Configuration Routes"
  ],
  "summary": "Multiple Ring Configuration Documents",
  "operationId": "Multiple_ring_configuration_Documents_v2_usercollection_ring_configuration_get",
  "parameters": [
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicRingConfiguration_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Ring Configuration Documents V2 Usercollection Ring Configuration Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/ring_configuration?fields=color,design' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/ring_configuration' \nparams = {'fields': 'color,design'}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/ring_configuration?fields=color,design', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/ring_configuration?fields=color,design\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/ring_configuration/{document_id}`

### GET — Single Ring Configuration Document

```json
{
  "tags": [
    "Ring Configuration Routes"
  ],
  "summary": "Single Ring Configuration Document",
  "operationId": "Single_ring_configuration_Document_v2_usercollection_ring_configuration__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicRingConfiguration"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/ring_configuration/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/ring_configuration/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/ring_configuration/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/ring_configuration/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/session`

### GET — Multiple Session Documents

```json
{
  "tags": [
    "Session Routes"
  ],
  "summary": "Multiple Session Documents",
  "operationId": "Multiple_session_Documents_v2_usercollection_session_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicSession_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Session Documents V2 Usercollection Session Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/session?start_date=2021-11-01&end_date=2021-12-01&fields=day,end_datetime' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/session' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,end_datetime' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/session?start_date=2021-11-01&end_date=2021-12-01&fields=day,end_datetime', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/session?start_date=2021-11-01&end_date=2021-12-01&fields=day,end_datetime\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/session/{document_id}`

### GET — Single Session Document

```json
{
  "tags": [
    "Session Routes"
  ],
  "summary": "Single Session Document",
  "operationId": "Single_session_Document_v2_usercollection_session__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicSession"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/session/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/session/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/session/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/session/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/sleep`

### GET — Multiple Sleep Documents

```json
{
  "tags": [
    "Sleep Routes"
  ],
  "summary": "Multiple Sleep Documents",
  "operationId": "Multiple_sleep_Documents_v2_usercollection_sleep_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicModifiedSleepModel_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Sleep Documents V2 Usercollection Sleep Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/sleep?start_date=2021-11-01&end_date=2021-12-01&fields=average_breath,average_heart_rate' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/sleep' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'average_breath,average_heart_rate' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/sleep?start_date=2021-11-01&end_date=2021-12-01&fields=average_breath,average_heart_rate', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/sleep?start_date=2021-11-01&end_date=2021-12-01&fields=average_breath,average_heart_rate\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/sleep/{document_id}`

### GET — Single Sleep Document

```json
{
  "tags": [
    "Sleep Routes"
  ],
  "summary": "Single Sleep Document",
  "operationId": "Single_sleep_Document_v2_usercollection_sleep__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicModifiedSleepModel"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/sleep/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/sleep/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/sleep/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/sleep/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/sleep_time`

### GET — Multiple Sleep Time Documents

```json
{
  "tags": [
    "Sleep Time Routes"
  ],
  "summary": "Multiple Sleep Time Documents",
  "operationId": "Multiple_sleep_time_Documents_v2_usercollection_sleep_time_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicSleepTime_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Sleep Time Documents V2 Usercollection Sleep Time Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/sleep_time?start_date=2021-11-01&end_date=2021-12-01&fields=day,optimal_bedtime' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/sleep_time' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,optimal_bedtime' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/sleep_time?start_date=2021-11-01&end_date=2021-12-01&fields=day,optimal_bedtime', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/sleep_time?start_date=2021-11-01&end_date=2021-12-01&fields=day,optimal_bedtime\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/sleep_time/{document_id}`

### GET — Single Sleep Time Document

```json
{
  "tags": [
    "Sleep Time Routes"
  ],
  "summary": "Single Sleep Time Document",
  "operationId": "Single_sleep_time_Document_v2_usercollection_sleep_time__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicSleepTime"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/sleep_time/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/sleep_time/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/sleep_time/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/sleep_time/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/tag`

### GET — Multiple Tag Documents

```json
{
  "tags": [
    "Tag Routes"
  ],
  "summary": "Multiple Tag Documents",
  "operationId": "Multiple_tag_Documents_v2_usercollection_tag_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "N/A. This route does not support field selection yet, all fields will be returned.",
        "title": "Fields"
      },
      "description": "N/A. This route does not support field selection yet, all fields will be returned."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_TagModel_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Tag Documents V2 Usercollection Tag Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/tag?start_date=2021-11-01&end_date=2021-12-01' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/tag' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/tag?start_date=2021-11-01&end_date=2021-12-01', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/tag?start_date=2021-11-01&end_date=2021-12-01\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/tag/{document_id}`

### GET — Single Tag Document

```json
{
  "tags": [
    "Tag Routes"
  ],
  "summary": "Single Tag Document",
  "operationId": "Single_tag_Document_v2_usercollection_tag__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/TagModel"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/tag/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/tag/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/tag/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/tag/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/vO2_max`

### GET — Multiple Vo2 Max Documents

```json
{
  "tags": [
    "VO2 Max Routes"
  ],
  "summary": "Multiple Vo2 Max Documents",
  "operationId": "Multiple_vO2_max_Documents_v2_usercollection_vO2_max_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicVO2Max_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Vo2 Max Documents V2 Usercollection Vo2 Max Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/vO2_max?start_date=2021-11-01&end_date=2021-12-01&fields=day,timestamp' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/vO2_max' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'day,timestamp' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/vO2_max?start_date=2021-11-01&end_date=2021-12-01&fields=day,timestamp', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/vO2_max?start_date=2021-11-01&end_date=2021-12-01&fields=day,timestamp\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/vO2_max/{document_id}`

### GET — Single Vo2 Max Document

```json
{
  "tags": [
    "VO2 Max Routes"
  ],
  "summary": "Single Vo2 Max Document",
  "operationId": "Single_vO2_max_Document_v2_usercollection_vO2_max__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicVO2Max"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/vO2_max/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/vO2_max/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/vO2_max/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/vO2_max/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/workout`

### GET — Multiple Workout Documents

```json
{
  "tags": [
    "Workout Routes"
  ],
  "summary": "Multiple Workout Documents",
  "operationId": "Multiple_workout_Documents_v2_usercollection_workout_get",
  "parameters": [
    {
      "name": "start_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "Start Date"
      }
    },
    {
      "name": "end_date",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string",
            "format": "date"
          },
          {
            "type": "null"
          }
        ],
        "title": "End Date"
      }
    },
    {
      "name": "next_token",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "title": "Next Token"
      }
    },
    {
      "name": "fields",
      "in": "query",
      "required": false,
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided.",
        "title": "Fields"
      },
      "description": "Comma-separated list of fields to include in the response, in addition to the always returned fields. Defaults to all fields if not provided."
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MultiDocumentResponse_PublicWorkout_"
              },
              {
                "$ref": "#/components/schemas/MultiDocumentResponseDict"
              }
            ],
            "title": "Response Multiple Workout Documents V2 Usercollection Workout Get"
          }
        }
      }
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/workout?start_date=2021-11-01&end_date=2021-12-01&fields=activity,calories' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/workout' \nparams={ \n    'start_date': '2021-11-01', \n    'end_date': '2021-12-01',\n    'fields': 'activity,calories' \n}\nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/workout?start_date=2021-11-01&end_date=2021-12-01&fields=activity,calories', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/workout?start_date=2021-11-01&end_date=2021-12-01&fields=activity,calories\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/usercollection/workout/{document_id}`

### GET — Single Workout Document

```json
{
  "tags": [
    "Workout Routes"
  ],
  "summary": "Single Workout Document",
  "operationId": "Single_workout_Document_v2_usercollection_workout__document_id__get",
  "parameters": [
    {
      "name": "document_id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Document Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PublicWorkout"
          }
        }
      }
    },
    "404": {
      "description": "Not Found"
    },
    "400": {
      "description": "Client Exception"
    },
    "401": {
      "description": "Unauthorized access exception. Usually means the access token is expired, malformed or revoked."
    },
    "403": {
      "description": "Access forbidden. Usually means the user's subscription to Oura has expired and their data is not available via the API."
    },
    "429": {
      "description": "Request Rate Limit Exceeded."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "BearerAuth": []
    },
    {
      "OAuth2": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/usercollection/workout/2-5daccc095220cc5493a4e9c2b681ca941e' \\\n--header 'Authorization: Bearer <token>' \\\n--header 'User-Agent: YourAppName/1.0'"
    },
    {
      "lang": "Python",
      "source": "import requests \nurl = 'https://api.ouraring.com/v2/usercollection/workout/2-5daccc095220cc5493a4e9c2b681ca941e' \nheaders = { \n  'Authorization': 'Bearer <token>', \n  'User-Agent': 'YourAppName/1.0' \n}\nresponse = requests.request('GET', url, headers=headers, params=params) \nprint(response.text)",
      "label": "Python"
    },
    {
      "lang": "JavaScript",
      "source": "var myHeaders = new Headers(); \nmyHeaders.append('Authorization', 'Bearer <token>'); \nmyHeaders.append('User-Agent', 'YourAppName/1.0'); \nvar requestOptions = { \n  method: 'GET', \n  headers: myHeaders, \n}; \nfetch('https://api.ouraring.com/v2/usercollection/workout/2-5daccc095220cc5493a4e9c2b681ca941e', requestOptions) \n  .then(response => response.text()) \n  .then(result => console.log(result)) \n  .catch(error => console.log('error', error));",
      "label": "JavaScript"
    },
    {
      "lang": "Java",
      "source": "OkHttpClient client = new OkHttpClient().newBuilder() \n  .build(); \nRequest request = new Request.Builder() \n  .url(\"https://api.ouraring.com/v2/usercollection/workout/2-5daccc095220cc5493a4e9c2b681ca941e\") \n  .method(\"GET\", null) \n  .addHeader(\"Authorization\", \"Bearer <token>\") \n  .addHeader(\"User-Agent\", \"YourAppName/1.0\") \n  .build(); \nResponse response = client.newCall(request).execute();",
      "label": "Java"
    }
  ]
}
```

## `/v2/webhook/subscription`

### GET — List Webhook Subscriptions

```json
{
  "tags": [
    "Webhook Subscription Routes"
  ],
  "summary": "List Webhook Subscriptions",
  "operationId": "list_webhook_subscriptions_v2_webhook_subscription_get",
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "items": {
              "$ref": "#/components/schemas/WebhookSubscriptionModel"
            },
            "type": "array",
            "title": "Response List Webhook Subscriptions V2 Webhook Subscription Get"
          }
        }
      }
    }
  },
  "security": [
    {
      "ClientIdAuth": [],
      "ClientSecretAuth": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/webhook/subscription' --header 'x-client-id: client-id' --header 'x-client-secret: client-secret' --header 'User-Agent: YourAppName/1.0'"
    }
  ]
}
```

### POST — Create Webhook Subscription

```json
{
  "tags": [
    "Webhook Subscription Routes"
  ],
  "summary": "Create Webhook Subscription",
  "operationId": "create_webhook_subscription_v2_webhook_subscription_post",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/CreateWebhookSubscriptionRequest"
        }
      }
    },
    "required": true
  },
  "responses": {
    "201": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/WebhookSubscriptionModel"
          }
        }
      }
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "ClientIdAuth": [],
      "ClientSecretAuth": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request POST 'https://api.ouraring.com/v2/webhook/subscription' --header 'x-client-id: client-id' --header 'x-client-secret: client-secret' --header 'User-Agent: YourAppName/1.0' --header 'Content-Type: application/json' --data-raw '{\n    \"callback_url\": \"https://my-api/oura/tag/delete\",\n    \"verification_token\": \"123\",\n    \"event_type\": \"delete\",\n    \"data_type\": \"tag\"\n}'"
    }
  ]
}
```

## `/v2/webhook/subscription/renew/{id}`

### PUT — Renew Webhook Subscription

```json
{
  "tags": [
    "Webhook Subscription Routes"
  ],
  "summary": "Renew Webhook Subscription",
  "operationId": "renew_webhook_subscription_v2_webhook_subscription_renew__id__put",
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/WebhookSubscriptionModel"
          }
        }
      }
    },
    "403": {
      "description": "Webhook with specified id does not exist."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "ClientIdAuth": [],
      "ClientSecretAuth": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request PUT 'https://api.ouraring.com/v2/webhook/subscription/renew/5d3fe17b-f880-4d93-b9b6-afbfb76c1e78' --header 'x-client-id: client-id' --header 'x-client-secret: client-secret' --header 'User-Agent: YourAppName/1.0' --header 'Content-Type: application/json'"
    }
  ]
}
```

## `/v2/webhook/subscription/{id}`

### GET — Get Webhook Subscription

```json
{
  "tags": [
    "Webhook Subscription Routes"
  ],
  "summary": "Get Webhook Subscription",
  "operationId": "get_webhook_subscription_v2_webhook_subscription__id__get",
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Id"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/WebhookSubscriptionModel"
          }
        }
      }
    },
    "403": {
      "description": "Webhook with specified id does not exist."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "ClientIdAuth": [],
      "ClientSecretAuth": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request GET 'https://api.ouraring.com/v2/webhook/subscription/5d3fe17b-f880-4d93-b9b6-afbfb76c1e78' --header 'x-client-id: client-id' --header 'x-client-secret: client-secret' --header 'User-Agent: YourAppName/1.0'"
    }
  ]
}
```

### PUT — Update Webhook Subscription

```json
{
  "tags": [
    "Webhook Subscription Routes"
  ],
  "summary": "Update Webhook Subscription",
  "operationId": "update_webhook_subscription_v2_webhook_subscription__id__put",
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Id"
      }
    }
  ],
  "requestBody": {
    "required": true,
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/UpdateWebhookSubscriptionRequest"
        }
      }
    }
  },
  "responses": {
    "200": {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/WebhookSubscriptionModel"
          }
        }
      }
    },
    "403": {
      "description": "Webhook with specified id does not exist."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "ClientIdAuth": [],
      "ClientSecretAuth": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request PUT 'https://api.ouraring.com/v2/webhook/subscription/5d3fe17b-f880-4d93-b9b6-afbfb76c1e78' --header 'x-client-id: client-id' --header 'x-client-secret: client-secret' --header 'User-Agent: YourAppName/1.0' --header 'Content-Type: application/json' --data-raw '{\n    \"callback_url\": \"https://my-api/oura/tag/delete\",\n    \"verification_token\": \"123\",\n    \"event_type\": \"delete\",\n    \"data_type\": \"tag\"\n}'"
    }
  ]
}
```

### DELETE — Delete Webhook Subscription

```json
{
  "tags": [
    "Webhook Subscription Routes"
  ],
  "summary": "Delete Webhook Subscription",
  "operationId": "delete_webhook_subscription_v2_webhook_subscription__id__delete",
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "required": true,
      "schema": {
        "type": "string",
        "title": "Id"
      }
    }
  ],
  "responses": {
    "204": {
      "description": "Successful Response"
    },
    "403": {
      "description": "Webhook with specified id does not exist."
    },
    "422": {
      "description": "Validation Error",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/HTTPValidationError"
          }
        }
      }
    }
  },
  "security": [
    {
      "ClientIdAuth": [],
      "ClientSecretAuth": []
    }
  ],
  "x-codeSamples": [
    {
      "lang": "cURL",
      "label": "cURL",
      "source": "curl --location --request DELETE 'https://api.ouraring.com/v2/webhook/subscription/5d3fe17b-f880-4d93-b9b6-afbfb76c1e78' --header 'x-client-id: client-id' --header 'x-client-secret: client-secret' --header 'User-Agent: YourAppName/1.0'"
    }
  ]
}
```
