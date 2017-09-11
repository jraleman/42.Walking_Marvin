#!/bin/sh

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.sh                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaleman <jaleman@student.42.us.org>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/29 14:19:21 by jaleman           #+#    #+#              #
#    Updated: 2017/08/29 14:19:22 by jaleman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Directories variables.
BIN_DIR="."
GYM_DIR="gym"
RES_DIR="resources"

# Check if the user uses a Mac.
if [ $(uname -s) = "Darwin" ] ; then
    echo " > Updating / installing python packages..."
    brew update
    brew install python
    brew install numpy
    brew install box2d
fi

# Check if there's a previous installation already.
if [ -d $BIN_DIR/$GYM_DIR/ ] ; then
    echo " > It seems that OpenAI Gym is already installed."
    while true; do
        read -p "Do you wish to overwrite the installation? [y / n] " yn
        case $yn in
            [Yy]* ) echo " > Cleaning previous installation..."; \
                    rm -Rf $BIN_DIR/$GYM_DIR/; break;;
            [Nn]* ) echo " > Nothing has been modified. Bye :)"; exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
fi

# Git clone the OpenAI Gym repository.
echo " > Git cloning the lastest OpenAI Gym commit from the repository..."
git clone https://github.com/openai/gym.git $BIN_DIR/$GYM_DIR/
cd $BIN_DIR/$GYM_DIR/

# Install the OpenAI Gym package.
echo " > Installing the OpenAI Gym package..."
pip install --user -e .
cd ../
#
# Extracts all the files needed for the walking marvin enviroment.
echo " > Extracting and installing the walking marvin enviroment..."
cd $RES_DIR/
unzip envs.zip
cd ../
yes | cp -Rf $RES_DIR/envs $BIN_DIR/$GYM_DIR/gym/

# Remove extracted files.
echo " > Cleaning files..."
rm -Rf $RES_DIR/envs/

# Shows a success message :D
echo " > Done! Everything is pepa."
echo "   Check the readme file to see how this shit works"
