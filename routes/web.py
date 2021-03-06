''' Web Routes '''
from masonite.helpers.routes import get, post
from masonite.routes import RouteGroup as group

ROUTES = [
    get('/', 'HomeController@index').name('home'),
    get('/login', 'LoginController@show').name('login'),
    post('/login', 'LoginController@store'),
    get('/register', 'RegisterController@show').name('register'),
    post('/register', 'RegisterController@store').name('register'),
    get('/questions/@id:int', 'QuestionController@show').name('questions.show'),
    get('/categories/@id:int/questions', 'CategoryController@index').name('categories.questions.index'),
    get('/users/@id:int', 'UserController@show').name('users.show'),

    group([
        get('/logout', 'LoginController@logout').name('logout'),

        # Question Routes
        group([
            get('/create', 'QuestionController@create').name('create'),
            post('', 'QuestionController@store').name('store'),
            post('/@id/answers', 'AnswerController@store').name('answers'),
            post('/@id/answers/@answer_id/accept', 'QuestionController@accept_answer').name('accept'),
            get('/@id/upvote', 'QuestionController@upvote').name('upvote'),
            get('/@id/downvote', 'QuestionController@downvote').name('downvote'),
        ], prefix='/questions', name='questions.'),

        # Me Routes
        group([
            get('/questions', 'QuestionController@questions').name('questions'),
            get('/answers', 'AnswerController@answers').name('answers'),
        ], prefix='/me', name='me.')
    ], middleware = ('auth',)),
]
