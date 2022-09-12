import React from 'react'
import User from './components/User.js'
import Project from './components/Project.js'
import ToDoList from './components/ToDo.js'
import {BrowserRouter, Route, Switch, Redirect, Link} from 'react-router-dom'
import axios from 'axios'
import UserList from "./components/User.js";
import ProjectList from "./components/Project.js";
import LoginForm from './components/Auth.js'


const NotFound404 = ({ location }) => {
return (
<div>
    <h1>Страница по адресу '{location.pathname}' не найдена</h1>
</div>
)
}
class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'projects': [],
            'users': []
}
}
    load_data() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                this.setState({authors: response.data})
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                this.setState({books: response.data})
            }).catch(error => console.log(error))
        get_token(username, password)
        {
            axios.post('http://127.0.0.1:8000/api-token-auth/', {
                username: username,
                password: password
            })
                .then(response => {
                    console.log(response.data)
                }).catch(error => alert('Неверный логин или пароль'))
        }
    }
}
        componentDidMount()
{
    this.load_data()
}
render()
{
    return (
        <div className="App">
            <BrowserRouter>
                <nav>
                <ul>
                <li>
                <Link to='/'>Users</Link>
                </li>
                <li>
                <Link to='/projects'>Projects</Link>
                </li>
                <li>
                <Link to='/login'>Login</Link>
                </li>

                </ul>
<               /nav>
        <Switch>
            <Route exact path='/' component={() => <UserList
                items={this.state.users} />} />
            <Route exact path='/projects' component={() => <ProjectList
                items={this.state.projects} />} />
            <Route exact path='/login' component={() => <LoginForm
get_token={(username, password) => this.get_token(username, password)} />} />
            <Route path="/project/:id">
<ProjectList items={this.state.projects} />
</Route>
<Redirect from='/users' to='/' />
<Route component={NotFound404} />
</Switch>
</BrowserRouter>
</div>
)
    }
}
export default App