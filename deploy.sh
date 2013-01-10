#!/bin/sh

cd ~/masenf-com
git pull origin master
if make ; then
    echo Copying data to webroot
    cp -a output/* ~/public_html/masenf.com/
else
    echo Build failed, nothing deployed
fi
