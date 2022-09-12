import React from 'react';

export class Menu extends React.Component{
    render() {
        let menus = [
            "Home",
            "Our partners",
            "Contacts"
        ]
        return <div>
            {menus.map((value, index)=>{
                return <div key={index}><Link label={value} /> </div>})}
                    </div>
                }
                    }


class Link extends React.Component{
    render(){
        const url = "/"  ;
        return <div>
            <a href={url}>{this.props.label}</a>
        </div>
    }
}

// ReactDOM.render(
//     <div>
//         <Menu />
//     </div>,
//     document.getElementById('content')
// );

