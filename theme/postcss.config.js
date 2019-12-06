const autoprefixer  = require("autoprefixer")
const cssnano       = require("cssnano")
const postcsshash   = require("postcss-hash")
const postcssimport = require("postcss-import")
const postcssnested = require("postcss-nested")
const purgecss      = require("@fullhuman/postcss-purgecss")
const tailwindcss   = require("tailwindcss")

const PRODUCTION = process.env.NODE_ENV === "production"

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
  map:    ctx.options.map,
  parser: ctx.options.parser,

  plugins: [
    postcssimport,
    postcssnested,
    tailwindcss,

    PRODUCTION && autoprefixer(),
    PRODUCTION && cssnano({
      preset: "default",
    }),
    PRODUCTION && postcsshash(),
    PRODUCTION && purgecss({
      content: ["./templates/**/*.html"],
      css:     ["./styles/**/*.css"],
      extractors: [
        {
          extractor:  TailwindExtractor,
          extensions: ["css", "html"],
        },
      ],
      whitelist:                 ["code", "pre", "table", "td", "th", "ul"],
      whitelistPatternsChildren: [/^highlight/],
    }),
  ],
})
