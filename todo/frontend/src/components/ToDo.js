import React from 'react'


const ToDoItem = ({item}) => {
    return (
        <tr>

            <td>{item.project}</td>
            <td>{item.text}</td>
            <td>{item.created_at}</td>
            <td>{item.updated_at}</td>
            <td>{item.user}</td>
            <td>{item.status}</td>
        </tr>
    )
}

const ToDoList = ({items}) => {
    return (
        <table>
            <tr>
                <th>project</th>
                <th>text</th>
                <th>created_at</th>
                <th>updated_at</th>
                <th>user</th>
                <th>status</th>
            </tr>
            {items.map((item) => <ToDoItem item={item} />)}
        </table>
    )
}
export default ToDoList