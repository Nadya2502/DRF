import React from 'react'


const ProjectItem = ({item}) => {
    return (
        <tr>

            <td>{item.name}</td>
            <td>{item.url}</td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <tr>

                <th>name</th>
                <th>url</th>
            </tr>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default ProjectList;

