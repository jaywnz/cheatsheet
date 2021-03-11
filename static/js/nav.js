"use strict";

document.addEventListener('DOMContentLoaded', function() {
    let list = document.getElementById('topnav');
    let headings = document.getElementsByTagName('h3');
    for (let i = 0; i < headings.length; i++) {
        let item = document.createElement('li');
        let link = document.createElement('a');
        let text = document.createTextNode(headings[i].innerText);

        // Build the anchor
        link.href = headings[i].getAttribute('id');
        link.appendChild(text);

        // Add anchor to list item
        item.appendChild(link);

        // Add list item to list
        list.appendChild(item);
    }
});