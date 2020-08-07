# jwt_token
Generating JWT token which is used for Authentication purpose.

# Intelligent concept to be learnt over here.

1. We are going to generate the JWT(JSON Web Token) for our Restful API using Flask Framework.
2. User has to Login while using his credentials(i.e, Username & Password).
3. In this case, I have 'Hard-Coded' the credentials else I have to connect with Database(any).
   a. Under Authorization, click on 'type' and select 'Basic Auth'.
   b. And then input your credentials(i.e, username: MR.X, password: password).
   c. We can see our enter password by checking 'check' option.

4. Once we will login, it will generate the unique JWT token for us.
5. That JWT token will the valid for certain time(here it's 30 seconds).

6. With this certain time, user has supposed to be logged in otherwise token will be invalid.
7. JWT token has to pass under the 'header' by adding key as 'x-access-tokens' and 
   value as JWT token(afkayfkzcbjcjchfafhakccacjahaa).
   
8. Hit the secure url while removing the login url.
9. Try to hit 'Send' button, you will see the message of 'Invalid Token'.