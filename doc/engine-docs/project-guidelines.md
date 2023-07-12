# Project Structure

`pyved-engine` was designed with the idea of making games much easier with python.
However, no matter how easy an engine is, it is very important to stay organized throughout
the project in order to debug problems
The ideal recommended structure for a game written using `pyved-engine` is as follows:
```bash
// just a sample folder structure based on HTML
// does not represent pyved engine structure
// TODO fix this
├── src
│   ├── controller
│   │   ├── **/*.css
│   ├── views
│   ├── model
│   ├── index.js
├── public
│   ├── css
│   │   ├── **/*.css
│   ├── images
│   ├── js
│   ├── index.html
├── dist (or build
├── node_modules
├── package.json
├── package-lock.json 
└── .gitignore
```