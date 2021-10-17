# cheatsheet.nz Reference Sheet Generator

*cheatsheet.nz* provides a uniform and dynamic template through which to display technical reference material. The current example is an HTML element reference sheet, though it works with any technical topic with a large number of elements. It is built with Flask and SQLite, and the layout with CSS Grid and flexbox.

*cheatsheet.nz* uses Flask's inbuilt Jinja2 templating system. It connects to an SQLite database and runs a series of SQL queries to populate the menu, categories and reference items. Images and captions are also supported for topics relying on visual aids.

Running on Gunicorn/Heroku.

- [App URL](https://cheatsheet-nz.herokuapp.com/)