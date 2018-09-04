.PHONY : all

nothing:
	echo '请指定命令'

intro:
	echo '默认执行第一命令，可以用伪目标来选择一些命令'

dev:
	pipenv run python ./dev.py ./index.py && make flask

flask:
	python ./index.py

demo1:
	echo '我是demo1'

demo2:
	echo '我是demo2'

all: demo1 demo2

pushIntro:
	echo '传递参数方法:make push msg="你好"'

push:
	git add . && git commit -m '$(msg)' && git push
