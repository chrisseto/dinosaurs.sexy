var del = require('del');

var gulp = require('gulp');
var gutil = require('gulp-util');
var uglify = require('gulp-uglify');
var minifyCSS = require('gulp-minify-css');
var concatCss = require('gulp-concat-css');

var watchify = require('watchify');
var browserify = require('browserify');

var buffer = require('vinyl-buffer');
var source = require('vinyl-source-stream');



gulp.task('clean', function() {
  del(['static/css', 'static/js']);
});

gulp.task('css', function(){
    gulp.src(['./node_modules/bootstrap/dist/css/*.min.css', 'dinosaurs/css/**/*.css'])
    .pipe(concatCss("site.min.css"))
    .pipe(minifyCSS())
    .pipe(gulp.dest('./static/css/'));

    gulp.src('./node_modules/bootstrap/dist/fonts/*')
    .pipe(gulp.dest('./static/fonts/'));
});

gulp.task('build', ['clean', 'css'], function() {
  var bundler = browserify({
      entries: 'dinosaurs/index.js',
    });

    bundler.bundle()
    .pipe(source('site.min.js'))
    .pipe(buffer())
    .pipe(uglify())
    .pipe(gulp.dest('./static/js'));
});

gulp.task('develop', function() {
  var bundler = watchify(browserify({
      cache: {}, packageCache: {}, fullPaths: true,
      entries: 'dinosaurs/index.js',
      debug: true
    }));
    // bundler.transform('cssify');
  bundler.on('update', rebundle);

  function rebundle() {
    return bundler.bundle()
      // log errors if they happen
      .on('error', gutil.log.bind(gutil, 'Browserify Error'))
      .pipe(source('site.min.js'))
      .pipe(gulp.dest('./static/js'));
  }

  return rebundle();
});


gulp.task('default', ['clean', 'css', 'develop']);
