# create index.html in the source folder and reference the app by adding a div with id="root"

    <div id="root" ></div>

# create a babelrc file in the root folder

# create a webpack config file in the root folder

# install the following dependencies

    npm install webpack webpack-cli webpack-dev-server --save-dev
    npm install path html-webpack-plugin --save-dev
    npm install --save-dev @babel/core @babel/node @babel/preset-env @babel/preset-react babel-loader
    npm install style-loader css-loader sass-loader node-sass image-webpack-loader --save-dev
    npm install file-loader @babel/plugin-proposal-class-properties --save-dev

# alter package.json as follows

    "scripts": {
    "webpack": "webpack",
    "start": "webpack serve",

},

# npm run webpack to build
