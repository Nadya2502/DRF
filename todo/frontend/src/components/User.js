import React from 'react'


const UserItem = ({item}) => {
    return (
        <tr>

            <td>{item.username}</td>
            <td>{item.first_name}</td>
            <td>{item.last_name}</td>
            <td>{item.date_of_birth}</td>
            <td>{item.mail}</td>

        </tr>
    )
}

const UserList = ({items}) => {
    return (
        <table>
            <tr>
                <th>username</th>
                <th>first_name</th>
                <th>last_name</th>
                <th>date_of_birth</th>
                <th>mail</th>

            </tr>
            {items.map((item) => <UserItem item={item} />)}
        </table>
    )
}
export default UserList