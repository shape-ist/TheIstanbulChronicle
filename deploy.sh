#!/bin/bash
cowsay deploying the chronicle... || echo * deploying the chronicle... *
heroku git:remote -a istchron
mv .gitignore .gitignore-deploy
git push heroku main
mv .gitignore-deploy .gitignore
git remote rm heroku