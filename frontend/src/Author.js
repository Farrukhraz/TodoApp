import React from 'react'


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>{author.first_name}</td>
            <td>{author.last_name}</td>
            <td>{author.birth_date}</td>
        </tr>
    )
}


const AuthorList = ({authors}) => {
    return (
        <table>
            <tr>
                <th>First name</th>
                <th>Last name</th>
                <th>Birth date</th>
            </tr>
            {authors.map((author) => <AuthorItem author={author}/>)}
        </table>
    )
}


export default AuthorList
