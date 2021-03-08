import React from 'react';
import '../components-CSS/NavBar.css';

function Header()
{
    return(
        <div classname = "navbarlist">
            <ul>
            <li><a href = "#Home">Home</a></li>
            <li><a href = "#Watch Live">WatchLive</a></li>
            <li><a href = "#Blog">Blog</a></li>
            <li><a href = "#About">About</a></li>
        </ul>
        </div>
        
    )
}
export default Header;
