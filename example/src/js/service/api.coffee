app = angular.module 'example.api', ['ngResource']

app.factory 'baseUrl', () ->
    'http://blog.agresebe.com'

app.run [ '$http', 'login', ($http, login) ->
    $http.defaults.headers.common.Authorization = 'Basic Y2FuZGlkYXRlOnlvdUNhbkRvSXQh'

    login.get()
]

app.factory 'login', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/login'
]

app.factory 'User', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/users/:username', username: '@username'
]

app.factory 'Post', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/posts/:id', id: '@id'
]

app.factory 'Photo', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/photos/:id', id: '@id'
]

# And the nested resources
app.factory 'UserPost', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/users/:username/posts/:id'
]

app.factory 'PostPhoto', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/posts/:post_id/photos/:id'
]
