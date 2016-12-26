app = angular.module 'example.api', ['ngResource']

app.factory 'baseUrl', () ->
    'http://blog.agresebe.com'

app.run [ '$http', 'login', ($http, login) ->
    $http.defaults.headers.common.Authorization = 'Basic Y2FuZGlkYXRlOnlvdUNhbkRvSXQh'
    $http.defaults.withCredentials = true;

    login.get()
]

app.factory 'login', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/login', {}, {withCredentials: true}
]

app.factory 'User', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/users/:username', {username: '@username'}, {withCredentials: true}
]

app.factory 'Post', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/posts/:id', {id: '@id'}, {withCredentials: true}
]

app.factory 'Photo', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/photos/:id', {id: '@id'}, {withCredentials: true}
]

# And the nested resources
app.factory 'UserPost', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/users/:username/posts/:id', {}, {withCredentials: true}
]

app.factory 'PostPhoto', ['baseUrl', '$resource', (baseUrl, $resource) ->
    $resource baseUrl + '/api/posts/:post_id/photos/:id', {}, {withCredentials: true}
]
