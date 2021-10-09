#!/bin/bash
# depends on: gh, git, heroku
#!/bin/bash

g='\033[1;32m' # green
r='\033[1;31m' # red
p='\033[1;35m' # purple
c='\033[1;36m' # cyan
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
    printf "${g}Release: ${w}Proceed releasing ${c}${releasetag}${w}? (Y/n) "
    read yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo abort && exit 1;;
        * ) ;;
    esac
done

printf "${c}INFO: ${w}Committing release to remote... "
git pull -q
git commit -q -a -m "Release: ${releasetag}"
git push -q

gh release create $releasetag
printf "${c}INFO: ${w}Deploying code...\n"
heroku git:remote -a istchron
mv .gitignore .gitignore-deploy
git push heroku main
printf "${c}INFO: ${w}Deploy complete, cleaning up...\n"
mv .gitignore-deploy .gitignore
git remote rm heroku
printf "${p}\nSuccesfully deployed the Chronicle!\n${w}"