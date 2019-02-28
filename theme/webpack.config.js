const path = require('path')
const ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  entry: './src/styles.css',
  mode:  process.env.NODE_ENV,

  output: {
    path: path.resolve(__dirname, 'static', 'css'),
  },

  module: {
    rules: [
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use:      ['css-loader', 'postcss-loader'],
        }),
      },
    ],
  },

  plugins: [
    new ExtractTextPlugin('styles.css', {
      disable: process.env.NODE_ENV === 'development',
    }),
  ],
}
