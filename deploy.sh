#!/bin/sh

cd ~/masenf-com
if git pull origin master ; then
    if make ; then
        echo Copying data to webroot
        cp -Rv output/* ~/public_html/masenf.com/
        cp -v output/.htaccess ~/public_html/masenf.com/
    else
        echo Build failed, nothing deployed
    fi
else
    echo Couldn\'t update from origin, nothing deployed
fi
