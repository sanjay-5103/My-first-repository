Base URL: http://127.0.0.1:8000/

# Auth (Djoser)
/auth/users/                – POST register user
/auth/users/me/             – GET current user (requires token)
/auth/token/login/          – POST obtain auth token
/auth/token/logout/         – POST logout (invalidate token)

# Menu
/restaurant/menu/           – GET list menu items, POST create
/restaurant/menu/<id>       – GET one, PUT/PATCH update, DELETE

# Bookings (ViewSet, requires token)
/restaurant/booking/tables/           – GET list bookings, POST create
/restaurant/booking/tables/<id>/      – GET one, PUT/PATCH/DELETE

# (Optional) DRF token endpoint (alternative to Djoser)
/restaurant/api-token-auth/  – POST {username, password} -> {"token": "..."}
