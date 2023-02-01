#!/bin/bash

if [[ $(python3 --version) =~ 3.10 ]]; then
	if [ ! -d ".trivenv" ]; then
		echo "Creating new virtual environment..."
		python3 -m venv .trivenv/
		source $PWD/.trivenv/bin/activate
		python3 -m pip install -r code/requirements.txt
	fi
else
	echo "Please upgrade Python to version 3.10"
	exit 1
fi

echo "Fetching missing datasets and models..."
if [ ! -d "data" ]; then
	if ! command -v unzip &> /dev/null; then
		echo "Please install unzip in order to unpack the datasets."
		exit
	fi
	mkdir data/
	# monument
	gdown https://drive.google.com/uc?id=15wo0HuLbAOkGgdY7zbwqppzfgiWeity9
	unzip -q -d data/ Monument.zip
	rm Monument.zip
	# lc-quad
	gdown https://drive.google.com/uc?id=1ZNTZnE-rmH7OTuRTCqPR18wKTPGD3PQO
	unzip -q -d data/ LC-QUAD.zip
	rm LC-QUAD.zip
fi
if [ ! -d "models/Monument" ]; then
	mkdir -p models/Monument
	gdown https://drive.google.com/u/0/uc?id=137_GiF1RlTDidF8psj7yg48soGzamV1N
	unzip -q -j -d models/Monument/ ConvS2S-forMonument.zip
	rm ConvS2S-forMonument.zip
fi
if [ ! -d "models/LC-QUAD" ]; then
	mkdir -p models/LC-QUAD
	gdown https://drive.google.com/u/0/uc?id=1wirMkFL_rKcjMcAJoa75EkZkq8P49TW9
	unzip -q -j -d models/LC-QUAD ConvS2S-forLC-QUAD.zip
	rm ConvS2S-forLC-QUAD.zip
fi
