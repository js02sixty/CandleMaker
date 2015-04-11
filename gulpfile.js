// Gulpfile.js

// Gulp Imports
var gulp = require('gulp')
var connect = require('gulp-connect')
var historyApiFallback = require('connect-history-api-fallback')
var stylus = require('gulp-stylus')
var cssmin = require('gulp-minify-css')
var rename = require('gulp-rename')

// Stylus Imports
var nib = require('nib')
var jeet = require('jeet')
var rupture = require('rupture')

// Path Information
var srvRoot = './candlemaker/home/static'
var styleIn = srvRoot + '/stylus/style.styl'
var styleOut = srvRoot + '/css'
var htmlIn = [srvRoot + '/*.html', srvRoot + '/partials/*.html']

// Connect Web Server
gulp.task('websrv', function() {
    connect.server({
        root: srvRoot,
        livereload: true,
        host: '0.0.0.0',
        port: 8080,
        middleware: function(connect, opt) {
            return [historyApiFallback]
        }
    })
})

// Compile style to css
gulp.task('stylus', function() {
    gulp.src(styleIn)
        .pipe(stylus({
            use: [
                nib(),
                jeet(),
                rupture()
            ],
            errors: true,
            linenos: false
        }))
    .pipe(gulp.dest(styleOut))
    .pipe(rename({suffix: '.min'}))
    .pipe(cssmin())
    .pipe(gulp.dest(styleOut))
})

// Watch Stylus
gulp.task('watchstyl', function() {
    gulp.watch(styleIn, ['stylus'])
})

// Watch All and reload server
gulp.task('watchreload', function() {
    gulp.watch(styleIn, ['stylus', function() {
        gulp.src(styleIn).pipe(connect.reload())
    }])
    gulp.watch(htmlIn, function() {
        gulp.src(htmlIn).pipe(connect.reload())
    })
})

// Run Web Server
gulp.task('runall', ['websrv', 'stylus', 'watchreload'])

// Default Gulp task to run
gulp.task('default', ['stylus', 'watchstyl'])
