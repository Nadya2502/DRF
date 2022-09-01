import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Menu} from './components/Menu.js'
import AuthorList from './components/Author.js'

import axios from 'axios'

class App extends React.Component {
constructor(props) {
super(props)
this.state = {
'authors': []
}
}
componentDidMount() {
axios.get('http://127.0.0.1:8000/api/v1/userlist/')
.then(response => {
const authors = response.data
this.setState(
{
'authors': authors
}
)
}).catch(error => console.log(error))
}

render () {
return (
<div>
<Menu  />
<AuthorList authors={this.state.authors} />

</div>
)
}
}

export default App;