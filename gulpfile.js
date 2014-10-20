var del = require('del');
var gulp = require('gulp');
var watchify = require('watchify');
var concat = require('gulp-concat');
var gutil = require('gulp-util');
var uglify = require('gulp-uglify');
var browserify = require('browserify');
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');

var paths = {
  scripts: ['dinosaurs/js/**/*.js'],
};


gulp.task('clean', function(cb) {
  del(['static/js'], cb);
});

gulp.task('build', ['clean'], function() {
  var bundler = watchify(browserify({
      cache: {}, packageCache: {}, fullPaths: true,
      entries: 'dinosaurs/index.js',
    }));

    return bundler.bundle()
    .on('error', gutil.log.bind(gutil, 'Browserify Error'))
    .pipe(source('site.min.js'))
    .pipe(buffer())
    .pipe(uglify())
    .pipe(gulp.dest('./static/js'));
});

gulp.task('develop', ['clean'], function() {
  var bundler = watchify(browserify({
      // Required watchify args
      cache: {}, packageCache: {}, fullPaths: true,
      // Specify the entry point of your app
      entries: 'dinosaurs/index.js',
      // Add file extentions to make optional in your requires
      // Enable source maps!
      debug: true
    }));
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


gulp.task('default', ['develop']);
