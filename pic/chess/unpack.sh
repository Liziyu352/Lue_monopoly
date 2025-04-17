#!/bin/bash

7z x 1.zip
rm 1.zip
rm '图层 1.png'
rm 背景.png

mv '图层 7.png' base.png # 唉不好好给图层取名
mv '图层 8.png' base.png # 唉不好好给图层取名
mv 平时的表情.png normal.png
mv 前进.png forward.png
mv 退格.png backward.png
mv 被别人指定.png selected.png
mv 坐牢.png jail.png
