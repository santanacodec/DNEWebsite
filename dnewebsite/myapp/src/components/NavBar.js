import React from 'react';
import '../components-CSS/NavBar.css';

function Header(props)
{
    return(
        <div classname = "navbarlist">
            <ul>
            <li><a href = "#Home">Home</a></li>
            <li><a href = "#Watch Live">WatchLive</a></li>
            <li><a href = "#Blog">Blog</a></li>
            <li><a href = "#About">About</a></li>
            <li id = "hi"> {props.name}</li>
        </ul>
        </div>
        


        
        
    )
}
export default Header;
