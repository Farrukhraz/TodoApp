import React from 'react'


const TicketItem = ({ticket}) => {
    return (
        <tr>
            <td>{ticket.title}</td>
            <td>{ticket.content}</td>
        </tr>
    )
}


const TicketList = ({tickets}) => {
    return (
        <table>
            <tr>
                <th>Title</th>
                <th>Content</th>
            </tr>
            {tickets.map((ticket) => <TicketItem ticket={ticket}/>)}
        </table>
    )
}


export default TicketList
