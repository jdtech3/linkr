uwsgi -s /tmp/linkr.sock --chmod=666 --manage-script-name --master --processes 4 --threads 2 --plugin python3 --mount /=app:app
