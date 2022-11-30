PY       ?= python3
VENV_PY  ?= venv/bin/python3
PYLINT   ?= venv/bin/pylint
PYTEST   ?= venv/bin/pytest

VENV         ?= venv
REQUIREMENTS  = requirements.txt
_PYTHONPATH    = .

PROJECT_NAME = adventofcode
HTML_STATIC_PATH = static
HTML_REPORT_PATH = docs

PYLINT_OPTS = --extension-pkg-allow-list="math"
PYTEST_OPTS = --durations=0 -v -n 4 --color=yes

install: env
	${VENV_PY} -m pip install -r "${REQUIREMENTS}"

env:
	${PY} -m venv "${VENV}"

all: test-2022 render lint

render:
	mkdir -p "${HTML_REPORT_PATH}" \
	&& cp -r "${PROJECT_NAME}/${HTML_STATIC_PATH}"/* "${HTML_REPORT_PATH}/" \
	&& for report in `ls ${HTML_REPORT_PATH} | grep report`; do sed -i .tmp -e 's/^\(.*<\/ul>\)/    <li><a href="'$${report}'">'$${report}'<\/a><\/li>\n\1/' "${HTML_REPORT_PATH}/index.html"; done \
	&& rm "${HTML_REPORT_PATH}"/*.tmp \
	&& echo open "${HTML_REPORT_PATH}/index.html"

test: test-2015 test-2016 test-2017 test-2018 test-2019 test-2020 test-2021 test-2022

lint:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYLINT} ${PYLINT_OPTS} "${PROJECT_NAME}"

test-2022:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/report-2022.html" "${PROJECT_NAME}/tests/y2022"

test-2021:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/report-2021.html" "${PROJECT_NAME}/tests/y2021"

test-2020:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/report-2020.html" "${PROJECT_NAME}/tests/y2020"

test-2019:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/report-2019.html" "${PROJECT_NAME}/tests/y2019"

test-2018:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/report-2018.html" "${PROJECT_NAME}/tests/y2018"

test-2017:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/report-2017.html" "${PROJECT_NAME}/tests/y2017"

test-2016:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/report-2016.html" "${PROJECT_NAME}/tests/y2016"

test-2015:
	PYTHONPATH="${_PYTHONPATH}:${PYTHONPATH}" ${PYTEST} ${PYTEST_OPTS} --html="${HTML_REPORT_PATH}/report-2015.html" "${PROJECT_NAME}/tests/y2015"