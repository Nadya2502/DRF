import React from 'react';
import logo from './logo.svg';
import './App.css';
import ProjectList from './components/Project.js'
import ToDoList from './components/ToDo.js'
import UserList from './components/User.js'
import {HashRouter, Route, Link, Redirect} from 'react-router-dom'


// const NotFound404 = ({ location }) => {
//     return (
//         <div>
//             <h1>Страница по адресу '{location.pathname}' не найдена</h1>
//         </div>
// )
// }


class App extends React.Component {

    constructor(props) {
        super(props)
        const project1 = {id: 1, name: 'project1', url: '12345'}
        const project2 = {id: 2, name: 'project2', url: '123456'}
        const projects = [project1, project2]
        const user1 = {id: 1, username: 'user1', first_name: 'first_name1', last_name:'lastname1', date_of_birth:'1980', mail:'mail1@mailru'}
        const user2 = {id: 2, username: 'user2', first_name: 'first_name2', last_name:'lastname2', date_of_birth:'1980', mail:'mail2@mailru'}
        const user3 = {id: 3, username: 'user3', first_name: 'first_name3', last_name:'lastname3', date_of_birth:'1980', mail:'mail3@mailru'}

        const users = [user1, user2, user3]
this.state = {
'projects': projects,
'users': users
}
}
render() {
        return (
            <div className="App">
            <HashRouter>
                <nav>
                    <ul>
                        <li>
                            <Link to='/'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/users'>Users</Link>
                        </li>
                    </ul>
                </nav>
            <Route exact path='/' component={() => <ProjectList items={this.state.projects} />} />
            <Route exact path='/users' component={() => <UserList items={this.state.users} />} />
            </HashRouter>
</div>
)
}
}

export default App;