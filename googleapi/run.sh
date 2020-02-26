# FN_AUTH_REDIRECT_URI should be the OAuth redirect URI which you set up earlier
# FN_CLIENT_ID Should be set to the Google OAuth client id which you saved earlier
# FN_CLIENT_SECRET Should be set to the Google OAuth client secret which you saved earlier
# FN_FLASK_SECRET_KEY should be a random value. This will be used for encrypting the cookie in the Flask session.

export FN_AUTH_REDIRECT_URI=http://localhost:8040/google/auth
export FN_BASE_URI=http://localhost:8040
export FN_CLIENT_ID=THE CLIENT ID WHICH YOU CREATED EARLIER
export FN_CLIENT_SECRET=THE CLIENT SECRET WHICH YOU CREATED EARLIER

export FLASK_APP=google_app.py
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY=SOMETHING RANDOM AND SECRET

python -m flask run -p 8040