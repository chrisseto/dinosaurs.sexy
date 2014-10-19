var del = require('del');

var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');


var paths = {
  scripts: ['dinosaurs/js/**/*.js'],
};

gulp.task('clean', function(cb) {
  del(['static/js'], cb);
});

gulp.task('minify', ['clean'], function() {
  return gulp.src(paths.scripts)
    .pipe(concat('site.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('static/js'));
});

gulp.task('concat', ['clean'], function() {
  return gulp.src(paths.scripts)
    .pipe(concat('site.js'))
    .pipe(gulp.dest('static/js'));
});

// Rerun the task when a file changes
gulp.task('watch', function() {
  gulp.watch(paths.scripts, ['concat']);
});

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['watch', 'concat']);
