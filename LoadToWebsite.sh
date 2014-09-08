#!/bin/bash
git pull 


for entry in ${find -name *.pdf | cut -f 4 -d '/' | grep Lec};
   do ln -s ${entry};
   done

