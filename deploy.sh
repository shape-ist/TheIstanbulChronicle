#!/bin/bash
# depends on: gh, git, heroku
#!/bin/bash

g='\033[1;32m' # green
r='\033[1;31m' # red
p='\033[1;35m' # purple
w='\033[0m' # white
printf "\n## ${p} Welcome to the Chroncile deployer ${w} ##\n\n"

printf "${g}Release: ${w}Enter a release version (e.g. 1.0.0): "
read VERSION
versionregex='^([0-9]+\.){0,2}(\*|[0-9]+)$'
if [[ ! $VERSION =~ $versionregex ]]; then
 printf "${r}ERROR:${w} Invalid semantic version: '$VERSION'\n"
 echo abort
 exit 1
fi

printf "${g}Release: ${w}Enter a release status (e.g. alpha, beta): "
read VERSIONSTATUS

if [ ! -z "$VERSIONSTATUS" ]
then
    VERSIONSTATUS="-${VERSIONSTATUS}"
fi

releasetag="v${VERSION}${VERSIONSTATUS}"

while true; do
    printf "${g}Release: ${w}Proceed releasing ${releasetag}? (Y/n) "
    read yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo abort && exit 1;;
        * ) ;;
    esac
done

git pull -q
git commit -q -a -m "Release: ${releasetag}"
git push -q

gh release create $releasetag
heroku git:remote -a istchron
mv .gitignore .gitignore-deploy
git push heroku main
mv .gitignore-deploy .gitignore
git remote rm heroku