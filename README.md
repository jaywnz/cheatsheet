# cheatsheet.nz Reference Sheet Generator

## Introduction

*cheatsheet.nz* is a reference sheet generator built with Flask and SQLite. It is designed for people who are after a quick way to access technical information and provides a uniform and dynamic template through which to display a variety of complex reference materials.

The layout is built on on CSS grid and flexbox and is fully responsive. It can be adapted for any topic which has a large number of elements.

*cheatsheet.nz* uses Flask and the inbuilt Jinja2 templating system. It connects to an SQLite database and runs a series of SQL queries to populate the menu, categories and reference items on the page. *cheatsheet.nz* also supports images and captions for topics which rely on visual aids.

## Changing the content

Data is stored in the following tables:

1. sheet
2. category
3. content

A custom sheet can be created so long as the original database structure and field names are followed.

## Future plans

*cheatsheet.nz* will be expanded to support multiple sheets, with a dropdown selector providing the user the ability to change reference sheets.