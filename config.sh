#!/bin/bash

project_path=$(cd `dirname $0`; pwd)
echo $1 > $project_path/token
