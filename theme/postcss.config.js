const autoprefixer = require('autoprefixer')
const cssnano      = require('cssnano')
const purgecss     = require('@fullhuman/postcss-purgecss')
const tailwindcss  = require('tailwindcss')

// Constant flag to indicate whether or not we should build for production.
const PRODUCTION = process.env.NODE_ENV === 'production'

// Custom PurgeCSS extractor for Tailwind that allows special characters in
// class names.
//
// https://github.com/FullHuman/purgecss#extractor
class TailwindExtractor {
  static extract(content) {
    return content.match(/[A-Za-z0-9-_:\/]+/g) || [];
  }
}

module.exports = ctx => ({
  map:     ctx.options.map,
  parser:  ctx.options.parser,
  plugins: [
    // Tailwind CSS will always be included, regardless of `NODE_ENV`.
    tailwindcss('./tailwind.js'),

    // Autoprefixer, Cssnano and Purgecss will only be included when
    // `NODE_ENV` is set to 'production'.
    PRODUCTION && autoprefixer,
    PRODUCTION && cssnano({
      preset: 'default',
    }),
    PRODUCTION && purgecss({
      content: ['./templates/**/*.html'],
      css:     ['./styles/**/*.css'],
      extractors: [
        {
          extractor:  TailwindExtractor,
          extensions: ['css', 'html'],
        },
      ],
      // Post content styling, the markup for which isn't caught when building
      // the CSS as it hasn't been generated yet.
      whitelist: ['code', 'highlight', 'pre', 'table', 'td', 'th', 'ul'],
    }),
  ],
})
