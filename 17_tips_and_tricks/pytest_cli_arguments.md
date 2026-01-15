pytest --headed --slowmo=400 --browser=firfox/webkit

## emulate any device
pytest --device="Pixel 5"

## enable tracing on tests
pytest --tracing on/off/retain-on-failure

## record a video on every test
pytest --video on

## create screenshots after test are done
pytest --screenshot on/only-on-failure

## run specific test from a file
pytest -k test_page_visits_docs



