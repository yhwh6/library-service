## Library service

DRF API service for library management

## Installing using GitHub

```bash
git https://github.com/yhwh6/library-service.git
cd library-service

python -m venv venv
sourve venv/bin/activate

pip install -r requirements.txt
rename .env.sample => .env and insert your data

python manage.py migrate
python manage.py runserver
````

## Getting access
<hr>

You can use following superuser:
```shell
- Email: admin@admin.com
- Password: qwerty123
```

Or create another one by yourself:

- create a user via `/users/create/`
- get access token via `/users/token/`


## Features
- JWT authentication
- Admin panel `/admin/`
- Documentation is located at `/schema/swagger/`
- Managing books and borrowings
- Filtering borrowing by active borrowing (`is_active`)
and `user_id` (admin only)
